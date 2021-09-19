FROM python:3.7-buster

COPY ./ /app
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r /app/requirements.txt

WORKDIR /app
CMD ["python3", "app.py"]
EXPOSE 5000:5000
