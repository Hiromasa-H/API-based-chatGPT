from flask import Flask, render_template, request, jsonify
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
from langchain.callbacks import get_openai_callback


import os

def create_file(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        # File doesn't exist, create it
        with open(file_path, "w") as file:
            # Writing some initial content to the file
            file.write("")
        print(f"File '{file_path}' created successfully.")
    else:
        print(f"File '{file_path}' already exists.")


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

max_tokens = 500

# chat = ChatOpenAI(temperature=0.9, max_tokens=500)
# chat = ChatOpenAI(temperature=0, openai_api_key=os.environ['OPENAI_API_KEY'])
chat = ChatOpenAI(temperature=0, openai_api_key=api_key,max_tokens=max_tokens)#,model_name="gpt-4")
history = ChatMessageHistory()

create_file('total_tokens.txt')
with open('total_tokens.txt', 'r') as file:
    total_tokens = int(file.read())
total_cost = 0
# total_tokens = 0

if os.path.exists('instructions.txt'):
    with open('instructions.txt', 'r') as file:
        instructions = str(file.read())
    instructions = SystemMessage(content=instructions)
else:
    instructions = None

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling API requests
@app.route('/chat', methods=['POST'])
def get_chat():
    global total_cost,history,total_tokens
    # Get the user's message from the request
    message = request.form['message']
    history.add_user_message(message)
    response = dict()

    # Make a request to the chatbot API
    with get_openai_callback() as cb:
        if instructions is not None:
            chat_response = chat([instructions]+history.messages).content
        else:
            chat_response = chat(history.messages).content
        message_tokens = cb.total_tokens

        # chat_response = f"{[instructions]+history.messages}"#"this is the response"
        # message_tokens = 10

        total_tokens += message_tokens
        
        # message_cost = message_tokens * 0.000002
        # message_cost = 18.0 * 0.000002

        with open('total_tokens.txt', 'w') as file:
            file.write(str(total_tokens))

        # print(f"total cost: {total_tokens,total_cost}")
    # response = f"your message was {message}, the response was {response.content}"
    # response = f"this is the current history {history}"
    
    # time.sleep(0.3)
    # response = "this is the response"
    history.add_ai_message(chat_response)

    # response = response.content

    # Return the response to the client
    response['message'] = chat_response
    response['message_tokens'] = message_tokens
    response['total_cost'] = total_tokens * 0.000002
    response['total_tokens'] = total_tokens

    return jsonify(response)
    # return response

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
