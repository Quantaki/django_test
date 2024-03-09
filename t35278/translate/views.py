from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.utils.translation import activate # if you to force translate to another language..
# Create your views here.

def home_view(request) :

    lang_pref = request.LANGUAGE_CODE
    trans_text = _("Hello world !")

    return HttpResponse(f"Text should be translated to {lang_pref} : {trans_text}")


