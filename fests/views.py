from django.shortcuts import render
from django.http import HttpResponse
from fests.models import Fest
import json

def home(request):
	return render(request, 'fests/fests.html')

def fests(request):
	sort = request.GET.get('sort', 'name')
	if request.GET.get('sort_dest', 'asc') == 'desc':
		sort = "-"+sort

	objs = Fest.objects.all()
	f = request.GET.get("filter")
	if f:
		objs = objs.filter(name__startswith=f.strip())
	objs = objs.order_by(sort)

	j = []
	for obj in objs:
		j.append(obj.get_dict())

	return HttpResponse(json.dumps(j))
