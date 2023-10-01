S. No.
LT/DT Code
EMP ID
USER NAME
Asset Type
DEPARTMENT
LAPTOP MAKE
SERIAL NUMBER
PROCESSER
RAM
STORAG TYPE
Screen Size
MANUFACTURING DATE
AGE
SAP CODE
Give Temprery Of USER
LT Condition
Other Details
LMS
HostName


tempery asset update -----






S. No
Emp Id
EMP Name
Alias ID
Email
Grade
Designation
Department
Job Profile
User Location
Region
Business Unit
Asset Location
1
Asset Type
Make
Model
Serial no.
Processor Type
processor Series
Current Age Year
Age Calculator
Portal Date (DD-MM-YYYY) Exp. 10-Jan-2022
Current Status
Display Size
Sap Asset Code
Current Hostname
Apex One
Ram
HDD Size
Hard Disk Type
OS
I verified it
verified  for Insurance
Current Status Final
In remarck if you have
Engg Name
CORP/State 
Department
Grade Wise                                                               
Make Wise                                          
Age Wise
PO No
Po Date
Price Without GST
UW
Budget Year
Old Emp Id
Old EMP Name
Desktop PAN India  Detail  15-02-23
SD

Asset Nature Text
Asset Mfg Year
Asset Location in SAP



# con=mysql.connect(host="localhost",user="root",password="yogsingh",port="3307" ,database="ams")
    # assetid=req.GET.get('assetid')
    # assettype=req.GET.get('assettype')
    # company=req.GET.get('company')
    # model=req.GET.get('model')
    # serial=req.GET.get('serial')
    # hostname=req.GET.get('hostname')
    # processor=req.GET.get('Processor')
    # ram=req.GET.get('ram')
    # Storage_type=req.GET.get('Storage_type')
    # Storage=req.GET.get('Storage')
    # screen_size=req.GET.get('screen_size')
    # Purchaseing_Date=req.GET.get('Purchaseing_Date')
    # asset_age=req.GET.get('asset_age')
    # sapcode=req.GET.get('sapcode')
    # tba=req.GET.get('tba')
    # ltdtcon=req.GET.get('ltdtcon')
    # other_details=req.GET.get('other_details')
    # asset_location=req.GET.get('asset_location')
    # asset_state=req.GET.get('asset_state')
    # status=req.GET.get('status')
    # scrap=req.GET.get('scrap')
    
    # print(login_user)
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
    # sql="insert into asset_data(asset_id,asset_type)values('02','lp')"
    # cr=con.cursor()
    # cr.execute(sql)
    # con.commit()
    # con.close()
    # return HttpResponse("done")
#asset_brand,serial_no,host_name,processor,ram,storage_type,storage_size,screen_size,purchaseing_date,asset_age,sap_code,ltdt_cond,Other_details,asset_location,asset_state,asset_status,asset_scrap









<table class="table">

    <tr>
        <th scope="col">Asset ID</th>
        <td> {{assetid_data.asset_id}}</td>
    </tr>
    <tr>
        <th scope="col">Asset Model No.</th>
        <td> {{assetid_data.asset_model}}</td>
    </tr>
    <tr>
        <th scope="col">Asset Serial No.</th>
        <td>{{assetid_data.serial_no}}</td>
    </tr>

    <tr>
        <th scope="col">Asset Host Name</th>
        <td> {{assetid_data.host_name}}</td>
    </tr>

    <tr>
        <th scope="col">Asset Location </th>
        <td> {{assetid_data.asset_location}}</td>
    </tr>


    <tr>
        <th scope="col">Asset Purchaseing Date</th>
        <td> {{assetid_data.purchasing_date}}</td>
    </tr>

    <tr>
        <th scope="col">TBA</th>
        <td> {{assetid_data.tba}}</td>
    </tr>



</table>





S---Bihar
    D--Bhagalpur
                             
Araria
Banka
Bhagalpur
Bhagalpur Plant
Forbesganj
Jamui
Katihar
Khagadia
Khagaria
Kishanganj
Lakhisarai
Madhepura
Munger
Purnia
Saharsa
Sultanganj
Supaul

    D- Muzzaffarpur
                                
Bagha
Begusarai
Betia
Betiah
Bettiah
Bhabhua
Darbhanga
Darbhanga
Jahanabad
Madhubani
Motihari
Muzaffarpur Plant
Muzaffarpur-Press
Muzzaffarpur
Muzzaffarpur Plant
Narkatiyaganj
Raxaul
Samastipur
Sheohar
Sitamadhi

 D --Patna
                                        
Arrah
Ara
Arwal
Aurangabad - Bihar
Bhabhua
Biharsharif
Bikramganj
Buxar
Chhapra
City Office
Dehri
Dumraon
Gaya
Gaya Plant
Gaya Project Office
Gopalganj
Hajipur
Jahanabad
Mohania
Nawada
Patna
Patna City Bureau
Patna Plant
Purnea
Rohtas
Sasaram
Shekhpura
Siwan


S-- Chandigarh
 Chandigarh
                    
Chandigarh
Chandigarh MYFM
Mohali
Sarhind Plant
Zirakpur
Panchkula
Mohali
Sirhind


s-   Chhattisgarh
     Bilaspur
                  
Ambikapur
Baikunthpur
Bilaspur
Bilaspur MYFM
Bilaspur Plant
Koriya

 Raigarh
                      
Bemetra
Dongargarh
Janjgir
Jashpur
Jharsuguda
Korba
Raigarh
Raigarh City
Raigarh Plant
Raigarh - DB Power
 Raipur
                          
Balod
Baloda Bazar
Bhilai
Dalli Rajra
Dantewada
Dhamtari
Durg
Jagdalpur
Kanker
Kawardha
Mahasamund
Raipur
Raipur MYFM
Rajnandgaon
Gujarat
 Ahmedabad
                                
Ahmd CG Road Office
Ahmedabad
Ahmedabad CG Road
Ahmedabad Digital
Ahmedabad Plant
Ahmedabad Press
Ahmedbad MYFM
Anand
Changodar
Deesa
Dwarka
Gandhinagar
Himatnagar
Himmatnagar
Khanpur
Mobri
Nadiad
Surendra Nagar
Surendranagar
Unjha
 Bhavnagar
                  
Bhavnagar
Bhavnagar HC Road
Mahuva
Sihor
Talaja
Vallabhipur
 Bhuj
                
Bhuj
Bhuj Plant
Bhujodi-Press
Gandhidham
 Junagadh
                
Amreli
Junagadh
Junagadh City
Porbandar
 Mehsana
                  
Bhandu
Mehsana
Modasa
Palanpur
Patan
Visnagar
 Rajkot
                 
Jamnagar
Metoda
Morbi
Rajkot
Rajkot FM
 Surat
                    
Bardoli
Chikli
Navsari
Silvasa
Surat
Surat MYFM
Surat Plant
Una-Gujarat
 Vadodara
                 
Anklesvar
Bharuch
Godhra
Vadodara
Vadodara Plant
 Vapi
                
Pardi
Valsad
Vapi
Vapi-Press
Haryana
 Ambala
                     
Ambala
Ambala Cantt.
Ambala Sadar
Kaithal
Karnal
Karnal FM
Kurukshetra
Yamuna Nagar
Yamunanagar
 Hisar
                     
Bhiwani
Charkhi Dadri
Dabawali
Dadri
Fatehabad
Hansi
Hisar
Hisar MYFM
Sirsa
 Panipat
                
Gohana
Panipat
Sonepat
Sonipat
 Rewari
                   
Faridabad
Gurgaon
Mahendergarh
Mahendragarh
Narnaul
Rewari
Rewari Plant
 Rohtak
                 
Bahadurgarh
Jhajjar
Jind
Rohtak
Rohtak Plant
Himachal Pradesh
 Shimla
                      
Dharamshala
Dharmshala
Hamirpur
Kullu
Mandi
Nahan
Nalgarh
Shimla
Solan
Hamirpur
Jammu & Kashmir
Jharkhand
 Dhanbad
                    
Bermo
Bokaro
Dhanbad
Dhanbad Plant
Giridih
Jamtara
Jharia
Katras
 Jamshedpur
                  
Chaibasa
Chakdharpur
Ghatshila
Ghatsila
Jamshedpur
Jamshedpur Plant
 Ranchi
                            
Chatra
Daltonganj
Garhwa
Gumla
Hazaribag
Khuti
Kodarma
Koderma
Lather
Lohardaga
Palamu
Ramgargh
Ramgarh Cant
Ranchi
Ranchi Plant
Simdega
Karnataka
Kerala
Madhya Pradesh
 Bhopal
                                            
Ashoknagar
Ashoknagar
Ashta
Bhopal
Bhopal Corp
Bhopal Digital
Bhopal MYFM
Bhopal Plant
Bhopal-Bairagarh Office
Bhopal-Bhel Office
Bhopal-E2
Bhopal-Kolar Office
Bhopal-Unit
Biaora
Corporate Classified
Corporate Editorial
Corporate HR
Corporate IT
Corporate VDI
DB Mall
Ganjbasoda
Guna
Jabalpur
Mandideep
Raisen
Rajgarh
Sanavad
Sehore
Sendhwa
Vidisha
Kolkata
Kolkatta
 Gwalior
                     
Bhind
Dabra
Datia
Gwalior
Gwalior MYFM
Gwalior Plant
Morena
Sheopur
Shivpuri
 Hoshangabad
                    
Betul
Harda
Hoshangabad
Hoshangabad Plant
Itarsi
Multai
Pipariya
Sarni
 Indore
                      
Alirajpur
Dewas
Dhar
Indore
Indore MYFM
Indore Plant
Indore-DNA
Jhabua
Mhow
Pithampur
 Khandwa
                     
Badwani
Barwani
Barwani
Burhanpur
Khandawa
Khandwa
Khandwa Plant
Khargon
Khargone
 Ratlam
                   
Garoth
Jaora
Manasa
Mandsaur
Neemuch
Ratlam
Ratlam Plant
 Sagar
                    
Bina
Chhatarpur
Chhattarpur
Damoh
Remote Support
Sagar
Sagar Plant
Tikamgarh
 Ujjain
                
Nagda
Shajapur
Ujjain
Ujjain Plant
Maharashtra
 Akola
                    
Akola
Akola Plant
Akola Press
Amravati
Buldhana
Nagpur
Nagpur FM
Yavatmal
 Aurangabad
                             
Bangalore
Ahmednagar
Aurangabad
Aurangabad FM
Aurangabad MYFM
Aurangabad Plant
Aurangabad-Unit Office
Beed
Hingoli
Jalna
Kolhapur
Nanded
Parbhani
Pune
Satara
Shridi
Waluj
 Jalgaon
                   
Bhusawal
Chalisgaon
Dhule
Jalgaon
Jalgaon FM
Jalgaon MYFM
Jalgaon Plant
 Mumbai
                
Mahim-Mumbai
Mum Mahim Corp
Mumbai
Mumbai - BKC
 Nasik
                      
Malegaon
Nashik
Nashik FM
Nashik Plant
Nasik
Nasik MYFM
Nasik Plant
Nasik Press
Sinner
Sinner
 Solapur
                   
Latur
Osmanabad
Solapur
Solapur City
Solapur FM
Solapur Plant
Solapur Press
Orissa
Punjab
 Amritsar
                   
Amritsar
Amritsar MYFM
Batala
Gurdaspur
Pathankot
Tarn Taran
Tarn-Taran
 Bathinda
                  
Abhor
Bathinda
Bathinda Press
Firozpur
Moga
Sangrur
 Jalandhar
                      
Jammu
Hamira
Hamira Plant
Hoshiarpur
Jalandhar
Jalandhar MYFM
Kapurthala
Nawanshahr
Phagwara
Ropar
 Ludhiana
                
Khanna
Ludhiana
Mandi Govindgarh
Patiala
Rajasthan
 Ajmer
              
Ajmer
Ajmer MYFM
 Alwar
                 
Alwar
Beawer
Behror
Bhiwadi
Kishangarh
 Banswara
               
Banswara
Dungarpur
Sagwara
 Barmer
                  
Balotra
Barmer
Jaisalmer
Jaisalmer
Pokhran
Pokran
 Bharatpur
              
Bharatpur
Dholpur
 Bhilwara
                
Bhilwara
Bhilwara
Bhilwara Plant
Chittorgarh
 Bikaner
               
Bikaner
Bikaner MYFM
Bikaner Plant
 Jaipur
                                
Abu Road
Bandikui
Chomu
Chomu
Corporate SAP
Dausa
Ganganpur City Plant
Gangapurcity Bureau
Hindaun City
Jaipur
Jaipur MYFM
Jaipur Press
Karauli
Karoli
Sawai Madhopur
Sawaimadhopur
Shahpura
Shivdaspura
Shivdaspura Plant
Tonk
 Jodhpur
                  
Bilara
Jodhpur
Jodhpur FM
Jodhpur Plant
Paota City office
Phalodi
 Kota
                     
Baran
Bundi
Jhalawar
Jhalawar
Kota
Kota FM
Kota Plant
Ramganj Mandi
Rawat Bhata
 Nagaur
                 
Kuchaman
Kuchaman City
Merta
Merta City
Nagaur
 Pali
              
Pali
Sirohi
 Sikar
                      
Aburoad
Bhinmal sachor
Chidawa
Churu
Jalor
Jhunjhunu
Neemkathana
Pali Plant
Sikar
Sumerpur
 Sriganganagar
                 
Hanumangarh
Hanumangarh
Sriganganagar
Sriganganagar Plant
Suratgarh
 Udaipur
                  
Dahod
Rajsamand
Udaipur
Udaipur FM
Udaipur MYFM
Udaipur Plant
Tamil Nadu
Uttar Pradesh
 Noida
                       
Dehradun
INS Delhi
Lucknow
New Delhi-Canaught Place
Noida
Noida - MPP
Noida FC10
Noida MP Printer
Noida MYFM
Tolstoy House – New Delhi
Varanasi









