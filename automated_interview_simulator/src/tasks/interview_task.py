from crewai import Task
from src.agents.interviewer_agent import interviewer_agent

interview_task = Task(
    description=(
        "Conduct a detailed technical interview for a candidate applying for a Python backend role. "
        "Ask relevant questions based on the resume and give feedback."
    ),
    expected_output="A well-formatted summary of the candidate's performance and suggestions for improvement.",
    agent=interviewer_agent
)