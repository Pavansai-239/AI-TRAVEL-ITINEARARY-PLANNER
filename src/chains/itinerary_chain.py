from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama3-70b-8192",  # Correct model name for Groq
    temperature=0.3
)

itinerary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful travel assistant. Create a day trip itinerary for {city} based on user's interest: {interest}. Provide a brief, bulleted itinerary."),
    ("human", "Create an itinerary for my day trip.")
])

def generate_itinerary(city: str, interests: list[str]) -> str:


    response = llm.invoke(
        itinerary_prompt.format_messages(
            city=city,
            interest=', '.join(interests)   # match 'interest' not 'interests'
        )
    )
    return response.content
