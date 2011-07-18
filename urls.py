from django.conf.urls.defaults import *
from recipe import views


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url('^index/$', 'recipe.views.index',name='index'),
    url('^detail/(?P<recipe_id>[\w-]+)/$', 'recipe.views.detail',name='recipe_detail'),
    (r'^search/', include('haystack.urls')),                   
    (r'^admin/', include(admin.site.urls)),
    #('^hello/$', hello),
) 
