import os, subprocess, sys, time

user = os.path.expanduser("~")
info = sys.version
if info[3] != ".":
    py = info[0] + info[2] + info[3]
else:
    py = info[0] + info[2]
sf_bit = f"{user}\\AppData\\Local\\Programs\\Python\\Python{py}\\Lib\\site-packages"
tt_bit = f"{user}\\AppData\\Local\\Programs\\Python\\Python{py}-32\\Lib\\site-packages"

def aprint(text, delay=0.03):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def ainput(text, delay=0.01):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    return input()
def line(x):
    aprint("=" * x)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def invalid_input():
    clear()
    aprint("Entrada inválida.")
    time.sleep(1)
    clear()
def menu():
    clear()
    no_input = True
    while no_input:
        try:
            option = int(ainput("[1] Instalar biblioteca\n[2] Reparar biblioteca\n[3] Desinstalar biblioteca\n[4] Sair\n> "))
            if option == 1:
                clear()
                stop = False
                while not stop:
                    clear()
                    lib = ainput("Digite o nome da biblioteca, /v para voltar ou /s para sair:\n> ")
                    if lib.lower() == "/v" or lib.lower() == "/voltar":
                        clear()
                        stop = True
                        menu()
                    elif lib.lower() == "/s" or lib.lower() == "/sair":
                        exit()
                    else:
                        clear()
                        if not os.path.exists(f"{sf_bit}\\{lib}") and not os.path.exists(f"{tt_bit}\\{lib}"):
                            try:
                                subprocess.run([sys.executable, "-m", "pip", "install", f"{lib}"], check=True)
                                aprint(f'"{lib.upper()}" foi instalada com sucesso!')
                            except Exception as error:
                                input(f"Ocorreu um erro. Possíveis causas: biblioteca inexistente ou conexão instável.\nSaída: {error}")
                        else:
                            aprint(f'"{lib.upper()}" já está instalada.')
            elif option == 2:
                clear()
                stop = False
                while not stop:
                    clear()
                    lib = ainput("Digite o nome da biblioteca, /v para voltar ou /s para sair:\n> ")
                    if lib.lower() == "/v" or lib.lower() == "/voltar":
                        clear()
                        stop = True
                        menu()
                    elif lib.lower() == "/s" or lib.lower() == "/sair":
                        exit()
                    else:
                        clear()
                        if os.path.exists(f"{sf_bit}\\{lib}") or os.path.exists(f"{tt_bit}\\{lib}"):
                            try:
                                subprocess.run([sys.executable, "-m", "pip", "install", "--force-reinstall", f"{lib}"], check=True)
                                aprint(f'"{lib.upper()}" foi reparada com sucesso!')
                            except Exception as error:
                                input(f"Ocorreu um erro. Possível causa: conexão instável.\nSaída: {error}")
                        else:
                            aprint(f'"{lib.upper()}" não está instalada.')
            elif option == 3:
                clear()
                stop = False
                while not stop:
                    clear()
                    lib = ainput("Digite o nome da biblioteca, /v para voltar ou /s para sair:\n> ")
                    if lib.lower() == "/v" or lib.lower() == "/voltar":
                        clear()
                        stop = True
                        menu()
                    elif lib.lower() == "/s" or lib.lower() == "/sair":
                        exit()
                    else:
                        clear()
                        if os.path.exists(f"{sf_bit}\\{lib}") or os.path.exists(f"{tt_bit}\\{lib}"):
                            try:
                                subprocess.run([sys.executable, "-m", "pip", "uninstall", f"{lib}", "-y"], check=True)
                                aprint(f'"{lib.upper()}" foi desinstalada com sucesso!')
                            except Exception as error:
                                input(f"Ocorreu um erro desconhecido.\nSaída: {error}")
                        else:
                            aprint(f'"{lib.upper()}" não está instalada.')
            elif option == 4:
                exit()
            else:
                invalid_input()
        except ValueError:
            invalid_input()
              
aprint("uk3run3l apresenta:\n")              
line(10)
aprint("Libs Installer")
line(10)
time.sleep(1)

menu()