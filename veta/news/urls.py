from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)