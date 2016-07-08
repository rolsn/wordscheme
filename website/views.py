from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as _login, logout as _logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from website.forms import RegistrationForm, LoginForm, ArticleForm, CommentForm
from website.models import Articles, Comments, UserRelationships, Ratings
from website.serializers import UserSerializer, RatingsSerializer

from random import randrange
import re

def index(request):
    if request.user is not None and request.user.is_active:
        return HttpResponseRedirect(reverse('main'))

    return render(request, 'website/index.html', {})


def format_urlname(text):
    """
    Creates IDs for various models based on the input text.
    """
    text = re.sub('[^A-Za-z0-9 ]', '', text)
    text = re.sub(' +', '-', text).lower().strip('-')[:40]
    prefix = '%06x' % randrange(16**6)

    return "%s-%s" % (prefix, text)


@require_http_methods(["GET", "POST"])
def new_registration(request):
    if request.method == "POST":
        regForm = RegistrationForm(request.POST)

        if not regForm.is_valid():
            return render(request, 'website/register.html', {'form': RegistrationForm().as_ul(), 'error': regForm.errors})

        try:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
        except KeyError:
            return HttpResponse("Invalid input.")

        userExists = True if len(User.objects.filter(username=username)) == 1 else False
        emailExists = True if len(User.objects.filter(email=email)) == 1 else False

        if userExists:
            return HttpResponse("Username already taken.")
        if emailExists:
            return HttpResponse("Email already registered.")

        try:
            User.objects.create_user(username, email, password)
        except:
            return HttpResponse("Error adding user.")

        user = authenticate(username=username, password=password)
        return login(request, user=user)
      
    if request.method == "GET":
        return render(request, 'website/register.html', {'form': RegistrationForm().as_ul()})


@require_http_methods(["GET", "POST"])
def login(request, **kwargs):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = kwargs['user'] if 'user' in kwargs.keys() else authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                _login(request, user)
                return HttpResponseRedirect(reverse('main'))
            else:
                return HttpResponse("User %s is disabled." % user.username)
        else:
            return HttpResponse("Invalid username or password.")
    
    if request.method == "GET":
        return render(request, 'website/login.html', {'form': LoginForm().as_ul()})

def logout(request):
    _logout(request)

    return HttpResponseRedirect(reverse('index'))


@login_required
def main(request):
    username = request.user
    uid = User.objects.get(username=username).id
    latestArticles = Articles.objects.all().order_by('-date')[:10]
    
    commentCounts = {}
    for art in latestArticles:
        numOfComments = len(Comments.objects.filter(art_id=art.id))
        commentCounts[art.id] = numOfComments

    return render(request, 'website/main.html', {
        "latestArticles"    : latestArticles,
        "commentCounts"     : commentCounts
        })


def article(request, urlname):
    try:
        article = Articles.objects.get(urlname=urlname)
    except Articles.DoesNotExist:
        raise Http404("Article not found.")

    comments = Comments.objects.filter(art_id=article.id)

    return render(request, 'website/article.html', {
        "article"       : article,
        "comments"      : comments,
        "comment_form"  : CommentForm()
        })


@login_required
def new_article(request):
    username = request.user

    if request.method == 'GET':
        username = request.user

        return render(request, 'website/new_article.html', {
            "username"  : username,
            "form"      : ArticleForm().as_ul(),
            })

    if request.method == 'POST':
        article_text = request.POST['article_text']
        subject = request.POST['subject']

        user = User.objects.get(username=username)

        article = Articles.objects.create(
                user_id         = user,
                date            = timezone.now(),
                article_text    = article_text,
                subject         = subject,
                urlname         = format_urlname(subject)
                )

        return HttpResponseRedirect(reverse('main'))


@login_required
@require_http_methods(["POST"])
def new_comment(request, urlname):
    username = request.user
    comment_text = request.POST['comment_text']

    try:
        article = Articles.objects.get(urlname=urlname)
    except:
        raise Http404("Article not found.")

    user = User.objects.get(username=username)

    Comments.objects.create(
            user_id         = username,
            art_id          = article,
            comment_text    = comment_text,
            date            = timezone.now()
            )

    return HttpResponseRedirect(reverse('articles', args=(urlname,)))


@login_required
@require_http_methods(["GET"])
def profiles(request, username):
    try:
        user = User.objects.get(username=username)
        uid = user.id
    except:
        raise Http404("User not found.")

    all_articles = Articles.objects.filter(user_id_id=uid)
    all_comments = Comments.objects.filter(user_id_id=uid)
    following = UserRelationships.objects.filter(follower_id=uid)

    return render(request, 'website/user.html', {
        "reqUser"       : user,
        "uid"           : uid,
        "allArticles"   : all_articles,
        "allComments"   : all_comments,
        "following"  : following
        })


@login_required
@require_http_methods(["GET"])
def search(request):
    if request.method == "POST":
        search_term = request.POST['search'];
        results = Articles.objects.filter(subject__icontains=search_term)

        return render(request, 'website/search.html', {
            "searchResults" : results
            })

    if request.method == "GET":
        return render(request, 'website/search.html', {})


@login_required
@require_http_methods(["GET"])
def following(request, username):
    try:
        user = User.objects.get(username = username)
        uid = user.id
    except:
        raise Http404("User not found.")

    following = UserRelationships.objects.filter(follower_id=uid);

    return render(request, 'website/following.html', {'object_list': following})


###
# REST Framework
###

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


@api_view(['GET', 'PUT'])
def ratings(request, pk):
    """
    Get or update an article rating.
    """

    try:
        rating = Ratings.objects.get(id=pk)
    except Ratings.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        ser = RatingsSerializer(rating)
        return Response(ser.data)
