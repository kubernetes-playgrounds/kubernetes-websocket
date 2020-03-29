FROM python:3

ADD server.py /
ADD requirements.txt /

RUN pip install -r requirements.txt
EXPOSE 8090
CMD [ "python", "-u", "./server.py" ]