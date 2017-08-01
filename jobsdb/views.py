from django.shortcuts import render

from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views import generic

from .models import Location, Connection


class IndexView( generic.ListView):
    template_name = 'jobsdb/index.html'
    context_object_name = 'location_list'
    model= Location
    

    def get_queryset(self):
        """Return the  location by order alphabetic."""
        return Location.objects.order_by('id')
   


    def get(self, *args, **kwargs):
    
        asjson = self.request.GET.get('asjson', "false")
        asjson=asjson.lower()=="true"
          
        if not asjson:
            return super(IndexView, self).get(*args, **kwargs)
        #https://stackoverflow.com/questions/39768671/how-to-return-jsonresponse-in-django-generic-listview
        
       
        #Get a specific fileds from queryset
        #https://docs.djangoproject.com/en/1.7/topics/serialization/
        
        data = [{"location_id": location.id, "location_name": location.location_name} for location in Location.objects.all()]
        
        return JsonResponse(data,safe=False)



class DetailView(generic.DetailView):
      model = Location
      template_name = 'jobsdb/connection_list.html'
