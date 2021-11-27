from django.db import models

# Create your models here.

class Visitante(models.Model):

    nome_completo=models.CharField(
        verbose_name="Nome Completo", 
        max_length=194)

    cpf=models.CharField(
        verbose_name="CPF",
        max_length=11)

    data_nascimento=models.DateField(
        verbose_name="Data de Nascimento",
        auto_now=False, 
        auto_now_add=False)

    numero_casa=models.PositiveBigIntegerField(
        verbose_name="Número da casa a ser visitada")

    placa_veiculo=models.CharField(
        verbose_name="Placa do veículo",
        max_length=7,
        blank=True,
        null=True)

    horario_chegada=models.DateTimeField(
        verbose_name="Horário de chegara na portaria",
        auto_now=True)

    horario_saida=models.DateTimeField(
        verbose_name="Horário de saída do condominio",
        auto_now=False,
        blank=True,
        null=True)

    horario_autorizacao=models.DateTimeField(
        verbose_name="Horário da autorização de entrada",
        auto_now=False,
        blank=True,
        null=True)

    morador_responsavel=models.CharField(
        verbose_name="Nome do morador responsável pela autorização de entrada do visitante",
        max_length=194,
        blank=True)

    registrado_por=models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Porteiro responsável pelo registro",
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name="Visitante",
        verbose_name_plural="Visitantes",
        db_table="visitante"

    def __str__(self):
        return self.nome_completo

