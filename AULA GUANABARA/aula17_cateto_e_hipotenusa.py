
#forma 1
#co = float(input('O comprimento do cateto oposto: '))
#ca = float(input('O comprimento do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hi))

#forma 2

#import math
#co = float(input('O comprimento do cateto oposto: '))
#ca = float(input('O comprimento do cateto adjacente: '))
#hi = math.hypot(co,ca)
#print('A hipotenusa vai medir {:.2f}'.format(hi))

#forma 3

from math import hypot
co = float(input('O comprimento do cateto oposto: '))
ca = float(input('O comprimento do cateto adjacente: '))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))