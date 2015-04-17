from django.db import models

# Create your models here.

class Report(models.Model):
    
    name = models.CharField(max_length=32);
    
    animal = models.CharField(max_length=32);
    
    breed = models.CharField(max_length=32);
    
    color = models.CharField(max_length=128);
    
    city = models.CharField(max_length=32);
        
    ZONE_CHOICES = (
        ('None','Sin zona'),
        ('N', 'Norte'),
        ('S', 'Sur'),
        ('C', 'Centro'),
        ('E','Este/Oriente'),
        ('O','Oeste/Occidente'),
                    )
    zone = models.CharField(max_length=32, choices=ZONE_CHOICES);
    
    n_hood = models.CharField(max_length=32);
    
    comment = models.TextField();
    
    TYPE_CHOICES = (
        ('0', 'Perdido'),
        ('1', 'Encontrado'),
        ('2','Visto'),
                    )
    
    type = models.CharField(max_length=16, choices=TYPE_CHOICES)
    
    email = models.EmailField(default="");
    phone = models.CharField(max_length=32,default="");
    
class ReportImage(models.Model):
    
    report_id = models.ForeignKey(Report)
    image = models.ImageField()