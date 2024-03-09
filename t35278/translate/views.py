from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
# Create your views here.

def home_view(request) :
    trans_text = _("Hello world !")
    lang_pref = request.LANGUAGE_CODE
    return HttpResponse(f"Text should be translated to {lang_pref} : {trans_text}")
