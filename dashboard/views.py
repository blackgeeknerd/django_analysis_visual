from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from dashboard.models import Order

# Create your views here.

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})


#function that sends the response with data to the pivot
#table on the apps' frontend
def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


