def itemPrice(barcode):
    # list to append the ASCII codes.
    li = []

    for i in barcode:
        n = ord(i)

        # finding the maximum digit of the ASCII code
        if n // 10:
            maxi = 0
            while n > 0:
                if n % 10 > maxi:
                    maxi = n % 10
                n = n // 10
            li.append(maxi)
        else:
            li.append(n)

    # returning the sum of list items
    return sum(li)

barcode = input("Enter barcode: ")
print(itemPrice(barcode))