import sqlite3
from pathlib import Path
from typing import Dict, Any,List
import json
import os


class JobDatabase:
    def __init__(self):
        current_dir = Path(__file__).parent
        self.db_path=current_dir/"jobs.sqlite"
        self.schema_path=current_dir/"schema.sql"
        self.__init__db()
        
    def __init__db(self):
        if not self.schema_path.exists():
            raise FileNotFoundError(f"Schema file not found: {self.schema_path}")
        
        with open(self.schema_path) as f:
            schema=f.read()
            
        with sqlite3.connect(self.db_path) as conn:
            conn.executescript(schema)
            
    def add_job(self,job_data:Dict[str,Any])->int:
        
        query="""
        INSERT INTO jobs(
            title, company, location, type, experience_level,
            salary_range, description, requirements, benefits
        ) VALUES(?,?,?,?,?,?,?,?,?)
        """
        
        with sqlite3.connect(self.db_path) as conn:
            cursor= conn.cursor()
            cursor.execute(
                query,
                (
                    job_data["title"],
                    job_data["company"],
                    job_data["location"],
                    job_data["type"],
                    job_data["experience_level"],
                    job_data["salary_range"],
                    job_data["description"],
                    json.dumps(job_data["requirements"]),
                    json.dumps(job_data.get("benefits",[])),
                )
            )
            return cursor.lastrowid
    
    def get_all_jobs(self)->List[Dict[str,Any]]:
        query="SELECT * FROM jobs ORDER BY created_at DESC"
        
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory=sqlite3.Row
            cursor=conn.cursor()
            cursor.execute(query)
            rows=cursor.fetchall()
            
            return [
                {
                    "id":row["id"],
                    "title":row["title"],
                    "company":row["company"],
                    "location":row["location"],
                    "type":row["type"],
                    "experience_level":row["experience_level"],
                    "salary_range":row["salary_range"],
                    "description":row["description"],
                    "requirements":json.loads(row["requirements"]),
                    "benefits":json.loads(row["benefits"]) if row["benefits"] else [],
                    "created_at":row["created_at"],
                }
                for row in rows
            ]
            
    def search_job(self,skills:List[str],experience_level:str)->List[Dict[str,Any]]:
        query="""
        SELECT * FROM jobs
        WHERE experience_level=?
        AND (
        """
        query_conditions=[]
        params=[experience_level]
        
        for skill in skills:
            query_conditions.append("requirements LIKE ?")
            params.append(f"%{skill}%")
            
        query+=" OR ".join(query_conditions) + ")"
        
        try:
            with sqlite3.connect(self.db.db_path) as conn:
                conn.row_factory=sqlite3.Row
                cursor=conn.cursor()
                cursor.execute(query,params)
                rows=cursor.fetchall()
                
                return [
                    {
                        "id":row["id"],
                        "title":row["title"],
                        "company":row["company"],
                        "location":row["location"],
                        "type":row["type"],
                        "experience_level":row["experience_level"],
                        "salary_range":row["salary_range"],
                        "description":row["description"],
                        "requirements":json.loads(row["requirements"]),
                        "benefits":(json.loads(row["benefits"]) if row["benefits"] else [])
                    }
                    for row in rows
                ]
        except Exception as e:
            print(f"Error in searching jobs: {e}")
            return []
        