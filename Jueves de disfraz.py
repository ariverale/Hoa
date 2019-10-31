print ( " En este programa te vamos a pedir tu edad y  lo que estudias ")
contador = 0
# Proceso
while contador < 10:
      edad = int ( input ( " Dime que edad tienes "))
      contador += 1
      if edad < 10:
         persona = 10
         diez = (  edad + persona )
         print ( f" Las personas de menor a diez años son{diez }")
