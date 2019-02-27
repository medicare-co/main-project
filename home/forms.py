from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from home.models import UserProfile, Order

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )

class EditUserDetailsForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            'address',
            'phone',
        )
    
    def save(self, commit=True):
        user = super(EditUserDetailsForm, self).save(commit=False)
        user.address = self.cleaned_data['address']
        user.phone = self.cleaned_data['phone']

        if commit:
            user.save()

        return user


class CreateOrder(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = (
            'name',
            'contents',
        )


class EditOrder(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('name', 'contents')

    def save(self, commit=True):
        order = super(EditOrder, self).save(commit=False)
        order.name = self.cleaned_data['name']
        order.contents = self.cleaned_data['contents']

        if commit:
            order.save()

        return order