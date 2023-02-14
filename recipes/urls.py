from django.http import HttpResponse
from django.urls import path

from recipes.views import home


def sobre(request):
    return HttpResponse("Oi, Roberto!")


urlpatterns = [
    path('', home),
    path("sobre", sobre),

]
