import math

# --- Punto 2

# T1(n) = 3n^2 + 50n -> Insertion/Bubble

# T2(n) = 8nlog2(n) + 200 -> Merge/Heapsort

# T3(n) = 0.2n^3 -> Floyd-Warshall

# T4(n) = 2^n -> Backtracking/Fuerza bruta

# Comparación T(1) vs T(2)
def compare_perfomance(n):
    for i in range(1, n):
        if(3*i**2 + 50*i) > (8*i*math.log(i) + 200):
            return i
    return -1

print(compare_perfomance(1000000))


# --- Punto 3

def prime_finder(a, b):
    cont = 0
    is_prime = True
    for i in range(a, b):

        if i < 2:
            is_prime = False
            continue
        elif i == 2:
            is_prime = True
        else:    
            for j in range(2, i - 1):
                if i % j == 0:
                    is_prime = False
                    break
                else:
                    is_prime = True
        
        if is_prime == True:
            cont += 1   

    return cont
          
print(prime_finder(1, 10))
            