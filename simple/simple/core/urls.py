from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'simple.core.views.home', name='home'),
    url(r'^contato/', 'simple.core.views.contact', name='contact'),
)