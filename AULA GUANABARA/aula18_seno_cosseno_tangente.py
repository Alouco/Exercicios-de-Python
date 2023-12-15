#import math
#angulo = float(input('Digite o ândulo que voce deseja: '))
#seno = math.sin(math.radians(angulo))
#print('O Angulo de {} tem Seno de {:.2f}'.format(angulo,seno))
#cosseno = math.cos(math.radians(angulo))
#print('O Angulo de {} tem Cosseno de {:.2f}'.format(angulo,cosseno))
#tangente = math.tan(math.radians(angulo))
#print('O Angulo de {} tem Tangente de {:.2f}'.format(angulo,tangente))


from math import radians, sin,cos,tan
angulo = float(input('Digite o ândulo que voce deseja: '))
seno = sin(radians(angulo))
print('O Angulo de {} tem Seno de {:.2f}'.format(angulo,seno))
cosseno = cos(radians(angulo))
print('O Angulo de {} tem Cosseno de {:.2f}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('O Angulo de {} tem Tangente de {:.2f}'.format(angulo,tangente))


