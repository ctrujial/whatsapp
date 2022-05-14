import  pywhatkit as pwk
from flask import Flask, request

numCelular = input("Digite el número de celular+57 con indicativo del pais (+57--------------------): ")
#id_grupo = input("Digite el id del grupo: ")
mensaje = input("Digite ahora el  mensaje: ")
hora = int(input("Digite la hora: "))
minuto = int(input("Digite el minuto: "))
#tiempodeespera = int(input("Digite el tiempo de espera: "))
#segundosCierre = int(input("Digite los segundos de cierre: "))


cerrar=input("\nDesea cerrar la ventana de Whatsapp? : s / n ") 

if  cerrar == "s":      
    pwk.sendwhatmsg(numCelular,mensaje,hora,minuto,True,5)  
    #pwk.sendwhatmsg_to_group(id_grupo,mensaje,hora,minuto,True,5)
      
else : 
    pwk.sendwhatmsg(numCelular,mensaje,hora,minuto,False,5)   
    #pwk.sendwhatmsg_to_group(id_grupo,mensaje,hora,minuto,False,5)







