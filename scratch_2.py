# Author: Kaveh Piroozram, 2018 Oct
# Aim: To find the lowest rate between several 
# phone operators based on the given phone prefix.

# For more efficiency the solution will be multiprocess search..
# first get number of cores, then assign the dict search to 
# different process affinities.. Also maybe to introduce
# generators instead of iterators..

import random
import time
import re
import json


# create a dictionary with unique entries
def price_list():

    #dict, Phone number prefixes max 7 digits.
    #Each operator supports 2k prefixes
    rate_table = {random.randint(1,9999999): round(random.uniform(0.1, 2.0), 2) for x in range(2000)}
    return rate_table

Amount= int(input('Please enter amount of price lists:'))

#list of dict
Operators = []

for i in range(Amount):

    #create a new price lists & store them for later usage
    lista=price_list()
    Operators.append(lista)

    #create log
    rate_file_name = "operator_" + str(i+1)
    with open(rate_file_name, 'w') as op_file:
        #data.write(str(lista)) #not friendly to verify manually..
        op_file.write ('[' + '\n'.join(json.dumps(i) for i in lista.items()) + ']\n')


#################################################
tmp = input('Please enter your phone number:')
tmp = tmp.lstrip("0") # 0046=> 46
phone_number= re.sub("\\+|\\-| |\\ ", "", tmp) #+46-730-8123 -> 467308123
if not phone_number.isdigit() :
        print("sorry!")
#################################################

# to search for first 7 characters
# country code max 3 digits , operator/area code max 4 digits

found=0
t = 0
# only pairs with right prefix are stored here for later comparision.
current_rate = dict.fromkeys("99999999", 99999.9999) #format
min_rate = 0


#loop through all operator lists & look for the right prefix
while (t < Amount):

    print("searching for prices at operator", t+1, "...")

    for prefix , rate in Operators[t].items():
        #print (prefix, "::", rate)

        s= str(prefix)

        for i in range (7,2, -1): #(46-73120, 46-7312, 46-731, 46-73, 46-7, 46)

            z= "^" + s[0:i]

            if (re.match(z, phone_number)):
                #get the dict element (prefix:rate)which matches the prefix at each loop
                #& store it in the current_rate dict
                 current_rate[t]= Operators[t].get(prefix) #(key=prefix) ==>value=rate

                 #here we could introduce a function to get the common numbers
                 #with the subscriber from begining.
                 #print ("found prefix", prefix )

                 found=1
                 break
    t +=1

    if (t == Amount):
        break


if (found):
    min_rate = min(current_rate.items(), key=lambda x: x[1])
    a = list(min_rate)  # access contents of iterable
    print ("Cheapest rate was offred by operator: ", a[0]+1,".The price is", a[1]," kr/min" )

else:
    print("Sorry no operator supports your number.")
 
