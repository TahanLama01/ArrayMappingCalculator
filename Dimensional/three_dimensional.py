from Core.mapping import Mapping

class ThreeDimensional(Mapping):
    def __init__(self):
        print("\nA[m][n][p] = Posisi Array yg dicari")
        self.m000           = input("M[0][0][0] = Posisi alamat awal index array (Contoh : 0021)\nMasukan M[0][0][0] = ")#"0021"
        self.jumElement1    = int(input("\njum.elemen1 = Banyak/batas index Baris/Tinggi (Contoh : 2 ([2][x][x]))\nMasukan jum.elemen1 = ")) #3
        self.jumElement2    = int(input("\njum.elemen2 = Banyak/batas index Kolom/Lebar (Contoh : 3 ([x][3][x]))\nMasukan jum.elemen2 = ")) #4
        self.jumElement3    = int(input("\njum.elemen2 = Banyak/batas index Blok/Panjang (Contoh : 4 ([x][x][4]))\nMasukan jum.elemen3 = ")) #2
        self.m              = int(input("\nm = Lokasi index 1 (Contoh : 2 ([2][x][x]))\nMasukan m = ")) #3
        self.n              = int(input("\nn = Lokasi index 2 (Contoh : 3 ([x][3][x]))\nMasukan n = ")) #4
        self.p              = int(input("\np = Lokasi index 3 (Contoh : 2 ([x][x][2]))\nMasukan p = ")) #3
        self.L              = int(input("\nL: Ukuran / Besar memory suatu type data (Contoh: (2=Integer, 4=Float))\nMasukan L = ")) #2

    def dimensional1_calculation1(self, m,elemen2,elemen3):
        return (m-1) * (elemen2 * elemen3)

    def dimensional1_calculation2(self, n,elemen3):
        return ((n-1) * (elemen3))

    def dimensional1_calculation3(self, p, L):
        return p-1

    def dimensional1_calculation4(self, a, b, c, L):
        return (a + b + c) * L

    def calculate(self):
        step1 = self.dimensional1_calculation1(self.m, self.jumElement2, self.jumElement3)
        step2 = self.dimensional1_calculation2(self.n,self.jumElement3)
        step3 = self.dimensional1_calculation3(self.p, self.L)
        step4 = self.dimensional1_calculation4(step1, step2, step3, self.L)
        step5 = self.quotient_and_residual_quotient(step4)
        step6 = self.decimal_numbers_check(step5)
        step7 = self.condition1(step5, step6)
        step8 = self.hexa_plus_hexa(self.m000, step5)
        step9 = self.looping(step8)
        step10 = self.zeroOutput(step9)
        self.output(step1, step2, step3, step4, step7,step10)

    def output(self, step1, step2, step3, step4, step7,step10):
        print("\nRumus:\n@M[m][n][p]   = M[0][0][0] + (((m-1) *(jum.elemen2 *jum.elemen3)) + ((n-1)*(jum.elemen3)) + ((p-1))* L\n")
        print(f"A[{self.m}][{self.n}][{self.p}].....")
        print(f"              = {self.m000}(H) + ((({self.m} - 1) * ({self.jumElement2} * {self.jumElement3})) + (({self.n} - 1) * {self.jumElement3}) + ({self.p} - 1)) * {self.L}")
        print(f"              = {self.m000}(H) + ({step1} + {step2} + {step3}) * {self.L}")
        print(f"              = {self.m000}(H) + {step4}(D)")
        print(f"              = {self.m000}(H) + {step7}(H)")
        print(f"              = {step10}(H)\n")