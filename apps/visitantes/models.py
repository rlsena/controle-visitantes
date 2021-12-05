from django.db import models

# Create your models here.

class Visitante(models.Model):

    STATUS_VISITANTE = [
        ("AGUARDANDO","Aguardando Autorização"),
        ("EM_VISITA", "Visita em andamento"),
        ("FINALIZADO","Visita finalizada")

    ]

    status = models.CharField(
        verbose_name="status",
        max_length=10,
        choices=STATUS_VISITANTE,
        default="AGUARDANDO"
    )

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


    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida
        
        return "Horario de saída não registrado"
    
    
    def get_horario_autorizacao(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao
        
        return "Visitante aguardando autorização"
    
    def get_morador_responsavel(self):
        if self.morador_responsavel:
            return self.morador_responsavel
        
        return "Visitante aguardando autorização"

    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
        
        return "Veículo não registrado"

    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)

            cpf1 = cpf[0:3]
            cpf2 = cpf[3:6]
            cpf3 = cpf[6:9]
            cpf4 = cpf[9:]

            cpf_formatado = f"{cpf1}.{cpf2}.{cpf3}-{cpf4}"

            return cpf_formatado

    class Meta:
        verbose_name="Visitante",
        verbose_name_plural="Visitantes",
        db_table="visitante"

    def __str__(self):
        return self.nome_completo

