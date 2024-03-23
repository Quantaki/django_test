from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.utils.translation import activate # if you to force translate to another language..

from translate.models import Test
# Create your views here.

def home_view(request) :

    context = {
        "data" : Test.objects.all(),
    }
    return render(request, "translate/home.html", context=context)


