"""Our first chatbot: Python talks to a model running in Ollama."""

import json
from urllib import request, error


def main():
    # This list holds the conversation until we close the program.
    messages = [
        {"role": "system", "content": "You are a friendly assistant. Explain things clearly and simply."}
    ]
    print("Your local chatbot is ready. Type /bye to quit.")

    while True:
        try:
            user_text = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if user_text == "/bye":
            print("Goodbye!")
            break
        if not user_text:
            continue

        messages.append({"role": "user", "content": user_text})
        payload = json.dumps({
            "model": "qwen3.5:4b",
            "messages": messages,
            "stream": False,
            "think": False,
            "options": {"num_ctx": 4096},
        }).encode("utf-8")
        # localhost means this request goes to our own computer.
        api_request = request.Request(
            "http://127.0.0.1:11434/api/chat",
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        print("Thinking…", flush=True)
        try:
            with request.urlopen(api_request, timeout=180) as response:
                reply = json.load(response)["message"]["content"]
        except (error.URLError, TimeoutError, OSError, ValueError, KeyError) as exc:
            messages.pop()
            print("Could not get a reply. Check that Ollama is running and qwen3.5:4b is installed.")
            print("Details:", exc)
            continue

        print("AI:", reply)
        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
