from django.shortcuts import render
from django.views.generic import ListView

from mainsite.models import News


# Create your views here.
def mainpage(request):
    return render(request, 'mainsite/index.html')

class NewsView(ListView):
    model = News
    queryset = News.objects.filter(draft=False).order_by('-id')
    template_name = "mainsite/blog-right-sidebar.html"
    paginate_by = 6