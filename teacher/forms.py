from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import User
from teacher.models import Teacher


class TeacherUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('is_teacher', 'username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('address', 'place', 'phone')
