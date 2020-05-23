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
    
    converter(base_initial,num,base_converted)
    #print(alter_list([1,2,3]))

   
    return 0



if __name__ == "__main__":
    run()