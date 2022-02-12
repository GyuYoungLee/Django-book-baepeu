from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import Bookmark


class BookmarkListView(generic.ListView):
    model = Bookmark
    paginate_by = 2


class BookmarkCreateView(generic.CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_create'  # default: bookmark_form.html
    success_url = reverse_lazy('bookmark:list')


class BookmarkDetailView(generic.DetailView):
    model = Bookmark


class BookmarkUpdateView(generic.UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'  # default: bookmark_form.html

    def get_success_url(self):
        return reverse_lazy('bookmark:detail', kwargs=self.kwargs)


class BookmarkDeleteView(generic.DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')
