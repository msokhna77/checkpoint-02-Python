def factorial(n): 
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
num = int(input("Donner un nombre: ")); 
print("Factoriel de ",num,"est", factorial(num))
"""if num<0:
    print("Merci de donner un nombre positif")
else:
    print("Factoriel de ",num,"est", factorial(num))
"""