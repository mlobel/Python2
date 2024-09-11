def number_compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            print("First is greater")

        elif a < b:
            print("Second is greater")

        else:
            print("Numbers are equal")
        
    else:
        print("Error: non-number detected")

number_compare(1, 1)
number_compare(-1, 1)
number_compare(1, -2)