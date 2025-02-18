# function to convert the number to decimal
def convert_to_dec(bin_number):
    dec_number = 0
    factor = 1
    while bin_number:
        # check if the number contains a digit other than is not 0 or 1
        if (bin_number % 10) not in [0, 1]:
            raise ValueError("The binary number should only contain 1s and 0s.")
        # the actual conversion
        dec_number += (bin_number % 10) * factor
        factor *= 2
        bin_number //= 10
    return dec_number

if __name__ == '__main__':
    bin_number = input("Enter the binary number (max. 8 digits): ")
    # check if the input is digit-only (a pseudo-number)
    if (bin_number.isdigit()):
        try:
            # send the number to convert function
            dec_number = convert_to_dec(int(bin_number))
        except ValueError as ve:
            print(f"Something went wrong: {ve}")
        else:
            print(dec_number)
    else:
        print("The binary number should only contain 1s and 0s.")