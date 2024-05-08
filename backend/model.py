from pydantic import BaseModel, Field
from datetime import datetime


# Token model for token response
class Token(BaseModel):
    access_token: str
    token_type: str
    
# class PostBase(BaseModel):
#     title: str
#     content: str
#     user_id: int

class Librarian(BaseModel):
    librarian_name: str
    password: str
    active: bool = Field(default=False)

class UserBase(BaseModel):
    username: str
    email : str
    password : str
    has_issued: bool = Field(default=False)

class Book(BaseModel):
    title : str
    author : int
    publisher : int
    category: int
    copies : int  = Field(default=1)

class BookIssueRecord(BaseModel):
    book_id: int
    user_id: int
    issue_time: str

class Author(BaseModel):
    name: str

class Publisher(BaseModel):
    name: str

class BookIssue(BaseModel):
    book_id: int
    user_id: int
    issued_by: int
    issue_time: datetime =None

class Category(BaseModel):
    name: str