from crewai import Agent
from langchain_openai import ChatOpenAI

interviewer_agent = Agent(
    role="AI Interviewer",
    goal="Simulate a professional technical interview based on user input",
    backstory=(
        "You are an AI-driven HR professional and technical expert conducting interviews "
        "to evaluate candidates' readiness, depth of knowledge, and communication skills."
    ),
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    verbose=True
)