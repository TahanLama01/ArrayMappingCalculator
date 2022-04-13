from Dimensional.one_dimensional import OneDimensional
from Dimensional.two_dimensional import TwoDimensional
from Dimensional.three_dimensional import ThreeDimensional
from time import sleep

class Menu:
    def __init__(self, menu_choice=0):
        dict_menu = {0:self.list_menu,1:self.calculator, 2:self.rumus, 3: self.quit}
        dict_menu[menu_choice]()

    def rumus(self):
        print("=" * 100)
        print("-" * 50)
        print("       Rumus Array Dimensi 1     ")
        print("@A[i]     = B + (i - 1) * L")
        print("-" * 50)
        print("       Rumus Array Dimensi 2       ")
        print("Rumus1 : Secara Baris Per Baris (Row Major Order / RMO)\n@M[i][j]  = M[0][0] + ((j - 1) * N + (i - 1)) * L")
        print("Rumus2 : Secara Kolom Per Kolom (Coloumn Major Order/CMO)\n@M[i][j]  = M[0][0] + ((j - 1) * K + (i - 1)) * L")
        print("-" * 50)
        print("       Rumus Array Dimensi 3       ")
        print("@M[m][n][p]   = M[0][0][0] + (((m-1) *(jum.elemen2 *jum.elemen3)) + ((n-1)*(jum.elemen3)) + ((p-1))* L")
        print("=" * 100)

    def list_menu(self):
        print("\n")
        print("=" * 32)
        print("\t*Full Kan Layar*")
        print(" 1. Kalkulator Array Dimensi 1-3")
        print(" 2. Rumus")
        print(" 3. Quit")
        print("=" * 32)

    def again(self):
        while True:
            try:
                question = int(input("\nIngin menghitung lagi?\n [0 = No / 1 = Yes]\n > "))
            except(ValueError):
                print("\n >! Tolong input Angka [0 / 1]")
                continue
            else:
                if question == 0 or question == 1:
                    break
                else:
                    print("\n >! Tolong input Angka [0 / 1]")
                    continue
        
        if question == 0:
            return 0
        else:
            return 1


    def calculator(self):
        list_array_dimensional = {1:OneDimensional, 2:TwoDimensional, 3:ThreeDimensional}
        while True:
            try:
                option = int(input("Kalkulator Array Dimensi berapa? [1/2/3]\n > "))
                start = list_array_dimensional[option]()
            except(KeyError):
                print("\n >! Mohon input Angka 1-3")
                continue
            except(ValueError):
                print("\n >! Tidak Menerima Huruf/Spasi")
                continue
            else:
                start.calculate()
                sleep(1)

            if self.again() == 1:
                continue
            else:
                break


    def quit(self):
        print("\n >! Quit !<\n")
        exit()
