while True:
    number = input("input any number ")
    if number.isdigit():
        print("good job moron you have entered the number")
        if int(number)%2 == 0:
            print("this is an even number")
        else:
            print("this is a odd number")
    else:
        print("this is not a number, please input a number moron")
