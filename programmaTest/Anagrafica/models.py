from django.db import models


# Create your models here.

class Cliente(models.Model):
    clienteId = models.AutoField(primary_key=True)
    aziendaFlag = models.BooleanField(default=False )
    clienteName = models.CharField(max_length=20,  null=True, blank=True)
    clienteCognome = models.CharField(max_length=20,  null=True, blank=True)
    clienteCodF = models.CharField(max_length=16,  null=True, blank=True)
    clienteregione = models.CharField(max_length=50,  null=True, blank=True)
    clientepiva = models.CharField(max_length=11,  null=True, blank=True)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clienti"
    
    def __str__(self) :
        return self.clienteName
    
class Contratto(models.Model):
    id_contratto = models.AutoField(primary_key=True)
    importo = models.FloatField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name= "Cliente",null=True, blank=True)
    data = models.CharField(max_length=10, null=True, blank=True)
    scadenzaContratto = models.CharField(max_length=10,null=True, blank=True)
    
    class Meta:
        verbose_name = "Contratto"
        verbose_name_plural = "Contratti"
    
    def __str__(self):
        return 'Contratto : '+ self.cliente.clienteName

class Pagamento(models.Model):
    id_Pagamento = models.AutoField(primary_key=True)
    dataPaga = models.DateField()
    importo = models.FloatField()
    id_Contratto = models.ForeignKey(Contratto, on_delete=models.CASCADE, to_field="id_contratto",related_name= "contratto")
    
    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamenti"
    
    def __str__(self):
        return 'Pagamento : '+ str(self.dataPaga)
