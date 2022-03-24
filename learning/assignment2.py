msg = ''
count = 1
mod_value = 10
after_mod_action = 0



while msg != 100 :
    userinput = input("Enter a number: ")
    msg = int(userinput)
    
    if msg < 100 :
        count *= int(userinput)
    elif msg > 100 :
        print("You are authorized to input under range 100")
        msg = 100
        after_mod_action = count % mod_value
    else:
        after_mod_action = count % mod_value
    
if msg == 100:
    print("Here is the multiplied answer: ",count)
    print("And the modulo operation answer is: ",after_mod_action)
else:
    print("Sorry I can not able to count")
        