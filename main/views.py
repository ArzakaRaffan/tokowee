from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

@login_required(login_url='/login')
def show_main(request):
    context = {
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'username': request.user.username
        }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    context = {
        'form': form,
        'username': request.user.username 
    }
    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    return render(request, "create_product.html", context)


def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully registered!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'create_account.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = Product.objects.get(pk=id)
    form = ProductForm(request.POST or None, instance=product)

    context = {
        'form': form,
        'username': request.user.username
    }

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    return render(request, "edit_product.html", context)


def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_ajax(request):
    itemName = strip_tags(request.POST.get("itemName"))
    itemDescription = strip_tags(request.POST.get("itemDescription"))
    itemPrice = strip_tags(request.POST.get("itemPrice"))
    itemStock = strip_tags(request.POST.get("itemStock"))
    itemImageURL = strip_tags(request.POST.get("itemImageURL"))
    itemCategory = strip_tags(request.POST.get("itemCategory"))
    user = request.user

    new_product = Product(
        itemName = itemName, itemDescription = itemDescription,
        itemPrice = itemPrice, itemStock = itemStock,
        itemImageURL = itemImageURL, itemCategory = itemCategory,
        user = user
    )

    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_product = Product.objects.create(
            user=request.user,
            itemName=data["itemName"],
            itemPrice=int(data["itemPrice"]),
            itemDescription=data["itemDescription"],
            itemStock=int(data["itemStock"]),
            itemCategory=data["itemCategory"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)