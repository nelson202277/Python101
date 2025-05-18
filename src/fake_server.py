from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Literal
import re

app = FastAPI()


class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


class ChatRequest(BaseModel):
    model: str
    messages: List[Message]
    temperature: float = 1.0
    max_tokens: int = 16


@app.post("/v1/chat/completions")
async def chat_completions(request: ChatRequest):
    question = request.messages[0].content
    match = re.search(r"america|china|japan", question.lower())
    response = match.group()[::-1] if match else "I don't know"
    return {
        "id": "chatcmpl-fake-id",
        "object": "chat.completion",
        "created": 1234567890,
        "model": request.model,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": response,
                },
                "finish_reason": "stop",
            }
        ],
        "usage": {"prompt_tokens": 10, "completion_tokens": 10, "total_tokens": 20},
    }
