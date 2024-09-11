def list_manipulation(lst, command, location, value=None):
    end_index = len(lst) - 1

    start_index = 0

    if command == 'add':
        if location == 'end':
            lst.append(value)
            print(lst)
            return lst
        
        elif location == 'beginning':
            lst.insert(0, value)
            print(lst)
            return lst
        
        else:
            print("Invalid Entry")
            return None
    
    elif command == 'remove':
        if location == 'end':
            lst.pop(end_index)
            print(lst)
            return lst
        
        elif location == 'beginning':
            lst.pop(start_index)
            print(lst)
            return lst
        
        else:
            print("Invalid Entry")
            return None
        
    else:
        print("Invalid Entry")
        return None


lst = [1, 2, 3]
list_manipulation(lst, 'remove', 'end')
list_manipulation(lst, 'remove', 'beginning')
print(lst)

lst = [1, 2, 3]
list_manipulation(lst, 'add', 'beginning', 20)
list_manipulation(lst, 'add', 'end', 30)
print(lst)

print(list_manipulation(lst, 'foo', 'end') is None)

print(list_manipulation(lst, 'add', 'dunno') is None)


