global indice_masa_corporal 
while (True):
    peso = float(input("ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura enm metros: "))
    if (peso > 0 and altura > 0 ):
        indice_masa_corporal = peso / (altura ** 2) 
        break #Forza a terminar el ciclo while -> finaliza la estructura iterativa
print("El índice de masa corporal (IMC) es:", round(indice_masa_corporal, 2))
if 0 <= indice_masa_corporal and indice_masa_corporal < 18.5:
    print("Clasificación: BAJO PESO")
elif 18.5 <= indice_masa_corporal and indice_masa_corporal < 25: 
    print("Clasificación: PESO NORMAL")      
elif 25 <= indice_masa_corporal and indice_masa_corporal < 30:
    print("Clasificación: SOBREPESO") 
elif 30 <= indice_masa_corporal and indice_masa_corporal < 35:
    print("Clasificación: OBESIDAD GRADO I")
elif 35 <= indice_masa_corporal and indice_masa_corporal < 40:
    print("Clasificación: OBESIDAD GRADO II")
elif 40 <= indice_masa_corporal:    
    print("Clasificación: OBESIDAD GRADO III") 
else:
    print("Error: En el índice de masa corporal")       
