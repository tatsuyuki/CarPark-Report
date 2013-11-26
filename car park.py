import datetime
from datetime import date
from datetime import timedelta
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
import csv
import os.path




### File path is temporary, to be updated on final version

### To declare a class for function reusability

if os.path.isfile("/Users/Michael/Documents/GitHub/Car Park Report/report.csv") == False:   #Check if table file exist
##USE DYNAMIC FILE NAME


    head = ['Ticket No.', 'Tenant', 'Time In', 'Time Out', 'Charge', 'Discount', 'Total'] 

    with open('/Users/Michael/Documents/GitHub/Car Park Report/report.csv', 'w') as a:   ###Create file and write header row if file 
        writer = csv.writer(a)                                                   ###does not exist
        ##writer.writerow("INPUT DYNAMIC DATE HERE")
        writer.writerow(head)
else:
    print ("File exist, entering appending mode")   #Message if file exist



##### Class for Code Reusability

class inc_project(object):

    def __init__(self):
        pass
        







def write_func():            ###Get input from user and append to table file
    
    dbase = []
    cur_tenant = ['YKCC', 'YK', 'RHB', 'KIBB', 'CECELIA', 'ykcc', 'yk', 'rhb', 'kibb', 'cecelia']

    Tix_No = raw_input("Ticket Number:  ")
    
    
    
  
    for i in cur_tenant:
        tenant = raw_input("Tenant:  ") ##Test for valid Tenant
        if tenant == i:
            break
        else:
            tenant = 'N/A'
            break

        

    time_in = str(raw_input("Time In (hhmmss):"))
    ###     While loop to ensure correct date format for ease of processing
    while len(time_in) != 6 or int(time_in[0:2]) > 24 or int(time_in[2:4]) > 60 or int(time_in[4:6]) > 60:
        time_in = str(raw_input("Invalid Time Format! Try again (hhmmss):"))
                   
    time_out = str(raw_input("Time Out (hhmmss):"))
    ###     While loop to ensure correct date format for ease of processing
    while len(time_out) != 6 or int(time_out[0:2]) > 24 or int(time_out[2:4]) > 60 or int(time_out[4:6]) > 60:
        time_out = str(raw_input("Invalid Time Format! Try again (hhmmss):"))

    
    
    


    dbase = [Tix_No, tenant, time_in, time_out]

    with open('/Users/Michael/Documents/GitHub/Car Park Report/report.csv', 'a') as b:
        writer = csv.writer(b)
        writer.writerow(dbase)
        
def read_func():            ###Print out table file
    with open('/Users/Michael/Documents/GitHub/Car Park Report/report.csv', 'r') as c:
        reader = csv.reader(c)
        for row in reader:
            print row

def dict_read():                        
    data_in = csv.DictReader(open("/Users/Michael/Documents/GitHub/Car Park Report/report.csv"))

    for r in data_in:
        print r
        
""" hp_interest to be modified to take 1 param, loan-number and match it against table in projection.csv for the
    respective loan.
    and subsequently the required details to calculate the interest
"""
def hp_interest(tenure, interest, amount, l_no):                                  ### Calculate HP interest given the param
    term_charge = float(amount * float(tenure/12)) * float(interest)/100 #Getting term charge
    ###print term_charge
    int_constant = float(((tenure)*(tenure+1))/2) #Calculating interest constant for use in formula 
    ###print int_constant                           *skipping full formula for simplicity
    instalment = tenure
    ###print instalment
    interest_tab = [str(l_no)]
    count = 0
    count_tab = ['Loan Number']
    while instalment > 0:
        interest = float(((instalment) / (int_constant)) * (term_charge))
        interest_tab.append(interest)
        count += 1
        instalment -= 1
        count_tab.append(count)

    hp_header = count_tab
    with open('/Users/Michael/Documents/GitHub/Int-Projection/HP_Int.csv', 'w') as h:
        writer = csv.writer(h)
        writer.writerow(hp_header)

    with open('/Users/Michael/Documents/GitHub/Int-Projection/HP_Int.csv', 'a') as ins:
        writer = csv.writer(ins)
        writer.writerow(interest_tab)
    
    

    ###for i in interest_tab:
    ###    print i
    ###for i in count_tab:
    ###    print i
    return interest_tab

def agreement_date(string):                 ###convert a set of string into date

    ag_date = datetime.strptime(str(string), '%Y%m%d')
   
    return ag_date

##generate list of 12 months and populate relavant interest

def calendar(string):

    c.header = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return






begin = raw_input("Write or Read?")
if (begin == "Write") or (begin == "write"):
    write_func()
    validinput = True
    
elif (begin == "Read") or (begin == "read"):
    read_func()
    validinput = True

else:
    validinput = False
    
while validinput == False:
    print ("Wrong input, please try again")
    begin = raw_input("Write or Read?")
    if begin == 'Write' or begin == 'write':
        write_func()
        validinput = True

    elif begin == 'Read' or begin == 'read':
        read_func()
        validinput = True


            



    
