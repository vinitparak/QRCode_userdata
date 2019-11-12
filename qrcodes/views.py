from django.shortcuts import render
from .models import qrcod
import request
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import QRForm
import pyqrcode 
from pyqrcode import QRCode 
# Create your views here.

def index(request):
	return render(request,'index.html')

def topics(request):
	topics = qrcod.objects.order_by('date_added')
	context = {'topics':topics}
	return render(request, 'qrcode.html', context)
	
def qr_topic(request):
	if request.method != 'POST':
		form = QRForm()
	else:
		form = QRForm(data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('qrcodes:topics'))

	context = {'form': form}
	return render(request, 'qrform.html', context)

def output(request):
	output = qrcod.objects.latest('date_added')
	result = str(output)	
	context = {'output':output}
	url = pyqrcode.create(result)
	url.svg("vinit12.svg", scale = 8)
	return render(request,'index.html', context)