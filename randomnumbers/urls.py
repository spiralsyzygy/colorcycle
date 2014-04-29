from django.conf.urls import patterns, include, url
from .views import nine_random_numbers

urlpatterns = patterns('',
    url(r'^nine_random_numbers/', nine_random_numbers, name='nine_random_numbers'),
)