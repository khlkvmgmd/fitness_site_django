from django.urls import reverse_lazy

from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import sendTelegram
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {'slider_list': slider_list,
                 'pc_1': pc_1,
                 'pc_2': pc_2,
                 'pc_3': pc_3,
                 'price_table': price_table,
                 'form': form,
                 }
    return render(request, './index.html', dict_obj)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name = name, order_phone = phone)
        element.save()
        sendTelegram(tg_name = name, tg_phone = phone)
        return render(request, './thanks.html', { 'name': name,})
    else:
        return render(request, './thanks.html')

def home(request):
    return render(request, 'home.html')

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})