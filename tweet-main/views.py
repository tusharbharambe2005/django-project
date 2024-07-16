from django.shortcuts import render
# from tweet import views
from tweet.models import Tweet

def home_page(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    if request.method == 'GET':
        su = request.GET.get('SearchName')
        if su!=None:
            tweets=Tweet.objects.filter(title__icontains=su)
    
    
    return render(request,'home.html',{'tweets':tweets})