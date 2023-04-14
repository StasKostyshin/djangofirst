from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Video
from django.views.generic.detail import DetailView



# Create your views here.
def video_home(request):
    video = Video.objects.order_by('-date')
    paginator = Paginator(video, 4)
    page = request.GET.get('page')
    try:
        video = paginator.page(page)
    except PageNotAnInteger:
        video = paginator.page(1)
    except EmptyPage:
        video = paginator.page(paginator.num_pages)
    vars = dict(
        video=video,
    )
    return render(request, 'video/video_home.html', {'video': video})

def video_detail(request):
    num_video = File.object.all()
    return render(request, 'details_video.html', context={'num_vid': num_video})


class VideoDetailView(DetailView):
    model = Video
    template_name = 'video/details_video.html'
    context_object_name = 'videos'

