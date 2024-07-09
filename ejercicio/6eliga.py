print("eliga:")
eliga=int(input("1(imc) 2(porcentaje grasa corporal) 3(tasa metabolia basal):"))
if eliga == 1: 
    peso=int(input("cuanto pesa?"))
    mide=float(input("cuanto mide?"))
    resul= peso / mide

    if resul <18.5:
        print("bajo de peso")
    elif resul > 18.5 or resul < 24.9:
        print(" adecuado")
    elif resul >30.0 or resul < 34.9:
        print("obesidad grado 1")
    elif resul > 35.0 or resul < 39.9:
        print(" obesidad grado 2 ")
    elif resul > 40:
        print(" obesidad grado 3")

elif eliga == 2:
    genero=int(input("1(masculino) 2(femenino)"))
    if genero == 1:
        edad=int(input("digite su edad"))
        peso=int(input("cuanto pesa?"))
        mide=float(input("cuanto mide?"))
        imc= peso / (mide*mide)
        
        porcentajeGC= 1.2 * imc + 0.23 * edad - 5.4 - 10.8
        
        print("su porcentaje de grasa corporal es: ",porcentajeGC)
    
    elif genero == 2:
        edad=int(input("digite su edad"))
        peso=int(input("cuanto pesa?"))
        mide=float(input("cuanto mide?"))
        imc= peso / (mide*mide)
        
        porcentajeGC= 1.2 * imc + 0.23 * edad - 5.4 - 0
        print("su porcentaje de grasa corporal es: ",porcentajeGC)

