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
from .forms import EditProfileForm,ResumeForm
from .models import UserProfile,Resume
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
    return render(request, 'editprofile.html', {'form': form})\


@login_required(login_url='/')
def resume(request):
    if request.method == 'POST':
        user_profile = request.user.profile
        form = ResumeForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            # file is saved
            #resume=Resume(user=request.user,file=request.FILES['resume_file'])
            #resume.save()
            form.save()
            return HttpResponseRedirect('resume')
    else:
        user_profile = request.user.profile
        form = ResumeForm(instance=user_profile)
    return render(request, 'resume.html', {'form': form})

@login_required(login_url='/')
def pdf_view(request):
    user_profile = request.user.profile
    resume_file = user_profile.resume_file
    print(resume_file.name)

    print('path is '+str(resume_file._get_path))
    print(str(resume_file._get_size))
    with open(resume_file.name, 'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed

