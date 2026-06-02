from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('about/', include('about_app.urls')),
    path('register/', include('register_app.urls')),
    path('login/', include('login_app.urls')),
    path('donate/', include('donation_app.urls')),
    path('human-food/', include('human_food_app.urls')),
    path('animal-food/', include('animal_food_app.urls')),
    path('admin-page/', include('admin_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)