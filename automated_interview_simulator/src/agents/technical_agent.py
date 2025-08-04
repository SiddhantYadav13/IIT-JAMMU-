from crewai import Agent
from langchain_openai import ChatOpenAI

technical_agent = Agent(
    role="Technical Interviewer",
    goal="Evaluate the candidate’s technical skills",
    backstory="A senior engineer experienced in assessing coding, problem-solving, and design ability.",
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    verbose=True
)