from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
import requests


@api_view(['GET'])
def rates(request):
    currencies = []
    from_value = (request.GET.getlist("from")[0])
    to_value = (request.GET.getlist("to")[0])
    value = (request.GET.getlist("value")[0])
    currencies.append(from_value)
    currencies.append(to_value)
    data = requests.get(f'https://exchange-rates-api.oanda.com/v2/rates/spot.json?api_key=LsNKUer4KkPC3Jpf38p8ysGz&base={from_value}&quote={to_value}')
    print(data.json()['quotes'][0]['midpoint'])
    result = float(data.json()['quotes'][0]['midpoint']) * float(value)
    return Response({"result": result})
