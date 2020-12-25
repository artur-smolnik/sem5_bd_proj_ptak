from django import forms

class NameForm(forms.Form):

    
    CHOICES = ( 
    (0, 'nie'), 
    (1, 'tak'), 
    )

    typ_sprzetu = forms.CharField(label='Typ sprzętu', max_length=30)      
    rozmiar_sprzetu = forms.IntegerField(label='Rozmiar sprzętu')      
    kolor_sprzetu = forms.CharField(label='Kolor sprzętu',  max_length=20)      
    cena_sprzetu = forms.IntegerField(label='Cena sprzętu') 

    czy_uszkodzony = forms.TypedChoiceField(choices=CHOICES)      