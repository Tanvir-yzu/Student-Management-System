from django.contrib import admin
from django.urls import path, include
from students import urls as student_urls  
import jet.dashboard

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')), 
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')), 
    path('admin/', admin.site.urls),
    path('', include(student_urls))  
]

# admin.site.site_header = "Book Management Admin"
# admin.site.site_title = "Book Management Portal"
# admin.site.index_title = "Welcome to Book Management System"