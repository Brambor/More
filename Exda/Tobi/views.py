from django.core.cache import caches
from django.views.generic import View

import simplejson as json

from .models import mydb


class Basic_view(View):
	def get(self, id):
		if mydb.objects.filter(id=id).exists():
			record = mydb.objects.get(id=id)
		else:
			record = mydb(id=id)
		record.n_of_requests += 1
		record.save()

		cache = caches["default"]
		ch = cache.get(id)

		if ch != None: #if ch in cache
			return json.dumps(ch)
		else:
			product = PostgreDriver.getProductById(id)
			#save to cache
			cache.set(id, product, None) #None because 'Cache je nekonečná– nemusíte se starat o její invalidaci. Jednou zacachovaná data nepotřebujeme nikdy mazat.'
			return json.dumps(product)