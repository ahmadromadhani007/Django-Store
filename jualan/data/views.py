from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

# Create your views here.


def home(request):

    list_customer = Customer.objects.order_by('-id')
    list_order = Order.objects.order_by('-id')
    total_orders = list_order.count()
    delivered = list_order.filter(status='Delivered').count()
    pending = list_order.filter(status='Pending').count()
    context = {
        'judul': 'Halaman Beranda',
        'menu': 'home',
        'customer': list_customer,
        'order': list_order,
        'data_total_orders': total_orders,
        'data_delivered': delivered,
        'data_pending': pending,
    }
    return render(request, 'data/dashboard.html', context)


def products(request):
    list_product = Product.objects.all()
    context = {
        'judul': 'Halaman Products',
        'menu': 'products',
        'product': list_product,
    }
    return render(request, 'data/products.html', context)


def customer(request, pk):
    detailcustomer = Customer.objects.get(id=pk)
    order_customer = detailcustomer.order_set.all()
    total_customer = order_customer.count()
    context = {
        'judul': 'Halaman Customer',
        'menu': 'customer',
        'customer': detailcustomer,
        'data_order_customer': order_customer,
        'data_total_customer': total_customer,
    }
    return render(request, 'data/customer.html', context)


def createOrder(request):
    formorder = OrderForm()
    if request.method == 'POST':
        formsimpan = OrderForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/')

    context = {
        'judul': 'Form Order',
        'form': formorder,
    }
    return render(request, 'data/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    formorder = OrderForm(instance=order)
    if request.method == 'POST':
        # print('Certak POST:', request.POST)
        formedit = OrderForm(request.POST, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('/')

    context = {
        'judul': 'Edit Order',
        'form': formorder,
    }
    return render(request, 'data/order_form.html', context)


def deleteOrder(request, pk):
    orderhapus = Order.objects.get(id=pk)
    if request.method == 'POST':
        orderhapus.delete()
        return redirect('/')
    context = {
        'judul': 'Hapus Data Order',
        'dataorderdelete': orderhapus,
    }
    return render(request, 'data/delete_form.html', context)
