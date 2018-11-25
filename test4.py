import math 
x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = math.cos(x)#cos(x)*cos(x) koda kluda
print("cos(%.2f) = %6.2f"%(x,y))
k = 0
a = (-1)**0*x**1/(1)
S = a
print("a0 = %6.2f S0 = %6.2f"%(a,S))
k = 1
#a = a * (-1)*x*x/(2*3)
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
#print("a1 = %6.2f S1 = %6.2f"%(a,S))
print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
k = 499
#a = a * (-1)*x*x/(4*5)
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
#print("a2 = %6.2f S2 = %6.2f"%(a,S))
print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
k = 500
#a = a * (-1)*x*x/(6*7)
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
#print("a3 = %6.2f S3 = %6.2f"%(a,S))
print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
print(("cos(%.2f)")%(x)) 
print("")
print("                        500 ")
print("                       _____")
print("                       \               k    2*k+1")
print("                        \           (-1) * x")
print(('cos(%.2f)')%(x), end="")
print('             = >       __________________')
print("                        /")
print("                       /_____          (2*k+1)!")
print("                         k=0")
print("")
print("                                     2")
print("                             (-1) * x")
print("Rekurences reizinatajs:_____________________")
print("                          k * 2 * (2*k+1)")









