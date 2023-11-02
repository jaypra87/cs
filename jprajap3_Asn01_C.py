"""
    CS1026a 2023
    Assignment 01 Project 01 - Part C
    Jay Prajapati
    251350172
    jprajap3
    08/06/2023
"""
# The 'transistors' gets the number of transistors the user wants
transistors = int(input("The starting number of transistors: "))
# The 'start_year' will get the year that the user wants to start at.
start_year = int(input("The year to start the calculations from: "))
# The 'number_of_year' will get the number of years after the 'start_year' that we need to go
numbers_of_year = int(input("The number of years to calculate: "))

# This print line prints the categories 'year', 'transistors' and 'flops'
print("YEAR :", "TRANSISTORS :", "FLOPS: ")


# This function is build to return the type of flop. This function will check if the flops ('flopValue') is greater than
# yotta, zetta, exa, peta, tera, tera, giga, mega, kilo and will check if it is less than kilo. If any of those conditions
# are true than the string will be returned.
def flop_type(flops):
    kilo = 1000
    mega = kilo * 1000
    giga = mega * 1000
    tera = giga * 1000
    peta = tera * 1000
    exa = peta * 1000
    zetta = exa * 1000
    yotta = zetta * 1000

    if flops >= yotta:
        return "yottaFLOPS"
    elif flops >= zetta:
        return "zetaFLOPS"
    elif flops >= exa:
        return "exaFLOPS"
    elif flops >= peta:
        return "petaFLOPS"
    elif flops >= tera:
        return "teraFLOPS"
    elif flops >= giga:
        return "gigaFLOPS"
    elif flops >= mega:
        return "megaFLOPS"
    elif flops >= kilo:
        return "kiloFLOPS"
    elif flops < kilo:
        return "FLOPS"


# This function is built to return the value of the flop type. After the value of the flop type is returned flops will be
# divided by this value.
def flop_value(flops_value):
    kilo = 1000
    mega = kilo * 1000
    giga = mega * 1000
    tera = giga * 1000
    peta = tera * 1000
    exa = peta * 1000
    zetta = exa * 1000
    yotta = zetta * 1000

    if flops_value >= yotta:
        return yotta
    elif flops_value >= zetta:
        return zetta
    elif flops_value >= exa:
        return exa
    elif flops_value >= peta:
        return peta
    elif flops_value >= tera:
        return tera
    elif flops_value >= giga:
        return giga
    elif flops_value >= mega:
        return mega
    elif flops_value >= kilo:
        return kilo
    elif flops_value < kilo:
        return 1


for year in range(start_year, start_year + numbers_of_year + 1, 2):
    # 'flops' hold the value of transistors * 50.
    flops = transistors * 50
    # 'flopsValue' calls the function 'flop_type' and then holds the string value of the flop type that was returned by the function
    flopsValue = flop_type(flops)
    # 'temp' calls the function 'flops_value'. Then 'flops' is divided by the value returned by the function 'flops_value'.
    # The significance of doing the division is so that it can be easily shortened to 2 decimal places when printing.
    temp = flops/flop_value(flops)
    print(year, "{:,}".format(transistors), "%.2f" % temp, flopsValue, f"{flops:,.0f}")
    transistors *= 2

print("END: Project One <01> – Part C")
print("Jay Prajapati jprajap3 251350172")
