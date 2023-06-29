n1 = float(input('Digite a nota da prova: '))
n2 = float(input('Digite a nota das atividades: '))
media = (n1 * 0.6) + (n2 * 0.4)
print('media: ',media)
if media<=4.9:
    print('Exame')
elif media<10:
    print('Passou, Parabéns!!')
