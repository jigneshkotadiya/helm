from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CusetomUser
from resume.models import Resume
from allauth.account.forms import SignupForm
from allauth.account.models import EmailAddress
# sign up default auth custom form
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CusetomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'is_student', )

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        print(user)

        if commit:
            # user table add
            user.save()

            # all auth email addres verify
            obj, created = EmailAddress.objects.get_or_create(user_id=user.id, verified=1, primary=1, email=user.email)
            obj.save()

            # resume table create
            obj, created = Resume.objects.get_or_create(user_id=user.id)
            obj.is_student = True
            obj.save()

        return user

# dont know
# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CusetomUser
#         fields = UserChangeForm.Meta.fields

# workwith all auth sign up
class MyCustomSignupForm(SignupForm):

    # first_name = forms.CharField(max_length=30, label='First Name')
    # last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        # user.first_name = self.cleaned_data['first_name']
        # user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        # Add your own processing here.
        user = super(MyCustomSignupForm, self).save(request)
        obj, created = Resume.objects.get_or_create(user=user)
        obj.is_student = True
        obj.save()
        # You must return the original result.
        return user
