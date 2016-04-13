from django.shortcuts import render
from django.views.generic.list import ListView

from .models import WatchList,ListEntry
from .forms import WatchListForm

# Create your views here.
class IndexPage(ListView):
    template_name = 'mainpage/index.html'
    context_object_name = 'mainpage_watchlists'

    def get_queryset(self):
        return WatchList.objects.order_by('user')

class ListViewPage(ListView):
    template_name = 'mainpage/list.html'
    context_object_name = 'watchlist'

    def get_queryset(self):
        list_id = self.kwargs['list_id']
        print("List id: " + list_id)
        return ListEntry.objects.filter(watchlist=list_id)

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        print("List id: " + self.kwargs['list_id'])
        context['list'] = WatchList.objects.get(pk=self.kwargs['list_id'])
        return context


def newlist(request):
    form = WatchListForm()
    return render(request, 'mainpage/newlist.html', {'form': form})
