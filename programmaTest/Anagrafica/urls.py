from django.urls import re_path
from Anagrafica import views

urlpatterns =[
    re_path(r'cliente/$',views.ClienteAPI),
    re_path(r'cliente/([0-9]+)$',views.ClienteAPI),
    re_path(r'contratto/$',views.ContrattoAPI),
    re_path(r'contratto/([0-9]+)$',views.ContrattoAPI),
    re_path(r'pagamenti/$',views.PagamentoAPI),
    re_path(r'pagamenti/([0-9]+)$',views.PagamentoAPI)
]