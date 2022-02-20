from django.shortcuts import render, redirect
from django.views import generic
from .models import Photo


def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos': photos})


class PhotoUploadView(generic.CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})


class PhotoDetailView(generic.DetailView):
    model = Photo
    template_name = 'photo/detail.html'


class PhotoUpdateView(generic.UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'


class PhotoDeleteView(generic.DeleteView):
    model = Photo
    template_name = 'photo/delete.html'
    success_url = '/'
