from fractions import Fraction
from math import floor
# import re


def input_number(input_num):
    input_num = input_num.split("_")

    if len(input_num) == 1:  # and bool(re.search("^(\d+){1}/(\d+)$", input_num[0]))
        return Fraction(input_num[0])
    else:
        dec = input_num[1].split("/")
        numerator = int(input_num[0]) * int(dec[1]) + int(dec[0])
        return Fraction(numerator, int(dec[1]))


def output_result(fraction):
    fraction_list = str(fraction).split("/")
    if len(fraction_list) == 1:
        return fraction_list[0]
    else:
        whole_num = floor(int(fraction_list[0]) / int(fraction_list[1]))
        frac_num = int(fraction_list[0]) % int(fraction_list[1])
        if whole_num == 0:
            return str(frac_num) + "/" + (fraction_list[1])
        else:
            return str(whole_num) + "_" + str(frac_num) + "/" + (fraction_list[1])


def fraction_trick():
    i = 0
    while i < 3:
        x = input("? ").strip().split()
        if len(x) < 3:
            print(
                "Please enter your input in a format: \n{whole number_}numerator/denominator e.g. '3_1/4'+spase+operator(*, /, +, -)+{whole number_}numerator/denominator")
            i += 1
        else:
            if x[1] == "*":
                result = output_result(input_number(x[0]) * input_number(x[2]))
            elif x[1] == "/":
                if input_number(x[2]) == 0:
                    result = "Never try this again! Only Chuck Norris can divide by zero!"
                else:
                    result = output_result(input_number(x[0]) / input_number(x[2]))
            elif x[1] == "+":
                result = output_result(input_number(x[0]) + input_number(x[2]))
            elif x[1] == "-":
                result = output_result(input_number(x[0]) - input_number(x[2]))
            else:
                result = "invalid operator"
            print("= " + str(result))
            break


# fraction_trick()