from django.urls import include, path
from . import views
from myapp.views import GeeksDetailView
from account import views

urlpatterns=[
path('user/', include('account.urls')),
path('',views.create_view),
path('list/',views.list_view),
path('<id>/', views.detail_view ),
path('<id>/update/',views.update_view)


]
