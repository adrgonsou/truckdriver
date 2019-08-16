FROM python:3
ADD . /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python","app.py"]