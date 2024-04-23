error = iput("Introduzca un código de error:\n")

match error:
    case "1":
        print("todo ok")

    case "2":
     print("error interno del servidor")
       
     case _:
     print("error no definido")


   