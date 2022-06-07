from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from news import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('/<slug:post>/', views.post_detail, name='post_detail'),
    
    path('add/', views.add, name='add'),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),

    path('login/', views.loginPage, name='login'),
    path('register/', views.regPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', views.homePage, name='home'),
    
    path('add/', views.add),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),
)
