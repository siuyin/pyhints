from pydantic import BaseModel  # type: ignore
from pydantic_ai import Agent  # type: ignore
from pydantic_ai.models.openai import OpenAIModel  # type: ignore
from pydantic_ai.providers.openai import OpenAIProvider  # type: ignore


class CityCountry(BaseModel):
    city: str
    state: str
    country: str


ollama_model = OpenAIModel(
    model_name="PetrosStav/gemma3-tools:4b",
    #model_name="gemma3:4b",
    #model_name="llama3.2:3b",
    provider=OpenAIProvider(base_url="http://imac2.h:11434/v1"),
)

agent = Agent(
    ollama_model,
    output_type=CityCountry,
    #system_prompt="extract location information",
)

if __name__ == "__main__":
    result = agent.run_sync("The atomic city")
    print(result.output)
    print(result.usage())
