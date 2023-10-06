from django.db import models

# Create your models here.
class Adresse(models.Model):
    straße = models.CharField(max_length=255)
    hausnummer = models.CharField(max_length=10)

class Kunde(models.Model):
    name = models.CharField(max_length=255)
    adresse = models.ForeignKey(Adresse,on_delete=models.CASCADE)
    
class Produkt(models.Model):
    name = models.CharField(max_length=255)
    preis_pro_einheit = models.DecimalField()
    
class Bestellung(models.Model):
    produkt = models.ForeignKey(Produkt,on_delete=models.CASCADE)
    kunde = models.ForeignKey(Kunde,on_delete=models.CASCADE)
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    