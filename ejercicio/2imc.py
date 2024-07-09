peso=int(input("cuanto pesa?"))
mide=float(input("cuanto mide?"))
resul= peso / (mide*mide)

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
    