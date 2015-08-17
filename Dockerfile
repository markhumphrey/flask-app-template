FROM python:2.7

WORKDIR /my_app
RUN virtualenv /env
ADD requirements.txt /my_app/requirements.txt
RUN /env/bin/pip install -r /my_app/requirements.txt
ADD . /my_app

EXPOSE 8080
CMD ["/env/bin/python", "main.py"]
