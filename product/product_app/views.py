from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from product_app.models import Product
from product_app.serializers import ProductSerializer
from product_app.product_services import get_customer_ids


@csrf_exempt
def p_list(request):

    if request.method == 'GET':
        pvar = Product.objects.all()
        serializer = ProductSerializer(pvar, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        customer_id = data.get('customer_id')
        if customer_id is None:
            return HttpResponseBadRequest("customer_id is required")

        customer_ids = get_customer_ids()

        if customer_id not in customer_ids:
            return HttpResponseBadRequest("Invalid customer_id")
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    


@csrf_exempt
def p_detail(request, pk):

    try:
        pdvar = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(pdvar)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(pdvar, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pdvar.delete()
        return HttpResponse(status=204)