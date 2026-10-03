import sys, time, subprocess, os

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
def line2(x):
    aprint("-" * x)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def inexistent_option_error():
    clear()
    
    line2(10)
    aprint("Opção inexistente. Retornando...")
    line2(10)
    time.sleep(1)
    
    clear()
    
def invalid_value_error():
    clear()
    
    line2(10)
    aprint("Valor inválido. Retornando...")
    line2(10)
    time.sleep(1)
    
    clear()
    
def exitt():
    clear()
    
    line2(10)
    aprint("Saindo...")
    line2(10)
    time.sleep(1)
    
    clear()
    
    exit()
    
line(10)
aprint("Libs Installer - v1.0.0")
line(10)
time.sleep(1)

try:
    versionn = sys.version

    aprint(versionn)
    
    versionn_ok = False
    
    while not versionn_ok:
        user_help = int(ainput("^ Acima você encontra a versão atual do seu Python. Informe quantos algarismos existem após o primeiro ponto, como por exemplo: 3.>14< = 2 e 3.>1< = 1:\n> "))
        
        if user_help == 2:
            versionn_ok = True
            versionn_path = versionn[0] + versionn[2] + versionn[3]
            
            clear()
            
        elif user_help == 1:
            versionn_ok = True
            versionn_path = versionn[0] + versionn[2]
            
            clear()
            
        else:
            inexistent_option_error()
except ValueError:
    invalid_value_error()
def menu(versionn_path):
    library = ainput("Nome de instalação da biblioteca por exemplo requests ou /sair:\n> ")
    
    if library.lower() == "/sair":
        exitt()
    else:
        try:
            user = os.path.expanduser("~")
            
            if os.path.exists(f"{user}\\AppData\\Local\\Programs\\Python\\Python{versionn_path}\\Lib\\site-packages\\{library}") or os.path.exists(f"{user}\\AppData\\Local\\Programs\\Python\\Python{versionn_path}-32\\Lib\\site-packages\\{library}"):
                
                clear()
                
                line2(10)
                aprint(f'A biblioteca "{library.upper()}" já está instalada.') 
                line2(10)
                time.sleep(1)
                
                clear()
                
                choose = ainput("Você gostaria de instalar outra biblioteca? Aperte Enter se não ou digite sim:\n> ")
                
                if choose.lower() == "sim":
                    
                    clear()
                    
                    menu(versionn_path)
                else:
                    
                    clear()
                    
                    exit()
            else:
                subprocess.run(["pip", "install", library], check=True)
                
                clear()
                
                line2(10)
                aprint(f'A biblioteca "{library.upper()}" foi instalada com sucesso!')
                line2(10)
                time.sleep(1)
                
                clear()
                
                choose = ainput("Você gostaria de instalar outra biblioteca? Aperte Enter se não ou digite sim:\n> ")
                
                if choose.lower() == "sim":
                    
                    clear()
                    
                    menu(versionn_path)
                else:
                    
                    clear()
                    
                    exit()
        except Exception as error:
            
            clear()
            
            line2(10)
            aprint(f'A biblioteca "{library.upper()}" não existe. Saída: {error}')
            line2(10)
            time.sleep(1)
            
            clear()
            
            choose = ainput("Você gostaria de instalar outra biblioteca? Aperte Enter se não ou digite sim:\n> ")
                
            if choose.lower() == "sim":
                    
                clear()
                    
                menu(versionn_path)
            else:
                    
                clear()
                    
                exit()
                
menu(versionn_path)