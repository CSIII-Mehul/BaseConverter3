import math


def alter_list(arr):
    alter = []
    index = []
    for j in range(len(arr)):
        index.append(j)
    doubled = lambda x,y: x*(2**y)
    for i in map(doubled,arr,index):
         alter.append(i)
         
    
  

    return alter

def converter(base_initial,num,base_converted):

    if base_initial != 10:
       to10 = 0
       counter = len(num)-1
       index = 0
       while counter > -1:
           to10 += int(num[counter]) * base_initial ** index
           counter -=1
           index +=1

       if base_converted ==10:
           return to10
       elif base_converted < 10:
           if to10 < base_converted:
               return to10
           else:
              return modulus(to10, base_converted)
       elif base_converted > 10 :
             return modulus(to10, base_converted)


    elif base_initial == 10:
        if base_converted == 10:
            return num
        elif base_converted < 10:
           if int(num) < base_converted:
               return int(num)
           else:
              return modulus(int(num), base_converted)
        elif base_converted > 10:
            return modulus(int(num), base_converted)



    return 0

def valid_number(num, base_initial):
   #while loop below looks to see if inputted number is valid given original base
    check = base_initial
    while check < 16:
        for i in range(len(num)):
            if check >= 10:
               if check == 10:
                    if "A" in num:
                        return False
               if check ==  11:
                    if "B" in num:
                        return False
               if check ==  12:
                    if "C" in num:
                        return False
               if check ==  13:
                     if "D" in num:
                        return False
               if check ==  14:
                    if "E" in num:
                        return False
               if check ==  15:
                    if "F" in num:
                        return False

            else:
                if str(check) in num:
                    return False

        check+=1

    return True
                
def modulus(num, base):
    new_num = ""
    num = num
    if base < 11:
     while num >= base:
        new_num += str(num % base)
        num = num // base
        if num < base:
            new_num += str(num)
            break
    else:
        if num < base:
            if num >=10:
                return alpha_change(num)
        while num >= base:
            if (num % base) >=10:
                new_num += str(alpha_change(num % base))
            else:
               new_num += str(num % base)
            num = num // base
            if num < base:
                 if (num) >=10:
                       new_num += str(alpha_change(num))
                 else:
                      new_num += str(num)
                 break


   
    return new_num[::-1]

def alpha_change(num):
    if num == 10:
       return "A"
    if  num ==  11:
         return "B"
    if num ==  12:
         return "C"
    if num ==  13:
       return "D"
    if num ==  14:
       return "E"
    if num ==  15: 
        return "F"

def run():

    base_initial = int(input("what base are you starting with?"))
    while base_initial < 0 or base_initial> 16: 
            base_initial = int(input("what base are you starting with?"))

    num = input("what number are you converting form that base?")
    while valid_number(num,base_initial) == False:
        num = input("what number are you converting form that base?")    

    base_converted = int(input("what base do you want to convert to?"))
    while base_converted < 0 or base_converted> 16: 
            base_converted = int(input("what base do you want to convert to?"))
    
    print(converter(base_initial,num,base_converted))
    

   
    return 0



if __name__ == "__main__":
    run()