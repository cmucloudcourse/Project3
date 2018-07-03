FROM ubuntu:latest
RUN apt-get update && apt-get install -y python-pip && pip install flask
COPY pyService.py /
EXPOSE 6000
CMD ["python", "pyService.py"]