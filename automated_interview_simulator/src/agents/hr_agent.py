from crewai import Agent
from langchain_openai import ChatOpenAI

hr_agent = Agent(
    role="HR Interviewer",
    goal="Evaluate the candidate’s behavioral and communication skills",
    backstory="A seasoned HR professional skilled at assessing personality, motivation, and culture fit.",
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    verbose=True
)