from django.shortcuts import render
from django.http import JsonResponse
from .models import Article, Commande, ArticleCommande
import json

def store(request):
    if request.user.is_authenticated:
        client = request.user.client
        commande, created = Commande.objects.get_or_create(Client=client, complete=False)
        articles = commande.articlecommande_set.all()
        cart_items = commande.get_cart_items()
    else:
        articles = []
        commande = {'get_cart_total': 0, 'get_cart_items': 0}
        cart_items = commande['get_cart_items']

    produits = Article.objects.all()
    context = {'produits': produits, 'cart_items':cart_items}
    return render(request, 'store/store.html', context)
def cart(request):
    if request.user.is_authenticated:
        client = request.user.client
        commande, created = Commande.objects.get_or_create(Client=client, complete=False)
        articles = commande.articlecommande_set.all()
        cart_total = commande.get_cart_total()
        cart_items = commande.get_cart_items()
    else:
        articles = []
        commande = {'get_cart_total': 0, 'get_cart_items': 0}
        cart_items = commande['get_cart_items']

    context = {'articles': articles, 'commande': commande, 'cartItems': cart_items}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        client = request.user.client
        commande, created = Commande.objects.get_or_create(Client=client, complete=False)
        articles = commande.articlecommande_set.all()
        cart_items = commande.get_cart_items()
    else:
        articles = []
        commande = {'get_cart_total': 0, 'get_cart_items': 0}
        cart_items = commande['get_cart_items']

    context = {'articles': articles, 'commande': commande,'cartItems': cart_items }
    return render(request, 'store/checkout.html', context)

def main(request):
    context = {}
    return render(request, 'store/main.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('Product ID:', productId)

    article = Article.objects.get(id=productId)
    client = request.user.client
    commande, created = Commande.objects.get_or_create(Client=client, complete=False)
    articleCommand, created = ArticleCommande.objects.get_or_create(commande=commande, article=article)

    if action == 'add':
        articleCommand.quantite += 1
    elif action == 'remove':
        articleCommand.quantite -= 1

    articleCommand.save()

    if articleCommand.quantite <= 0:
        articleCommand.delete()

    return JsonResponse('Article was updated', safe=False)
