FROM ubuntu

RUN apt update
RUN apt install python3-pip -y

RUN pip install flask

COPY . /9

CMD python3 /9/Server.py
