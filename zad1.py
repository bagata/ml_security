"" "Masz listę od 0 do 18. Twoim zadaniem jest zostawić tylko liczby, które dzielą się na 4 bez reszty " \
"czyli 0, 4, 8, 12 i 16). Nie używaj czystego Pythona, tylko postaraj się wykorzystać nowe biblioteki. """

import numpy as np

list0_18= np.array([range(0,19)])
list_modulo4=list0_18[list0_18% 4==0]
print(list_modulo4)
