# Type help("robodk.robolink") or help("robodk.robomath") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/robodk.html
# Note: It is not required to keep a copy of this file, your Python script is saved with your RDK project
from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox
# Link to RoboDK
    
RDK = Robolink()


def create():
    



    #Este es el objeto que vamos a crear dinámicamente
    botella=RDK.Item('placa')
    #Este es el sistema de referencia en el que meteremos el elemento copiado
    padre=RDK.Item('mesa')
    place=RDK.Item('placas')


    for i in range(6):
        for j in range(3):
            # Aquí va tu lógica
            #Copiamos el objeto
            botella.Copy()
            #Pegamos el objeto
            botella_copia=RDK.Paste()
            #Lo metemos en el sistema de referencia donde estarán todos los objetos
            botella_copia.setParent(padre)

            #Cambiamos la posición del elemento copiado haciendo una traslación que corresponde
            #en el eje X a el número de veces que hemos hecho avanzar ya la cinta
            botella_copia.setPose(transl(80 + (i*70),0 + (j*140),10))
            botella_copia.setParentStatic(place)

            #hacemos visible el objeto nuevo
            botella_copia.setVisible(1)

            pass
        
    RDK.setParam('table_width', 0)
    RDK.setParam('table_length', 0)
    RDK.setParam('cont_placa', 18)
