from django import forms
from django.forms import fields
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = ["nome_completo","cpf","data_nascimento","numero_casa","placa_veiculo"]
        error_messages = {
            "nome_completo":{
                "required": "O nome completo do visitante é obrigatório para o registro"
            },
            "cpf":{
                "required": "O CPF do visitante é obrigatório para o registro"
            },
            "data_nascimento":{
                "required": "A data de nascimento o do visitante é obrigatória para o registro",
                "invalid": "Preencha a data de nascimento em um formato válido (DD/MM/AAAA)"
            },
            "numero_casa":{
                "required": "Informe o número da casa a ser visitada"
            }
                    

        }
    
class AutorizaVisitanteForm(forms.ModelForm):
    morador_responsavel = forms.CharField(required = True)

    class Meta:
        model = Visitante
        fields = [
            "morador_responsavel"
        ] 
        error_messages = {
            "morador_responsavel": {
                "required": "Informe o nome do morador responsável por autorizar a entrada do visitante"
            }
        }
