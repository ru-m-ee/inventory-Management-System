from rest_framework import serializers
from customer_app.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'username', 'email', 'product_id']