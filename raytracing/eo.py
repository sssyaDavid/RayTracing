from .specialtylenses import *

class PN_33_921(AchromatDoubletLens):
    """PN_33_921

    .. csv-table::
        :header: Parameter, value

        "fa", "100.0"
        "fb", "78.32"
        "R1", "64.67"
        "R2", "-64.67"
        "R3", "-343.59"
        "tc1", "26.0"
        "tc2", "12.7"
        "te", "24.66"
        "n1", "1.6700"
        "n2", "1.8467"
        "diameter", "75"

    """
    def __init__(self):
        # PN for Part number
        super(PN_33_921,self).__init__(fa=100.00,fb=78.32, R1=64.67,R2=-64.67, R3=-343.59, 
                                    tc1=26.00, tc2=12.7, te=24.66, n1=1.6700, n2=1.8467, diameter=75,
                                    label="EO #33-921",
                                    url="https://www.edmundoptics.com/p/75mm-dia-x-100mm-fl-vis-0-coated-achromatic-lens/3374/")

class PN_33_922(AchromatDoubletLens):
    """PN_33_922

    .. csv-table::
        :header: Parameter, value

        "fa", "150.0"
        "fb", "126.46"
        "R1", "92.05"
        "R2", "-72.85"
        "R3", "-305.87"
        "tc1", "23.2"
        "tc2", "23.1"
        "te", "36.01"
        "n1", "0.5876"
        "n2", "0.5876"
        "diameter", "75"

    """
    def __init__(self):
        # PN for Part number
        super(PN_33_922,self).__init__(fa=150.00,fb=126.46, R1=92.05,R2=-72.85, R3=-305.87, 
                                    tc1=23.2, tc2=23.1, te=36.01, n1=N_BAK1.n(0.5876), n2=N_SF8.n(0.5876), diameter=75,
                                    label="EO #33-922",
                                    url="https://www.edmundoptics.com/p/75mm-dia-x-150mm-fl-vis-0-coated-achromatic-lens/3376/")

class PN_88_593(AchromatDoubletLens):
    """PN_88_593

    .. csv-table::
        :header: Parameter, value

        "fa", "200.0"
        "fb", "187.69"
        "R1", "118.81"
        "R2", "-96.37"
        "R3", "-288.97"
        "tc1", "17.94"
        "tc2", "6.00"
        "te", "15.42"
        "n1", "1.5168"
        "n2", "1.6727"
        "diameter", "75"

    """
    def __init__(self):
        super(PN_88_593,self).__init__(fa=200.00,fb=187.69, R1=118.81, R2=-96.37, R3=-288.97, 
                                    tc1=17.94, tc2=6.00, te=15.42, n1=1.5168, n2=1.6727, diameter=75,
									label="EO #88-593",
                                    url="https://www.edmundoptics.com/p/75mm-dia-x-200mm-fl-vis-0deg-coated-achromatic-lens/30844/")

class PN_85_877(AchromatDoubletLens):
    """PN_85_877

    .. csv-table::
        :header: Parameter, value

        "fa", "-10.0"
        "fb", "-11.92"
        "R1", "-6.55"
        "R2", "-5.10"
        "R3", "89.10"
        "tc1", "1.0"
        "tc2", "2.5"
        "te", "4.2"
        "n1", "0.5876"
        "n2", "0.5876"
        "diameter", "6.25"

    """
    def __init__(self):
        super(PN_85_877,self).__init__(fa=-10.0,fb=-11.92, R1=-6.55, R2=5.10, R3=89.10, 
                                    tc1=1.0, tc2=2.5, te=4.2, n1=N_BAF10.n(0.5876), n2=N_SF10.n(0.5876), diameter=6.25,
                                    label="EO #85-877",
                                    url="https://www.edmundoptics.com/p/625mm-dia-x10mm-fl-vis-nir-coated-negative-achromatic-lens/28478/")

class PN_49_389(AchromatDoubletLens):
    """PN_49_389

    .. csv-table::
        :header: Parameter, value

        "fa", "75.0"
        "fb", "61.17"
        "R1", "51.88"
        "R2", "-32.79"
        "R3", "-309.45"
        "tc1", "20.0"
        "tc2", "4.5"
        "te", "17.07"
        "n1", "0.5876"
        "n2", "0.5876"
        "diameter", "50.00"

    """
    def __init__(self):
        super(PN_49_389,self).__init__(fa=75.0,fb=61.17, R1=51.88, R2=-32.79, R3=-309.45, 
                                    tc1=20.0, tc2=4.5, te=17.07, mat1=N_BAF10, mat2=N_SF10, wavelengthRef=0.5876, diameter=50.0,
                                    label="EO #49-389",
                                    url="https://www.edmundoptics.com/p/50mm-dia-x-75mm-fl-vis-nir-coated-achromatic-lens/9821/")

class PN_15_195(SingletLens):
    """PN_15_195

    .. csv-table::
        :header: Parameter, value

        "fa", "24.0"
        "fb", "14.73"
        "R1", "12.51"
        "R2", "inf"
        "tc", "14.0"
        "te", "3.21"
        "n1", "1.52"
        "mat", "liba2000+"
        "diameter", "30.00"
        "wavelengthRef", "0.5876"

    """
    def __init__(self):
        super(PN_15_195,self). __init__(f=24.0, fb=14.73, R1=12.51, R2=float("+inf"), 
                 tc=14.10, te=3.21, n=1.52, diameter=30.0, mat=None, wavelengthRef=0.5876,
                 url="https://www.edmundoptics.com/p/30mm-dia-x-24mm-fl-mgfsub2sub-coated-molded-aspheric-condenser-lens/43076/",
                 label='EO #15-195', wavelength=None)
