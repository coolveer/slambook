from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('login_pro',views.login_pro,name='login'),
    path('signup',views.signup_view,name='signup'),
    path('detail/<pk>',views.detail,name='detail'),
    path('home/<pk>',views.home,name='home'),
    path('signup_pro',views.signup_pro,name='signup_pro'),
    path('slambook',views.detail_slam,name='slambook'),
    path('slambook/<pk>/<fname>',views.detail_slam,name='slambook'),
    path('logout',views.logout_view,name='logout'),
    path('process/<pk>',views.process_slam,name='process'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)