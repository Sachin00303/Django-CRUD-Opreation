from django.urls import path
from . import views
urlpatterns = [
    #path('',views.showfilter, name="showdata"),
    #path('',views.show, name="showdata"),
   
    #path('ragister/',views.ragister, name="create"),
    #path('update/<int:id>/',views.update, name="update"),
    # path('details/<int:id>/',views.delete, name="details"),
    #path('delete/<int:id>/',views.delete, name="delete"),
    #path('bulkinsert/',views.bulk_insert, name="bulk"),
    path('upload/',views.upload ,name="upload"),
    
    path('ragister/',views.ragisterView.as_view(), name="create"),
    path('update/<int:pk>/',views.updatempview.as_view(), name="update"),
    path('delete/<int:pk>/',views.ModelDeleteView.as_view(), name="delete"),
    path('detail/<int:pk>',views.ModelDetailView.as_view(), name="details"),
    path('Showlist/',views.showListView.as_view(), name="showdata"),
   # path('ragister/',views.empview.as_view(), name="create"),
]