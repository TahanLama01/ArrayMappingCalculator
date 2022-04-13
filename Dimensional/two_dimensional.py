from Core.mapping import Mapping

class TwoDimensional(Mapping):
    def __init__(self):
        print("\nM[i][j] = Posisi Array yg dicari")
        self.m00    = input("M[0][0] = Posisi alamat awal index array (Contoh : 0011)\nMasukan M[0][0] = ") #"0011"
        self.i      = int(input("\ni = Index Baris (Contoh : 3)\nMasukan i = ")) #3
        self.j      = int(input("\nj = Index kolom (Contoh : 2)\nMasukan j = ")) #2
        self.K      = int(input("\nL = Ukuran memory type data (Contoh: (2=Integer, 4=Float))\nMasukan L = ")) #4
        self.N      = int(input("\nK = Banyaknya elemen per kolom (Contoh : 3)\nMasukan K = ")) #3
        self.L      = int(input("\nN = Banyaknya elemen per baris (Contoh : 2)\nMasukan N = ")) #4

    def dimensional2_calculation(self, i, j, X, L):
        return ((self.j - 1) * X + (self.i - 1)) * self.L

    def calculate(self):
        KN = [self.K, self.N]
        for KandN in KN:
            step1 = self.dimensional2_calculation(self.i, self.j, KandN, self.L)
            step2 = self.quotient_and_residual_quotient(step1)
            step3 = self.decimal_numbers_check(step2)
            step4 = self.condition1(step2, step3)
            step5 = self.hexa_plus_hexa(self.m00, step2)
            step6 = self.condition2(step5)
            step7 = self.zeroOutput(step6)
            self.output(KandN, step1, step4, step7)

    def output(self, KandN, step1, step4, step7):
            if KandN == self.K:
                print("\nRumus1 : Secara Baris Per Baris (Row Major Order / RMO)\n@M[i][j]  = M[0][0] + ((j - 1) * N + (i - 1)) * L")
                print(f"A[{self.i}][{self.j}]..... Secara Baris Per Baris (Row Major Order / RMO)")
            else:
                print("\nRumus2 : Secara Kolom Per Kolom (Coloumn Major Order/CMO)\n@M[i][j]  = M[0][0] + ((j - 1) * K + (i - 1)) * L")
                print(f"A[{self.i}][{self.j}]..... Secara Kolom Per Kolom (Coloumn Major Order/CMO)")
                
            print(f"          = {self.m00}(H) + (({self.j} - 1) * {KandN} + ({self.i} - 1)) * {self.L}")
            print(f"          = {self.m00}(H) + {step1}(D)")
            print(f"          = {self.m00}(H) + {step4}(H)")
            print(f"          = {step7}(H)\n")