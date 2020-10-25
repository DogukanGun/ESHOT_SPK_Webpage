from django import forms
options=(
    ("1","Var"),
    ("2","Yok"),
    ("3","Belirsiz"),
)
class Plate(forms.Form):
    vehicle_id=forms.CharField( max_length=20, required=False)
    plate=forms.CharField(max_length=20,required=False) 
    def clean(self):
        vehicle_id=self.cleaned_data.get("vehicle_id")
        plate=self.cleaned_data.get("plate")
        result={
            "vehicle_id":vehicle_id,
            "plate":plate
        }
        return result
class Spk_Validator(forms.Form):
    spk_no=forms.CharField(max_length=20,required=False)
    spk_choose=forms.ChoiceField(choices=options)
    validator_no=forms.CharField(max_length=20,required=False)
    
