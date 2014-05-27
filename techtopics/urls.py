from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'techtopics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    # change to http://IP/testMongo/list, and focus to testMongoapp.views.list_business
    url(r'^techtopics/list$', 'techtopicApp.views.list_topics'),
    # topics
    url(r'^techtopics/topic/(?P<topic_id>\w+)/$', 'techtopicApp.views.detail_topic'),
    url(r'^techtopics/topic/create$', 'techtopicApp.views.create_topic'),
    url(r'^techtopics/topic/delete/(?P<topic_id>\w+)/$', 'techtopicApp.views.delete_topic'),
    # user
    url(r'^techtopics/user/list$', 'techtopicApp.views.list_user'),
    url(r'^techtopics/user/register$', 'techtopicApp.views.create_user'),
    url(r'^techtopics/login$', 'techtopicApp.views.user_login'),
    url(r'^techtopics/logout$', 'techtopicApp.views.user_logout'),
    url(r'^techtopics/user/(?P<user_id>\w+)/$', 'techtopicApp.views.detail_user'),
    # comments
    url(r'^techtopics/topic/(?P<topic_id>\w+)/submit_comment$', 'techtopicApp.views.submit_comment')
)
