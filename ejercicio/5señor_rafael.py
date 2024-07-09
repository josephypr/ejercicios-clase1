ganso= "14%"
camisa= 35000
pantalon= 75000
celular= 900000
subtotal= pantalon + camisa
porcentaje= 14 / 100
descuento1= camisa * porcentaje
resultado1= camisa - descuento1
descuento2= pantalon * porcentaje
resultado2= pantalon - descuento2
total_ropa= resultado1 + resultado2
total_gastado= total_ropa + celular

print("subtotal", subtotal, "dolares")
print("descuento:" , ganso)
print("total gastado en la tienda COSTA AZUL", total_ropa, "dolares" )
print("total gastado en el dia:",total_gastado, "dolares")