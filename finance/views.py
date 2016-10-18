from django.shortcuts import render
from django.http import HttpResponse


def front_page(request):
	return render(request, 'finance/index.html')

def charges_page(request):
	return render(request, 'finance/context.html')



# Create your views here.
