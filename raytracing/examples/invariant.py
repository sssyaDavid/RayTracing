import envexamples
from raytracing import *

#path = ImagingPath()
#path.name = "4f system, 1 cm object, small lenses"
#path.append(Space(d=5000))
#path.append(Lens(f=5000, diameter=2500))
#path.append(Space(d=15000))
#path.append(Lens(f=10000,diameter=2500))
#path.append(Space(d=10000))
#path.display()
#path.saveFigure('object-smallLenses.png')

path = ImagingPath()
path.name = "4f system, 1 cm object, small and large lenses"
path.append(Space(d=5000))
path.append(Lens(f=5000, diameter=2500))
path.append(Space(d=1500))
path.append(Lens(f=1000,diameter=5000))
path.append(Space(d=10000))
for i in range(500):
    path.display()
path.saveFigure('object-smallLargeLenses.png')

#path = ImagingPath()
#path.name = "4f system, calculated field of view, small lenses"
#path.append(Space(d=5))
#path.append(Lens(f=5, diameter=2.5))
#path.append(Space(d=15))
#path.append(Lens(f=10,diameter=2.5))
#path.append(Space(d=10))
#path.display(onlyPrincipalAndAxialRays=True, limitObjectToFieldOfView=True)
#path.saveFigure('fov-smallLenses.png', onlyChiefAndMarginalRays=True, limitObjectToFieldOfView=True)

#path = ImagingPath()
#path.name = "4f system, improved field of view, small and large lenses"
#path.append(Space(d=5))
#path.append(Lens(f=5, diameter=2.5))
#path.append(Space(d=15))
#path.append(Lens(f=10,diameter=5.0))
#path.append(Space(d=10))
#path.display(onlyPrincipalAndAxialRays=True, limitObjectToFieldOfView=True)
#path.saveFigure('fov-smallLargeLenses.png', onlyChiefAndMarginalRays=True, limitObjectToFieldOfView=True)

#path = ImagingPath()
#path.name = "4f systeme, no change in field of view with large first lens"
#path.append(Space(d=5))
#path.append(Lens(f=5, diameter=5.0))
#path.append(Space(d=15))
#path.append(Lens(f=10,diameter=5.0))
#path.append(Space(d=10))
#path.display(onlyPrincipalAndAxialRays=True, limitObjectToFieldOfView=True)
#path.saveFigure('fov-largeLenses.png', onlyChiefAndMarginalRays=True, limitObjectToFieldOfView=True)
