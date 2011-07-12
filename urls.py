from django.conf.urls.defaults import *



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    #('^hello/$', hello),
    url('^index/$', 'recipe.views.index',name='recipe_index'),
    url('^detail/(?P<recipe_id>\d+)/$', 'recipe.views.detail',name='recipe_detail')
)
