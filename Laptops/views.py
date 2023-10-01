import mysql.connector as mysql
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from Laptops.models import asset_data,emp_data,assign_assets_data_m


# Create your views here.

def Home_Page(req):
    return render(req,"login_page.html")

#   ================================================================================== 

def login_method(req):
 
    if req.method=="POST":
        u=req.POST.get('username')
        p=req.POST.get('password')
       
        # fm=AuthenticationForm(request=req,data=req.POST)
        # if fm.is_valid():
        #     uname=fm.cleaned_data['username']
        #     upass=fm.cleaned_data['password']
        #     user=authenticate(username=uname,password=upass)
        #     if user is not None:
        #         login(req,user)
        #         return render(req,"Dashboard.html",{'user':user})
        user=authenticate(username=u,password=p) 
        if user is not None:   
            login(req,user)
            return HttpResponseRedirect('Dashboard')
        else:
            msg= messages.error(req," Invalid User & Password")
            return HttpResponseRedirect('/')   
    else:
        fm=AuthenticationForm()
        return HttpResponseRedirect('login')
    

       

#   ================================================================================== 

def logined_method(req):
        if req.user.is_authenticated: 
          totoal_asset= asset_data.objects.all().count()
          total_emp=emp_data.objects.all().count()
          assign_asset_c= asset_data.objects.filter(assign_status="True").count()
          unassign_asset_c=asset_data.objects.filter(assign_status="False",asset_scrap='No').count()
          scrap_asset=asset_data.objects.filter(asset_scrap="Yes").count()
          
          



          return render(req,"Dashboard1.html",{'user':req.user,'totoal_asset':totoal_asset,'scrap_asset':scrap_asset,'total_emp':total_emp,'assign_asset_c':assign_asset_c,'unassign_asset_c':unassign_asset_c})
        else:
              return HttpResponseRedirect('/')   


#   ================================================================================== 

def logout_method(req):
    logout(req)
    return HttpResponseRedirect('/')

#   ================================================================================== 
def add_asset_method(req):
    if req.user.is_authenticated:   
     return render(req,'add_asset.html',{'user':req.user})
    else:
         return HttpResponseRedirect('/')



def Employees_method(req):
    if req.user.is_authenticated:
        total_asset= asset_data.objects.all()

        return render(req,"Employees.html",{'user':req.user,'total_asset':total_asset})
    else:
        return HttpResponseRedirect('/')


def save_asset(req):
   try:
       if req.user.is_authenticated: 
         if req.method=="GET":
            # assetid=req.GET.get('assetid')
            login_user=req.user
            assettype=req.GET.get('assettype')
            company=req.GET.get('company')
            model=req.GET.get('model')
            serial=req.GET.get('serial')
            hostname=req.GET.get('hostname')
            processor=req.GET.get('Processor')
            ram=req.GET.get('ram')
            Storage_type=req.GET.get('Storage_type')
            Storage=req.GET.get('Storage')
            screen_size=req.GET.get('screen_size')
            Purchaseing_Date=req.GET.get('Purchaseing_Date')
            asset_age=req.GET.get('asset_age')
            sapcode=req.GET.get('sapcode')
            tba=req.GET.get('tba')
            ltdtcon=req.GET.get('ltdtcon')
            other_details=req.GET.get('other_details')
            asset_location=req.GET.get('asset_location')
            asset_state=req.GET.get('asset_state')
            scrap=req.GET.get('scrap')
            
            # print(assetid)
            print(login_user)
            # print(assettype)
            # print(company)
            # print(model)
            # print(serial)
            # print(hostname)
            # print(processor)
            # print(ram)
            # print(Storage_type)
            # print(Storage)
            # print(screen_size)
            # print("dTW",Purchaseing_Date) #2023-07-13
            # print(asset_age)
            # print(sapcode)
            # print(tba)
            # print(ltdtcon)
            # print(other_details)
            # print(asset_location)
            # print(asset_state)
            # print(status)
            # print(scrap)

            asset=asset_data(login_user=str(req.user),asset_type=assettype,Company_name=company,asset_model=model,
                              serial_no=serial,host_name=hostname,processor=processor,ram=ram,storage_type=Storage_type,storage=Storage,
                              screen_size=screen_size, purchasing_date=Purchaseing_Date,asset_age=asset_age,sap_code=sapcode,tba=tba,
                              lt_dt_cond=ltdtcon,other_details=other_details,asset_location=asset_location,asset_state=asset_state,asset_scrap=scrap)
            asset.save()
            return HttpResponse("Data Save Susefully")
       else:
         return HttpResponseRedirect('/')

   except:
       return render(req,'add_asset.html',{'user':req.user})



def save_emp_data(req):
   try:
        if req.user.is_authenticated:
            if req.method=="POST":
                login_user=req.user
                emp_id=req.POST.get('emp_id')
                alias_id=req.POST.get('alias_id')
                email_address=req.POST.get('email_address')
                grade=req.POST.get('grade')
                designation=req.POST.get('designation')
                department=req.POST.get('department')
                job_profile=req.POST.get('job_profile')
                user_location=req.POST.get('user_location')
                user_state=req.POST.get('user_state')
                region=req.POST.get('region')
                business_unit=req.POST.get('business_unit')

                print(login_user)
                print(emp_id)
                print(email_address)
                print(business_unit)

                emp_d=emp_data(emp_id=emp_id,login_user=str(login_user),alias_id=alias_id,email_address=email_address,grade=grade,designation=designation
                               ,department=department,job_profile=job_profile,user_location=user_location,user_state=user_state,region=region,business_unit=business_unit)
                emp_d.save()
                return HttpResponse(" Emp Data saved sucessfully!!")


        else:
            return HttpResponseRedirect('/')
   except:
         return HttpResponseRedirect('Add_Employees')

        

def Search_Assign_Emp(req):
    if req.user.is_authenticated:
      try:
        if req.method=="GET":
            s_emp=req.GET.get('emp_id')
           
            s_emp1=assign_assets_data_m.objects.filter(emp_id1=s_emp)
        
            return render(req,'Search_Assign_Emp.html',{'s_emp1':s_emp1})
        else:
          return render(req,'Search_Assign_Emp.html')
      except:
         return HttpResponseRedirect('Search_Assign_Emp')
        
    else:
        return HttpResponseRedirect('/')



def Search_Assign_AssetId(req):
 
     if req.user.is_authenticated:
      try:
        if req.method=="GET":
            s_asset=req.GET.get('asset_id')
            
            s_asset1=assign_assets_data_m.objects.filter(asset_id1=s_asset)
            
            return render(req,'Search_Assign_AssetId.html',{'s_asset1':s_asset1})
        else:
          return render(req,'Search_Assign_AssetId.html')
      
      except:
          return HttpResponseRedirect('Search_Assign_AssetId')
          
        
     else:
        return HttpResponseRedirect('/')















def Assign_Asset_method(req):
    if req.user.is_authenticated:
        total_asset= asset_data.objects.filter(assign_status=False,asset_scrap='No').all()
        total_emp= emp_data.objects.filter(status=False).all()
       
        return render(req,"assign_asset.html",{'user':req.user,'total_asset':total_asset,'total_emp':total_emp,'assetid':0})
    else:
        return HttpResponseRedirect('/')


def Remove_Assign_Asset(req):
  try:  
    if req.user.is_authenticated:
        if req.method=="POST":
            asg_id=req.POST.get('assignId')
            asg_id1=assign_assets_data_m.objects.filter(pk=asg_id)
           

            for i in asg_id1:
                print(i.asset_id1.asset_id)
                print(i.emp_id1.emp_id)

                delete_asset_id=asset_data.objects.get(pk=i.asset_id1.asset_id)
                delete_emp_id=emp_data.objects.get(pk=i.emp_id1.emp_id)
                print(delete_asset_id.assign_status)
                print(delete_emp_id.status)

                delete_asset_id.assign_status=False
                delete_asset_id.save()

                delete_emp_id.status=False
                delete_emp_id.save()            
           
            asg_id1.delete()

            return HttpResponseRedirect('total_assign_asset')
    else:
        return HttpResponseRedirect('/')
  except:
      return HttpResponseRedirect('total_assign_asset')


def Delete_emp(req):
  try:  
    if req.user.is_authenticated:
        if req.method=="POST":
            del_empid=req.POST.get('Del_empId')
            del_empid1=emp_data.objects.get(pk=del_empid)
            del_empid1.delete()
            return HttpResponseRedirect('total_emp')
        
    else:
        return HttpResponseRedirect('/')
  except:
      return HttpResponseRedirect('total_emp')






def total_asset(req):
  if req.user.is_authenticated:
    total_asset= asset_data.objects.all()
    
    return render(req,'Total_Asset.html',{'total_asset':total_asset})
  else:
    return HttpResponseRedirect('/')
  

def total_emp(req):
    if req.user.is_authenticated:
        total_emp=emp_data.objects.all()
        return render(req,'Total_Emp.html',{'total_emp':total_emp})
    else:
        return HttpResponseRedirect('/')



def total_assign_asset(req):
  if req.user.is_authenticated:
    total_assign_data=assign_assets_data_m.objects.all()
    return render(req,'Total_Assign_Asset.html',{'total_assign_data':total_assign_data})
  else:
      return HttpResponseRedirect('/')


def total_unassign_asset(req):
    if req.user.is_authenticated:
        total_unassign_asset=asset_data.objects.filter(assign_status='False',asset_scrap='No').all()
        print(total_unassign_asset)
        return render(req,'Total_Unassign_Asset.html',{'total_unassign_asset':total_unassign_asset})
    else:
        return HttpResponseRedirect('/')


def total_scrap_asset(req):
    if req.user.is_authenticated:
        total_scrap_asset=asset_data.objects.filter(asset_scrap='Yes').all()
       
        return render(req,'Total_Scrap_Asset.html',{'total_scrap_asset':total_scrap_asset})
    else:
        return HttpResponseRedirect('/')



def Search_asset_method(req):
  try:
    if req.user.is_authenticated:
        if req.method=="POST":
            assetid=req.POST.get('asset_id')
            assetid_data=asset_data.objects.all().get(pk=assetid)
            total_asset= asset_data.objects.filter(assign_status=False).all()
            total_emp= emp_data.objects.filter(status=False).all()
          
            return render(req,"assign_asset.html",{'user':req.user,'total_asset':total_asset,'assetid_data':assetid_data,'total_emp':total_emp,'assetid':assetid})
        else:
           return render(req,"assign_asset.html",{'user':req.user,'total_asset':total_asset,'total_emp':total_emp})
    else:
        return HttpResponseRedirect('/')
  except:
       return render(req,"assign_asset.html",{'user':req.user,'total_asset':total_asset,'total_emp':total_emp})
  

def Search_emp_method(req,asid):
 try:
    if req.user.is_authenticated:
       
       if req.method=="POST":
          empid=req.POST.get('emp_id')
          if asid != 0: 
            empid_data=emp_data.objects.all().get(pk=empid)

            assetid_data=asset_data.objects.all().get(pk=asid)
            
            
            total_asset= asset_data.objects.filter(assign_status=False).all()
            total_emp= emp_data.objects.filter(status=False).all()
            
            return render(req,"assign_asset.html",{'user':req.user,'total_asset':total_asset,'empid_data':empid_data,'total_emp':total_emp,'assetid':asid,'assetid_data':assetid_data,})
          else:
              msg= messages.error(req," Please Select Asset Before Select Emp. ")
              return HttpResponseRedirect('http://127.0.0.1:8000/Assign_Asset')

       else:
           return render(req,"assign_asset.html",{'user':req.user,'total_asset':total_asset,'total_emp':total_emp})
     
    else:
        return HttpResponseRedirect('/')
 except:
       return render(req,"assign_asset.html",{'user':req.user,'total_asset':total_asset,'total_emp':total_emp})
  





def assign_asset_data(req):
  try:
    if req.method=="POST":
        if req.POST.get('asset_id')=="":
            msg= messages.error(req," Please Select Asset for Assign Asset ")
            return HttpResponseRedirect('Assign_Asset')
        if req.POST.get('emp_id')=="":
             msg= messages.error(req," Please Select Emp for Assign Asset ")
             return HttpResponseRedirect('Assign_Asset')
        
        login_user1=req.user

        asset_id=req.POST.get('asset_id')
        asset_model=req.POST.get('asset_model')
        serial=req.POST.get('serial')
        hostname=req.POST.get('hostname')
        asset_location=req.POST.get('asset_location')
        Purchaseing_Date=req.POST.get('Purchaseing_Date')
        tba=req.POST.get('tba')

        emp_id=req.POST.get('emp_id')
        alias_id=req.POST.get('alias_id')
        email_address=req.POST.get('email_address')
        grade=req.POST.get('grade')
        designation=req.POST.get('designation')
        department=req.POST.get('department')

        asset_id1=int(asset_id)
        emp_id1=int(emp_id)

      
        
        if asset_id1 and emp_id1 > 0:
            asset_id1=str(asset_id)
            emp_id1=str(emp_id)

            asset_id_main=asset_data.objects.get(pk=asset_id1)
            
            emp_id_main=emp_data.objects.get(pk=emp_id1)

            assign_asset_data12=assign_assets_data_m(login_user=str(login_user1),asset_id1=asset_id_main,asset_model=asset_model,serial_no=serial,host_name=hostname,
                                                   asset_location=asset_location,purchasing_date=Purchaseing_Date,tba=tba,
                                                   emp_id1=emp_id_main,alias_id=alias_id,email_address=email_address,grade=grade,designation=designation,department=department)
            assign_asset_data12.save()

            asset_id_main=asset_data.objects.get(pk=asset_id1)
            asset_id_main.assign_status=True
            asset_id_main.save()

            emp_id_main=emp_data.objects.get(pk=emp_id1)
            emp_id_main.status=True
            emp_id_main.save()

            return HttpResponse("Asset Assigned to Emp...")
  except:
      msg= messages.error(req," Please Select Asset and Emp for Assign Asset ")
      return HttpResponseRedirect('Assign_Asset')
       
     
   
   


