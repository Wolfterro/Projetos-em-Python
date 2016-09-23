#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
The MIT License (MIT)

Copyright (c) 2016 Wolfgang Almeida <wolfgang.almeida@yahoo.com>

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

#========================================
# Criado por: Wolfterro
# Versão: 1.0 - Python 2.x
# Data: 21/09/2016
#========================================

from __future__ import print_function

import os
import sys
import json
import urllib2

# Chave API do Google Maps
# Necessária caso queira um controle maior de verificações de endereços ou um
# limite maior caso possua um plano pago, mas não é obrigatória.
#
# Deixe em branco caso não tenha, mas lembre-se que o limite de verificação
# é de 2.500 vezes por dia!
#
# Para obter uma chave, utilize o endereço abaixo (requer conta do Google):
# https://developers.google.com/maps/documentation/geocoding/get-api-key?hl=pt-br
# ===============================================================================
GOOGLEAPI_KEY = ""

# Versão do programa
# ==================
VERSION = "1.0"

# Alterando codificação padrão
# ============================
reload(sys)
sys.setdefaultencoding('utf-8')

# Imprimindo as informações na tela
# =================================
def printIPInformation(ipInformation, ipLocation):
	print("\n[IPyInfo] Imprimindo informações sobre o endereço IP ...")
	print("========================================================")
	if 'ip' in ipInformation:
		print("Endereço IP: %s" % (ipInformation['ip']))
	if 'hostname' in ipInformation:
		print("Hostname: %s" % (ipInformation['hostname']))
	if 'city' in ipInformation:
		print("Cidade: %s" % (ipInformation['city']))
	if 'region' in ipInformation:
		print("Região: %s" % (ipInformation['region']))
	if 'country' in ipInformation:
		print("País: %s" % (ipInformation['country']))
	print("Endereço (estimativa): %s" % (ipLocation))
	if 'postal' in ipInformation:
		print("Cod. Postal: %s" % (ipInformation['postal']))
	if 'loc' in ipInformation:
		print("Latitude/Longitude: %s" % (ipInformation['loc']))
	if 'org' in ipInformation:
		print("Organização: %s" % (ipInformation['org']))
	print("========================================================\n")

# Resgatando localização do endereço IP
# =====================================
def getIPLocation(latitLongit):
	urlApiGoogleMaps = "https://maps.googleapis.com/maps/api/geocode/json?latlng=%s&key=%s" % (latitLongit, GOOGLEAPI_KEY)
	
	try:
		responseMaps = urllib2.urlopen(urlApiGoogleMaps)
		jsonFileMaps = json.loads(responseMaps.read())
	except Exception:
		return "Endereço não disponível!"

	if jsonFileMaps['status'] == "OVER_QUERY_LIMIT":
		return "Limite de verificação excedido!"
	
	elif jsonFileMaps['status'] == "OK":
		for elements in jsonFileMaps['results']:
			if 'formatted_address' in elements:
				return str(elements['formatted_address'])
			else:
				return "Endereço não disponível!"

# Resgatando latitude e longitude através da resposta
# ===================================================
def getIPLatitLongit(ipInformation):
	try:
		return "%s" % (ipInformation['loc'])
	except Exception:
		return "0,0"

# Resgatando informações sobre o endereço IP
# ==========================================
def getIPInformation(ipAddress):
	if ipAddress == None:
		IPINFO_API_URL = "http://ipinfo.io/json"
	else:
		IPINFO_API_URL = "http://ipinfo.io/%s/json" % (ipAddress)
	
	try:
		responseIP = urllib2.urlopen(IPINFO_API_URL)
		ipInformation = json.loads(responseIP.read())
		return ipInformation
	except Exception:
		print("[IPyInfo] Erro! Não foi possível obter informações! Saindo ...")
		sys.exit(1)

# Menu de ajuda
# =============
def helpMenu():
	print("====================")
	print("IPyInfo - Versão %s" % (VERSION))
	print("====================\n")

	print("Uso: ./IPyInfo.py [OPÇÕES] [IP]")
	print("-------------------------------\n")

	print("[Opções]")
	print("--------")
	print(" -h || --help\t\tMostra este menu de ajuda.")
	print(" -i || --ip\t\tMostra as informações do endereço IP selecionado.\n")

	print("Nota:")
	print("-----\n")
	print("Este programa faz uso da API do Google Maps para decodificar a localização estimada dos IP's.\n")
	
	print("Porém, há um limite diário de 2.500 verificações, caso exceda este limite, você poderá ficar")
	print("sem a localização estimada dos endereços, mas poderá ainda possuir a latitude e longitude dos")
	print("mesmos, podendo então verificar manualmente suas localizações.\n")

	print("----------------------------------------------------------------------------------------------\n")

	print(" *** Este programa é licenciado sob a licença MIT ***\n")
	print("Copyright (c) 2016 Wolfgang Almeida <wolfgang.almeida@yahoo.com>")
	print("Repositório no GitHub: https://github.com/Wolfterro/Projetos-em-Python/IPyInfo\n")

# Método principal
# ================
def main():
	argc = len(sys.argv)

	if argc > 2:
		if str(sys.argv[1]) == "-i" or str(sys.argv[1]) == "--ip":
			ipInformation = getIPInformation(str(sys.argv[2]))
			latitLongit = getIPLatitLongit(ipInformation)
			ipLocation = getIPLocation(latitLongit)
			printIPInformation(ipInformation, ipLocation)

		elif str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help":
			helpMenu()
	
	elif argc == 2:
		if str(sys.argv[1]) == "-i" or str(sys.argv[1]) == "--ip":
			print("[IPyInfo] Erro! Nenhum endereço IP inserido! Saindo ...")
			sys.exit(1)

		elif str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help":
			helpMenu()
	
	else:
		ipInformation = getIPInformation(None)
		latitLongit = getIPLatitLongit(ipInformation)
		ipLocation = getIPLocation(latitLongit)
		printIPInformation(ipInformation, ipLocation)

# Inicializando programa
# ======================
if __name__ == "__main__":
	main()