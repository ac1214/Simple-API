FROM python:3.5.9-stretch

RUN pip install flask

COPY ./app.py /deploy/

WORKDIR /deploy/

EXPOSE 80

ENTRYPOINT ["python", "app.py"]
