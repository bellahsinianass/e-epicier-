from django import forms
from src.models import Produit  

class ProduitForm(forms.ModelForm):  
    class Meta:  
        model=Produit
        fields = "__all__" 