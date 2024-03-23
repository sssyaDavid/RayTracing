TITLE       = "Kohler illumination"
DESCRIPTION = """
"""

import envexamples
import time
from raytracing import *
from decimal import Decimal

def exampleCode():
    #start_time = time.time()
    
    path = ImagingPath()
    path.name = "Kohler illumination with 1 cm wide lamp and 0.5 NA"
    path.append(Space(d=40))
    path.append(Lens(f=40,diameter=25, label='Collector'))
    path.append(Space(d=40+25))
    path.append(Lens(f=25, diameter=75, label='Condenser'))
    path.append(Space(d=25))
    path.append(Space(d=9))
    path.append(Lens(f=9, diameter=8, label='Objective'))
    path.append(Space(d=9))
    path.showLabels=True
    #elapsed_original = time.time() - start_time
    #print(f"Elapsed time, original: {elapsed_original:.2f} s")
    print(path.fieldStop())
    print(path.fieldOfView())
    for i in range(3):
        ObjectRays(diameter=15000, H=8000, T=4000, halfAngle=1000)
	#path.saveFigure("Illumination.png", onlyPrincipalAndAxialRays=True, limitObjectToFieldOfView=True)

if __name__ == "__main__":
    exampleCode()
