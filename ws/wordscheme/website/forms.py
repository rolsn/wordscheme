from django.forms import ModelForm
from django.contrib.auth.models import User

from models import Articles, Comments

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['subject', 'article_text']

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_text']
