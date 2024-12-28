from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login',views.Login,name="Login"),
    path('register',views.Register,name="Register"),
    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

