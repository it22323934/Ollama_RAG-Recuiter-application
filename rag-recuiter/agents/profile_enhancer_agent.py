from typing import Dict, Any
from swarms import Agent

def profile_enhancer_agent_function(extracted_info: Dict[str, Any]) -> Dict[str, Any]:
    enhanced_profile = extracted_info.copy()
    total_experience_years = sum(item["years"] for item in extracted_info["experience"])
    enhanced_profile["summary"]=(
        f"{extracted_info['name']} has {total_experience_years} years of experience."
    )
    return enhanced_profile

profile_enhancer_agent = Agent(
    name="profile_enhancer_agent",
    model="llama3.2",
    instructions="Enhance the candidate's profile based on the extracted information",
    function=[profile_enhancer_agent_function]
)
    