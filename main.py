import os
import sys
import numberSystems
import time

sys.path.append(os.path.realpath("."))
import inquirer

def validate(answers, current):
    if current == "":
        raise inquirer.errors.ValidationError("", reason="Input cannot be empty")
    if answers["input_base"] == "Decimal":
        if (current.count(".") == 1) and ((answers["output_base"] != "Decimal") and (answers["output_base"] != "Binary")):
            raise inquirer.errors.ValidationError("", reason="Fractional decimal numbers can only be converted to binary")
        
        if current.count(".") > 1:
            raise inquirer.errors.ValidationError("", reason="Decimal numbers can only contain one decimal point")
        
        for i in range(len(current)):
            if (current[i] not in "0123456789.") and (((i != 0) and (current[i] == "-")) or ((i != 0) and (current[i] == "+"))):
                raise inquirer.errors.ValidationError("", reason="Decimal numbers can only contain digits 0-9")
            
        if (float(current) < 0) and ((answers["output_base"] != "Decimal") and (answers["output_base"] != "Binary")):
            raise inquirer.errors.ValidationError("", reason="Negative decimal numbers can only be converted to binary")
            
    if answers["input_base"] == "Binary":
        if current.count(".") > 1:
            raise inquirer.errors.ValidationError("", reason="Binary numbers can only contain one decimal point")
        
        if current[0] == ".":
            raise inquirer.errors.ValidationError("", reason="Binary numbers cannot start with a decimal point (Consider adding a 0 before the decimal point)")
        
        if (current[0] == "1") and (answers["output_base"] != "Binary") and (answers["output_base"] != "Decimal"):
            raise inquirer.errors.ValidationError("", reason="Negative binary numbers can only be converted to decimal")
        
        for i in current:
            if i not in "01.":
                raise inquirer.errors.ValidationError("", reason="Binary numbers can only contain digits 0-1")
            
    if answers["input_base"] == "Hexadecimal":
        for i in current:
            if i not in "0123456789ABCDEF":
                raise inquirer.errors.ValidationError("", reason="Hexadecimal numbers can only contain digits 0-9 and letters A-F")
            
    if answers["input_base"] == "Octal":
        for i in current:
            if i not in "01234567":
                raise inquirer.errors.ValidationError("", reason="Octal numbers can only contain digits 0-7")
            
    return True

# Create a dictionary to map choices to numeric values
base_mapping = {
    "Decimal": 10,
    "Binary": 2,
    "Hexadecimal": 16,
    "Octal": 8
}

questions = [
    inquirer.List(
        "input_base",
        message="What is your input?",
        choices=["Decimal", "Binary", "Hexadecimal", "Octal"]
    ),
    inquirer.List(
        "output_base",
        message="What base do you want the output in?",
        choices=["Decimal", "Binary", "Hexadecimal", "Octal"]
    ),
    inquirer.Text(
        "input",
        message="Enter your number",
        validate=validate
    )
]

answers = inquirer.prompt(questions)

# Override the "input_base" key with its numeric value
answers["input_base"] = base_mapping[answers["input_base"]]
answers["output_base"] = base_mapping[answers["output_base"]]

input_base = answers["input_base"]
output_base = answers["output_base"]
number = answers["input"]

if input_base == output_base:
    print("You don't need to convert!")
    exit(0)
    

if input_base == 10:
    number = float(number)
    if output_base == 2:
        print(numberSystems.dec2twosbin(number))
    elif output_base == 8:
        print(numberSystems.dec2any(number, 8))
    elif output_base == 16:
        print(numberSystems.dec2any(number, 16))
    time.sleep(5)
elif input_base == 2:
    if output_base == 10:
        print(numberSystems.twosbin2dec(number))
    elif output_base == 8:
        print(numberSystems.dec2any(numberSystems.any2dec(number, 2), 8))
    elif output_base == 16:
        print(numberSystems.dec2any(numberSystems.any2dec(number, 2), 16))
    time.sleep(5)
elif input_base == 8:
    if output_base == 10:
        print(numberSystems.any2dec(number, 8))
    elif output_base == 2:
        print(numberSystems.dec2any(numberSystems.any2dec(number, 8), 2))
    elif output_base == 16:
        print(numberSystems.dec2any(numberSystems.any2dec(number, 8), 16))
    time.sleep(5)
elif input_base == 16:
    if output_base == 10:
        print(numberSystems.any2dec(number, 16))
    elif output_base == 2:
        print(numberSystems.dec2any(numberSystems.any2dec(number, 16), 2))
    elif output_base == 8:
        print(numberSystems.dec2any(numberSystems.any2dec(number, 16), 8))
    time.sleep(5)
