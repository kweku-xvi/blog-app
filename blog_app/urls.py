"""blog_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('signup/', user_views.signup, name='signup'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', user_views.LogIn.as_view(), name='login'),
    path('logout/', user_views.LogOut.as_view(), name='logout'),
    path('password-reset/', user_views.UserPasswordReset.as_view(), name='password_reset'),
    path('password-reset/done/', user_views.UserPasswordResetDone.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/token/', user_views.UserPasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', user_views.UserPasswordResetComplete.as_view(), name = 'password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)