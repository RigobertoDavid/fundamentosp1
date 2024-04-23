def primerwhile():
 text="" 

 while text !="hi":
    print("Ingrese el saludo correcto")
    text=input()
 print("Ese es el saludo correcto")

# primerwhile()

def verifpassw():
 passw=""
 cont=1
 print("Ingrese su password ")
 passw=input()
 while passw !="1234" and cont<3:
    print("Su password es incorrecta")
    cont=cont+1
    passw=input()
    if cont==3:
      print ("Usted ha bloqueado su contraseña")
    
 
 print("Bienvenido Usuario Admin")

#verifpassw()


#verifpassw()
#primerwhile()

###come la cena 

def comecena():
  cantcomida=100

  while cantcomida !=0:
    Print ("¿Desea comer?")
    cucharada=input()
    if cucharada=="si":
      cantcomida=cantcomida-25
      print("La cantidad de comida es", cantcomida)

    else:
      print("Usted ya dejó de comer")
      cantcomida=0
      
   
#comecena()






def cantmicro():
  cantmicros=int (0)
  hora = int(8)
  
  #las micros pasan solo hasta las 2
  #el usuario comienza a esperar a las 8
  #cada vez que dice que no, pasa una hora


while cantmicros !=int(3) and hora != (12):
  print("ha pasado una micro?")    
                                       
  respuesta=input()

  if respuesta==("si"):
    cantmicros=cantmicros+int(1)
    print ("la cantidad de micros que han pasado son", cantmicros)
    if cantmicros == int(3):
      print ("\")
    

   
 