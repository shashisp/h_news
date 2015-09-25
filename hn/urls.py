from django.conf.urls import patterns, include, url
from django.contrib import admin
from news.views import ArticleListView, VoteFormView, ReadFormView, DeleteFormView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'news.views.home', name='home'),
    url(r'^$', ArticleListView.as_view(), name='home'),
    url(r'^login/', 'users.views.login', name='login'),
    url(r'^logout/', 'users.views.logout', name='logout'),
    url(r'^register/$', 'users.views.register', name='register'),
    url(r'^submit/$', 'news.views.create_new', name='submit'),
    url(r'^vote/$', login_required(VoteFormView.as_view()), name="vote"),
    url(r'^read/$', login_required(ReadFormView.as_view()), name="read"),
    url(r'^delete/$', login_required(DeleteFormView.as_view()), name="delete"),

    url(r'^admin/', include(admin.site.urls)),
)
