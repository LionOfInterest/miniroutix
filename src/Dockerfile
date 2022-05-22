FROM python:slim-bullseye

RUN apt update && apt upgrade -yq

RUN apt install gcc -y

COPY . /app/

WORKDIR /app/

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "app.py" ]
