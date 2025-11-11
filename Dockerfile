FROM python:3.10.2-slim as base

WORKDIR /app

COPY . .

CMD python argparse_dialogue.py