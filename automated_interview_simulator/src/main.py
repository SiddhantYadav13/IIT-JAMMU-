import os
from dotenv import load_dotenv
from crewai import Crew

from src.agents.hr_agent import hr_agent
from src.agents.technical_agent import technical_agent

from src.tasks.hr_task import hr_task
from src.tasks.technical_task import technical_task

load_dotenv()

crew = Crew(
    agents=[hr_agent, technical_agent],
    tasks=[hr_task, technical_task],
    verbose=True
)

crew.kickoff()