print("=== INSTALADOR DE BIBLIOTECAS PARA PYTHON ===")
import sys
versionn = sys.version
print(versionn)
try:
    versionn_ok = False
    while not versionn_ok:
        user_help = int(input("Acima você encontra a versão do seu Python, informe quantos algarismos existem após o primeiro ponto (EX: 3.>14< = 2 e 3.>1< = 1): "))
        if user_help == 2:
            versionn_path = versionn[0] + versionn[2] + versionn [3]
            versionn_ok = True
        elif user_help == 1:
            versionn_path = versionn[0] + versionn[2]
            versionn_ok = True
except ValueError:
    print("2, 1 ou 0, qualquer outro valor não é aceito")
    input()
start = input("Aperte 'ENTER' para iniciar ou digite /sair: ")
if start.lower() == "/sair":
	import time
	print("Saindo /")
	time.sleep(2)
	exit()
else:
	def enter(versionn_path):
		library = input("Nome de instalação da biblioteca (EX: REQUESTS) ou /sair: ")
		if library.lower() == "/sair":
			import time
			print("Saindo /")
			time.sleep(2)
			exit()
		else:
			try:
				import subprocess
				import os
				user = os.path.expanduser("~")
				if os.path.exists(f"{user}\\AppData\Local\\Programs\\Python\\Python{versionn_path}\\Lib\\site-packages\\{library}") or os.path.exists(f"{user}\\AppData\Local\\Programs\\Python\\Python{versionn_path}-32\\Lib\\site-packages\\{library}"):
					print(f"A biblioteca '{library.upper()}' já está instalada!")
					choose = input("Você gostaria de instalar outra biblioteca? Aperte 'ENTER' se não ou digite /sim: ")
					if choose.lower() == "/sim":
						enter(versionn_path)
					else:
						exit()
				else:
					subprocess.run(["pip", "install", library], check=True)
					print(f"A biblioteca '{library.upper()}' foi instalada com sucesso!")
					choose = input("Você gostaria de instalar outra biblioteca? Aperte 'ENTER' se não ou digite /sim: ")
					if choose.lower() == "/sim":
						enter(versionn_path)
					else:
						exit()
			except Exception:
				print(f"A biblioteca '{library.upper()}' não existe")
				choose = input("Você gostaria de instalar outra biblioteca? Aperte 'ENTER' se não ou digite /sim ")
				if choose.lower() == "/sim":
					enter(versionn_path)
				else:
					exit()
	enter(versionn_path)