from django.core.cache import caches
from django.http import HttpResponse
from django.views.generic import View

import json

from .models import mydb, PostgreDriver #Tenhle PostgreDriver je zkušební


class Basic_view(View): # http://127.0.0.1:8000/14/ třeba
	def get(self, request, id):
		a = mydb.objects.filter(id=id).exists()
		if a:
			record = mydb.objects.get(id=id)
		else:
			record = mydb(id=id)
		record.n_of_requests += 1
		record.save()

		cache = caches["default"]
		ch = None #cache.get(id)

		if ch != None: #if ch in cache
			return HttpResponse(json.dumps(ch), content_type="application/json")
		else:
			product = PostgreDriver.getProductById(id) # dá json data
			#save to cache
			cache.set(id, product, None) #None protože 'Cache je nekonečná– nemusíte se starat o její invalidaci. Jednou zacachovaná data nepotřebujeme nikdy mazat.'
			return HttpResponse(json.dumps(product), content_type="application/json")