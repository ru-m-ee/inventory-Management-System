import requests
import json

def get_customer_ids():
    url = 'http://127.0.0.1:8004/customer/'

    try:
        response = requests.get(url)
        response.raise_for_status()
        customer_data = response.json()
        print(customer_data)
        customer_ids = [customer['id'] for customer in customer_data]
        return customer_ids
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving customer data: {e}")
        return None
