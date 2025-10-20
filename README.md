# Parciales — Análisis de Algoritmos (193502)

Universidad Francisco de Paula Santander Ocaña  
Programa: Ingeniería de Sistemas  
Semestre: V  
Créditos: 3  
Asignatura: **Análisis de Algoritmos** 

---

## Instrucciones generales

- Tiempo máximo: **60 minutos**  
- Cada parcial tiene **4 puntos (25 pts c/u)**  
- Usa Python o Java.  
- Para comparar funciones, basta con un **`for` + `if`** y reportar el menor `n` que verifica la desigualdad.  
- Justifica con fórmulas y razonamiento.  

---

# Parcial — Versión A

### Punto 1 (25 pts) — Ordena por complejidad
Ordena de menor a mayor las siguientes funciones (asintóticamente).  
Si dos son del mismo orden, indícalo.


![Logo](https://lh3.googleusercontent.com/pw/AP1GczOgpGBrm2bFBeJEo7b9KpmVW1WB0J7_4xhzREWWmsjd8ejMOn5_QmXnv9ji2z7BlyVAVmYl0jOEs01Vmf9-wEbyuZo7S5DK2xYmuN-cOR2my9LOms5kM5FlcbG3I19k3Xc8nwGVtFKco2O2QXg4DLUn=w128-h290-s-no?authuser=0)

### Respuesta

log(n) < (log(n))^2 < sqrt(n) < n < n/log(n) n^(1.5) < n^2 < 2^n < n!
---

### Punto 2 (25 pts) — Identifica y confronta
Asocia cada \(T(n)\) con un algoritmo plausible. Luego compara **dos pares** y encuentra el umbral de `n` con un `for` + `if`.

- T1(n) = 3n^2 + 50n 
- T2(n) = 8nlog2(n) + 200 
- T3(n) = 0.2n^3
- T4(n) = 2^n

Algoritmos posibles:  
- Insertion/Bubble (peor caso)  
- Merge/Heapsort  
- Floyd–Warshall (triple bucle)  
- Backtracking/Fuerza bruta  

### Respuesta

#### T1(n) = 3n^2 + 50n -> Insertion/Bubble

#### T2(n) = 8nlog2(n) + 200 -> Merge/Heapsort

#### T3(n) = 0.2n^3 -> Floyd-Warshall

#### T4(n) = 2^n -> Backtracking/Fuerza bruta

### Conclusión a la comparación entre T(1) y T(2)

- Para n=4: T1(4) = 248, T2(4) ≈ 264 → T1 < T2
- Para n=5: T1(5) = 325, T2(5) ≈ 293 → T2 < T1

El umbral se encuentra en n = 5, a partir de este valor T(2) = 8nlog2(n) + 200 presenta un tiempo de ejecución inferior a T(1) = 3n^2 + 50n

### Conclusión a la comparación entre T(1) y T(3)

- Para n=24: T1(24) = 2928.00, T3(24) = 2764.80 → T3 < T1 
- Para n=25: T1(25) = 3125.00, T3(25) = 3125.00 → T1 = T3 
- Para n=26: T1(26) = 3328.00, T3(26) = 3515.20 → T1 < T3 

Por lo tanto, el umbral se encuentra en n = 26

---

### Punto 3 (25 pts) — Ejercicio lógico
#### Isaac y los intervalos mágicos

Isaac, convencido de que tiene un talento especial para los números, asegura que puede contar al instante cuántos primos existen en cualquier rango que le propongan sus amigos. Para comprobarlo, ellos le entregan una lista con N pares de números (a,b), y él debe responder de inmediato cuántos números primos hay en cada intervalo. A partir de esta historia, elabora el análisis necesario para resolver el problema y define claramente qué se recibe como entrada, qué se debe producir como salida y qué lógica se requiere para verificar la afirmación de Isaac. 


### Respuesta
Dado un rango (a, b), para cada valor i dentro del rango (a, b) el algoritmo debe realizar un bucle de complejidad O(√i / 2) ≈ O(√i), que en el peor caso es O(√b). Si consideramos b - a = n obtenemos que la complejidad temporal del problema es O((b-a)*√b) = O(n*√b) 

---

### Punto 4 (25 pts) — Cuestionario

[![Click here!!](https://cf.quizizz.com/img/wayground/brand/plans/logo-basic.png)](https://wayground.com/join?gc=846438)
