from crewai import Task
from src.agents.technical_agent import technical_agent

technical_task = Task(
    description="Conduct a technical interview focusing on coding, logic, and problem-solving.",
    expected_output="Summarize the candidate’s technical abilities and areas for improvement.",
    agent=technical_agent
)