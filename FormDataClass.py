class FormData(object):
    def __init__(self, filename, startT, endT, heightTh, hCheck, eCheck, wEqField, wEqForest,
                 forestCoef, fieldCoef, sCoef, nCoef, wCoef, eCoef, pCoef):
        self.file = filename
        self.sTime = startT
        self.eTime = endT
        self.hThresh = heightTh
        self.heightTh = heightTh
        self.hCheck = hCheck
        self.eCheck = eCheck
        self.wEqField = wEqField
        self.wEqForest = wEqForest
        self.forestCoef = forestCoef
        self.fieldCoef = fieldCoef
        self.sCoef = sCoef
        self.nCoef = nCoef
        self.wCoef = wCoef
        self.eCoef =  eCoef
        self.pCoef = pCoef