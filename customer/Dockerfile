FROM python:3.10
ENV PYTHONUNBUFFERED 1

WORKDIR /customer .
COPY . .

RUN pip install --upgrade pip
RUN pip install -r /customer/requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
