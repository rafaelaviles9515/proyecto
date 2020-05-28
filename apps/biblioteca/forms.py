from django import forms

from apps.biblioteca.models import Libro

class LibroForm(forms.ModelForm):

	class Meta:
		model= Libro

		fields=[
			'codigo',
			'nombre',
			
					]
		labels = {
			'codigo': 'Escriba el codigo',
			'nombre': 'Escriba el nombre del libro',
			
		}
		widgets= {
			'codigo': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			
		}