# API-based-chatGPT

This repository contains code for a web application that enables the user to use chat-GPT3.5 or chat-GPT4 via an API.

The UI is still rough, but here's a screenshot:

![](readme_content/screenshot.png)

## Prerequisites

- Create a paid account on [OpenAI](https://beta.openai.com/).
- Create and save your API key

## Installation
1. Clone this repository `git clone https://github.com/Hiromasa-H/API-based-chatGPT.git`
2. Install the requirements `pip install -r requirements.txt`
3. create a `.env` file in the root directory and add the following lines:
```
OPENAI_API_KEY=<your API key>
```
4. run `python3 app.py` 


## Optional
- To give your chatbot some instructions, simply create a file called `instructions.txt` in the root directory and add your instructions there. The instructions will be sent to the API before the chat starts.

## TODO
- [ ] Add past conversation history
- [ ] Add GPT4
- [x] Add instructions
- [ ] Allow new lines in input field
- [ ] Add profile pictures?
- [ ] Add stream ability
- [ ] Use multiple chat API modules at once to generate chats