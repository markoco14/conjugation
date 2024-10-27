from typing import Union

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()

templates = Jinja2Templates(directory="templates")

PRONOUNS = ["I", "You", "He", "She", "It", "We", "They"]
NAMES = [
    "Todd", "Jane", "John", "Alice", "Bob", "Eve", "Charlie", "Carol", "David",
    "Frank", "Grace", "Hank", "Ivy", "Jack", "Kara", "Liam", "Mona", "Nate",
    "Olivia", "Paul", "Quinn", "Rachel", "Sam", "Tina", "Uma", "Victor",
    "Wendy", "Xander", "Yara", "Zane"
]

TWO_NAMES = [f"{random.choice(NAMES)} and {random.choice(NAMES)}" for _ in range(2)]

@app.get("/")
def read_root(
    request: Request,
):
    list1 = [random.choice(PRONOUNS) for _ in range(3)]
    list1.append(random.choice(NAMES))
    list1.append(random.choice(NAMES))
    list1.append(random.choice(NAMES))
    list1.append(random.choice(TWO_NAMES))
    list2 = [random.choice(PRONOUNS) for _ in range(3)]
    list2.append(random.choice(NAMES))
    list2.append(random.choice(NAMES))
    list2.append(random.choice(NAMES))
    list2.append(random.choice(TWO_NAMES))
    list3 = [random.choice(PRONOUNS) for _ in range(3)]
    list3.append(random.choice(NAMES))
    list3.append(random.choice(NAMES))
    list3.append(random.choice(NAMES))
    list3.append(random.choice(TWO_NAMES))
    print(list1)
    context = {
        "request": request,
        "list1": list1,
        "list2": list2,
        "list3": list3,
    }
    return templates.TemplateResponse("index.html", context)
