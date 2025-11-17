FROM python:3.12-slim

WORKDIR /app

COPY . .

CMD python argparse_dialogue.py --age 23 --name "Victor" --gender "Male"