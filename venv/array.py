import string

def print_formatted(number):
    # your code goes here

    w = len(str(bin(number)).replace('0b', ''))
    for i in range(1, number + 1):
        decimal = str(int(i)).rjust(w, ' ')
        octal = oct(int(i)).replace('0o', '').rjust(w, ' ')
        hexa = hex(int(i)).upper().replace('0X', '').rjust(w, ' ')
        bi = bin(int(i)).replace('0b', '').rjust(w, ' ')

        print (decimal, octal, hexa, bi)

print_formatted(17)
string.ascii_lowercase