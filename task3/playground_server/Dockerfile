FROM ubuntu:latest
RUN apt-get update && apt-get install -y python-pip && pip install flask
COPY pyService.py /playground_server/
EXPOSE 6000
CMD ["python", "/playground_server/pyService.py"]