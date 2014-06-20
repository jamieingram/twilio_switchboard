"""
switchboard.creator
-----------------------
"""

from django.conf.urls import patterns, url


urls = [
    url(r'^twilio/welcome/$', 'welcome', name='welcome'),
    url(r'^twilio/welcome/options/$',
        'welcome_options', name='welcome_options'),
    url(r'^twilio/welcome/options/submit$',
        'handle_welcome_options', name='handle_welcome_options'),

    url(r'^twilio/login/$', 'login', name='login'),
    url(r'^twilio/login/submit$', 'handle_login', name='handle_login'),

    url(r'^twilio/connect/$', 'connect', name='connect'),
    url(r'^twilio/connect/submit$', 'handle_connect', name='handle_connect'),
    url(r'^twilio/connect/record$', 'handle_record', name='handle_record'),

    url(r'^twilio/user/([0-9]{6})/messages/$',
        'twilio_messages', name='twilio_messages'),

    url(r'^user/([0-9]{6})/$', 'user', name='user'),
    url(r'^user/([0-9]{6})/messages/$', 'messages', name='messages'),
    url(r'^$', 'home', name='home')
]

urlpatterns = patterns('switchboard.twiliorouter.views', *urls)
