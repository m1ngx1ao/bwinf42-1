import os
from input_leser import Parameter
from loeser import loese
from output_schreiber import schreibe

dateien = os.scandir('junior1/input')
for datei in dateien:
    schreibe(datei.name, loese(Parameter(datei.name)))