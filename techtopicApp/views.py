from django.shortcuts import render

# Create your views here.


# -*- encoding: utf-8 -*-
import time
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from techtopicApp.models import Topics
from techtopicApp.models import Comments
from mongoengine.django.auth import User
from django.contrib.auth import authenticate, login, logout

def list_topics(request):
    return TemplateResponse(request, 'techtopics/topic_list.html', {'topic_list': Topics.objects})


def detail_topic(request, topic_id):
    return TemplateResponse(request, 'techtopics/topic_detail.html',
                            {'topic': Topics.objects(id=topic_id).first(), 'comments': Comments.objects})


def create_topic(request):
    if request.user.is_authenticated():
        print('auth by '+str(request.user))
        if request.method == 'POST':
            csrf(request)
            post = request.POST.copy()
            post.pop('csrfmiddlewaretoken')
            model = Topics()
            model.topic = post.get('topic')
            model.introduce = post.get('introduce')
            model.auther = request.user
            model.createtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            if model.save():
                return redirect('/techtopics/topic/'+model.id.__str__())
        elif request.method == 'GET':
            return TemplateResponse(request, 'techtopics/topic_create.html')
    else:
        login_require = True
        return TemplateResponse(request, 'techtopics/topic_list.html', {'login_require': login_require})

def delete_topic(request, topic_id):
    model = Topics.objects(id=topic_id).first()
    comms = Comments.objects(topiclink=model)
    for subcomms in comms:
        subcomms.delete()
    model.delete()
    return redirect('/techtopics/list')


def create_user(request):
    if request.method == 'POST':
        user = User.create_user(request.POST['username'], request.POST['password'], request.POST['email'])
        if user.is_active == True:
            print('True')
            return redirect('/techtopics/list')
    elif request.method == 'GET':
        return TemplateResponse(request, 'techtopics/user_create.html')

def user_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            print('Auth_OK')
            login(request, user)
            #return TemplateResponse(request, 'techtopics/topic_list.html', {'topic_list': Topics.objects})
            return redirect('/techtopics/list')
        else :
            return TemplateResponse(request, 'techtopics/user_login.html')
    elif request.method == 'GET':
        return TemplateResponse(request, 'techtopics/user_login.html')

def user_logout(request):
    if request.user.is_authenticated():
        print('IS_AUTHENTICATED')
        logout(request)
        print(request.user)
        return redirect('/techtopics/list')
    else :
        print('ISNOT_AUTHENTICATED')
        result = 'ISNOT_AUTHENTICATED'
        return TemplateResponse(request, 'techtopics/user_login.html', {'result': result})

def list_user(request):
    return TemplateResponse(request, 'techtopics/user_list.html', {'user_list': User.objects})

def detail_user(request, user_id):
    return TemplateResponse(request, 'techtopics/user_detail.html', {'user': User.objects(id=user_id).first()})

def submit_comment(request, topic_id):
    if request.user.is_authenticated():
        if request.method == 'POST':
            csrf(request)
            post = request.POST.copy()
            # post.pop('CsrfResponseMiddlewaretoken')
            model = Comments()
            model.auther = request.user
            model.context = post.get('context')
            model.commtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            model.topiclink = Topics.objects(id=topic_id).first()
            if model.save():
                print('CommentOK')
                return redirect('/techtopics/topic/'+topic_id+'/')
            else:
                print('CommentNotOK')
                return redirect('/techtopics/topic/'+topic_id+'/')
        elif request.method == 'GET':
            return redirect('/techtopics/topic/'+topic_id+'/')
    else:
        login_require = True
        return TemplateResponse(request, 'techtopics/topic_list.html', {'login_require': login_require})