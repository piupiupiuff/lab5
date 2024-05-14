FROM python:3
WORKDIR /lab2
COPY 12.py /lab2/lab2.py
ENTRYPOINT ["python3", "lab2.py"]