from django.db import models
from datetime  import date
from django.utils import timezone
# Create your models here.
class adress(models.Model):
    street=models.CharField(max_length=50,null=False,blank=False) 
    cite=models.CharField(max_length=100,default="")
    zipcode=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=100,default="")

    class Meta: #customize the model
      #we can personaliez properties like name of the table 
      db_table='adress'

class Location(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False) 
    familyName=models.CharField(max_length=50,null=False,blank=False)
    date=models.DateField(default=date(2004,1,1))
    description=models.TextField(max_length=200)
    #email=models.EmailField(null=True,blank=True,unique=True)
    email=models.EmailField(primary_key=True)
    adresse=models.OneToOneField(adress,on_delete=models.SET_NULL,null=True,blank=True)
    class Meta: #customize the model
      #we can personaliez properties like name of the table 
      db_table='Location'
class event(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False) 
    date=models.DateField(default=date(2004,1,1))
    time=models.TimeField()
    description=models.TextField(max_length=200)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    ## wahdo ya3ref clé primaire *--1
    
    #email=models.EmailField(null=True,blank=True,unique=True)
    class Meta: #customize the model
      #we can personaliez properties like name of the table 
      db_table='event'
      ordering=['name','date','time']
      unique_together=['name','date','time']
class animation(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False) 
    phone=models.CharField(max_length=50,null=False,blank=False)
    birthDate=models.DateField(default=date(2004,1,1))
    level=models.CharField(max_length=20)
    description=models.TextField(max_length=200)
    #email=models.EmailField(null=True,blank=True,unique=True)
    email=models.EmailField(primary_key=True)
    a=models.ManyToManyField(event )#mra Rbarka w win nheb

    class Meta: #customize the model
      #we can personaliez properties like name of the table 
      db_table='animation'
class Organizer(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False) 
    phone=models.CharField(max_length=50,null=False,blank=False)
    email=models.EmailField(null=True,blank=True,unique=True)
    event_org=models.ManyToManyField(event)
    class Meta: #customize the model
      #we can personaliez properties like name of the table 
      db_table='Organizer'

class contributor(models.Model):
   lastName=models.CharField(max_length=50,null=False,blank=False)
 
   familyName=models.CharField(max_length=50,null=False,blank=False)
   birthDate=models.DateField(default=date(2004,1,1))   
   email=models.EmailField(max_length=20,unique=True)
   class meta :
      abstract=True
      ordering=["email"]   


class participant(contributor):
    
    level=models.CharField(max_length=20)
    description=models.TextField(max_length=200)
    #email=models.EmailField(null=True,blank=True,unique=True)
    adrr=models.OneToOneField(adress,on_delete=models.CASCADE)
    part_event_reserv=models.ManyToManyField(event,through='reservation',through_fields =('participant','event')) ##lehne ki yabda lazmk table akher 
    
    class Meta: #customize the model
      #we can personaliez properties like name of the table 
      db_table='participant'
#class abstract maandouch wled pas d'instance nekhdm bih kn lel héritage 
# animator et participant aandhom des attributs kifkif donc bsh naaemlo class pour héritage contributor 

class Reservation(models.Model):
    price=models.FloatField(null=False,blank=False) 
    nbr=models.FloatField(null=False,blank=False) 
    date=models.DateField(default=date(2004,1,1))
    participant=models.ForeignKey(participant,on_delete=models.CASCADE)## wahdo ya3ref clé primaire
    event=models.ForeignKey(event,on_delete=models.CASCADE)## wahdo ya3ref clé primaire
    loc=models.OneToOneField(Location,on_delete=models.CASCADE)
    type=models.CharField(max_length=30,choices=[('VIP','Very important Person'),('S','Simple...')])
    class Meta: #customize the model
      #we can personaliez properties like name of the table 
      db_table='Reservation'
      unique_together=['participant','event']
class Animator(contributor): #(models.Model):

   phone=models.CharField(max_length=30)
   animator_event=models.ManyToManyField(event)
   class Meta:
      db_table='Animator'
class Ticket(models.Model):
    price=models.FloatField(null=False,blank=False) 
    reservation=models.OneToOneField(Reservation,on_delete=models.CASCADE)
    barCide=models.CharField(max_length=300,null=True,blank=True)
  
    class Meta: #customize the model
      #we can personaliez properties like name of the table 
      db_table='Ticket'
    def __str__(self):
       return self.reservation.event.name +" " +self.reservation.participant.email      
#task model
## fl many to many w yabda hachtich b table nhot manytomany fi ay wahed w nzid aafsa exemple event wv orginizer si non exemple reservation w participanyt w event felekher nzid fl class meta eli houma uniquetogether les deux
##    part_event_reserv=models.ManyToManyField(Event,through='reservation',through_fields =('participant','event'))z ##lehne ki yabda lazmk table akher 
## 7EL sql plus usename w lkol mbaed a3mel create database events_db 
## /l bsh ychouf el base
## connexion
## /c events_db
## events_db#
## /dt lel details
# mbaed na3mel makemigration w migrate