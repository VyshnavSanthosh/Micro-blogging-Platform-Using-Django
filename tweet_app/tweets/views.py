from django.shortcuts import redirect, render, HttpResponse
from .models import Tweet
from .forms import TweetForm ,UserRegistrationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

# Create your views here.

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created')
    return render(request, "tweet_list.html", {'tweets': tweets})

@login_required # make this function only used after login
def create_tweet(request):
    if request.method =='POST':
        formTweet = TweetForm(request.POST, request.FILES)
        if formTweet.is_valid():
            tweet = formTweet.save(commit=False)
            tweet.user = request.user #to get the username
            tweet.save()
            return redirect('tweet_list')
    else:
        formTweet = TweetForm()
    return render(request, 'tweet_create.html', {'formTweet': formTweet})

@login_required
def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk= tweet_id, user = request.user) # only the user should be able to edit this post 
    if request.method == 'POST':
        formTweet = TweetForm(request.POST, request.FILES, instance=tweet)
        if formTweet.is_valid():
            tweet = formTweet.save(commit=False)#Commit = false is used to further make modifications in that data
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list') # redirects to tweet_list page
    else:
            formTweet = TweetForm(instance=tweet) #Instance is used to edit the existiong tweet instead of creating new one
    return render(request,'tweet_create.html',{'formTweet': formTweet})

@login_required
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

def userRegisteration(request):
    if request.method == 'POST':
        tweetForm = UserRegistrationForm(request.POST)
        if tweetForm.is_valid():
            user = tweetForm.save(commit=False)
            user.set_password(tweetForm.cleaned_data['password1'])
            user.save()
            login(request, user)  # Corrected the order of arguments
            return redirect('tweet_list')
    else:
        tweetForm = UserRegistrationForm()
    return render(request, 'registration/register.html', {'tweetForm': tweetForm})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('tweet_list') 
    return render(request, 'registration/logout.html')