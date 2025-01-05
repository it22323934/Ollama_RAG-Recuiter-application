from typing import Dict, Any
from .base_agent import BaseAgent

class MatcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Matcher",
            instructions="""Match candidates to job descriptions based on:
            - Skills match percentage
            - Experience relevance
            - Qualifications alignment
            - Cultural fit indicators
            - Personality traits
            Provide detailed reasoning and compatilibity scores.
            Return matches in JSON format with title,match_score and location fields.""",
        )
        
    async def run(self, messages:list)->Dict[str,Any]:
        """Match the candidate with available positions"""
        print("Matcher: Matching candidates with available positions...")
        
        analysis_results=eval(messages[-1]["content"])
        
        sample_jobs = [
            {
                "title": "Senior Software Engineer",
                "company": "TechCorp",
                "location": "San Francisco, CA",
                "required_skills": ["Python", "AWS", "Docker", "Kubernetes", "CI/CD"],
                "min_experience_years": 5,
                "qualifications": ["Bachelor's in Computer Science", "Cloud certification"],
                "cultural_values": ["innovation", "teamwork", "continuous learning"],
                "personality_traits": ["analytical", "problem-solver", "collaborative"],
                "salary_range": {"min": 130000, "max": 180000},
                "job_type": "Full-time",
                "department": "Engineering"
            },
            {
                "title": "Data Scientist",
                "company": "DataWorks Inc",
                "location": "Boston, MA",
                "required_skills": ["Python", "SQL", "Machine Learning", "TensorFlow", "Statistics"],
                "min_experience_years": 3,
                "qualifications": ["Master's in Data Science", "Research experience"],
                "cultural_values": ["data-driven", "research-oriented", "innovative"],
                "personality_traits": ["detail-oriented", "curious", "methodical"],
                "salary_range": {"min": 115000, "max": 160000},
                "job_type": "Full-time",
                "department": "Data Science"
            },
            {
                "title": "DevOps Engineer",
                "company": "CloudScale Solutions",
                "location": "Austin, TX",
                "required_skills": ["AWS", "Terraform", "Jenkins", "Python", "Linux"],
                "min_experience_years": 4,
                "qualifications": ["Bachelor's in related field", "AWS certification"],
                "cultural_values": ["automation", "reliability", "efficiency"],
                "personality_traits": ["systematic", "proactive", "team-player"],
                "salary_range": {"min": 120000, "max": 170000},
                "job_type": "Full-time",
                "department": "Infrastructure"
            },
            {
                "title": "Frontend Developer",
                "company": "WebUI Systems",
                "location": "Remote",
                "required_skills": ["React", "TypeScript", "HTML5", "CSS3", "Jest"],
                "min_experience_years": 2,
                "qualifications": ["Bachelor's degree", "Frontend certification"],
                "cultural_values": ["user-focused", "creative", "agile"],
                "personality_traits": ["creative", "detail-oriented", "communicative"],
                "salary_range": {"min": 90000, "max": 140000},
                "job_type": "Full-time",
                "department": "Frontend Development"
            },
            {
                "title": "Product Manager",
                "company": "ProductLabs",
                "location": "Seattle, WA",
                "required_skills": ["Product Strategy", "Agile", "Data Analysis", "Stakeholder Management"],
                "min_experience_years": 5,
                "qualifications": ["Bachelor's in Business/Technology", "PMP certification"],
                "cultural_values": ["customer-first", "innovation", "collaboration"],
                "personality_traits": ["leadership", "strategic", "excellent-communicator"],
                "salary_range": {"min": 125000, "max": 175000},
                "job_type": "Full-time",
                "department": "Product"
            }
        ]
        
        matching_reponse = self._query_ollama(
            f""" Analyse the following profile and provide job matches in valid JSON format:
            Profile : {analysis_results['skills_analysis']}
            Available Jobs : {sample_jobs}
            
            Return ONLY a JSON object with this extact structure:
            {{
                "matched_jobs:[
                    {{
                        "title":"job title",
                        "match_score":"85%",
                        "location":"job location"
                    }}
                ],
                "match_timestamp":"2025-01-05",
                "number of matches":2
            }}"""
        )
        
        parsed_response = self._parse_json_safely(matching_reponse)
        
        # Fallback to sample data if parsing fails
        if "error" in parsed_response:
            return {
                "matched_jobs":[
                    {
                        "title":"Senior Software Engineer",
                        "match_score":"90%",
                        "location":"San Francisco, CA"
                    }
                ],
                "match_timestamp":"2025-01-05",
                "number of matches":2
            }
                
        return parsed_response 