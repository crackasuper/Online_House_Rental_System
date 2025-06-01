from django import forms
from allauth.account.forms import SignupForm
from django.core.validators import EmailValidator

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(
        required=True,
        validators=[EmailValidator()],
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'})
    )
    role = forms.ChoiceField(
        choices=[
            ('tenant', 'Tenant'),
            ('owner', 'Property Owner')
        ],
        widget=forms.RadioSelect,
        required=True,
        initial='tenant'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email address is required.")
        return email

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        
        # Update the user's profile with the selected role
        profile = user.profile
        profile.role = self.cleaned_data['role']
        profile.save()
        
        return user 