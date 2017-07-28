from django.shortcuts import render

from django.http import HttpResponse
import json

from django.views import generic

from .models import Location, Connection


class IndexView( generic.ListView):
    template_name = 'jobsdb/index.html'
    context_object_name = 'location_list'
    model= Location
    

    def get_queryset(self):
        """Return the  location by order alphabetic."""
        return Location.objects.order_by('id')

class DetailView(generic.DetailView):
      model = Location
      template_name = 'jobsdb/connection_list.html'
