
def any2dec(num, base: int, twosComplement=False):
    num = str(num)[::-1]
    total = 0
    if base == 2:
        for i in range(len(num)):
            if not twosComplement:
                total += int(num[i]) * (2**i)
            elif twosComplement:
                if i == len(num) - 1:
                    total -= int(num[i]) * (2**i)
                else:
                    total += int(num[i]) * (2**i)
    elif base == 8:
        for i in range(len(num)):
            total += int(num[i]) * (8**i)
    elif base == 16:
        hexDict = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
        for i in range(len(num)):
            total += hexDict[num[i]] * (16**i)
    return total

def dec2any(num: int, base: int):
    if base == 2:
        num = int(num)
        binNum = ""
        while num > 0:
            binNum += str(num % 2)
            num = num // 2
        return binNum[::-1]
    elif base == 8:
        num = int(num)
        octNum = ""
        while num > 0:
            octNum += str(num % 8)
            num = num // 8
        return octNum[::-1]
    elif base == 16:
        num = int(num)
        hexDict = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
        hexNum = ""
        while num > 0:
            if num % 16 > 9:
                hexNum += hexDict[num % 16]
            else:
                hexNum += str(num % 16)
            num = num // 16
        return hexNum[::-1] 

def twosbin2dec(num:str):
    dotCount = num.count(".")
    if dotCount > 1:
        raise "DecimalPointError"
    sumFrac = 0
    sumInt = 0


    if dotCount == 1:
        intPart, fracPart = num.split(".")

        sumInt = any2dec(intPart, 2, twosComplement=True)

        i = 1
        for frac in fracPart:
            sumFrac += int(frac)*(1/(2**i))
            i +=1

    elif dotCount == 0:
        sumInt = any2dec(num, 2, twosComplement=True)
        
    return sumFrac + sumInt

def dec2twosbin(num:float):
    if str(num)[0] == "-":
        negative = True
    else:
        negative = False
    
    intPart = int(num)

    if negative:
        binIntPart = dec2any(-intPart,2)
    else:
        binIntPart = dec2any(intPart,2)
    
    fracPart = abs(num - intPart)
    binFracPart = ""
    #if you input input a repeating decimal, this will not work
    if fracPart != 0:
        prod = 0
        while prod != 1:
            prod = fracPart * 2
            if prod >= 1:
                binFracPart += "1"
                fracPart = prod - 1
            else:
                binFracPart += "0"
                fracPart = prod
    if negative:
        pos_result = "0" + binIntPart + "." + binFracPart
        #flip the bits
        flipped_result = ""
        for i in pos_result:
            if i == "0":
                flipped_result += "1"
            elif i == "1":
                flipped_result += "0"
            elif i == ".":
                flipped_result += "."
        #add 1
        result = ""
        carry = 1
        for i in flipped_result[::-1]:
            if i == ".":
                result += "."
            elif i == "0":
                if carry == 1:
                    result += "1"
                    carry = 0
                else:
                    result += "0"
            elif i == "1":
                if carry == 1:
                    result += "0"
                else:
                    result += "1"
        return result[::-1]
    return "0" + binIntPart + "." + binFracPart

if __name__ == "__main__":
    print("This is a module. Please import it into another file.")
    exit(0)