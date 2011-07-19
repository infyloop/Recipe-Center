from django.conf.urls.defaults import *
from recipe import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from djangoratings.views import AddRatingFromModel

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url('^index/$', 'recipe.views.index',name='index'),
    url('^detail/(?P<recipe_id>[\w-]+)/$', 'recipe.views.detail',name='recipe_detail'),
    (r'^search/', include('haystack.urls')),                   
    (r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),
     url(r'^rate-my-post/(?P<object_id>\d+)/(?P<score>\d+)/$', AddRatingFromModel(), {
        'app_label': 'recipe',
        'model': 'RecipeDump',
        'field_name': 'rating',
    },name='vote'),


                       
    #('^hello/$', hello),
) 
urlpatterns += staticfiles_urlpatterns()

