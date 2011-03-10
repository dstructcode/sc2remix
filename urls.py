from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('dciphrd.sc2remix.views',
    # Example:
    # (r'^dciphrd/', include('dciphrd.foo.urls')),

    (r'^$', 'upload_replay'),
    (r'^(?P<r_id>\w+)$', 'parsed'),
    (r'^d/(?P<r_id>\w+)$', 'download_replay'),
    (r'^a/d/(?P<r_id>\w+)$', 'download_archive'),
#    (r'^item/(?P<item_id>\d+)/$', 'item'),
#    (r'^item/search/$', 'item_search'),
#    (r'^post/(?P<post_id>\d+)/$', 'post'),
#    (r'^post/(?P<post_id>[0-9]+)/comments/get/(?P<comment_id>[0-9]+)/', 'get_comments'),
)
