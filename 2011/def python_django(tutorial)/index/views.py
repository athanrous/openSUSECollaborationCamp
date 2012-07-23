from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    onoma = 'zoumpis'
    eponimo = 'zoumpis-rousinopoulos'
    arithmos_mitroou = '666'
    return render_to_response(
            'index.html',
            {'name': onoma, 'surname': eponimo, 'reg_id': arithmos_mitroou },
            context_instance = RequestContext(request))
