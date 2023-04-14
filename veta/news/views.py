from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Articles
from django.views.generic.detail import DetailView

# Create your views here.
def news_home(request):
    news = Articles.objects.order_by('-date')
    paginator = Paginator(news, 3)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    vars = dict(
        news=news,
        )
    return render(request, 'news/news_home.html', {'news': news})

def news_detail(request):
    num_img = Image.object.all()
    return render(request, 'details_view.html', context={'num_img': num_img})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'




