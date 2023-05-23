from flask import Flask, render_template, request
import requests
import time
app = Flask(__name__)

# Chatbot Backend
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.memory import ChatMessageHistory

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
# chat = ChatOpenAI(temperature=0.9, max_tokens=500)
# chat = ChatOpenAI(temperature=0, openai_api_key=os.environ['OPENAI_API_KEY'])
chat = ChatOpenAI(temperature=0, openai_api_key=api_key,max_tokens=50)#,model_name="gpt-4")
history = ChatMessageHistory()



# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling API requests
@app.route('/chat', methods=['POST'])
def get_chat():
    # Get the user's message from the request
    message = request.form['message']
    history.add_user_message(message)

    # Make a request to the chatbot API
    response = chat(history.messages).content
    # response = f"your message was {message}, the response was {response.content}"
    # response = f"this is the current history {history}"
    
    time.sleep(1)
    # response = "this is the response"
    history.add_ai_message(response)

    # response = response.content

    # Return the response to the client
    return response

# # Function to make a request to the chatbot API
# def chatbot_api_request(message):
#     # Make a request to the chatbot API with the user's message
#     response = requests.post('YOUR_CHATBOT_API_URL', json={'message': message})
    
#     # Get the response from the chatbot API
#     response_data = response.json()

#     # Extract the chatbot's response
#     chatbot_response = response_data['response']

#     # Return the chatbot's response
#     return chatbot_response

if __name__ == '__main__':
    app.run(debug=True)
