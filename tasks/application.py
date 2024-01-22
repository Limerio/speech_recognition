import random
import subprocess


def run(args, response):
    subprocess.run(f'pythonw utils/run_process.py {args[1]}')
    return random.choice(response).replace("[application]", args[1])
