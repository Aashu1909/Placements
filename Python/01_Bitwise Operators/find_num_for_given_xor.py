def find_number_for_XOR(n):
    number=bin(n).replace("0b","")
    a=""
    b=""
    # and to find the maximum product 
    counter=0
    for char in str(number):
        print("char",char)
        if char=="1":
            if counter%2==0:
                a+="0"
                b+="1"
                counter+=1
            else:
                a+="1"
                b+="0"
                counter+=1
        else:
            a+="1"
            b+="1"
            counter+=1
    print(int(a,2),str(a))
    print(int(b,2),str(b))

find_number_for_XOR(13)