directorio_cliente = """nif;nombre;email;teléfono;descuento
\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5
\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8
\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2
\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"""

cliente = {}
datos = {}
datos_insertados = ""

buscado = directorio_cliente.find(";")
print(buscado)

for i in range(len(directorio_cliente)):
    if buscado:
        datos_insertados += directorio_cliente[i]
        
print (datos_insertados)
