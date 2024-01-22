import random
from datetime import datetime


def run(args, response: str):
    return random.choice(response).replace('[time]', datetime.now().strftime("%H:%M"))
