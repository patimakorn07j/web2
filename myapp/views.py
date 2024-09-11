from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def pic1(request):
	return render(request, 'pic1.html')

def pic2(request):
	return render(request, 'pic2.html')

def pic3(request):
	return render(request, 'pic3.html')

def myself(request):
	return render(request, 'myself.html')