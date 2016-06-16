#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import sys
import urllib2

version = "1.0"

# Verificando o Diretório Principal do Programa
# =============================================
def main_directory():
	if os.path.exists("z0r"):
		os.chdir("z0r")
	else:
		print("Criando pasta 'z0r' ...")
		os.makedirs("z0r")
		os.chdir("z0r")

# Menu de Ajuda
# =============
def help():
	print("z0r Downloader: Baixe animações do z0r.de!")
	print("==========================================")
	print("Uso: z0r-downloader.py [argumento] [id] ...\n")

	print("Argumentos:")
	print("-----------")
	print(" -h || --help\t\tMostra este menu de ajuda")
	print(" -i || --input\t\tBaixa através de ID's inseridas na linha de comando")
	print(" -r || --range\t\tBaixa animações entre um valor mínimo e um valor máximo")
	print(" -a || --all\t\tBaixa TODAS as animações do z0r.de\n")

	print("Exemplo de uso para argumento '-r' ou '--range':")
	print("------------------------------------------------")
	print("Uso: z0r-downloader.py [-r/--range] [min] [max]\n")

# Método Para Download das Animações Entre Um Valor e Outro
# =========================================================
def download_animations_ranged(min, max, total):
	counter = 1
	for x in xrange(min, max + 1):
		url = "http://z0r.de/L/z0r-de_" + str(x) + ".swf"
		file_anim = open(str(x) + ".swf", "wb")
		try:
			response = urllib2.urlopen(url)
			print("Baixando animação (ID: %d) [%d/%d] ..." % (x, counter, total + 1))
			data = response.read()
			file_anim.write(data)
			file_anim.close()
			counter += 1
		except Exception:
			print("Erro! Não foi possível baixar animação (ID: %d)! Pulando [%d/%d] ..." % (x, counter, total + 1))
			file_anim.close()
			os.remove(str(x) + ".swf")
			counter += 1

# Método Para Download de TODAS as Animações
# ==========================================
def download_ALL_animations():
	print(" ")
	for x in xrange(0, sys.maxint):
		url = "http://z0r.de/L/z0r-de_" + str(x) + ".swf"
		file_anim = open(str(x) + ".swf", "wb")
		try:
			response = urllib2.urlopen(url)
			print("Baixando animação (ID: %d) ..." % (x))
			data = response.read()
			file_anim.write(data)
			file_anim.close()
		except urllib2.HTTPError, e:
			if e.code == 404:
				print("Concluído!!")
				file_anim.close()
				os.remove(str(x) + ".swf")
				sys.exit(0)
			else:
				print("Erro! Não foi possível baixar animação (ID: %d)! Pulando ..." % (x))
				file_anim.close()
				os.remove(str(x) + ".swf")

# Método Para Download das Animações, Modo Múltiplo e Modo Simples
# ================================================================
def download_animation(id, multiple, argc):
	# Modo Múltiplo
	# =============
	if multiple == True and id == None:
		for x in range(2, argc):
			id = str(sys.argv[x])
			url = "http://z0r.de/L/z0r-de_" + id + ".swf"
			print("Baixando animação (ID: %s) [%d/%d] ..." % (id, x - 1, argc - 2))
			file_anim = open(id + ".swf", "wb")
			try:
				response = urllib2.urlopen(url)
				data = response.read()
				file_anim.write(data)
				file_anim.close()
			except Exception:
				print("Erro! Não foi possível baixar animação (ID: %s)! Pulando ..." % (id))
				file_anim.close()
				os.remove(id + ".swf")
	# Modo Simples
	# ============
	else:
		url = "http://z0r.de/L/z0r-de_" + id + ".swf"
		print("\nBaixando animação (ID: %s) ..." % (id))
		file_anim = open(id + ".swf", "wb")
		try:
			response = urllib2.urlopen(url)
			data = response.read()
			file_anim.write(data)
			file_anim.close()
		except Exception:
			print("Erro! Não foi possível baixar animação (ID: %s)! Saindo ..." % (id))
			file_anim.close()
			os.remove(id + ".swf")

# Método Principal do Programa
# ============================
def main():
	argc = len(sys.argv)
	main_directory()

	print("=====================")
	print("z0r Downloader - v%s" % (version))
	print("=====================\n")

	if argc <= 1:
		id = raw_input("Insira APENAS a ID da animação: ")
		multiple = False
		download_animation(id, multiple, argc)
	elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
		help()
	elif sys.argv[1] == "-i" or sys.argv[1] == "--input":
		multiple = True
		download_animation(None, multiple, argc)
	elif sys.argv[1] == "-r" or sys.argv[1] == "--range":
		min = int(sys.argv[2])
		max = int(sys.argv[3])

		if min > sys.maxint or max > sys.maxint:
			print("Erro! Valor mínimo ou máximo muito grande! Use '-h' ou '--help' para ajuda.")
			print("Uso: z0r-downloader.py [-r/--range] [min] [max]")
			sys.exit(1)
		elif min < 0 or max < 0:
			print("Erro! Valor mínimo ou máximo possui número negativo! Use '-h' ou '--help' para ajuda.")
			print("Uso: z0r-downloader.py [-r/--range] [min] [max]")
			sys.exit(1)
		
		total = max - min

		if total < 0:
			print("Erro! Argumento inserido deve seguir o padrão 'min' e 'max'! Use '-h' ou '--help' para ajuda.")
			print("Uso: z0r-downloader.py [-r/--range] [min] [max]")
			sys.exit(1)
		else:
			download_animations_ranged(min, max, total)
	elif sys.argv[1] == "-a" or sys.argv[1] == "--all":
		print("Aviso! Este procedimento baixa TODAS as animações do z0r.de!! Isto pode levar um tempo ...")
		choose = raw_input("Deseja baixar TODAS as animações? [s/N]: ")
		choose = choose.upper()

		if choose == "S":
			download_ALL_animations()
		else:
			sys.exit(0)
	else:
		print("Erro! Argumento desconhecido! Use '-h' ou '--help' para ajuda.")
		print("Uso: z0r-downloader.py [argumento] [id] ...")

# Inicializando Programa
# ======================
if __name__ == "__main__":
	main()
