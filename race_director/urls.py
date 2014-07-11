from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'race_director.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'results.views.home', name='home'),
    url(r'^register/$', 'results.views.register', name='register'),
    url(r'^profile/$', 'results.views.profile', name='profile'),






    url(r'^clubs/$', 'results.views.clubs', name='clubs'),
    url(r'^clubs/new/$', 'results.views.new_club', name='new_club'),
    url(r'^clubs/(?P<club_id>\w+)/$', 'results.views.view_club', name='view_club'),
    url(r'^clubs/(?P<club_id>\w+)/edit/$', 'results.views.edit_club', name='edit_club'),
    url(r'^clubs/(?P<club_id>\w+)/delete/$', 'results.views.delete_club', name='delete_club'),

    url(r'^races/$', 'results.views.races', name='races'),
    url(r'^races/new/$', 'results.views.new_race', name='new_race'),
    url(r'^races/results/(?P<race_id>\w+)/$', 'results.views.view_race_results', name='view_race_results'),
    url(r'^races/(?P<race_id>\w+)/$', 'results.views.view_race', name='view_race'),
    url(r'^races/(?P<race_id>\w+)/edit/$', 'results.views.edit_race', name='edit_race'),
    url(r'^races/(?P<race_id>\w+)/delete/$', 'results.views.delete_race', name='delete_race'),

    url(r'^racers/$', 'results.views.racers', name='racers'),
    url(r'^racers/new/$', 'results.views.new_racer', name='new_racer'),
    url(r'^racers/(?P<racer_id>\w+)/$', 'results.views.view_racer', name='view_racer'),
    url(r'^racers/(?P<racer_id>\w+)/edit/$', 'results.views.edit_racer', name='edit_racer'),
    url(r'^racers/(?P<racer_id>\w+)/delete/$', 'results.views.delete_racer', name='delete_racer'),

    url(r'^results/$', 'results.views.results', name='results'),
    url(r'^results/new/$', 'results.views.new_result', name='new_result'),
    url(r'^results/(?P<result_id>\w+)/$', 'results.views.view_result', name='view_result'),
    url(r'^results/(?P<result_id>\w+)/edit/$', 'results.views.edit_result', name='edit_result'),
    url(r'^results/(?P<result_id>\w+)/delete/$', 'results.views.delete_result', name='delete_result'),



)
