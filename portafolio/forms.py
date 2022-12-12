from django import forms
from django.contrib.auth.forms import UserCreationForm



class RegistroUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
class PortafolioForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=250)
    foto = forms.URLField(label='Ingresa url de la imagen')
    url = forms.URLField()
    tags = forms.CharField(max_length=100)


    def clean(self):
 
        # data from the form is fetched using super function
        super(PortafolioForm, self).clean()
         
        # extract the username and text field from the data
        titulo = self.cleaned_data.get('titulo')
        descripcion = self.cleaned_data.get('descripcion')
        foto = self.cleaned_data.get('foto')
        url = self.cleaned_data.get('url')
        tags = self.cleaned_data.get('tags')
 
        # conditions to be met for the username length
        if titulo is None:
            self._errors['titulo'] = self.error_class([
                'El título es reqerido'])
        if titulo and len(titulo) < 3:
            self._errors['titulo'] = self.error_class([
                'Ingresar al menos tres caracters'])

        if descripcion is None:
            self._errors['descripcion'] = self.error_class([
                'La descripcion es reqerida'])  
        if descripcion and len(descripcion) < 4:
            self._errors['descripcion'] = self.error_class([
                'Ingresar al menos 4 caracters'])

        if foto is None:
            self._errors['foto'] = self.error_class([
                'La foto es reqerida'])
        if foto and len(foto) < 10:
            self._errors['foto'] = self.error_class([
                'Ingresar al menos 10 caracters'])
        
        if url is None:
            self._errors['url'] = self.error_class([
                'La url es reqerida'])
        if url and len(url) < 10:
            self._errors['url'] = self.error_class([
                'Ingresar al menos 10 caracters'])

        if tags is None:
            self._errors['tags'] = self.error_class([
                'Los tags son reqeridos'])
        if tags and len(tags) < 4:
            self._errors['tags'] = self.error_class([
                'Ingresar al menos 4 caracters'])
    

       
 
        # return any errors if found
        return self.cleaned_data