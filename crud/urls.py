from django.conf.urls import url, re_path
from . import views

urlpatterns= [
    url(r'^$', views.index, name='index'),
    url(r'^admin$', views.admin, name='admin'),
	url(r'^log$', views.log, name='log'),
	url(r'^login$', views.login, name='login'),
	url(r'^sign$', views.sign, name='sign'),
	url(r'^signup$', views.signup, name='signup'),
    url(r'^pup$', views.pup, name='pup'),
    url(r'^purp$', views.purp, name='purp'),
    url(r'^pview$', views.pview, name='pview'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^myupdate$', views.myupdate, name='myupdate'),
    url(r'^daily$', views.daily, name='myupdate'),
    url(r'^dview$', views.dview, name='dview'),
    url(r'^enq$', views.enq, name='enq'),
    url(r'^enquirer', views.enquirer, name='enquirer'),
    url(r'^fview$', views.fview, name='fview')
]