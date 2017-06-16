from django.conf.urls import url
from rango import views

urlpatterns = [ 
				url(r'^$', views.index, name='index'), # ^$ - Empty String - Homepage
				url(r'^about/', views.about, name='about'),
			  ]