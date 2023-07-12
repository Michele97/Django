from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from Anagrafica.models import Cliente,Contratto,Pagamento
from Anagrafica.serializers import ClienteSerializer, ContrattoSerializer, PagamentoSerializer

# Creazione API per Cliente

@csrf_exempt
def ClienteAPI(request,id=None):
    if request.method == 'GET': 
        clienti = Cliente.objects.all()
        clienti_serializer = ClienteSerializer(clienti, many=True)
        return JsonResponse(clienti_serializer.data, safe=False)
    
    elif request.method == 'POST':
        clienti_data =JSONParser().parse(request)   
        clienti_serializer = ClienteSerializer(data=clienti_data)   
        if clienti_serializer.is_valid():
            clienti_serializer.save()
            return JsonResponse("Add Successfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
        
    elif request.method == 'PUT':
        clienti_data =JSONParser().parse(request)
        clienti = Cliente.objects.get(clienteId=clienti_data['clienteId']) 
        clienti_serializer = ClienteSerializer(clienti, data=clienti_data)
        if clienti_serializer.is_valid():
            clienti_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    
    elif request.method == 'DELETE':
        if id is not None:
            # Logica per eliminare il cliente corrispondente all'ID
            cliente = Cliente.objects.get(clienteId=id)
            cliente.delete()
            return JsonResponse("Deleted Successfully!!", safe=False)
        else:
            return JsonResponse("ID not provided", status=400, safe=False)
    else:
        return JsonResponse("Invalid request method", status=400, safe=False)

    
#Creazione API per Contratto

@csrf_exempt
def ContrattoAPI(request,id=0):
    if request.method == 'GET': 
        contratti = Contratto.objects.all()
        contratti_serializer = ContrattoSerializer(contratti, many=True)
        return JsonResponse(contratti_serializer.data, safe=False)
    
    elif request.method == 'POST':
        contratti_data =JSONParser().parse(request)   
        contratti_serializer = ContrattoSerializer(data=contratti_data)
        print(contratti_data)
        print(contratti_serializer)
        if contratti_serializer.is_valid():
            contratti_serializer.save()
            return JsonResponse("Add Successfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
        
    elif request.method == 'PUT':
        contratti_data =JSONParser().parse(request)
        contratti = Contratto.objects.get(id_contratto=contratti_data['id_contratto']) 
        contratti_serializer = ContrattoSerializer(contratti, data=contratti_data)
        if contratti_serializer.is_valid():
            contratti_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    
    elif request.method == 'DELETE':
        contratti=Contratto.objects.get(id_contratto=id)
        contratti.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)
    
#Creazione API per Pagamenti

@csrf_exempt
def PagamentoAPI(request,id=0):
    if request.method == 'GET': 
        pagamenti = Pagamento.objects.all()
        pagamenti_serializer = PagamentoSerializer(pagamenti, many=True)
        return JsonResponse(pagamenti_serializer.data, safe=False)
    
    elif request.method == 'POST':
        pagamenti_data =JSONParser().parse(request)   
        pagamenti_serializer = PagamentoSerializer(data=pagamenti_data)
        if pagamenti_serializer.is_valid():
            pagamenti_serializer.save()
            return JsonResponse("Add Successfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
        
    elif request.method == 'PUT':
        pagamenti_data =JSONParser().parse(request)
        pagamenti = Pagamento.objects.get(id_Pagamento=pagamenti_data['id_Pagamento']) 
        pagamenti_serializer = PagamentoSerializer(pagamenti, data=pagamenti_data)
        if pagamenti_serializer.is_valid():
            pagamenti_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    
    elif request.method == 'DELETE':
        pagamenti=Pagamento.objects.get(id_Pagamento=id)
        pagamenti.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)