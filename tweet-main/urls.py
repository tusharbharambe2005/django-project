
from django.contrib import admin
from django.urls import path,include
from tweet import views as tweet_view
import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views
from .views import home_page
urlpatterns = [
    path('',home_page),
    path('tweet/',include('tweet.urls')),
    path('admin/', admin.site.urls),
    path('update/', include('django.contrib.auth.urls')),

]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)        