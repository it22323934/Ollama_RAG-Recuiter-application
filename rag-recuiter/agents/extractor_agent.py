from pdfminer.high_level import extract_text
from .base_agent import BaseAgent
from typing import Dict, Any

class ExtractorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Extractor",
            instructions="""Extract and structure information from the resumes.
            Focus on: Perosnal information, Education, Work experience, Skills, Certifications, Awards, Publications, Projects, Languages, Hobbies, References, etc.
            Provide output in a clear, structured format.
            """,
        )
        
    async def run(self,messages:list)->Dict[str,Any]:
        """Extract information from the pdf"""
        print("Extracting: Extracting information from the pdf...")
        
        resume_data = eval(messages[-1]["content"])
        
        #Extract text from the pdf
        if resume_data.get("file_path"):
            raw_text=extract_text(resume_data["file_path"])
        else:
            raw_text=resume_data.get("text","")
            
        extracted_info=self._query_ollama(raw_text)
        
        return {
            "raw_text":raw_text,
            "structured_data":extracted_info,
            "extraction_status":"Completed"
        }        