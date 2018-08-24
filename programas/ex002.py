

hora = input('sho me da time \n')
if int(hora) > 24:
    hora = int(hora) % 24
else:
    alarm = input('how many time from now U PEASANT')
    alarm = int(alarm) % 24
    print('the alarm is set to {}'.format(alarm))


