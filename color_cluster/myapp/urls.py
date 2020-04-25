from django.conf.urls import url
from .views import MyappView

urlpatterns = [
               url(r'', MyappView.as_view(), name='index'),
               ]