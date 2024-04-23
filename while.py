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

verifpassw()


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
      
   
comecena()
    