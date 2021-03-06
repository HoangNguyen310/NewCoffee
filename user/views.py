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
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home:index')
        except:
            return redirect('user:register')


# class InfoController(LoginRequiredMixin, View):
class InfoController(View):
    # login_url = 'user:login'

    def get(self, request):
        return render(request, 'info.html')

    def post(request):
        user = request.user
        fname = request.POST['Firstname']
        lname = request.POST['Lastname']
        email = request.POST['Email']
        phone = request.POST['Phone']
        address = request.POST['Address']

        user.first_name = fname
        user.last_name = lname
        user.email = email
        user.phone = phone
        user.address = address

        user.save()
        return redirect('user:info')
