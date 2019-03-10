import sys

def write(text, flush=True):
    sys.stdout.write(text)
    if flush:
        sys.stdout.flush()

def inplace_write(text, last_len, flush=True):
    write("\r" + text + (max(last_len - len(text), 0) * " "))

def backspace(n=1):
    write("\b \b" * n)
