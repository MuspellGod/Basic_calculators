from django import forms
from django.contrib.auth.forms import UserCreationForm  # Import Django's built-in form for user creation
from django.contrib.auth.models import User  # Import User model

# Create a custom signup form extending Django's UserCreationForm
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add an email field to the signup form

    class Meta:
        model = User  # The model that this form will create is User
        fields = ('username', 'email', 'password1', 'password2')  # Specify which fields will appear in the form

    def save(self, commit=True):
        user = super().save(commit=False)  # Call the save method of the parent form (UserCreationForm) without saving yet
        user.email = self.cleaned_data['email']  # Set the email address from form input
        if commit:  # If commit is true, save the User object to the database
            user.save()
        return user  # Return the saved User object
