from django.urls import path
from.import views

urlpatterns = [
    path('', views.index1, name='index1'),
    path('index1/index/', views.index, name='index'),
    path('adminpage/',views.adminpage,name="adminpage"),
    path('adminpage/adminlogin/',views.adminlogin,name="adminlogin"),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('index1/index/delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),

]

