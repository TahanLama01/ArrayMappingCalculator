from Core.mapping import Mapping

class OneDimensional(Mapping):
    def __init__(self):     
        print("\n@A[i]: Posisi Array yg dicari")   
        self.B =     input("B: Posisi awal index di memory komputer (Contoh: 0011)\nMasukan B = ") #"0011" 
        self.i = int(input("\ni: Subkrip atau indeks array yg dicari (Contoh: 3)\nMasukan i = ")) #3
        self.L = int(input("\nL: Ukuran / Besar memory suatu type data (Contoh: (2=Integer, 4=Float))\nMasukan L = ")) #2

    def dimensional1_calculation(self, i, L):
        return (i - 1) * L

    def calculate(self):
        step1 = self.dimensional1_calculation(self.i, self.L)
        step2 = self.quotient_and_residual_quotient(step1)
        step3 = self.decimal_numbers_check(step2)
        step4 = self.condition1(step2, step3)
        step5 = self.hexa_plus_hexa(self.B, step2)
        step6 = self.condition2(step5)
        step7 = self.zeroOutput(step6)
        self.output(step1, step4, step7)

    def output(self, step1, step4, step7):
        print("\nRumus:\n@A[i]     = B + (i - 1) * L\n")
        print(f"A[{self.i}].....")
        print(f"          = {self.B}(H) + ({self.i} - 1) * {self.L}")
        print(f"          = {self.B}(H) + {step1}(D)")
        print(f"          = {self.B}(H) + {step4}(H)")
        print(f"          = {step7}(H)\n")