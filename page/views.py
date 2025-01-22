from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Topics, Comments, LikesDislikes
import random
from .form import TopicForm, SearchForm, CommentForm
from .logic import search_logic

# Create your views here.

#function to render the homepage at the requested url
def home(request):
    return render(request, 'page/home.html')

#function to render all the topics from the topic list 
def pages(request):
    topics = Topics.objects.all().values()
    return render(request, "page/index.html",{"topics": topics} )
        
            
    return render( request, 'page/index.html', {"topics": topics})

#function to add a new topic
def add(request):
    if request.method == "POST":
        new_topic_data = TopicForm(request.POST, request.FILES)
        #if new_topic_data.is_valid():
        new_topic_data.save()
        return render(request, "page/index.html",{"topics": Topics.objects.all().values()})
    return render(request, "page/add.html", {"add_topic_form": TopicForm()})
        
#function to search a topic. Topic can be searched based on the heading or the desc. 
def search(request):
    search_form = SearchForm()
    final_list = search_logic(request)
    if final_list:
        return render(request,'page/index.html', {"topics": final_list})
    return render(request, "page/search.html", {"search_form":search_form})

#function to show a random topic if the use is not sure what to browse
def random_topic(request):
    topics = Topics.objects.all().values()
    topic = random.choice(topics)
    return render(request, "page/topic1.html", {"topic":topic })


#function to show the details of a choosen topic by the user 
def topic(request, id):
    topic =Topics.objects.get(pk=id)
    comment=Comments.objects.filter(each_topic=topic).values()
    like_dislike=LikesDislikes.objects.get(each_topic=topic)

    #adding comments logic here
    if request.method == "POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            each_topic=Topics.objects.get(pk=id)
            comments = Comments(each_topic=each_topic, comments=form.cleaned_data["comments"])
            comments.save()
            return render(request, "page/topic1.html", {"topic": topic, "form":CommentForm(),"comments":comment, "likes_dislikes":like_dislike})
  
    return render(request, "page/topic1.html", {"topic": topic, "form":CommentForm(),"comments":comment, "likes_dislikes":like_dislike})
#function to add a like to a topic 
def like(request,id):
    topic = Topics.objects.get(pk=id)
    comment=Comments.objects.filter(each_topic=topic).values()
    like_dislike=LikesDislikes.objects.get(each_topic=topic).values()

    if request.method == "POST":
        like = LikesDislikes.objects.get(each_topic=topic)
        like.like +=1
        like.save()
        return render(request, "page/topic1.html", {"topic": topic, "form":CommentForm(),"comments":comment, "likes_dislikes":like_dislike})

    return render(request, "page/topic1.html", {"topic":topic})  
#function to add a dislike to a topic
def dislike(request,id):
    topic = Topics.objects.get(pk=id).values()
    comment=Comments.objects.filter(each_topic=topic).values()
    like_dislike = LikesDislikes.objects.filter(each_topic=topic).values()

    if request.method == "POST":
        like = LikesDislikes.objects.get(each_topic=topic)
        like.dislike +=1
        like.save()
        return render(request, "page/topic1.html", {"topic": topic, "form":CommentForm(),"comments":comment, "likes_dislikes":like_dislike})

    return render(request, "page/topic1.html", {"topic":topic})     

#function to edit a topic in the database
def edit(request, id):
    topics = Topics.objects.all().values()
    topic=Topics.objects.get(id=id)
   
    edit_form=TopicForm(instance=topic)
    if request.method =="POST":
        edit_form=TopicForm(request.POST, request.FILES, instance=topic)
        if edit_form.is_valid():
            edit_form.save()
        return render(request, "page/topic1.html",{ "topic":topic})
    return render(request, "page/edit.html", {"form":edit_form, "topic":topic})
def delete(request, id):
    topic=Topics.objects.get(id=id)
    topic.delete()
    return render(request,"page/index.html",{"topics":Topics.objects.all().values()})
 
 #function to add a comment to a topic
# 
# def add_cooment(request,id):
    # topic=Topics.objects.get(pk=id)
#   
