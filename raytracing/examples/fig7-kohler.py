#

from raytracing import *

def exampleCode(comments=None):
    illumination = ImagingPath()
    illumination.design(fontScale=1.5)
    illumination.append(Space(d=20))
    illumination.append(Lens(f=10, diameter=25.4, label="Collector"))
    illumination.append(Space(d=30))
    illumination.append(Aperture(diameter=2, label="Field diaphragm"))
    illumination.append(Space(d=10+30))
    illumination.append(Lens(f=30, diameter=25.4, label="Condenser"))
    illumination.append(Space(d=30+30))
    illumination.append(Lens(f=30, diameter=25.4, label="Objective"))
    illumination.append(Space(d=30+30))
    illumination.append(Lens(f=30, diameter=25.4, label="Tube"))
    illumination.append(Space(d=30+30))
    illumination.append(Lens(f=30, diameter=25.4, label="Eyepiece"))
    illumination.append(Space(d=30+2))
    illumination.append(Lens(f=2, diameter=10, label="Eye Entrance"))
    illumination.append(Space(d=2))
    illumination.display(interactive=False, raysList=[
                           LampRays(diameter=1000, NA=500, N=200, T=600, z=66.666666, rayColors='r', label="Source"),
                           ObjectRays(diameter=2000, halfAngle=1000, H=200, T=200, z=120, rayColors='g', color='g', label="Sample")], removeBlocked=False)

if __name__ == "__main__":
    import envexamples
    exampleCode()