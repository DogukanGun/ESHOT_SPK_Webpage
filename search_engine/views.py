from django.shortcuts import render,redirect
from authentication.models import User
from django.contrib.auth.decorators import user_passes_test
import pandas as pd
from .forms import Plate,Spk_Validator
from .models import PlateRequest 
# Create your views here. 
def search_engine(request):   
    return render(request,"search_engine.html")
def id_request(request):
    return render(request,"id_request.html")
def id_request(request):
    vehicle=None
    vehicle_=pd.read_csv("vehicles.csv")
    vehicles_list=vehicle_.values.tolist() 
    if request.method=="POST":
        spk_validator_form=Spk_Validator(request.POST)
        if spk_validator_form.is_valid():
            spk_exists=spk_validator_form.cleaned_data['spk_choose']
            if spk_exists=="Var":
                spk_number=spk_validator_form.cleaned_data['spk_no']
                validator_no=spk_validator_form.cleaned_data['validator_no']
                for i in vehicles_list:
                    if i[1]==validator_no and i[3]==validator_no:
                        vehicle=i
            else:
                validator_no=spk_validator_form.cleaned_data['validator_no']
                for i in vehicles_list:
                    if i[1]==validator_no:
                        vehicle=i
            if vehicle is not None:
                context={
                    "PLAKA":"35"+vehicle[0],
                    "VALIDATORNO":vehicle[1],
                    "SKPVARMI":"SKP VAR" if vehicle[2]==1 else "SPK YOK",
                    "SPKNO":vehicle[3]
                    } 
            return render(request,"result.html",context)
    else:
        spk_validator_form=Spk_Validator()
    context={
        "form":spk_validator_form
    }
    return render(request,"id_request.html",context                                                                  )
def plate_request(request): 
    plates=pd.read_csv("vehicles.csv")
    plates_list=plates.values.tolist() 
    if request.method=='POST':
        plate_form=Plate(request.POST) 
        if plate_form.is_valid(): 
            plate=plate_form.cleaned_data['plate']
            vehicle_id=plate_form.cleaned_data['vehicle_id']
            if plate is None:
                plate="None"
            plate_model=PlateRequest(plate=plate,vehicle_id=vehicle_id,user_id=request.user.id)
            plate_model.save()   
            return render(request,"result.html")
    else: 
        plate_form=Plate()
    context={
        "form":plate_form,
        "plates":plates_list
    } 
    return render(request,'plate_request.html',context)
def result(request,id):   
    vehicle=None   
    context=None
    vehicle_=pd.read_csv("vehicles.csv")
    vehicles_list=vehicle_.values.tolist() 
    for i in vehicles_list: 
        if int(id)==int(i[0]): 
            car_plate=i[1]
    validator=pd.read_csv("validators.csv")
    validators_list=validator.values.tolist()  
    for i in validators_list:
        print("{} {} ".format(i[0],car_plate[2:len(car_plate)]))
        if str(i[0])==str(car_plate[2:len(car_plate)]):
            vehicle=i
    
    if vehicle is not None:
        context={
            "PLAKA":"35"+vehicle[0],
            "VALIDATORNO":vehicle[1],
            "SKPVARMI":"SKP VAR" if vehicle[2]==1 else "SPK YOK",
            "SPKNO":vehicle[3]
        } 
    return render(request,'result.html',context)