import os
import dialogflow_v2 as dialogflow
from google.api_core.exceptions import InvalidArgument

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/google/credentials.json"

DIALOGFLOW_PROJECT_ID = "your-project-id"
DIALOGFLOW_LANGUAGE_CODE = "pt-BR"
SESSION_ID = "your-session-id"

def detect_intent(text):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

    text_input = dialogflow.types.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    return response.query_result.fulfillment_text

while True:
    user_input = input("Você: ")
    response = detect_intent(user_input)
    print("Bot: " + response)
