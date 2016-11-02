from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from finance.forms import ChargesForm
from finance.generator import random_transactions

def get_value_date(request):
	if request.method == 'POST':
		form = ChargesForm(request.POST)
		info = 'Форма заполнена, но некорректна'
		if form.is_valid():
			info = 'Форма заполнена и корректна'
			#return HttpResponseRedirect('/charges/')
		return render(request, 'finance/charges.html', {'form': form, 'info': info})
	else:
		info = 'Форма не заполнена'
		form = ChargesForm()
		return render(request,'finance/charges.html',{'form': form,'info': info})


def table_page(request):
	transactions = random_transactions()
	income = list()
	outcome = list()
	for each in transactions:
		if each[1] > 0:
			income.append(each)
		else:
			outcome.append([each[0], -1 * each[1]])
	return render(request, 'finance/table.html', {'income': income, 'outcome': outcome})


