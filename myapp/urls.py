from django.urls import path
#now import the views.py file into this code
from . import views
from myapp.views import GeeksDetailView

urlpatterns=[
path('',views.create_view),
path('list/',views.list_view),
path('<id>/', views.detail_view ),
path('<id>/update/',views.update_view)


]
