from django import forms

from backOffice.models import Clients

class ClientForm(forms.ModelForm):
   class Meta:
     model = Clients
     #fields = '__all__'
     exclude = ('Code','Sommeil','Secteur','Commercial','Activite','Categorie','Adresse','Champs_Sup_1', 'Champs_Sup_2', 'Champs_Sup_3', 'Champs_Sup_4', 'Champs_Sup_5')