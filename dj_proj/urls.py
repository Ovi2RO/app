"""
URL configuration for dj_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
"""
1. `from django.contrib import admin`: This import allows you to include the Django admin site 
in your project.

2. `from django.urls import path, include`: This import is used to define URL patterns in Django and 
include other URL configurations.
"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('home/', include('home.urls')),
]
"""
- `path('admin/', admin.site.urls)`: This URL pattern maps the '/admin/' URL to the Django admin site. 
It allows you to access the admin interface and perform administrative tasks.

- `path('', include('accounts.urls'))`: This URL pattern includes the URL patterns defined in the 
'accounts.urls' module. It allows you to handle URLs related to user authentication and account management.

- `path('home/', include('home.urls'))`: This URL pattern includes the URL patterns defined in the 'home.urls' 
module. It allows you to handle URLs related to the home page or other features of your application.
"""