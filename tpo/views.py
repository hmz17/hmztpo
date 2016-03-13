from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from django.shortcuts import render_to_response
import json

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout, login

from social.backends.oauth import BaseOAuth1, BaseOAuth2
from social.backends.google import GooglePlusAuth
from social.backends.utils import load_backends
from .forms import EditProfileForm
from .models import UserProfile
from django.contrib.auth.models import User




# Create your views here.
def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('home.html',
                             context_instance=context)

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')

@login_required(login_url='/')
def editprofile(request):
    if request.method == "POST":
        user_profile = request.user.profile
        form = EditProfileForm(request.POST,instance=user_profile)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect(home)

    else:
        user_profile = request.user.profile
        form = EditProfileForm(instance=user_profile)
    return render(request, 'editprofile.html', {'form': form})
