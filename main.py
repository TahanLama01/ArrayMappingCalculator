from Core.mapping import Mapping
from Core.menu import Menu
from os import system

if __name__ == "__main__":
    system("cls")
    while True:
        Menu(0)
        try:
            menu_choice = int(input("\nMenu?\n > "))
            Menu(menu_choice)
        except(KeyError):
            print("\n >! Mohon input Angka 1-3")
            continue
        except(ValueError):
            print("\n >! Tidak Menerima Huruf/Spasi")
            continue

        


