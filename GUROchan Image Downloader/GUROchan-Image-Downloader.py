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

import os
import sys
import urllib2

#------------------------------------
# Criado por: Wolfterro
# Versão: 1.0 - Python 2.x
# Data: 06/06/2016
#------------------------------------

version = "1.0"

# Verificação da Pasta Principal do Programa
# ==========================================
def main_folder():
	if os.path.exists("GUROchan"):
		os.chdir("GUROchan")
	else:
		print("[GUROchan Image Downloader] Criando Pasta 'GUROchan' ...")
		os.makedirs("GUROchan")
		os.chdir("GUROchan")

# Verificação de Pasta da Board e do Tópico Escolhido
# ===================================================
def board_thread_folder(board_name, folder_name):
	if os.path.exists(board_name):
		os.chdir(board_name)
	else:
		print("[GUROchan Image Downloader] Criando Pasta '" + board_name + "' ...")
		os.makedirs(board_name)
		os.chdir(board_name)

	if os.path.exists(folder_name):
		os.chdir(folder_name)
	else:
		print("[GUROchan Image Downloader] Criando Pasta '" + folder_name + "' ...")
		os.makedirs(folder_name)
		os.chdir(folder_name)

# Resgate da Página do Tópico Escolhido e Retorno de Suas Informações
# ===================================================================
def get_page_info(url):
	global response

	print("\n[GUROchan Image Downloader] Recuperando Informações da URL ...")

	response = urllib2.urlopen(url).read().decode('utf-8')
	soup = BeautifulSoup(response, 'html.parser')

	get_title = soup.title.string.replace("GUROchan :: ", "")
	get_title_folder = get_title.replace(" ", "_").replace("/", "-")

	get_board_value = soup.find('input', {'name' : 'board'}, {'type' : 'hidden'}).get('value')
	if get_board_value == "g":
		get_board = "Guro"
	elif get_board_value == "f":
		get_board = "Freakshow"
	elif get_board_value == "s":
		get_board = "Scat"
	elif get_board_value == "fur":
		get_board = "Furry"
	elif get_board_value == "art":
		get_board = "Artwork"
	elif get_board_value == "3dcg":
		get_board = "3DCG"
	elif get_board_value == "p2p":
		get_board = "File-Sharing"
	elif get_board_value == "req":
		get_board = "Requests"
	elif get_board_value == "rp":
		get_board = "Role-playing"
	elif get_board_value == "dis":
		get_board = "Discussion"
	elif get_board_value == "lit":
		get_board = "Literature"
	else:
		get_board = "Other"

	return [get_title_folder, get_title, get_board]

# Download de Imagens do Tópico Escolhido
# =======================================
def download_images(img, current, total):
	download_link = "https://www.gurochan.ch" + img
	response_download = urllib2.urlopen(download_link)

	filename = os.path.basename(download_link)

	if os.path.isfile(filename) == True:
		print("[Download] Imagem '" + filename + "' já existe! Pulando [%d/%d] ..." % (current, total))
	else:
		print ("[Download] Baixando Imagem '" + filename + "' [%d/%d] ..." % (current, total))

		with open(filename, "wb") as file:
			while True:
				data = response_download.read()
				if not data:
					break
				file.write(data)

# Recuperação de Links das Imagens e Solicitação de Download pelo Método 'download_images'
# ========================================================================================
def get_page_links(url, thread_name):
	soup = BeautifulSoup(response, 'html.parser')
	links = soup.findAll('a', href=True, attrs={'class', 'file'})

	announcer = "[GUROchan Image Downloader] Baixando Imagens de '" + thread_name + "' ..."
	print(announcer)
	print("=" * len(announcer))
	
	current = 0
	total = 0
	for total_links in links:
		total += 1

	for link in links:
		current += 1
		download_images(link['href'], current, total)

# Método Principal do Programa
# ============================
def main():
	main_folder()

	print("======================================")
	print("GUROchan Image Downloader - Versão %s" % (version))
	print("======================================\n")
	
	url = raw_input("Insira a URL do Tópico: ")
	
	get_folder_name, get_thread_name, get_board_name = get_page_info(url)
	board_thread_folder(get_board_name, get_folder_name)
	get_page_links(url, get_thread_name)

# Inicializando Programa
# ======================
main()
