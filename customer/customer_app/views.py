from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest

# Create your views here.
from django.shortcuts import render
from customer_app.customer_services import get_product_ids

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from customer_app.models import Customer
from customer_app.serializers import CustomerSerializer



@csrf_exempt
def api_list(request):

    if request.method == 'GET':
        apivar = Customer.objects.all()
        serializer = CustomerSerializer(apivar, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        product_id = data.get('product_id')
        if product_id is None:
            return HttpResponseBadRequest("product_id is required")
        
        product_ides = get_product_ids()
        if product_id not in product_ides:
            return HttpResponseBadRequest("Invalid product id")
        
        try:
            # Check if the customer already has a product
            existing_customer = Customer.objects.get(product_id=product_id)
            return HttpResponseBadRequest("Product already has a customer")
        except Customer.DoesNotExist:
            pass 
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def api_detail(request, pk):

    try:
        dvar = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CustomerSerializer(dvar)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(dvar, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        dvar.delete()
        return HttpResponse(status=204)