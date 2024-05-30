import datetime 

dt = datetime.datetime.now()

print(dt)

dia = datetime.datetime.now().day

print(dia)

from pathlib import *

directorioAct = Path.cwd()

print(directorioAct)

import math as sex
print(sex.acos(0.5))

from io import *  
archivo = open(r"arhivo.txt","w")
archivo.write("nombre:papito edad: 20")
archivo.close()

archivo = open
