from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('todoes/', include('todosaz_todoes.urls')),
    path('accounts/', include('todosaz_accounts.urls')),
    path('news/', include('todosaz_news.urls')),
    path('settings/', include('todosaz_settings.urls')),
    path('api/', include('todosaz_api.urls')),
    path('', include('todosaz_contact.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
