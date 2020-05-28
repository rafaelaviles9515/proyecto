from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.biblioteca.views import libro_view, libro_list, libro_edit, libro_delete, index

urlpatterns = [
		url(r'^$', login_required(index), name='index_libro'),
 		url(r'^nuevo$', login_required(libro_view), name='libro_crear'),
  	 	url(r'^listar$',login_required(libro_list), name='libro_listar'),
  	 	url(r'^editar/(?P<id_libro>\d+)/$', login_required(libro_edit), name='libro_editar'),
     	url(r'^eliminar/(?P<id_libro>\d+)/$', login_required(libro_delete), name='libro_eliminar'),
]