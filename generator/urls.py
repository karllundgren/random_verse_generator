from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    
]
urlpatterns += [
    path('verse', views.display_verse, name='display-verse'),
    path('account/', include('django.contrib.auth.urls')),
]

'''
account/login/ [name='login']
account/logout/ [name='logout']
account/password_change/ [name='password_change']
account/password_change/done/ [name='password_change_done']
account/password_reset/ [name='password_reset']
account/password_reset/done/ [name='password_reset_done']
account/reset/<uidb64>/<token>/ [name='password_reset_confirm']
account/reset/done/ [name='password_reset_complete']
'''

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)