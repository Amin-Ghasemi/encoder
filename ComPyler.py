import platform
import marshal, base64
from os import system, getcwd
from colorama import Fore, Style

def clear():
    os_name = platform.system()
    if os_name == "Windows":
        system("cls")
    elif os_name == "Linux":
        system("clear")
    else:
        pass

def menu():
    print(f"""{Fore.LIGHTBLUE_EX}
        ____          _    __
       / __ \_____   | |  / /__  ____  ____  ____ ___
      / / / / ___/   | | / / _ \/ __ \/ __ \/ __ `__ \\
     / /_/ / /       | |/ /  __/ / / / /_/ / / / / / /
    /_____/_/        |___/\___/_/ /_/\____/_/ /_/ /_/

    t.me/Dr_Venom

\n   {Fore.WHITE}1 {Fore.GREEN}-{Fore.LIGHTWHITE_EX} ComPyler{Style.RESET_ALL} 
    """)
    print(Style.RESET_ALL)

    while True:
        command = input(f"   {Fore.LIGHTGREEN_EX}*{Style.RESET_ALL} Select a Option  {Fore.GREEN}➜{Style.RESET_ALL}  ")
        if command == "1":
            compiler()
        elif command.lower() == "e" or command.lower() == "exit":
            exit()
        else:
            clear()
            menu()

def compiler():
    print(f"\n        ^ location {Fore.GREEN}➜ {Fore.LIGHTRED_EX} {getcwd()}{Style.RESET_ALL}\n")

    file_name = input(f"             {Fore.LIGHTGREEN_EX}*{Style.RESET_ALL} Enter file Name {Fore.GREEN}➜ {Style.RESET_ALL} ")
    darsad = 1
    file_name_replace =file_name.replace(".py", "")
    compiled_file_name = f"{file_name_replace}"

    for i in range(25):
        try:
            file_py = open(f"{file_name}", 'r', encoding="utf8")
            file_py_read = file_py.read().encode('UTF-8')
            encoded = base64.b85encode(file_py_read)
            code = f"""global codes\ncodes = compile(base64.b85decode({encoded}), "Dr_Venom", "exec")"""
            exec(code)
            z = base64.b85encode(marshal.dumps(codes))
            file_name = file_name.replace(".py", "")
            compiled = open(f"{compiled_file_name}_compiled.py", "w")

            compiled.write(f"import marshal, base64\nexec(marshal.loads(base64.b85decode({z})))")

            file_py.close()
            compiled.close()

            file_name = f"{compiled_file_name}_compiled.py"

            clear()
            darsad = round(darsad, 1)
            print(f"\n\t{darsad}%")
            darsad += 4.1
            status = True
        except:
            status = False
    clear()

    if status:
        darsad = 100
        print(f"\n\t{Fore.LIGHTGREEN_EX}{darsad}% Compeleted {compiled_file_name}_compiled.py{Style.RESET_ALL}")
    else:
        print(f"\n\t{Fore.LIGHTRED_EX}Error in Compeleted.{Style.RESET_ALL}")
        
    input("\n\n\tEnter To continue...")

    clear()
    menu()

global file_name

clear()
menu()
