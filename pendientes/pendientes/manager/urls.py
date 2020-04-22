from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('addpending/',views.AddPending.as_view(), name = 'add-pending'),
    path('workdetail/<int:pk>/',views.ViewWorkDetail.as_view(), name = 'work-detail'),
    path('searchwork/',views.SearchWork.as_view(), name = 'search-work'),
    path('updatework/<int:pk>/',views.UpdateWork.as_view() , name= 'update-work'),
    path('onlycs/',views.onlycs, name = 'only-cs'),
    path('pendtosend/',views.pendtosend, name = 'pend-to-send'),
    path('pendcontested/',views.pendcontested, name = 'pend-contested'),
    path('pendcontestedNR/',views.pendcontestedNR, name = 'pend-contestedNR'),
    path('pendaztool/',views.pendaztool, name = 'pend-az-tool'),
    path('pendinstall/',views.pendinstall, name = 'pend-install'),
    path('penddoc/',views.penddoc, name = 'pend-doc'),
    path('pendpic/',views.pendpic, name = 'pend-pic'),
    path('export/xls/', views.export_users_xls, name='export_users_xls'),
    path('deletework/<int:pk>',views.DeleteWorkSheet.as_view(), name = 'delete-work'),
]