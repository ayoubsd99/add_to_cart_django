from django.shortcuts import render
from django.views import View
# Create your views here.
import  simplejson as JSON
#from django.http import JsonResponse
from django.http import HttpResponse

from app.models import Item

def item_info(item):
    return{
        'id':item.id,
        'title':item.title,
        'price':item.price,
        'description':item.description
    }

def list_items(request):
    data={}
    json_items=[]
    for item in Item.objects.all():
        json_items.append(item_info(item))
    data['items']=json_items

    return HttpResponse(JSON.dumps(data),content_type='application/json')


class ItemsView(View):
    template='index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template)
        

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')