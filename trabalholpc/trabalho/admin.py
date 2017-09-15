from django.contrib import admin
from trabalho.models import *
# Register your models here.
admin.site.register(Autor)
admin.site.register(Evento)
admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(EventoCientifico)
admin.site.register(ArtigoCientifico)