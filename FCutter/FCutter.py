#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Termux
#!/data/data/com.termux/files/usr/bin/python2
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
import os
import sys
import subprocess

# Alterando a codificação do programa
# ===================================
reload(sys)
sys.setdefaultencoding('utf-8')

# Versão do programa
# ==================
VERSION = "1.0"

# Classe principal do programa
# ============================
class FCutter(object):
	# Iniciando objetos da classe
	# ===========================
	def __init__(self, sourceFile, outputFile):
		self.sourceFile = sourceFile
		self.outputFile = outputFile

	# Iniciando métodos da classe
	# ===========================
	def start(self):
		if self.checkSourceFile():
			self.inputStartTime()
			self.inputEndTime()

			if self.warningCut():
				self.cut()
		else:
			print(u"[FCutter] Erro! Arquivo fonte não existe ou inacessível!")
			printUsage()

	# Verificando arquivo fonte
	# =========================
	def checkSourceFile(self):
		return os.path.exists(self.sourceFile)

	# Inserindo tempo inicial de corte
	# ================================
	def inputStartTime(self):
		self.startTime = raw_input(u"[FCutter] Insira o tempo inicial: ")

		if self.startTime == "":
			self.startTime = "0"

		try:
			if ":" in self.startTime:
				h,m,s = self.startTime.split(":")
				self.startTime = int(h) * 3600 + int(m) * 60 + int(s)
			else:
				self.startTime = int(self.startTime)
		except Exception as e:
			self.startTime = 0

		if self.startTime < 0:
			self.startTime = 0

	# Inserindo tempo final de corte
	# ==============================
	def inputEndTime(self):
		self.endTime = raw_input(u"[FCutter] Insira o tempo final: ")

		if self.endTime == "":
			self.endTime = "0"

		try:
			if ":" in self.endTime:
				h,m,s = self.endTime.split(":")
				self.endTime = int(h) * 3600 + int(m) * 60 + int(s)
				self.duration = self.endTime - self.startTime
			else:
				self.endTime = int(self.endTime)
				self.duration = self.endTime - self.startTime
		except Exception as e:
			self.endTime = 0
			self.duration = 0

		if self.duration < 0:
			self.duration = 0

	# Informando ao usuário o tempo de corte
	# ======================================
	def warningCut(self):
		m,s = divmod(self.duration, 60)
		h,m = divmod(m, 60)

		print(u"[FCutter] Tempo de duração do corte: %02d:%02d:%02d (%d segundos)" % (h,
			m, s, self.duration))

		if self.duration <= 0:
			print(u"\n[FCutter] Erro! Tempo de duração igual a zero! Saindo...")
			return False
		else:
			choice = raw_input(u"\n[FCutter] Deseja fazer o corte? [s/N]: ")
			if choice.upper() == "S":
				return True
			else:
				return False

	# Resgatando o comando de corte do FFmpeg
	# =======================================
	def getCommand(self):
		videosX264 = [".mp4", ".avi", ".flv"]
		videosVP8 = [".webm"]
		file, ext = os.path.splitext(self.outputFile)

		if self.outputFile.endswith(".mp3"):
			return "ffmpeg -ss %d -t %d -i \"%s\" -acodec copy \"%s\""

		if ext in videosX264:
			return "ffmpeg -ss %d -t %d -i \"%s\" -c:v libx264 -crf 0 \"%s\""
		elif ext in videosVP8:
			return "ffmpeg -ss %d -t %d -i \"%s\" -c:v libvpx -crf 4 \"%s\""
		else:
			return "ffmpeg -ss %d -t %d -i \"%s\" \"%s\""

	# Executando comando de corte do FFmpeg
	# =====================================
	def cut(self):
		orig = u"\n[FCutter] Recortando arquivo: \"%s\"" % (self.sourceFile)
		dest = u"[FCutter] Destino: \"%s\"" % (self.outputFile)

		print(orig)
		print(dest)
		if len(orig) > len(dest):
			print("-" * len(orig) + "\n")
		else:
			print("-" * len(dest) + "\n")

		command = self.getCommand() % (self.startTime, self.duration,
			self.sourceFile, self.outputFile)
		subprocess.call(command, shell=True)

	# DEBUG: Imprime o tempo inicial, final e duração em segundos
	# ===========================================================
	def printTimes(self):
		print(u"Tempo inicial: %d segundos" % (self.startTime))
		print(u"Tempo final: %d segundos" % (self.endTime))
		print(u"Duração: %d segundos" % (self.duration))

# Imprimindo informações de uso do programa
# =========================================
def printUsage():
	print(u"[FCutter] Uso: %s <Arquivo Fonte> <Arquivo Destino>" % (str(sys.argv[0])))

# Imprimindo tela de ajuda do programa
# ====================================
def printHelp():
	print(u"====================")
	print(u"FCutter - Versão %s" % (VERSION))
	print(u"====================")
	printUsage()

	print(u"\nDescrição:")
	print(u"----------")
	print(u"Este é um simples programa que possui a função de realizar cortes em")
	print(u"arquivos de multimídia utilizando o FFmpeg para realizar este procedimento.\n")

	print(u"Ao invocar o programa com os arquivos fonte e de destino, o programa irá pedir")
	print(u"ao usuário para inserir o tempo inicial de corte e o tempo final de corte.\n")

	print(u"O usuário poderá inserir o tempo em segundos ou em formato HH:mm:ss!\n")

	print(u"Caso o tempo de duração do corte seja igual a zero, o corte será descartado!")

	print(u"\nOpções:")
	print(u"-------\n")

	print(u"  -h || --help\t\tMostra esta tela de ajuda.")

	print(u"\n------------------------------------------------------\n")

	print(u" *** Este programa é licenciado sob a Licença MIT ***")

# Método inicial do programa
# ==========================
def main():
	argc = len(sys.argv)

	if argc >= 3:
		f = FCutter(str(sys.argv[1]), str(sys.argv[2]))
		f.start()
	elif argc == 2:
		if str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help":
			printHelp()
		else:
			print(u"[FCutter] Erro! Falta argumentos!")
			printUsage()
	else:
		print(u"[FCutter] Erro! Falta argumentos!")
		printUsage()

# Iniciando programa
# ==================
if __name__ == "__main__":
	main()
