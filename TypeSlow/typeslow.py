#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
The MIT License (MIT)

Copyright (c) 2017 Wolfgang Almeida

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

# Imports gerais
# ==============
from __future__ import print_function
from time import sleep
import sys

# Abrindo arquivo e resgatando conteúdo
# =====================================
def openFile(file):
	f = open(file, "r")
	message = f.read()
	f.close()
	return message

# Imprimindo mensagem na tela com intervalo
# =========================================
def typeSlow(message, time):
	for i in message:
		print(i, end="")
		sys.stdout.flush()
		sleep(time)
	print()

# Método principal do script
# ==========================
def main():
	if len(sys.argv) > 2:
		typeSlow(openFile(str(sys.argv[1])), float(sys.argv[2]))
	else:
		print("Erro! Programa requer dois argumentos!")
		print("Uso: %s <ARQUIVO> <INTERVALO>" % (str(sys.argv[0])))

# Inicializando script
# ====================
if __name__ == "__main__":
	main()