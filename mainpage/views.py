from django.shortcuts import render,redirect
from django.views.generic.list import ListView

from .models import WatchList,ListEntry
from .forms import WatchListForm,EntryForm

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
    if request.method == "POST":
        formdata = WatchListForm(request.POST)
        if formdata.is_valid():
            watchlist = formdata.save(commit=False)
            watchlist.save()
            return redirect('viewlist', list_id=watchlist.pk)
    else:
        form = WatchListForm()
        return render(request, 'mainpage/newlist.html', {'form': form})

def newentry(request, list_id):
    if request.method == "POST":
        formdata = EntryForm(request.POST)
        if formdata.is_valid():
            listentry = formdata.save()
            listentry.watchlist = list_id
            listentry.save()
            return redirect('viewlist', list_id=listentry.watchlist)
    else:
        form = EntryForm()
        return render(request, 'mainpage/newentry.html', {'form': form, 'list_id': list_id})
    
