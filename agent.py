from agno.agent import Agent
from agno.models.openai import OpenAIChat 
from agno.tools.googlecalendar import GoogleCalendarTools
import datetime
import os
from tzlocal import get_localzone_name

# Storage 
from agno.storage.postgres import PostgresStorage 

credentials_path = "client_secret_126868835843-nmika7ldh47eqrmeln65h8vsaqh74ec5.apps.googleusercontent.com.json"
agent_id = 'gpt-4o'
db_url = 'postgresql+psycopg://ai:ai@localhost:5532/ai'

agent = Agent(
    name="Google Calendar Assistant",
    model=OpenAIChat(id=agent_id),
    storage=PostgresStorage(
        table_name='agent_sessions', 
        db_url=db_url, 
    ),
    instructions=[
        f"""
        You are scheduling assistant . Today is {datetime.datetime.now()} and the users timezone is {get_localzone_name()}.
        You should help users to perform these actions in their Google calendar:
            - get their scheduled events from a certain date and time
            - create events based on provided details
        """
    ],
    tools=[GoogleCalendarTools(credentials_path=credentials_path)], 
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    add_history_to_messages=True, 
    debug_mode=True, 
)

# agent.print_response("Give me the list of todays events", markdown=True)