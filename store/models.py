from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    utilisateur=models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=30, null=True, blank=False)
    prenom=models.CharField(max_length=30, null=True, blank=False)
    email=models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    prix = models.FloatField(null=True, blank=True)
    etat = models.BooleanField(default=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)  # Reste comme un champ ImageField

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except Exception as e:
            print(f"Erreur lors de la récupération de l'image: {e}")
            url = ''
        return url

    
    

class Commande(models.Model):
    Client=models.ForeignKey(Client,null=True,blank=False, on_delete=models.SET_NULL)
    la_date=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False, null=True,blank=False)
    transaction_id=models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.id)
    
    def get_cart_total(self):
        articlescommande = self.articlecommande_set.all()
        total = sum([item.gettotal for item in articlescommande])
        return total
    
    def get_cart_items(self):
        articlescommande = self.articlecommande_set.all()
        total = sum([item.quantite for item in articlescommande])
        return total
    
class ArticleCommande(models.Model):
    article=models.ForeignKey(Article, null=True,on_delete=models.SET_NULL)
    commande=models.ForeignKey(Commande, null=True, on_delete=models.SET_NULL)
    quantite=models.IntegerField(default=0,null=True, blank=True)
    la_date=models.DateTimeField(auto_now_add=True)

    @property
    def gettotal(self):
        totale = self.article.prix*self.quantite
        return totale

class Ordre_expedition(models.Model):
    Client=models.ForeignKey(Client,null=True,on_delete=models.SET_NULL)
    commande=models.OneToOneField(Commande,null=True,on_delete=models.SET_NULL)
    adresse=models.CharField(max_length=100, null=True, blank=False)
    cite=models.CharField(max_length=100, null=True, blank=False)
    code=models.CharField(max_length=6,null=True,blank=True)

    def __str__(self):
        return self.adresse
