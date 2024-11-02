from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(Commande)
admin.site.register(Article)
admin.site.register(ArticleCommande)
admin.site.register(Ordre_expedition)
