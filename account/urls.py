from django.urls import path

from account.views import SignUpView

from django.conf.urls import url
#from account.views import signup#, activate, account_activation_sent


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
     #url(r'^signup/$', signup, name='signup'),
    #url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #    activate, name='activate'),
]
