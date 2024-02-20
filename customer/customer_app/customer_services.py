import requests
import json

def get_product_ids():
    url = 'http://127.0.0.1:8005/product/'

    try:
        response = requests.get(url)
        response.raise_for_status()
        product_data = response.json()
        print(product_data)
        product_ids = [product['id'] for product in product_data]
        return product_ids
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving product data: {e}")
        return None