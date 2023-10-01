from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.Home_Page),
    path('login',views.login_method,name="login"),
    path('Dashboard',views.logined_method,name="logined"),
    path('logout',views.logout_method,name="logout"),
    path('Add_Asset',views.add_asset_method,name="add_asset"),
    path('Add_Employees',views.Employees_method,name="Employees"),
    path('Assign_Asset',views.Assign_Asset_method,name="Assign_Asset"),
    path('Search_Assign_Emp',views.Search_Assign_Emp,name="Search_Assign_Emp"),
    path('Search_Assign_AssetId',views.Search_Assign_AssetId,name="Search_Assign_AssetId"),



    path('save_asset',views.save_asset,name="save_asset"),
    path('save_emp_data',views.save_emp_data,name="save_emp_data"),
    path('assign_asset_data',views.assign_asset_data,name="assign_asset_data"),



    path('total_asset',views.total_asset,name="total_asset"),
    path('total_emp',views.total_emp,name="total_emp"),
    path('total_assign_asset',views.total_assign_asset,name="total_assign_asset"),
    path('total_unassign_asset',views.total_unassign_asset,name="total_unassign_asset"),
    path('total_scrap_asset',views.total_scrap_asset,name="total_scrap_asset"),

    path('Remove_Assign_Asset',views.Remove_Assign_Asset,name="Remove_Assign_Asset"),
    path('Delete_emp',views.Delete_emp,name="Delete_emp"),


    path('Search_asset',views.Search_asset_method,name="Search_asset"),
    path('Search_emp/<int:asid>',views.Search_emp_method,name="Search_emp"),
    
   
    
]