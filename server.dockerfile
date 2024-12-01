FROM python:3.9
COPY ./requirements.txt requirements.txt
COPY ./README.md README.md
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./app app
CMD ["fastapi", "run", "app/main.py", "--port", "8889"]
