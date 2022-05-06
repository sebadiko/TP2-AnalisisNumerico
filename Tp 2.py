import numpy as np
import os
# Libreria de Calculo numerico para un gran volumen de datos
from numpy.lib.shape_base import split

def menu(): #Ociones
    os.system("CLS")
    print("METODOS DE CALCULO")
    print(" ---Metodos---")
    print(" 1- Metodo de SOR")
    print(" 2- Metodo de Potencia Inversa + Aitken")
    print(" ---Ejemplos de Metodo SOR(Chapra)---")
    print(" 3- Ejercicio Nº11.8: Metodo SOR")
    print(" 4- Ejercicio Nº11.11: Metodo SOR (Con relajacion y sin relajacion)")
    print(" 5- Ejercicio Nº11.12: Metodo SOR (Con relajacion y sin relajacion)")
    print(" ---Ejemplos de Metodo Potencia Inversa(Burden)---")
    print(" 6- Ejercicio Nº1.e: Metodo de Potencia Inversa(Tres primeras Iteraciones)")
    print(" 7- Ejercicio Nº3.f: Metodo de Potencia Inversa(Tres primeras Iteraciones)")
    print(" ---Salida---")
    print(" 8- Salir")
    try:
        numeroDeMetodo = int(input("Elija una opcion (1-8): "))
    except ValueError:  # En caso de error vuelve al menu
        menu()
    while True: #Cuando la opcion es elegida, ingresa a un ciclo while que llevará a ejecutar el numero seleccionado mediante estructuras condicionales (if)
        if numeroDeMetodo == 1:
            os.system("CLS")
            print("Opcion 1: metodo SOR")
            while True:
                try:
                    ordenMatrizCoeficinte = int(
                        input("Orden de la matriz de coeficiente: "))
                except:
                    continue
                else:
                    break
            print("Ingrese datos de la matriz de coeficientes")
            matrizCoeficiente = []
            for i in range(ordenMatrizCoeficinte):
                while True:
                    try:
                        matriz = [float(x) for x in input(
                            "Fila {0}: ".format(i+1)).split()]
                    except:
                        continue
                    else:
                        if(len(matriz) == ordenMatrizCoeficinte):
                            matrizCoeficiente.append(matriz)
                            break
                        else:
                            continue
            print("Ingresar datos de la matriz de terminos independientes")
            while True:
                try:
                    matrizIndependiente = [float(x) for x in input(
                        "Terminos independientes: ").split()]
                except:
                    continue
                else:
                    if(len(matrizIndependiente) == ordenMatrizCoeficinte):
                        break
                    else:
                        continue
            while True:
                try:
                    w = float(input("Coeficiente de Relajacion: "))
                except:
                    continue
                else:
                    break
            while True:
                try:
                    toleranciaAceptada = float(
                        input("Ingresar numero de Tolerancia: "))
                except:
                    continue
                else:
                    break
            while True:
                try:
                    iteracionesMaximas = int(
                        input("Ingrese numero maximo de iteraciones: "))
                except:
                    continue
                else:
                    break
            metodoSOR(ordenMatrizCoeficinte, matrizCoeficiente, matrizIndependiente, np.zeros(
                ordenMatrizCoeficinte), w, toleranciaAceptada, iteracionesMaximas)
            atras()
        elif numeroDeMetodo==2:
            os.system("CLS")
            print("2- Metodo de Potencia Inversa + Aitken")
            while True:
                try:
                    ordenMatrizInversa= int(input("Ingrese orden de la matriz de coeficientes: "))
                except:
                    continue
                else:
                    break
            print("Ingrese datos de la matriz de coeficientes: ")
            matrizI=[]
            for i in range(ordenMatrizInversa):
                while True:
                    try:
                        matriz = [float(x) for x in input("Fila {0}: ".format(i+1)).split()]
                    except:
                        continue
                    else:
                        if(len(matriz)==ordenMatrizInversa):
                            matrizI.append(matriz)
                            break
                        else:
                            continue
            print("Ingrese datos del autovector inicial separtados por espacios")
            while True:
                try:
                    vector= [float(x) for x in input("AutoVector: ").split()]
                except:
                    continue
                else:
                    if(len(vector)== ordenMatrizInversa):
                        break
                    else:
                        continue
            while True:
                try:
                    tolerancia=float(input("Ingrese Tolerancia: "))
                except:
                    continue
                else:
                    break
            while True:
                try:
                    maximaIteraciones= int(input("Ingrese numero maximo de iteraciones: "))
                except:
                    continue
                else:
                    break
            metodoPIn(ordenMatrizInversa, np.array(matrizI), np.array(vector), tolerancia, maximaIteraciones)
            atras()
        elif numeroDeMetodo==3:
            os.system("CLS")
            print("3- Ejercicio Nº11.8: Metodo SOR")
            metodoSOR(3, [[15, -3, -1], [-3, 18, -6], [-4, -1, 12]], [3800, 1200, 2350], np.zeros(3), 1.2, 1e-3, 100)
            atras()
        elif numeroDeMetodo==4:
            os.system("CLS")
            print("4- Ejercicio Nº11.11: Metodo SOR")
            print("Metodo SOR con relajacion 0.95")
            metodoSOR(3, [[-3, 1, -12], [6, -1, -1], [6, 9, 1]], [50, 3, 40], np.zeros(3), 0.95, 1e-3, 100)
            print("Metodo SOR sin relajacion")
            metodoSOR(3, [[-3, 1, -12], [6, -1, -1], [6, 9, 1]], [50, 3, 40], np.zeros(3), 0, 1e-3, 100)
            atras()
        elif numeroDeMetodo==5:
            os.system("CLS")
            print("5- Ejercicio Nº11.12: Metodo SOR")
            print("Metodo SOR con relajacion 1.2")
            metodoSOR(3, [[2, -6, -1], [-3, -1, 7], [-8, 1, -2]], [-38, -34, -20], np.zeros(3), 1.2, 1e-3, 100)
            print("Metodo SOR sin relajacion")
            metodoSOR(3, [[2, -6, -1], [-3, -1, 7], [-8, 1, -2]], [-38, -34, -20], np.zeros(3), 0, 1e-3, 100)
            atras()
        elif numeroDeMetodo==6:
            os.system("CLS")
            print("6- Ejercicio Nº1.e: Metodo de Potencia Inversa(Tres primeras Iteraciones)")
            metodoPIn(4, np.array([[5., -2., -1/2., 3/2.], [-2., 5., 3/2., -1/2.], [-1/2., 3/2., 5., -2.], [3/2., -1/2., -2., 5.]]), np.array([1., 1., 0., -3.]), 1e-3, 3)
            atras()
        elif numeroDeMetodo==7:
            os.system("CLS")
            print("7- Ejercicio Nº3.f: Metodo de Potencia Inversa(Tres primeras Iteraciones)")
            metodoPIn(4, np.array([[5., -2., -1/2., 3/2.], [-2., 5., 3/2., -1/2.], [-1/2., 3/2., 5., -2.], [3/2., -1/2., -2., 5.]]), np.array([1., 1., 0., -3.]), 1e-3, 3)
            atras()
        else:
            quit()
    



def atras():
    input(">> Presione una tecla para volver al menu <<")
    menu()

#Metodo SOR
def metodoSOR(ordenM, datosM, terminoIndepM, vectorIncognitas, relajacion, tolerancia, maxIteraciones):
    error = 100000        
    x = np.copy(vectorIncognitas)       #Vector auxiliar del vector inicial de incognitas
    contIt = 0                 
    error1 = [0]

    while error > tolerancia:
        if(contIt > maxIteraciones):
            print(' --- ERROR//ITERACIONES SUPERADAS//ERROR---                        ')
            break
        print("Iteración: ", contIt)
        for i in range(ordenM):
            sumatoria = 0
            for j in range(ordenM):
                if i != j:
                    sumatoria += (datosM[i][j] * vectorIncognitas[j])
            vectorIncognitas[i] = (relajacion * ((terminoIndepM[i] - sumatoria) / datosM[i][i])) + (1 - relajacion) * vectorIncognitas[i]
            print("x(",i,"): ", vectorIncognitas[i])
        error = np.linalg.norm(vectorIncognitas - x)      
        error1.append(error)                
        x = np.copy(vectorIncognitas)                    
        print("  ERROR: ", error1[contIt])
        contIt += 1

#Metodo Potencia Inversa
def metodoPIn(ordenM, datosM, autoVector, tolerancia, maxIteraciones):
    arrayAitken = []  
    matrizIdentidad = np.eye(ordenM)     

    #Muestra por pantalla los valores
    print("{0:^3} - {1:^37} - {2:^12} - {3:^12}".format('i', 'AutoVector', 'AutoValor', 'Aitken'))


    k = 0
    q = np.dot(autoVector, np.dot(datosM, autoVector)) / np.dot(autoVector, autoVector)
    p = find_p(autoVector)
    error = 1
    autoVector = autoVector / autoVector[p]
    while error > tolerancia:
        if(k > maxIteraciones):
            print(' --- ERROR//ITERACIONES SUPERADAS//ERROR---                        ')
            break
        y = np.linalg.solve(datosM - q * matrizIdentidad, autoVector)       
        μ = y[p]      
        p = find_p(y)     
        error = np.linalg.norm(autoVector - y / y[p],  np.inf)
        autoVector = y / y[p]
        μ = (1 / μ) + q 
        #Acelerdor de Aitken.
        if(len(arrayAitken)>1):
            #se calcula el aitken y se guarda el autovalor en el array de aitken
            aitkenResult = Aitken(arrayAitken[-2], arrayAitken[-1], μ)
            print(f"{k:03d} - [{autoVector[0]: 9.8f} {autoVector[1]: 9.8f} {autoVector[2]: 9.8f}] - {μ: >12.8f} - {aitkenResult: >12.8f}")
            arrayAitken.clear()
        else:
            #se guarda el autovalor en el array de aitken
            arrayAitken.append(μ)
            print(f"{k:03d} - [{autoVector[0]: 9.8f} {autoVector[1]: 9.8f} {autoVector[2]: 9.8f}] - {μ: >12.8f} - " + ' '*12 +  "")
        k += 1

def find_p(x):
    #Se calcula P
    return np.argwhere(np.isclose(np.abs(x), np.linalg.norm(x, np.inf))).min()

#Metodo Aitken

def Aitken(p0, p1, p2):
    return p0-((p1-p0)**2)/(p2-2*p1+p0)

menu()