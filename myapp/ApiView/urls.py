from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Blank,name="Blank"),
    path('allPosts/',views.PostList,name="PostList"),
    path('createPost/',views.PostCreate,name="PostCreate"),
    path('updatePost/<int:pk>',views.PostUpdate,name="PostUpdate"),
    path('deletePost/<int:pk>',views.PostDelete,name="PostDelete"),
    
  

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

