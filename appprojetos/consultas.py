from appprojetos.models import *
'''''
for e in ProjetoPesquisa.objects.all():
    print(e.titulo,end=' membros do projeto \n')
    for i in e.membro.all():
        print(i.nome)

for at in Atividade.objects.filter(dataInicio__month=5,
                                   dataInicio__year=2015):
    print(at)

for me in MembroParticipante.objects.filter(nome__startswith='A'):
    print(me)
'''''

ativ= ProjetoPesquisa.objects.all()
for e in ativ:
    soma = 0
    print(e.titulo)
    for i in e.atividade_set.all():
        soma+=i.custo
    print('total ',soma)




#print(ProjetoPesquisa.objects.all())

#{1:s}