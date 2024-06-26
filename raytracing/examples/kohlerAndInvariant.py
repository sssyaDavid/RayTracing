import envexamples

from raytracing import *

'''
DESCRIPTION
'''

#print("The Lagrange Invariant of this system is {}".format(illumination1.lagrangeInvariant()))

def displayMultiple(paths: list,
                    limitObjectToFieldOfView=False,
                    onlyPrincipalAndAxialRays=False,
                    removeBlockedRaysCompletely=False,
                    comments=None):
    fig, axes = plt.subplots(figsize=(10, 7))
    for path in paths:
        path.createRayTracePlot(axes=axes, limitObjectToFieldOfView=False,
                                onlyPrincipalAndAxialRays=False,
                                removeBlockedRaysCompletely=False)
    # can only def callbacks for only one path
    axes.callbacks.connect('ylim_changed', paths[0].updateDisplay)
    axes.set_ylim([-paths[0].displayRange(axes) / 2 * 1.5, paths[0].displayRange(axes) / 2 * 1.5])
    paths[0]._showPlot()


# Source with Kohler illumination 
illumination1 = ImagingPath()
illumination1.fanNumber = 20
illumination1.fanAngle = 0.5
illumination1.design(rayColors = ["r","r","r"])
illumination1.append(Space(d=5))
illumination1.append(Lens(f=5, diameter=50, label="Extra Lens 1"))
illumination1.append(Space(d=5))
illumination1.append(Lens(f=5, diameter=50, label="Extra Lens 2"))
illumination1.append(Space(d=5))
illumination1.append(Lens(f=5, diameter=50, label="Extra Lens 3"))
illumination1.append(Space(d=5))
illumination1.append(Lens(f=5, diameter=50, label="Extra Lens 4"))
illumination1.append(Space(d=10))
illumination1.append(Lens(f=10, diameter=100, label="Collector"))
illumination1.append(Space(d=10+30))
illumination1.append(Lens(f=30, diameter=100, label="Condenser"))
illumination1.append(Space(d=30+30))
illumination1.append(Lens(f=30, diameter=100, label="Objective"))
illumination1.append(Space(d=30+30))
illumination1.append(Lens(f=30, diameter=100, label="Tube"))
illumination1.append(Space(d=30+30))
illumination1.append(Lens(f=30, diameter=100, label="Eyepiece"))
illumination1.append(Space(d=30+2))
illumination1.append(Lens(f=2, diameter=10, label="Eye Entrance"))
illumination1.append(Space(d=2))
for i in range(200):
    illumination1.display()


#displayMultiple([illumination3, illumination1])
#displayMultiple([illumination3, illumination2])
