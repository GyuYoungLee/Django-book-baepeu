from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'photo'

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('upload/', views.PhotoUploadView.as_view(), name='photo_upload'),
    path('detail/<int:pk>', views.PhotoDetailView.as_view(), name='photo_detail'),
    path('update/<int:pk>', views.PhotoUpdateView.as_view(), name='photo_update'),
    path('delete/<int:pk>', views.PhotoDetailView.as_view(), name='photo_delete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
