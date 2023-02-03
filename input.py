personal_info = {}
while True:
    choice = input("""Enter a choice:
    1: Add Info
    2: Show Info
    f: Finish
    """)
    if choice == '1':
        name = input("Enter a Name: ")
        if name not in personal_info:
            age = int(input("Age: "))
            weight = float(input("Weight: "))
            height = float(input("Height: "))
            marital_status = input("y/n (married/single)")
            personal_info[name] = [age, weight, height, marital_status]
        else:
            print("this Name already exists")
    elif choice == '2':
        for k, v in personal_info.items():
            print(f"Name: {k}, Age: {v[0]}, Weight: {v[1]}, Height: {v[2]}, Married: {v[3]}")
    elif choice == "f":
        print("finished.") 
        break
