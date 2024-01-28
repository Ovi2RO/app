from django.contrib import admin
from django.urls import path, include
from django.conf import settings # import for images to show up in the browser
from django.conf.urls.static import static # import for images to show up in the browser
from accounts.views import landing_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_view, name='landing_view'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('home/', include('home.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('laika/',include('laika.urls')),
    path('test/', include('A_test_post_app.urls')),     # away
    path('parenting/', include('get_app.urls')),
    path('sport/',include('tennis_app.urls')),
    path('chat_rooms/', include('rooms.urls')),

    path('apis/', include('apis.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # this line allows images to show up in the browser during development

