import datetime
import json
from django.shortcuts import render


def main(request):
    title = "главная"
    with open('./static/content/main/products.json') as f:
        products = json.load(f)
    content = {"title": title, "products": products}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = "продукты"
    with open('./static/content/products/links_menu.json') as f:
        links_menu = json.load(f)
    with open('./static/content/products/same_products.json') as f:
        same_products = json.load(f)
    content = {"title": title, "links_menu": links_menu,
               "same_products": same_products}
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    visit_date = datetime.datetime.now()
    with open('./static/content/contact/contact.json') as f:
        locations = json.load(f)
    content = {"title": title, "visit_date": visit_date,
               "locations": locations}
    return render(request, "mainapp/contact.html", content)
