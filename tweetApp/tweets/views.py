from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')



def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-createdAt')
    return render(request, 'tweetList.html', {'tweets': tweets})

def tweetCreate(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()

    return render(request, 'tweetForm.html',{'form':form})


def tweetEdit(request, tweetID):
    tweet = get_object_or_404(Tweet, pk=tweetId, user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')

    else:
        form = TweetForm(instance=tweet)

    return render(request, 'tweetForm.html',{'form':form})


def tweet_delete(request, tweetID):
    tweet = get_object_or_404(Tweet, pk=tweetID, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    
    return render(request, 'tweetConfirmDelete.html',{'tweet':tweet})
    


