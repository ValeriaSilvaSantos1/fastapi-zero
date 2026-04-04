from pydantic import BaseModel


class Message(BaseModel):
    Message: str


class Age(BaseModel):
    Age: int


class User(BaseModel):
    Name: str
