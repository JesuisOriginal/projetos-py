days = [0, 1 , 2, 3, 4, 5, 6]
semana = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]
hj = input('informe o dia atual')
hj = int(hj)
print('hj eh dia {}'.format(semana[hj]))
estadia = input('quantos tempos vc vai ficar aq?')
estadia = int(estadia)
saida = (hj + estadia) % 7
print('saida dia {}'.format(semana[saida]))