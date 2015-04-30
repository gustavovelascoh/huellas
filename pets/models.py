from django.db import models

# Create your models here.

class Report(models.Model):
    
    name = models.CharField(max_length=32,blank=True);
    
    animal = models.CharField(max_length=32);
    
    breed = models.CharField(max_length=32,default="Criollo");
    
    color = models.CharField(max_length=128,blank=True);
    
    city = models.CharField(max_length=32);
    
    GENRE_CHOICES = (
        ('None','Desconocido'),
        ('M', 'Macho'),
        ('F', 'Hembra'),
        )
    
    genre = models.CharField(max_length=32, choices=GENRE_CHOICES, default='None');
        
    ZONE_CHOICES = (
        ('None','Sin zona'),
        ('N', 'Norte'),
        ('S', 'Sur'),
        ('C', 'Centro'),
        ('E','Este/Oriente'),
        ('O','Oeste/Occidente'),
                    )
    zone = models.CharField(max_length=32, choices=ZONE_CHOICES);
    
    n_hood = models.CharField(max_length=32,default="NA");
    
    comment = models.TextField();
    
    TYPE_CHOICES = (
        ('0', 'Perdido'),
        ('1', 'Encontrado'),
        ('2','Visto'),
                    )
    
    type = models.CharField(max_length=16, choices=TYPE_CHOICES)
    
    reporter_name = models.CharField(max_length=32, default="Anonymous");
    email = models.EmailField(default="",blank=True);
    phone = models.CharField(max_length=32,default="",blank=True);
    
class ReportImage(models.Model):
    
    report_id = models.ForeignKey(Report)
    image = models.ImageField()
