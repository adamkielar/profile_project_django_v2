from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from . import forms
from . import models


def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        reverse('accounts:view_profile', )
                    )
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            return HttpResponseRedirect(reverse('accounts:view_profile',))
    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))


@login_required
def view_profile(request):
    return render(request, 'accounts/view_profile.html')


@login_required
def edit_profile(request):
    user_form = forms.UserForm(instance=request.user)
    profile_form = forms.ProfileForm(instance=request.user.profile)
    avatar_from = forms.AvatarForm(instance=request.user.profile)

    if request.method == 'POST':
        user_form = forms.UserForm(request.POST, instance=request.user)
        profile_form = forms.ProfileForm(request.POST, instance=request.user.profile)
        avatar_from = forms.AvatarForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid() and avatar_from.is_valid():
            user_form.save()
            profile_form.save()
            avatar_from.save()
            messages.success(
                request,
                "Profile updated !"
            )
            return HttpResponseRedirect(reverse('accounts:view_profile',))

    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'avatar_form': avatar_from,
    })


@login_required
def change_password(request):
    form = forms.PasswordChangeForm(request.user)

    if request.method == 'POST':
        form = forms.PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect(reverse('accounts:change_password',))

    return render(request, 'accounts/change_password.html', {'form': form})


@login_required
def avatar_view(request):
    avatar_from = forms.AvatarForm(instance=request.user.profile)

    if request.method == 'POST':
        avatar_from = forms.AvatarForm(request.POST, request.FILES, instance=request.user.profile)
        if avatar_from.is_valid():
            avatar_from.save()
            messages.success(
                request,
                "Profile updated !"
            )
            return HttpResponseRedirect(reverse('accounts:view_profile',))

    return render(request, 'accounts/avatar_view.html', {'avatar_form': avatar_from})

