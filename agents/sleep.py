from smolagents import CodeAgent, tool, LiteLLMModel


model = LiteLLMModel(
    model_id="ollama/qwen2:7b",  
    api_key="ollama"
)

# Tool for suggesting sleep advice based on user input
@tool
def analyze_sleep(occasion: str) -> str:
    """
    Suggest a sleep routine based on the user's sleep needs or situation.
    Args:
        occasion: The type of sleep issue or need.
    """
    # Offering sleep tips for different situations
    if occasion == "insomnia":
        return "Try a warm bath, light stretching, or listening to calming music before bed."
    elif occasion == "stress":
        return "Deep breathing exercises or meditation before sleep can help relieve stress."
    elif occasion == "jetlag":
        return "Try adjusting your sleep schedule gradually and stay hydrated to reduce jet lag effects."
    elif occasion == "general":
        return "Establish a consistent sleep schedule, avoid caffeine, and ensure your bedroom is dark and quiet."
    else:
        return "A relaxing pre-bed routine including reading a book and limiting screen time is always beneficial."

# Create the SleepAgent with the tools and model
agent = CodeAgent(tools=[analyze_sleep], model=model)

# Running the agent with an example query
response = agent.run("What should I do if I have insomnia?")
print(response)

