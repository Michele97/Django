from rest_framework import serializers
from Anagrafica.models import Cliente, Contratto, Pagamento

class ClienteSerializer(serializers.ModelSerializer):
   class Meta:
       model = Cliente
       
       fields = ('clienteId',
                'aziendaFlag',
                'clienteName', 
                'clienteCognome', 
                'clienteCodF', 
                'clienteregione', 
                'clientepiva' 
                )
       
class ContrattoSerializer(serializers.ModelSerializer):
    
    class Meta:
       model = Contratto
       
       fields = ('id_contratto', 
                'importo', 
                'cliente', 
                'data',
                'scadenzaContratto',
                )
       
class PagamentoSerializer(serializers.ModelSerializer):
   class Meta:
       model = Pagamento
       fields = ('id_Pagamento',
                'dataPaga',
                'importo', 
                'id_Contratto'
                )