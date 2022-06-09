from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Profile,Order, SellOrder
from django.views.decorators.csrf import csrf_exempt
from .forms import OrderForm, SellOrderForm
import requests


def home_page(request):
    price=get_price()
    return render(request,'app/home_page.html',{'price':price})

@csrf_exempt
def register_user(request):
    price=get_price()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"Registration Successful!")
            profile=Profile()
            profile.user_profile=request.user
            profile.initial_balance=100000+(price*5)
            profile.save()
            return redirect('profile')
    else:
        form=UserCreationForm()
    return render(request,'app/register_user.html',{'form':form,'price':price})


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out!")
    return redirect("home_page")

@csrf_exempt
def login_user(request):
    price=get_price()
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.success(request,'There was an error logging in, try again...')
            return render(request,'app/login_user.html',{'price':price})
    else:
        return render(request,'app/login_user.html',{'price':price})

def personal_profile(request):
    price = get_price()
    profile=Profile.objects.get(user_profile=request.user)
    return render(request,'app/logged_in.html',{'username':profile.user_profile,'btc':profile.btc,'price':price,'usd':profile.usd})

def publish_order(request):
    price = get_price()
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            profile=Profile.objects.get(user_profile=request.user)
            if (profile.btc-order.quantity)>=0:
                profile.btc-=order.quantity
                order.profile = request.user
                order.save()
                profile.save()
                messages.success(request, 'Offer published!')
                return redirect('profile')
            else:
                messages.success(request, 'You dont have enough bitcoins!')
                return redirect('profile')
    else:
        form=OrderForm()
    return render(request,'app/new_order.html',{'form':form,'price':price})

def orders_list(request):
    price = get_price()
    orders=Order.objects.all()
    sellorders=SellOrder.objects.all()
    return render(request,'app/orders_list.html',{'orders':orders,'price':price,'sellorders':sellorders})

def order_details(request,pk):
    price = get_price()
    order=get_object_or_404(Order,pk=pk)
    return render(request,'app/order_details.html',{'order':order,'price':price})

def purchase(request,pk):
    price = get_price()
    buyer_profile=Profile.objects.get(user_profile=request.user)
    order=Order.objects.get(pk=pk)
    seller_profile=Profile.objects.get(user_profile=order.profile)
    if buyer_profile.usd >= order.price:
        buyer_profile.btc+=order.quantity
        buyer_profile.usd -= order.price
        seller_profile.usd+=order.price
        buyer_profile.save()
        seller_profile.save()
        order.delete()
    else:
        messages.success(request,'Ops! You dont have enough money...')
        return redirect('profile')
    return render(request,'app/purchase.html',{'quantity':order.quantity,'seller':seller_profile.user_profile,'price':price})

URL="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"

def get_price():
    try:
        response=requests.get(URL.format()).json()
        a=int(response['USD'])
        return a
    except:
        return False

def analytics(request):
    price=get_price()
    profile=Profile.objects.get(user_profile=request.user)
    initial_balance=profile.initial_balance
    actual_balance=profile.usd+(profile.btc*price)
    total_gain=actual_balance-initial_balance
    return render(request,'app/analytics.html',{'initial_balance':initial_balance,'actual_balance':actual_balance,'gain':total_gain,'price':price})

def publish_buy_order(request):
    price = get_price()
    if request.method=="POST":
        form=SellOrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            profile=Profile.objects.get(user_profile=request.user)
            if (profile.usd-order.price)>=0:
                profile.usd-=order.price
                order.buyer_profile = request.user
                order.save()
                profile.save()
                messages.success(request, 'Offer published!')
                return redirect('profile')
            else:
                messages.success(request, 'Ops. There is an error... Try again.')
                return redirect('profile')
    else:
        form=OrderForm()
    return render(request,'app/new_order.html',{'form':form,'price':price})

def sell(request,pk):
    price = get_price()
    seller_profile=Profile.objects.get(user_profile=request.user)
    order=SellOrder.objects.get(pk=pk)
    buyer_profile=Profile.objects.get(user_profile=order.buyer_profile)
    if seller_profile.btc >= order.quantity:
        seller_profile.btc-=order.quantity
        buyer_profile.btc+=order.quantity
        seller_profile.usd+=order.price
        buyer_profile.save()
        seller_profile.save()
        order.delete()
    else:
        messages.success(request,'Ops! You dont have enough BTC...')
        return redirect('profile')
    return render(request,'app/sell.html',{'quantity':order.quantity,'buyer':buyer_profile.user_profile,'price':price})

def buy_order_details(request,pk):
    price = get_price()
    order=get_object_or_404(SellOrder,pk=pk)
    return render(request,'app/buy_order_details.html',{'order':order,'price':price})


