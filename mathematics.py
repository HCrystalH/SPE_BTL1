import math

'''
    This function used to find Probability 
    of 0 customers in the system

    s: number of servers
    c: capacity
'''
def P_0 (lamda, muy, c, s):
    p = 1.0
    for i in range(1, s):
        p += (pow((lamda/muy), i) / math.factorial(i))
    p += ((pow((lamda/muy), s) / math.factorial(s)) * ((1-pow((lamda/(s*muy)), (c-s+1))) / (1-(lamda/(s*muy)))))
    return pow(p, -1)

#Function to find probability of n customers in the system
def P_n (lamda, muy, c, s, n):
    if n < s and n >= 1:
       return ((pow((lamda/muy), n)) / math.factorial(n)) * P_0(lamda, muy, c, s)
    elif n > c:
        return 0
    return ((pow((lamda/muy), n)) / (math.factorial(s) * pow(s, (n-s)))) * P_0(lamda, muy, c, s) 

#Function to find Average Number of Customers in System (include in Waiting queue and being served)
def L_s (lamda, muy, s):
    P0 = P_0(lamda,muy,c,s)
    return ((lamda*muy*pow(lamda/muy,s)*P0)/( math.factorial(s-1)* pow((s*muy - lamda),2) )   + lamda/muy )

#Function to find Average Number of Customers in Queue
def L_q (lamda, muy, c, s):
    l = 0
    for i in range(s, c + 1):
        l += ((i-s) * P_n(lamda, muy, c, s, i))
    return l

'''
    Function find Average Time a customer spend in Queue
    (a.k.a Average Waiting Time)
'''
def W_q(lamda, muy, c, s):
    return (L_q(lamda, muy, c, s) / lamda * (1 - P_n(lamda, muy, c, s, c)))

'''
    Function to find Average Time a customer spend in System 
    (a.k.a Avg Service Time)
'''
def W_s(lamda, muy, c, s):
    return (W_q(lamda, muy, c, s) + (1 / muy))


if __name__ == '__main__':
 
    while(1):
        number_of_customer = input("Enter Number of customer in system: ")
        lamda_str = input("Enter arrival rate: ")
        muy_str = input("Enter service rate: ")
        c_str = input("Enter capacity of system: ")
        s_str = input("Enter number of servers: ")
        lamda = float(lamda_str)
        muy = float(muy_str)
        c = int(c_str)
        s = int(s_str)
        n = int(number_of_customer)
        print("--------------------------------------------------------")
        print("Probabity of no customer in system: ", P_0(lamda,muy,c,s) )
        print("Probabity of n customers in system: ", P_n(lamda,muy,c,s,n) )
        print("Avg Number of customer in queue", L_q(lamda,muy,c,s) )
        print("Avg Number of customer in system", L_s(lamda,muy,s) )
        print("Avg Waiting time: ", W_q(lamda,muy,c,s) )
        print("Avg Response time: ", W_s(lamda,muy,c,s) )
        print("--------------------------------------------------------")