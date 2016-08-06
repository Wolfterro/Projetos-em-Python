#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import sys
import shutil

#----------------------------------------
# Criado por: Wolfterro
# Versão: 1.0 - Python 2.x
# Data: 01/06/2016
#----------------------------------------

version = "1.0"

# Menu de Ajuda
# =============
def help():
	print ("Uso: ./Heavy-R Downloader.py [Argumento] [ID] ...")
	print ("-------------------------------------------------\n")

	print ("Argumentos:")
	print ("-----------")
	print ("-h || --help\t\tMostra esta tela de ajuda")
	print ("-u || --url\t\tUtiliza URL's inseridas como argumentos para o script\n")

	print (" * Caso o modo 'URL' não consiga baixar o vídeo, utilize o modo simples, executando o programa sem uso de argumentos.\n")

# Verificação de Pasta
# ====================
def check_folder():
	if os.path.exists("Heavy-R"):
		os.chdir("Heavy-R")
	else:
		print ("[Heavy-R Downloader] Pasta 'Heavy-R' não existe! Criando ...\n")
		os.makedirs("Heavy-R")
		os.chdir("Heavy-R")

# Download de Vídeos em Modo Simples e Modo URL
# =============================================
def get_video_simple_mode(get_video_url):
	if get_video_url == None:
		get_video_url = raw_input("Insira a URL do vídeo: ").replace(" ", "")

	separator = "/"

	get_video_id = get_video_url.replace("http://www.heavy-r.com/video/", "").split(separator, 1)[0]
	get_video_name = get_video_url.replace("http://www.heavy-r.com/video/", "").split(separator, 1)[1].replace("/", "")

	print ("[Heavy-R Downloader] Baixando página do vídeo selecionado (" + get_video_name.replace("_", " ") + ") ...")

	generated_folder = get_video_id + "-" + get_video_name

	if os.path.exists(generated_folder):
		print ("[Heavy-R Downloader] Erro! Vídeo já existe na pasta! Abortando ...")
		print ("\n==================================================================\n")
	
	else:
		os.makedirs(generated_folder)
		os.chdir(generated_folder)

		os.system("wget -O index.html " + "\"" + get_video_url + "\"" + " -q --show-progress")

		print ("[Heavy-R Downloader] Analisando página em busca de link ...")

		if os.path.getsize("index.html") == 0:
			print ("[Heavy-R Downloader] Erro! Página corrompida ou não existente! Removendo pasta ...")
			print ("\n==================================================================================\n")
			os.chdir("..")
			shutil.rmtree(generated_folder)
			return

		os.system("grep -m 1 'file: ' index.html >> link.txt")

		print ("[Heavy-R Downloader] Baixando vídeo através do link encontrado ...")

		file_link = open("link.txt")
		linha_link = file_link.readlines()
		get_download_link = str(linha_link[0]).replace("file: ", "").replace("'", "").replace(",", "").replace(" ", "").replace("\n", "")
		file_link.close()

		os.system("wget -O " + get_video_name + ".mp4 " + "\"" + get_download_link + "\"" + " -q --show-progress")

		print ("[Heavy-R Downloader] Verificando se o vídeo foi baixado corretamente ...", end="")

		if os.path.getsize(get_video_name + ".mp4") == 0:
			print (" !! FALHA !!")
			falha = True
		else:
			print (" OK!")
			falha = False

		print ("[Heavy-R Downloader] Eliminando arquivos temporários e com falhas ...")
		print ("\n=====================================================================\n")

		os.remove("link.txt")
		os.remove("index.html")
		os.chdir("..")

		if falha == True:
			shutil.rmtree(generated_folder)

# Método Principal
# ================
def main():
	argc = len(sys.argv)

	print ("===============================")
	print ("Heavy-R Downloader - Versão %s" % (version))
	print ("===============================\n")

	if argc <= 1:
		check_folder()
		get_video_simple_mode(None)

	elif str(sys.argv[1]) == "-u" or str(sys.argv[1]) == "--url":
		check_folder()
		if argc <= 2:
			print ("[Heavy-R Downloader] Erro! Falta URL's! Use -h ou --help para ajuda.\n")
		else:
			for x in range(2, argc):
				get_video_simple_mode(str(sys.argv[x]))

	elif str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help":
		help()

	else:
		check_folder()
		get_video_simple_mode(None)

# Inicializando Programa
# ======================
main()