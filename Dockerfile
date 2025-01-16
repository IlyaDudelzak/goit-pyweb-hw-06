FROM python:3.13-slim

ENV APP_HOME /app 

WORKDIR $APP_HOME

COPY . .

RUN pip install --no-cache -r requirements.txt 

VOLUME $APP_HOME/db

ENTRYPOINT [ "python", "app/main.py" ]

