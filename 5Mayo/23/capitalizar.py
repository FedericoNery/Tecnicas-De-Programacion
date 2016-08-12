#!/usr/bin/env python3

# muestra un string
# pasado como argumento
# en mayusculas
#
# Ej. capitalizar -m Uno
# UNO
#
import argparse

p = argparse.ArgumentParser()

p.add_argument("-m","--mensaje")
p.add_argument("-o","--opa",action="store_true")
p.add_argument("-s","--salu")
p.add_argument("-V","--version",action="store_true")

argumentos = p.parse_args()

if argumentos.mensaje:
    if argumentos.opa:
        print(argumentos.mensaje.upper())
    else:
        print(argumentos.mensaje.lower())

if argumentos.salu:
    print(argumentos.salu)

if argumentos.V:
    print("v. 0.8 - 2016")



