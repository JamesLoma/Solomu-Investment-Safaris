from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404
from django.urls.conf import include

admin.site.site_header = "Tourism Admin"
admin.site.site_title = "Tourism Admin Portal"
admin.site.index_title = "Tourism To VogueVue"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('safaris.urls'))
]

handler404 = 'safaris.views.error_404'