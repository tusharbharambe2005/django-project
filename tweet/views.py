from django.shortcuts import render,redirect
from .models import Tweet
from .forms import TweetForm,UserRegistrationForm
from django.shortcuts import get_object_or_404
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
# views.py

def index(request): 
    # data = Tweet.objects.all()
    return render(request,'index.html')

  

# def search(request):
#     Data = Tweet.objects.all()
#     if request.method == 'get':
#         su = request.GET.grt('SearchName')
#         if su!=None:
#             Data = Tweet.objects.filter(user=su)
    
#     return render(request, 'tweet_list.html',Data)


def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    if request.method == 'GET':
        su = request.GET.get('SearchName')
        if su!=None:
            tweets=Tweet.objects.filter(title__icontains=su)
    
    
    return render(request,'tweet_list.html',{'tweets':tweets})

@login_required
def tweet_create(request):
    if request.method=="POST":
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request,'tweet_form.html',{'form':form})


logger = logging.getLogger(__name__)

@login_required
def tweet_edit(request, tweet_id):
    try:
        tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
        logger.info(f"Tweet found: {tweet}")
        
        if request.method == 'POST':
            logger.info("POST request received")
            form = TweetForm(request.POST, request.FILES, instance=tweet)
            if form.is_valid():
                logger.info("Form is valid")
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                return redirect('tweet_list')
            else:
                logger.warning("Form is not valid")
        else:
            logger.info("GET request received")
            form = TweetForm(instance=tweet)
        
        logger.info("Rendering form")
        return render(request, 'tweet_form.html', {'form': form})
    
    except Exception as e:
        logger.error(f"Error in tweet_edit view: {e}")
        return render(request, 'tweet_form.html', {'form': None, 'error': str(e)})


@login_required
def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html', {'tweet':tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html', {'form':form})


