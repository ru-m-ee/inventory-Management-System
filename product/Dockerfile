FROM python:3.10
ENV PYTHONUNBUFFERED 1

WORKDIR /home/rumee/inventory-Management-System/customer/product
COPY ./home/rumee/inventory-Management-System/product/requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
