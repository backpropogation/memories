from django.contrib import admin
from django.urls import include, path

from apps.router import router
from apps.users.views import FacebookLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/facebook/login/', FacebookLogin.as_view(), name='fb_login'),
    path('api/', include(router.urls)),
]
