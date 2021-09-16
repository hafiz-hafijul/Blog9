from main.models import Post
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import UserLoginForm, UserForm
from django.views import View
from .models import Profile
from .forms import ProfileForm


def getslug(request):
    return{
        'profile': Profile.objects.all()
    }


class UserSignView(View):
    def get(self, request):
        form = UserForm()

        return render(request, 'authen/sign.html', {'form': form, })

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))

        return render(request, 'authen/sign.html',  {'form': form, })


def userlogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            obj = authenticate(username=uname, password=upass)
            if obj is not None:
                login(request, obj)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
    return render(request, 'authen/login.html', {'form': form})


def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            content = form.cleaned_data['content']
            obj = Profile(name=name, content=content)
            user = obj.save(commit=False)
            user.user = request.user
            user.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ProfileForm()
    return render(request, 'authen/profile.html', {'form': form})


def getProfile(request, profile_slug):
    ins = request.user
    pro = get_object_or_404(Profile, slug=profile_slug)
    acc = Profile.objects.filter(user=ins)
    pos1t = Post.objects.filter(author=ins)[:1]
    post = Post.objects.filter(author=ins)[1:4]
    return render(request, 'authen/profile.html', {'acc': acc, 'pro': pro, "post": post, 'post1': pos1t})
