from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'race_director.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'results.views.home', name='home'),
    url(r'^register/$', 'results.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),


    url(r'^profile/$', 'results.views.profile', name='profile'),
    url(r'^profile/(?P<user_id>\w+)/update/$', 'results.views.profile_update', name='profile_update'),



    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # Support old style base36 password reset links; remove in Django 1.7
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),





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




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
