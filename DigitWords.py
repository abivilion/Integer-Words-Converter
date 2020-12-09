# Python program to print a given number in
# words. The program handles numbers
# from 0 to 9999

# A function that prints
# given number in words

def convert_to_words(num):
    # Get number of digits
    # in given number
    l = len(num)
    n = l - 1

    # Base cases
    if l == 0:
        print("empty string")
        return

    if l > 4:
        print("Length more than 4 is not supported")
        return

    # The first string is not used,
    # it is to make array indexing simple
    single_digits = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]

    # The first string is not used,
    # it is to make array indexing simple
    two_digits = ["", "", "ten", "eleven", "twelve",
                  "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eighteen",
                  "nineteen"]

    # The first two string are not used,
    # they are to make array indexing simple
    tens_multiple = ["", "", "twenty", "thirty", "forty",
                     "fifty", "sixty", "seventy", "eighty",
                     "ninety"]

    tens_power = ["hundred", "thousand"]

    # Used for debugging purpose only
    print(num, ":", end=" ")

    # For single digit number
    if l == 1:
        v = int(num[0])
        print(single_digits[v])
        return

    # Iterate while num is not '\0'
    x = 0
    while x < len(num):

        # Code path for first 2 digits
        if l >= 3:
            if int(num[x]) != 0:
                print(single_digits[int(num[x])],
                      end=" ")
                print(tens_power[l - 3], end=" ")
            # here len can be 3 or 4

            l -= 1

        # Code path for last 2 digits
        else:

            # Need to explicitly handle
            # 10-19. Sum of the two digits
            # is used as index of "two_digits"
            # array of strings
            if not int(num[x]):
                sum = (int(num[x]) + int(num[x]))
                print(two_digits[sum])
                return

            # Need to explicitely handle 20
            elif (int(num[x]) == 2 and
                  int(num[x + 1]) == 0):
                print("twenty")
                return

            # Rest of the two digit
            # numbers i.e., 21 to 99
            else:
                i = int(num[x])
                if i > 0:
                    print(tens_multiple[i], end=" ")
                else:
                    print("", end="")
                x += 1
                if int(num[x]) != 0:
                    print(single_digits[int(num[x])])
        x += 1

    # Driver Code


z = input("Enter number:")
convert_to_words(z)
