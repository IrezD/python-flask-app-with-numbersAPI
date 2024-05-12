FROM python:alpine

WORKDIR /home

COPY . /home

RUN pip install flask \
    pip install requests

EXPOSE 5000

CMD [ "python", "main.py" ]
