from typing import Dict, Any
from .base_agent import BaseAgent


class AnalyzerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Analyzer",
            instructions="""Analyze candidate profiles for:
            1. Key skills and expertise level
            2. Years of experience
            3. Educational qualifications
            4. Career progression
            5. Potential red flags
            Provide detailed analysis with specific observations.""",
        )

    async def run(self, messages: list) -> Dict[str, Any]:
        """Analyze the extracted resume data"""
        print("🔍 Analyzer: Analyzing candidate profile")

        extracted_data = eval(messages[-1]["content"])
        analysis_results = self._query_ollama(str(extracted_data["structured_data"]))

        return {
            "skills_analysis": analysis_results,
            "analysis_timestamp": "2024-03-14",
            "confidence_score": 0.85,
        }