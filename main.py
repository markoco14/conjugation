from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import random

from grammar import PRONOUNS, NAMES, TWO_NAMES, PRESENT_SIMPLE_PLUS_S, PRESENT_SIMPLE_PLUS_ES, PRESENT_SIMPLE_PLUS_IES

app = FastAPI()

templates = Jinja2Templates(directory="templates")



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
    s_verb = random.choice(PRESENT_SIMPLE_PLUS_S)
    es_verb = random.choice(PRESENT_SIMPLE_PLUS_ES)
    ies_verb = random.choice(PRESENT_SIMPLE_PLUS_IES)
    context = {
        "request": request,
        "list1": list1,
        "list2": list2,
        "list3": list3,
        "s_verb": s_verb,
        "es_verb": es_verb,
        "ies_verb": ies_verb,
    }
    return templates.TemplateResponse("index.html", context)
