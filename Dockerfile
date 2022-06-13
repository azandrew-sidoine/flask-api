FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install vim -y

WORKDIR /home

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3000

CMD [ "python3","/home/src/app.py" ]

