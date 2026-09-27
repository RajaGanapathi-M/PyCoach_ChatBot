import os
import gradio as gr
# pyrefly: ignore [missing-import]
import spaces
from huggingface_hub import InferenceClient

hf_token = os.environ.get("HF_TOKEN")
client = InferenceClient(token=hf_token)

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are PyCoach, an expert Python Full-Stack & AI Trainer. "
        "Explain programming concepts clearly, debug code, "
        "and provide structured, encouraging examples."
    )
}

# The @spaces.GPU decorator satisfies ZeroGPU's startup checker
@spaces.GPU
def stream_chat(message, history):
    if not hf_token:
        yield "⚠️ Missing HF_TOKEN! Please configure it under Space Settings -> Variables and secrets."
        return

    # Build message history
    messages = [SYSTEM_PROMPT]
    if history:
        for turn in history:
            if isinstance(turn, (list, tuple)) and len(turn) >= 2:
                if turn[0]:
                    messages.append({"role": "user", "content": str(turn[0])})
                if turn[1]:
                    messages.append({"role": "assistant", "content": str(turn[1])})
            elif isinstance(turn, dict) and "role" in turn and "content" in turn:
                messages.append(turn)

    messages.append({"role": "user", "content": str(message)})

    try:
        response_stream = client.chat.completions.create(
            model="Qwen/Qwen2.5-72B-Instruct",
            messages=messages,
            max_tokens=512,
            stream=True
        )

        partial_reply = ""
        for chunk in response_stream:
            if chunk.choices and len(chunk.choices) > 0:
                delta = chunk.choices[0].delta
                if hasattr(delta, "content") and delta.content:
                    partial_reply += delta.content
                    yield partial_reply

        if not partial_reply:
            yield "I processed your request, but received an empty response. Please try rephrasing."

    except Exception as err:
        yield f"⚠️ API Error: {err}"

demo = gr.ChatInterface(
    fn=stream_chat,
    title="🐍 PyCoach AI",
    description="Your interactive Python mentor & debugger.",
    examples=[
        ["What is the difference between a list and a tuple?"],
        ["How do Python decorators work behind the scenes?"],
        ["Explain list comprehensions with a quick code snippet."]
    ],
    cache_examples=False  # Stops the container from attempting to pre-run examples on start
)

if __name__ == "__main__":
    demo.launch()