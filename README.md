# Making Actual AI

Learning Python, GitHub, and AI by building a local chatbot, one step at a time.

## First version

This Python program chats with Qwen through Ollama on your own computer.
It remembers messages during the current session. Closing the program clears
the conversation; nothing is saved to disk.

## Run it

1. Install Python 3 and [Ollama](https://ollama.com/download/mac).
2. Open Ollama and download the model if needed: `ollama pull qwen3.5:4b`.
3. From this project folder, run `python3 chat.py`.
4. Type a message. Use `/bye` to quit.

No extra Python packages or paid API keys are required. Internet is needed
to download the software and model; chat requests go to local Ollama.

## What we are learning

- `input()` reads what you type; `print()` shows a reply.
- A `while` loop repeats the conversation.
- A list called `messages` stores the conversation.
- An API is a way for programs to communicate. We use Ollama's local chat API.
- Git records checkpoints called commits; GitHub hosts a copy of the project.

The model has a limited context window, so very long conversations will not
retain every earlier detail. This is a learning prototype.
