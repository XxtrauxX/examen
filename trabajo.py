# test python 

# EJemplos datos del archivo 
# prueba 1

print( """
      
      
CODPROD;DESCPROD;UNIDAD DE VALOR
001;Arroz 5kg;20000
002;Aceite vegetal 1L;12000
003;Azúcar 1 kg;5500
004;Leche en polvo 500g;9500
005;Café molido 250g;15000 
      
      

      
      
      """)



#archivdat ={"nombre": "carlos_martinez","nombre": "ana_gomez", "nombre": "pedro_rodriguez", }
datosglob={}
print(" Ingrese los datos.dat a este software para generar informes ")
nom= input(" Ingrese el nombre de quien estara la factura\n ")
for i in range(2):
    datos={}
    codigo = int( input(" codigo? "))
    datos["descprod;"] = input("ingrese la descripcion del producto\n ")
    datos["unival;"] = int(input("Ingrese el valor del producto "))
    #datosglob[archivos] = datos
    datosglob[codigo] = datos
    
    #sum+=datos['unival;']
    
    #print(sum)
    
    
print(">" * 30)
print(f" La facura con no. resolucion 679 a nombre de {nom}")
for k in datosglob.keys():
    print("descprod;", datosglob[k]['descprod;'])
    print(f"unival ;  ${datosglob[k]['unival;']:,}")
    print("-" * 30), "\n"
    
    
    
    
    
    
    
    
    
    
    """""
          
          Ejemplo de datos del archivo:
CÓDIGO;NOMBRE;TELÉFONO
001;Carlos Martínez;3104567890
002;Ana Gómez;3201234567
003;Pedro Rodríguez;3159876543
004;Laura Pérez;3112345678
005;Jorge Ramírez;3123456789

          
          
      
                              """""

    dDatos={}
print(">" * 30)
for e in range (2):
    datos2={}
    codig2= int(input(" codigo del cliente:  "))
    nom2= input("Ingrese el nombre del cliente: \n")
    telefono= int(input("Ingrese el numero del cliente: \n"))
    
    
    dDatos[codig2] = datos2
for a in datosglob.keys():
    print("nombre;", datosglob[a]['nom2'])
    print(f"telefono;   {datosglob[a]['telefono']:,}")
    print(">", *30)
        
"""""""""""""""""
        CODFACT;AÑO;MES;DIA;CODCLI;CODPROD;UNIDADESPROD;VALOR;VALORFACT
001;2024;09;21;001;001;2;40000;66635
001;2024;09;21;001;003;3;16500;66635
002;2024;08;15;002;004;1;9500;25585
002;2024;08;15;002;002;1;12000;25585
003;2024;07;30;003;005;5;75000;89250
004;2024;09;10;004;003;4;22000;51135
004;2024;09;10;004;005;1;15000;51135
005;2024;06;25;005;001;1;20000;23800
006;2024;09;05;003;002;2;24000;35105
006;2024;09;05;003;004;1;9500;35105

    
        
    
    
    
    


                                                                                            """""""""""

print(">"*30)
for i in range(10):
    datos3={}
    codfact= int(input(" Ingrse el codigo de la factura:  "))
    año= int(input("Ingrese el año de la factura:  "))
    mes= int(input(" Ingrese el mes de la facura:   "))
    dia= int(input(" ingrese el dia de la factura:  "))
    codcli= int(input(" ingrese el codigo del cliente:  "))
    unidprod= int(input(" ingrese las unidades por producto:  "))
    valor= int(input(" ingrese el valor facturado:  "))
    
    datosglob[codfact] = datos3
    
    
    for j in datosglob.keys():
        print("codfact;", datosglob[j]['codfact'])
        print("año;", datosglob[j]['año'])
        
    
    
    
    
    
    



    
    


    
    






