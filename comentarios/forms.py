from django.forms import ModelForm
from .models import  Comentario
import requests

class FormComentario(ModelForm):

    def clean(self):
        raw_data = self.data
        
        recaptcha_response = raw_data.get('g-recaptcha-response')

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': 'PUT YOUR KEY HERE',
                'response': recaptcha_response
            }
        )
        recaptcha_result = recaptcha_request.json()

        if not recaptcha_result.get('sucess'):
            self.add_error(
                'comentario',
                'Prove que você não é um robô.'
            ) 

        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome_comentario')
        email = cleaned_data.get('email_comentario')
        comentario = cleaned_data.get('comentario')

        if len(nome) < 4:
            self.add_error(
                'nome_comentario',
                'O nome precisa ter mais que 4 caracteres.'
            ) 
  

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')