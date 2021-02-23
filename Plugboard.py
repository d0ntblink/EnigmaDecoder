'''
Gary Khodayari
2020/10/24
'''
import os
import time
#########
#########
KEY = "Key so far is :"
lletter_pool = "qwertyuiopasdfghjklzxcvbnm"
uletter_pool = "QWERTYUIOPASDFGHJKLZXCVBNM"
new_lletter_pool = str(lletter_pool)
new_uletter_pool = str(uletter_pool)
chose_letter_prompt = ("welcome to the intial setup, Plugboard settings\n"
"\n"
"\n"
"chose the letters you want to switch\n"
"the formation in which you have to chose the chaning letter are <letter 1>:<letter 2>\n"
"in which :\n" 
"the letter 1 is the letter you wish to change and letter 2 is the letter you wish to change it with\n"
"\n"
"\n"
"type \"next\" to procede to the next step\n")
error_prompt = "\n Something went terribly wrong\n recheck your input and try again!"
#########
#########
def test() :
    print(new_lletter_pool)
    print(new_uletter_pool)
    #print(lletter_pool[lletter_pool.find(user_letters[0])] , lletter_pool[lletter_pool.find(user_letters[2]) ] , lletter_pool.find(user_letters[0]) , lletter_pool.find(user_letters[2]) )
    time.sleep(10)
#########
#########
while True :
    os.system('cls||clear')
    print(chose_letter_prompt)
    user_letters = str(input())
    user_letters = user_letters.lower()
    #test()

    if user_letters == "next" :
        break
    elif user_letters == "test" :
        while True :
            print(new_lletter_pool[lletter_pool.find(input().lower())])
    elif ( len(user_letters) == 3 ) and (user_letters[1] == ":") and ( user_letters[0] in (lletter_pool + uletter_pool)) and ( user_letters[2] in ( lletter_pool + uletter_pool )) :
        new_lletter_pool = new_lletter_pool[:lletter_pool.find(user_letters[0])] + user_letters[2] + new_lletter_pool[lletter_pool.find(user_letters[0])+1:]
        new_lletter_pool = new_lletter_pool[:lletter_pool.find(user_letters[2]) ] + user_letters[0] + new_lletter_pool[lletter_pool.find(user_letters[2]) +1:]
        new_uletter_pool = new_lletter_pool.swapcase()
        KEY = KEY + "%s = %s ," % (user_letters[0] , user_letters[2])
        #test()
    elif user_letters == "key" :
        print(KEY)
        time.sleep(2)
    else :
        print(error_prompt)
        time.sleep(2)