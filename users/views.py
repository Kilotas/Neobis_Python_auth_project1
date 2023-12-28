from django.views import View
from django.contrib.auth.forms import UserCreationForm, authenticate
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from users.forms import UserCreationForm
from django.contrib.auth.views import LoginView


class Register(View):

    templates_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.templates_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }

        return render(request, self.templates_name, context)


