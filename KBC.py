amount=0
print('\033[4m''\033[95m'"\tWELCOME TO KBC GAME:-\n")
question=["1)what is the capital of india ?","2)who was the first pm in india ?"
         ,"3)which city known as pink city ?","4)who is the father of india ?"
         ,"5)how many days in a leap year ?","6)what is the real name of carriminati ?"
         ,"7)which is the smllest city in india ?","8)who is the father of computer ?"
         ,"9)which is the costly phone in india ?","10)which is the largest country in population in world?"]
option= [["1)manipur","2)bihar","3)rajasthan","4)delhi","5)lifeline"],
         ["1)ramanujan","2)dr rajendra prasad","3)siwaji the boss","4)jd the loop","5)lifeline"],
         ["1)maharastra","2)goa","3)jaipur","4)alipur","5)lifeline"],
         ["1)prime minister","2)president","3)vidhayak","4)public","5)lifeline"],
         ["1)345","2)423","3)366","4)365","5)lifeline"],
         ["1)raju","2)ghanshyam","3)ajay nagar","4)babu rao","5)lifeline"],
         ["1)mumbai","2)goa","3)jaipur","4)panipath","5)lifeline"],
         ["1)robbert frost","2)shakespear","3)charles babbage","4)king luis","5)lifeline"],
         ["1)oppo","2)vivo","3)iphone","4)samsung","5)lifeline"],
         ["1)bangal","2)america","3)india","4)europe","5)lifeline"]]
solution= [4,2,3,2,3,3,2,3,3,3]
lifeline=["1)50-50","2)audience pole","3)phone a friend","4)skip"]
for i in range(len(question)):
    print('\033[m',question[i],"\n"'\033[0m')
    for j in option[i]:
        print("  "'\033[93m',j,'\033[0m')
    user= int(input("\nenter your answer: "))
    print()
    if user==solution[i]:
        print('\033[92m',"correct answer\n you won 1000\n",'\033[0m')
        amount+=1000
        continue
    elif user==5:
        if len(lifeline)!=0:
            for lf in lifeline:
                print('\033[94m',lf,'\033[0m')
            demand= int(input("\nchoose any lifeline: "))
            if demand==1:
                lifeline.remove("1)50-50")
            elif demand==2:
                lifeline.remove("2)audience pole")
            elif demand==3:
                lifeline.remove("3)phone a friend")
            else:
                lifeline.remove("4)skip")
            if demand==1:
                print('\033[94m'"options are:",solution[i],"and 1"'\033[0m')
                user=int(input("now choose any one b/w this: "))
                if user==solution[i]:
                    print('\033[92m',"correct answer\n you won 1000\n",'\033[0m')
                    amount+=1000
                else:
                    print('\033[91m'"wrong"'\033[0m')
            elif demand==2:
                print(solution[i],"=70%,other option= 30%")
                user= int(input("choose any option: "))
                if user==solution[i]:
                    print('\033[92m',"correct answer\n you won 1000\n",'\033[0m')
                    amount+=1000
                else:
                    print('\033[91m',"wrong"'\033[0m')
            elif demand==3:
                print("your friend suggestion is ",solution[i])
                user= int(input("enter : "))
                if user==solution[i]:
                    print('\033[92m',"correct answer\n you won 1000\n",'\033[0m')
                    amount+=1000
                else:
                    print('\033[91m',"wrong"'\033[0m')
            elif demand==4:
                print("let's move to next question: ")
                continue
        else:
            print("you don't have more lifeline.. \n")
    else:
        print('\033[91m',"wrong answer\n"'\033[0m')
        continue
print("your total amount is ",amount)
