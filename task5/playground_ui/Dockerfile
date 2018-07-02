FROM ubuntu:latest
RUN apt-get update && apt-get install -y python-pip && pip install flask requests
COPY playground.py /playground_ui/
COPY site /playground_ui/site
EXPOSE 5000
CMD ["python", "/playground_ui/playground.py"]
