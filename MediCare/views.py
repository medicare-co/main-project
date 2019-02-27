from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from home.forms import EditProfileForm, EditUserDetailsForm, EditOrder, CreateOrder
from django.contrib.auth import update_session_auth_hash
from home.models import Order
from random import randint

def home_redirect(request):
        return redirect('/home')

def view_profile(request):
        items = Order.objects.filter(user_id__exact=request.user.pk)[:2]
        args = {'user': request.user, 'items': items}

        return render(request, 'accounts/view_profile.html', args)

def edit_profile(request):
        try:
                if request.method == 'POST':
                        form = EditProfileForm(request.POST, instance=request.user)

                        if form.is_valid():
                                form.save()
                                return redirect('.')

                else:
                        form = EditProfileForm(instance=request.user)
                        args = {'form': form}
                        return render(request, 'accounts/edit_profile.html', args)
        except AttributeError:
                args = {'error': AttributeError}
                return render(request, 'accounts/edit_profile.html', args)

def edit_details(request):
        if request.method == 'POST':
                form = EditUserDetailsForm(request.POST, instance=request.user)

                if form.is_valid():
                        form.save()
                        return redirect('.')

        else:
                form = EditUserDetailsForm(instance=request.user)
                args = {'form': form}
                return render(request, 'accounts/edit_profile.html', args)

def edit_order(request, pk):
        order = get_object_or_404(Order, pk=pk)

        if request.method == 'POST':
                form = EditOrder(request.POST, instance=order)
                if form.is_valid():
                        form.save()
                return redirect('.')

        else:
                form = EditOrder(instance=order)
                args = {'form': form}
                return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
        if request.method == 'POST':
                form = PasswordChangeForm(data=request.POST, user=request.user)

                if form.is_valid():
                        form.save()
                        update_session_auth_hash(request, form.user)
                        return redirect('../profile')
                
                else:
                        return redirect('/accounts/password')

        else:
                form = PasswordChangeForm(user=request.user)
                args = {'form': form}
                return render(request, 'accounts/change_password.html', args)

def view_orders(request):
        term = ''
        items = Order.objects.filter(user_id__exact=request.user.pk)

        if 'search' in request.GET:
                term = request.GET['search']
                items = items.filter(name__icontains=term)
        
        num = len(items)
        args = {'user': request.user, 'items': items, 'num': num, 'doc': randint(0,1), 'term': term}

        return render(request, 'accounts/view_orders.html', args)

def create_order(request):
        if request.method == 'POST':
                form = CreateOrder(request.POST)
                if form.is_valid():
                        order = form.save(commit=False)
                        order.name = form.cleaned_data['name']
                        order.contents = form.cleaned_data['contents']
                        order.creator = request.user
                        order.user_id = request.user.pk
                        form.save()
                        return redirect('view_orders')
        else:
                form = CreateOrder()

                args = {'form': form}
                return render(request, 'accounts/create_order.html', args)