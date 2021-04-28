from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('register/', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('directory/', include('directory_page.urls')),
    path('email/', include('sendmail.urls')),
    path('dates/', include('semester_dates.urls')),
    path('enter/', include('enter.urls')),
    path('reports/', include('reports.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
