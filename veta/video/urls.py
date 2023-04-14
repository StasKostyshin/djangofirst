from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.video_home, name='video_home'),
    path('<int:pk>', views.VideoDetailView.as_view(), name='video-detail')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)