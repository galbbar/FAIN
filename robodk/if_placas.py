
# You can also use the new version of the API:
from robodk import robolink    # RoboDK API
from robodk import robomath    # Robot toolbox
RDK = robolink.Robolink()

# Forward and backwards compatible use of the RoboDK API:
# Remove these 2 lines to follow python programming guidelines
from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox
# Link to RoboDK

import crear_placas as creador

# Notify user:

cont = RDK.getParam('cont_placa', str_type=True)
# Program example:


if cont == 0 :
    creador.create()
