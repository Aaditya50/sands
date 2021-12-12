from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Customer, Dealer
from django.db import models





class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)
    image = forms.ImageField()


    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.image = self.cleaned_data.get('image')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number = self.cleaned_data.get('phone_number')
        customer.location = self.cleaned_data.get('location')
        customer.save()
        return user


class DealerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)
    image = forms.ImageField()


    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_dealer = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.image = self.cleaned_data.get('image')

        user.save()
        dealer = Dealer.objects.create(user=user)
        dealer.phone_number = self.cleaned_data.get('phone_number')
        dealer.designation = self.cleaned_data.get('designation')
        dealer.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']