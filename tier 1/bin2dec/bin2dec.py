def convert_to_dec(bin_number):
    dec_number = 0
    factor = 1
    while bin_number:
        if (bin_number % 10) not in [0, 1]:
            raise ValueError("The binary number should only contain 1s and 0s.")
        dec_number += (bin_number % 10) * factor
        factor *= 2
        bin_number //= 10
    return dec_number

if __name__ == '__main__':
    bin_number = input("Enter the binary number (max. 8 digits): ")
    if (bin_number.isdigit()):
        try:
            dec_number = convert_to_dec(int(bin_number))
        except ValueError as ve:
            print(f"Something went wrong: {ve}")
        else:
            print(dec_number)

    else:
        print("The binary number should only contain 1s and 0s.")