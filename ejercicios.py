import math

# --- Punto 2

# T1(n) = 3n^2 + 50n -> Insertion/Bubble

# T2(n) = 8nlog2(n) + 200 -> Merge/Heapsort

# T3(n) = 0.2n^3 -> Floyd-Warshall

# T4(n) = 2^n -> Backtracking/Fuerza bruta

# Comparación T(1) vs T(2)
def compare_t1_t2(n):
    for i in range(1, n):
        t1_val = 3*i**2 + 50*i
        t2_val = 8*i*math.log2(i) + 200

        print(f"n={i}: T1({n}) = {t1_val:.2f}, T2({n}) = {t2_val:.2f}")
        if(t1_val) > (t2_val):
            return i          
    return -1
    
# Comparación T(1) vs T(3)
def compare_t1_t3(n):
    for i in range(1, n):
        t1_val = 3*i**2 + 50*i
        t3_val = 0.2*i**3

        print(f"n={i}: T1({n}) = {t1_val:.2f}, T3({n}) = {t3_val:.2f}")
        if(t3_val) > (t1_val):
            return i
    return -1

print(compare_t1_t2(10000), compare_t1_t3(10000))


# --- Punto 3

def prime_finder(a, b):
    cont = 0
    
    for i in range(a, b + 1):
        if i < 2:
            continue
        elif i == 2:
            cont += 1
        elif i % 2 == 0:
            continue
        else:
            is_prime = True
            for j in range(3, int(math.sqrt(i)) + 1, 2): 
                if i % j == 0:
                    is_prime = False
                    break
            
            if is_prime:
                cont += 1
    
    return cont
          
print(prime_finder(1, 10))
            
