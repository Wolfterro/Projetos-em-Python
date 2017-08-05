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

from __future__ import print_function
from bs4 import BeautifulSoup
from urllib2 import urlparse

import os
import sys
import urllib2

#----------------------------------------
# Criado por: Wolfterro
# Versão: 1.2 - Python 2.x
# Data: 18/09/2016
#----------------------------------------

# Changing default encoding
# =========================
reload(sys)
sys.setdefaultencoding('utf-8')

# Versão do programa
# ==================
version = "1.2"

#=======================================================
# Métodos de verificação de pasta principal e dos vídeos
#=======================================================

# Verificação da pasta principal
# ==============================
def checkFolder():
	if os.path.exists("Heavy-R"):
		os.chdir("Heavy-R")
	else:
		print("[Heavy-R Downloader] Pasta 'Heavy-R' não existe! Criando ...\n")
		os.makedirs("Heavy-R")
		os.chdir("Heavy-R")

# Verificação da pasta do vídeo a ser baixado
# ===========================================
def checkVideoFolder(videoTitle, videoID):
	folderName = "%s-[%s]" % (videoTitle.replace("/", "-").replace("\\", "-"), videoID)
	
	if os.path.exists(folderName):
		print("[Heavy-R Downloader] Aviso! Pasta '%s' já existe!" % (folderName))
		overwrite = raw_input("[Heavy-R Downloader] Você deseja sobrescrever o vídeo? [s/N]: ")

		if overwrite.upper() == "S":
			os.chdir(folderName)
		else:
			print("[Heavy-R Downloader] Saindo ...")
			sys.exit(0)
	else:
		os.makedirs(folderName)
		os.chdir(folderName)

#=====================================================
# Métodos de download e resgate de valores do programa
#=====================================================

# Imprimindo barra de processo no terminal
# ========================================
def printProgressBar(now, total, width=50):
	progress = float(now) / float(total)
	bar = ('#' * int(width * progress)).ljust(width)
	percent = progress * 100.0
	to_print = 'Downloading: [%s] %.2f%%\r' % (bar, percent)
	print(to_print, end='')
	if round(percent) >= 100:
		print('%s\r' % (' ' * len(to_print)), end='')

# Iniciando o processo de download
# ================================
def downloadProcess(videoFileURL, videoTitle, videoID):
	print("[Heavy-R Downloader] Iniciando download de '%s' - ID: %s ..." % (videoTitle, videoID))
	
	response = urllib2.urlopen(videoFileURL)
	total = response.headers['content-length']
	downloaded = 0
	newVideoFileName = "%s.mp4" % (videoTitle.replace("/", "-").replace("\\", "-"))
	with open(newVideoFileName, 'wb') as file:
		while True:
			data = response.read(4096)
			downloaded += len(data)
			if not data:
				break
			file.write(data)
			printProgressBar(downloaded, total)

	print("\n[Heavy-R Downloader] Processo de download concluído!")

# Resgatando a URL do arquivo de vídeo
# ====================================
def getVideoFileURL(videoURL):
	response = urllib2.urlopen(videoURL)
	soup = BeautifulSoup(response, 'html.parser')
	return soup.find('source', {'type' : 'video/mp4'}).get('src')

# Resgatando o título do vídeo
# ============================
def getVideoTitle(videoURL):
	try:
		response = urllib2.urlopen(videoURL)
	except Exception:
		print("[Heavy-R Downloader] Erro! Não foi possível acessar URL %s!" % (videoURL))
		print("[Heavy-R Downloader] Verifique a URL do vídeo e tente novamente.")
		sys.exit(1)
	
	soup = BeautifulSoup(response, 'html.parser')
	return soup.title.string

# Resgatando a ID do vídeo através da URL
# =======================================
def getVideoID(videoURL):
	urlSplit = urlparse.urlsplit(videoURL)
	toParse = str(urlSplit[2])

	try:
		videoID = toParse.split("/")[2]
	except Exception:
		print("[Heavy-R Downloader] Erro! Não foi possível extrair ID do vídeo!")
		print("[Heavy-R Downloader] Verifique se a URL do vídeo não está incompleta e tente novamente.")
		sys.exit(1)

	return videoID

# Verificando o domínio da URL inserida
# =====================================
def checkURLDomain(videoURL):
	urlSplit = urlparse.urlsplit(videoURL)
	if str(urlSplit[1]) != "heavy-r.com" and str(urlSplit[1]) != "www.heavy-r.com":
		print("[Heavy-R Downloader] Erro! URL inválida! Saindo...")
		sys.exit(1)

# Resgatando a URL do vídeo através do usuário,
# caso não tenha inserido pela linha de comando
# =============================================
def getVideoURL():
	videoURL = raw_input("[Heavy-R Downloader] Insira a URL do vídeo: ")

	if videoURL == "":
		print("[Heavy-R Downloader] Erro! Nenhuma URL inserida! Saindo...")
		sys.exit(1)

	print("")
	return videoURL

# Método principal para o início do processo de download
# ======================================================
def beginProgramProcesses(videoURL):
	if videoURL == None:
		videoURL = getVideoURL()

	checkURLDomain(videoURL)
	
	videoID = getVideoID(videoURL)
	videoTitle = getVideoTitle(videoURL)
	checkVideoFolder(videoTitle, videoID)

	videoFileURL = getVideoFileURL(videoURL)
	downloadProcess(videoFileURL, videoTitle, videoID)

# Menu de Ajuda
# =============
def help():
	print("Uso: ./Heavy-R Downloader.py [Argumento] [URL / ID]")
	print("---------------------------------------------------\n")

	print("Argumentos:")
	print("-----------")
	print("-h || --help\t\tMostra esta tela de ajuda")
	print("-u || --url\t\tUtiliza a URL inserida como argumento no programa")
	print("-i || --id\t\tUtiliza a ID inserida como argumento no programa\n")

# Método Principal
# ================
def main():
	argc = len(sys.argv)

	checkFolder()

	print("===============================")
	print("Heavy-R Downloader - Versão %s" % (version))
	print("===============================\n")

	if argc > 2:
		if str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help":
			help()
		
		elif str(sys.argv[1]) == "-u" or str(sys.argv[1]) == "--url":
			beginProgramProcesses(str(sys.argv[2]))

		elif str(sys.argv[1]) == "-i" or str(sys.argv[1]) == "--id":
			completeURL = "http://www.heavy-r.com/video/%s/Generic_Video_Title/" % (str(sys.argv[2]))
			beginProgramProcesses(completeURL)

		else:
			print("[Heavy-R Downloader] Erro! Argumento desconhecido! Use -h ou --help para ajuda.\n")
			sys.exit(1)
	
	elif argc == 2:
		if str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help":
			help()
		
		elif str(sys.argv[1]) == "-u" or str(sys.argv[1]) == "--url":
			print("[Heavy-R Downloader] Erro! Falta URL! Use -h ou --help para ajuda.\n")
			sys.exit(1)

		elif str(sys.argv[1]) == "-i" or str(sys.argv[1]) == "--id":
			print("[Heavy-R Downloader] Erro! Falta ID! Use -h ou --help para ajuda.\n")
			sys.exit(1)

		else:
			print("[Heavy-R Downloader] Erro! Argumento desconhecido! Use -h ou --help para ajuda.\n")
			sys.exit(1)
	
	else:
		beginProgramProcesses(None)

if __name__ == "__main__":
	main()