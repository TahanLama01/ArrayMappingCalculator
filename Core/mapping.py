class Mapping:
    min_hexadecimal = 10
    hexadecimal = 16

    def decimal_to_hexadecimal(self, input: int or str) -> int or str:
        if type(input) == type(1):
            output = {10:"A",11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
        else:
            output = {"A":10,"B":11, "C":12, "D":13, "E":14, "F":15}
        return output[input]

    def quotient_and_residual_quotient(self, qarq: int) -> int or list:
        if qarq >= self.min_hexadecimal:
            calculation_result = []
            while True:
                if qarq >= self.hexadecimal:
                    calculation_result.insert(0, str(qarq % self.hexadecimal))
                    qarq = int(qarq / self.hexadecimal)
                else:
                    calculation_result.insert(0, str(qarq))
                    break
            return calculation_result
        else:
            return qarq

    def decimal_numbers_check(self, dnc:int or list) -> int or list:
        if type(dnc) == type(["this_lists"]):
            calculation_result = []
            for i in dnc:
                try:
                    calculation_result.append(self.decimal_to_hexadecimal(int(i)))
                except(KeyError):
                    calculation_result.append(i)
            return calculation_result
        else:
            return dnc

    def return_hph(self, hph:list, str_borm:list or str) -> list:
        index = -1
        if len(hph) >= len(str_borm):
            while index != (-len(hph) + -1):
                try:
                    hph[index] = str(int(hph[index]) + int(str_borm[index]))
                    index -= 1
                except(IndexError):
                    break
        else:
            while index != (-len(str_borm) + -1):
                try:
                    str_borm = str(int(str_borm[index]) + int(hph[index]))
                    index -= 1
                except(IndexError):
                    hph = str_borm
                    break
        return hph
        
    def hexa_plus_hexa(self, BorM00orM000:str, hph:int or list) -> list:
        str_borm = str(int(BorM00orM000))

        list_borm = []
        for index in str_borm:
            list_borm.append(index)

        if type(hph) == type(["this_lists"]):
            hph = self.return_hph(hph, str_borm)

            int_hph = []
            for i in hph:
                int_hph.append(int(i))
            hph = int_hph

            index = -1
            while index != (-len(hph) + -1):
                if hph[index] >= self.hexadecimal:
                    hph[index + -1] += 1
                    hph[index] -= self.hexadecimal
                index += -1

            return self.decimal_numbers_check(hph)

        else:
            int_borm = int(BorM00orM000)
            int_borm += hph
            hph = int_borm
            return hph

    def condition1(self, results_step1, results_step2):
        if type(results_step1) != type(["ini_list"]):
            value = str(results_step1)[-1]
        else:
            results_step2_value = ""
            for value in results_step2:
                results_step2_value += value
            value = results_step2_value

        return value

    def condition2(self, results_step3):
        if type(results_step3) == type(["ini_list"]):
            steps = ""
            for step in results_step3:
                steps += str(step)
            results_step3 = steps
        return results_step3

    def zeroOutput(self,steps):
        zero = "0"
        i = 0
        j = 4

        if type(steps) != type("ini_string"):
            steps = str(steps)

        for i in range(len(steps) + 1):
            if len(steps) == i:
                step = f"{zero * j}{steps}"
                break
            j -= 1
        return step

    def looping(self, steps):
        step = ""
        for value in steps:
            step += str(value)
        return step
