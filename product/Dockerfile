FROM python:3.10
ENV PYTHONUNBUFFERED 1

WORKDIR /product .
COPY . .

RUN pip install --upgrade pip
RUN pip install -r /product/requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
