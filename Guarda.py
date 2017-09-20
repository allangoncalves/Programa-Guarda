#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hmac, os, json, sys

class Guarda():

	def __init__(self):
		self.files = {}#Dicionario com os arquivos atuais
		self.early = {}#Dicionario com os arquivos antigos
		self.changed = {}#alterações realizadas

	#recupera os dados dos arquivos JSON
	def loadData(self):
		for directory, folderName, file in os.walk(".", topdown=True):
				for name in file:
					if name != ".hashs" and name != ".changes":
						fullName = os.path.join(directory, name).decode('unicode-escape')
						self.files[fullName] = None
		
		if os.path.isfile(".hashs"):
			with open(".hashs", "r") as input:
				file_str  = input.read()
				self.early = json.loads(file_str)

		if os.path.isfile(".changes"):
			with open(".changes", "r") as input:
				file_str  = input.read()
				self.changed = json.loads(file_str)
		
		self.calculateHash()

	#salva os dados em arquivos JSON (changes e hashs)
	def saveData(self):
			with open(".changes", "w") as inputFile:
				jsondata = json.dumps(self.changed, ensure_ascii=True, indent=4)
				inputFile.write(jsondata)

			with open(".hashs", "w") as inputFile:
				jsondata = json.dumps(self.files, ensure_ascii=True, indent=4)
				inputFile.write(jsondata)
	
	#realiza o calculo HMAC de todos os arquivos do diretório
	def calculateHash(self):
			for fullName in self.files:
				with open(fullName, "r") as input:
					file_str  = input.read()
					myhash = hmac.new(file_str).hexdigest().decode('unicode-escape')
					if fullName not in self.early:#verifica se o arquivo já existe no tabela
						self.changed[fullName] = 0
					elif not self.early[fullName] == myhash:#se previamente foi provado que ele existe, então é necessário verificar se ele foi alterado
						self.changed[fullName] = 1
					self.files[fullName] = myhash
					self.early[fullName] = myhash

	#verifica se houve alterações
	def verifyChanges(self):
		diff = set(self.files.items()) ^ set(self.early.items())##DIFERENÇA SIMETRICA ENTRE OS ARQUIVOS QUE TINHAM ANTES E DEPOIS

		for item in self.changed:
			if int(self.changed[item]) == 0:#0 representa que o arquivo foi adicionado
				print("@@@ {} foi adicionado. @@@".format(item))
			elif int(self.changed[item]) == 1:# 1 representa que o arquivo foi alterado
				print("@@@ {} foi alterado. @@@".format(item))
			self.changed[item] = 2 #2 representa arquivo analisado, util para as proximas verificações
		for d in diff:
			print("@@@ {} foi removido. @@@".format(d))


if __name__ == '__main__':

	if len(sys.argv) >= 3:
		g = Guarda()
		if sys.argv[1]=="-i" or sys.argv[1] == "-t":
			os.chdir(sys.argv[2])
			g.loadData()
			if sys.argv[1] == "-t":
				g.verifyChanges()
			g.saveData()
		elif sys.argv[1]=="-x":#opçao -x
			os.chdir(sys.argv[2])
			if os.path.isfile(".hashs") and os.path.isfile(".changes"):#verifica se os arquivos realmente existem
				os.remove(".hashs")
				os.remove(".changes")
			else:
				print("Você não criou ou já removeu o arquivo de Hashs")
		else:
			print("OPÇÃO INVALIDA!")
	else:
		print("Argumentos insuficientes.")