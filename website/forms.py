from django.forms import ModelForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User

from models import Articles, Comments, Guilds

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
                'password': PasswordInput()
                }

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
                'password' : PasswordInput()
                }

class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['subject', 'article_text', 'public']

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_text']

class GuildCreateForm(ModelForm):
    class Meta:
        model = Guilds
        fields = ['name', 'description']
