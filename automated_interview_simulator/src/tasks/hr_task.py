from crewai import Task
from src.agents.hr_agent import hr_agent

hr_task = Task(
    description="Conduct a behavioral interview focusing on communication, teamwork, and cultural fit.",
    expected_output="Summarize the candidate’s strengths and weaknesses from an HR perspective.",
    agent=hr_agent
)