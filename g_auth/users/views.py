from typing import Any
import json
from django.contrib.auth.models import (
    User
)
from django.forms.forms import BaseForm
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    View, ListView, CreateView, TemplateView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)

from users.models import (
    Profile
)

from users.forms import (
    ProfileForm
)

from django.contrib.auth.forms import UserCreationForm

class HomePage(TemplateView):
    template_name = 'home.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)
    

class UserRegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "auth/register.html"
    success_url = reverse_lazy('users:dash')


class CreateProfile(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "profile-create.html"
    model = Profile
    form_class = ProfileForm


    def form_valid(self, form: BaseForm) -> HttpResponse:
        profile_inc = form.save(commit=False)
        profile_inc.user = self.request.user
        profile_inc.save()

        return redirect(reverse_lazy('users:dash'))



class ProfileDelete(LoginRequiredMixin, SuccessMessageMixin,View):
    success_message = "Profile Deleted!"


    def post(self, request, *args, **kwargs):
        request.user.profile.delete()
        return redirect(reverse_lazy("users:dash"))

    # def delete(self, request, *args, **kwargs):
    #     print('working')
    #     request.user.profile.delete()
    #     return redirect(request,"users:dash")



class ProfileDash(LoginRequiredMixin, View):
    model = Profile
    template_name = 'profile-dash.html'
    
    def get(self, request, *args, **kwargs):
        user = request.user
        try:
            profile = user.profile
        except:
            profile = None

        custom_context = {'user': user, 'profile': profile}

        return render(request=request, template_name=self.template_name, context=custom_context)
    
    def post(self, request, *args, **kwargs):

        try:
            u_instance = User.objects.get(id=request.user.id)
        except Exception as p:
            u_instance = None
            return JsonResponse({'status': 'bad', 'msg': f'{str(p)[0:100]}'}, status=400)

        try:
            p_instance = Profile.objects.get(user=request.user)
        except Exception as p:
            p_instance = None
            return JsonResponse({'status': 'bad', 'msg': f'{str(p)[0:100]}'}, status=400)

        f_name = None
        l_name = None
        email = None
        bio = None

        # print(request.headers)
        req_data = request.body.decode('utf-8')
        req_json = json.loads(req_data)
        
        if req_json.get('name') == 'first_name':
            f_name = req_json.get('value')

        if req_json.get('name') == 'last_name':
            l_name = req_json.get('value')

        if req_json.get('name') == 'email':
            email = req_json.get('value')

        if req_json.get('name') == 'bio':
            bio = req_json.get('value')




        if f_name:
            
            try:
                u_instance.first_name = f_name
                u_instance.save()
                return JsonResponse({'status': 'ok', 'msg': 'First Name Updated!'})
            except:
                return JsonResponse({'status': 'bad', 'msg': '''First Name Can't Update or Saved!'''}, status=400)


        if l_name:
            
            try:
                u_instance.last_name = l_name
                u_instance.save()
                return JsonResponse({'status': 'ok', 'msg': 'Last Name Updated!'})
            except:
                return JsonResponse({'status': 'bad', 'msg': '''Last Name Can't Update or Saved!'''}, status=400)


        if email:
            
            try:
                u_instance.email = email
                u_instance.save()
                return JsonResponse({'status': 'ok', 'msg': 'Email Name Updated!'})
            except:
                return JsonResponse({'status': 'bad', 'msg': '''Email Can't Update or Saved!'''}, status=400)

        if bio:
            
            try:
                p_instance.bio = bio
                p_instance.save()
                return JsonResponse({'status': 'ok', 'msg': 'Bio Updated!'})
            except:
                return JsonResponse({'status': 'bad', 'msg': '''Bio Can't Update or Saved!'''}, status=400)
            
        return JsonResponse({"status": "bad", "msg": "Deafult errors!"}, status=400)









# class ProfileCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = None
#     form_class = None
#     success_message = "Profile Created!"
#     success_url = reverse_lazy('users:dash')



