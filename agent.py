from agno.agent import Agent
from agno.tools.googlecalendar import GoogleCalendarTools
import datetime
import os
from tzlocal import get_localzone_name

credentials_path = "client_secret_126868835843-nmika7ldh47eqrmeln65h8vsaqh74ec5.apps.googleusercontent.com.json"
agent = Agent(
    tools=[GoogleCalendarTools(credentials_path=credentials_path)],
    show_tool_calls=True,
    instructions=[
        f"""
        You are scheduling assistant . Today is {datetime.datetime.now()} and the users timezone is {get_localzone_name()}.
        You should help users to perform these actions in their Google calendar:
            - get their scheduled events from a certain date and time
            - create events based on provided details
        """
    ],
    add_datetime_to_instructions=True,
)

agent.print_response("Give me the list of todays events", markdown=True)