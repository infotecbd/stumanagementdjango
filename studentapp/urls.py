
from django.urls import path
from .views import HomePage, Add_Std, EditStd, DeleteStd  # import from views function name or page name

urlpatterns = [
    path('', HomePage, name='homePage'),
   
  
    path("addstd/", Add_Std, name='addstd'),
    path("edit/<int:id>/", EditStd, name='edit'),
    path("delete/<int:id>/", DeleteStd, name='delete'),
]
