from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from user.models import CustomerUser
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginController(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(username=username, password=password)
        if user is None:
            return redirect('user:login')
        else:
            login(request, user)
            return redirect('home:index')


class LogoutController(View):
    def get(self, request):
        logout(request)
        return redirect('home:index')


class RegisterController(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST['Username']
        email = request.POST['Email']
        password = request.POST['Password']
        phone = request.POST['Phone']
        address = request.POST['Address']

        try:
            CustomerUser.objects.create_user(
                username=username, email=email, password=password, phone=phone, address=address
            )
            return redirect('user:login')
        except:
            return redirect('user:register')


class InfoController(LoginRequiredMixin, View):
    login_url = 'user:login'

    def get(self, request):
        return render(request, 'info.html')

    def post(request, user_id):
        user = CustomerUser.objects.get(username=user_id)
        user.username = request.POST['Username']
        user.email = request.POST['Email']
        user.phone = request.POST['Phone']
        user.address = request.POST['Address']

        try:
            user.save()
            return redirect('user:info')
        except:
            return redirect('home:index')
