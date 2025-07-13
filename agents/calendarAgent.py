from smolagents import CodeAgent, tool, LiteLLMModel

model = LiteLLMModel(
    model_id="ollama/qwen2:7b",  
    api_key="ollama"
)

calendar_event = None  # Store a single event description

# Tool to add a calendar event (just a text description)
@tool
def add_calendar_event(event_description: str) -> str:
    """
    Adds a calendar event description to local storage.
    Args:
        event_description: The description of the event (e.g., 'Meeting with Mohammad').
    """
    global calendar_event  # Use the global variable to store the event description
    calendar_event = event_description
    return f"Event added: {event_description}"

# Tool to retrieve the stored calendar event description
@tool
def get_calendar_event() -> str:
    """
    Retrieves the stored calendar event description.
    """
    if not calendar_event:
        return "final_answer('No event scheduled.')"
    return f"final_answer('Stored event: {calendar_event}')"

# Create the agent with the tools
calendar_agent = CodeAgent(tools=[add_calendar_event, get_calendar_event], model=model, max_steps=1)

# Example interactions
response = calendar_agent.run("Add a calendar event 'Meeting with Mohammad'")
print(response)

response = calendar_agent.run("What is my event?")
print(response)
