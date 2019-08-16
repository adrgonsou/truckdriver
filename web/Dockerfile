FROM python:3
ADD . /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
#RUN pip install --upgrade pip
CMD ["python","app.py"]