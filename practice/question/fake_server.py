from fastapi import FastAPI
import pandas as pd

from typing import List
from pydantic import BaseModel, Field


class EchoRequest(BaseModel):
    message: str


class Answer(BaseModel):
    Country: str = Field()
    City: str = Field()
    Famous_Food: str = Field()

    def __eq__(self, other):
        assert isinstance(other, Answer), "Only works for same class"
        return (
            self.City == other.City
            and self.Country == other.Country
            and self.Famous_Food == other.Famous_Food
        )


ANSWER = pd.read_csv("../answer/common.csv")
ANSWER = list(
    map(
        lambda x: Answer(**x),
        ANSWER.sort_values(by="Country").to_dict(orient="records"),
    )
)

app = FastAPI()


@app.get("/")
def hello_world():
    return "hello_world"


@app.post("/echo/")
def echo(message: EchoRequest):
    return_message = message.message[::-1]
    return f"Message recieve: {message.message}... {return_message}"


@app.post("/check_answer/")
def check_answer(answers: List[Answer]):
    print(answers)
    if len(answers) != len(ANSWER):
        return "Wrong!"
    print([(i, j) for i, j in zip(ANSWER, answers)])
    print([i == j for i, j in zip(ANSWER, answers)])
    if any(i != j for i, j in zip(ANSWER, answers)):
        return "Wrong!"

    return "Correct!"
