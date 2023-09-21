calcular_subtotal=lambda precio, cantidad : precio *cantidad
calcular_descuento=lambda  cantidad , subtotal : 0.19* subtotal if cantidad >10 else 0
calcular_iva=lambda subtotal: 0.10 *subtotal
calcular_total=lambda subtotal, descuento ,iva: subtotal- descuento+ iva

#corrremos el programa

producto=input(("digite el nombre del producto :"))
precio= int (input(("digite el precio por unidad : ")))
cantidad= int (input(("digite la cantidad de productos a comprar :")))

subtotal= calcular_subtotal (precio ,cantidad) 
descuento=calcular_descuento (cantidad, subtotal)
iva= calcular_iva (subtotal)
total=calcular_total (subtotal, descuento, iva)

print (f'producto: {producto}')
print(f'subtotal :{subtotal}')
print(f'cantidad :{cantidad}')
print(f'descuento : {descuento}')
print(f'iva : {iva}')
print(f'Total {total}')
    
 # el  ejercicio constaba de usar el lambda para crear o calcular el subtotal el descuento junto con el iva y el total 
 #sobre un producto el descuento y el iva era a merce de elegirlo
 