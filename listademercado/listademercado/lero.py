from django.shortcuts import render
from rest_framework.decorators import api_view


@api_view()
def lero(request):

    return render(request, 'lero.html')
