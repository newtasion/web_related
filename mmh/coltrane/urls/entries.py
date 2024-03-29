from django.conf.urls.defaults import *
from django.views.generic import date_based
#from django.views.generic import list_detail


from coltrane.models import Entry

entry_info_dict = {
    'queryset': Entry.live.all(),
    'date_field': 'pub_date',
}

explicit_name_dict = {
    'template_object_name': 'object_list',
}

# Change the variable sent to archive index to 'object_list' instead of 'latest'
# This is useful for reusing templates because now each will pass the same named object
explicit_entry_info_dict = dict(entry_info_dict.items() + explicit_name_dict.items())


from coltrane.models import Category


#urlpatterns = patterns('',
#    (r'^1$', 'django.views.generic.date_based.archive_index', dict(explicit_entry_info_dict, template_name='coltrane/entry_archive.html'), 'coltrane_entry_archive_index'),
#    (r'^$', 'django.views.generic.date_based.archive_index', dict(explicit_entry_info_dict, template_name='coltrane/entry_archive.html'), 'coltrane_entry_archive_index'),
#    (r'^links/(?P<slug>[-\w]+)/$', 'coltrane.views.link_category_detail', {}, 'coltrane_entry_detail'),
#    (r'^(?P<year>\d{4})/$', 'archive_year', entry_info_dict, 'coltrane_entry_archive_year'),
#    #(r'^(?P<year>\d{4})/$', 'archive_year', dict(entry_info_dict, template_name='coltrane/entry_archive_year.html'), 'coltrane_entry_archive_year'),
#    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', dict(entry_info_dict,template_name='coltrane/entry_detail.html'), 'coltrane_entry_detail'),
#)


urlpatterns = patterns('django.views.generic.date_based',
    (r'^$', 'archive_index', explicit_entry_info_dict, 'coltrane_entry_archive_index'),
    
    (r'^(?P<year>\d{4})/$', 'archive_year', entry_info_dict, 'coltrane_entry_archive_year'),
    
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'archive_month', entry_info_dict, 'coltrane_entry_archive_month'),
    
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'archive_day', entry_info_dict, 'coltrane_entry_archive_day'),
    
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', entry_info_dict, 'coltrane_entry_detail'),
)
