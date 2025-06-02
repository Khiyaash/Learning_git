from pydantic import BaseModel # type: ignore
from typing import List,Dict, Optional

class User(BaseModel):
    username: str
    password: Optional[str] = None
    likes: Dict[str,int]

class comment(BaseModel):
    author: str
    comment: str
    likes: int

class Post(BaseModel):
    author: str
    coauthor: Optional[str] = None
    date: str
    title: str
    content: str
    id: int
    likes: List[str]
    comments: List[comment]


comments = [
    comment(author="johndoe",
    comment="This is a comment!",
    likes=2)]

post = Post(author="johndoe",
co_author="janedoe",
date="1/1/1970",
title="Cool post",
content="Cool content",
id=10101,
likes=["johndoe","janedoe"],
comments=comments)

print(post)