from . import views
from django.urls import path
app_name="search_engine"
urlpatterns = [ 
    path('search_engine',views.search_engine,name="search_engine"),
    path('id_request',views.id_request,name="id_request"),
    path('plate_request',views.plate_request,name="plate_request"),
    path('search_engine/result/<int:id>/',views.result,name="result"),
]
