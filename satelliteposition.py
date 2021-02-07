class SatXYZ():

    def __init__(self, x,y,z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def GetX(self):
        return self.x

    def GetY(self):
        return self.y

    def GetZ(self):
        return self.z

class SatellitePosition():

    def __init__(self, Time, prn, SatXYZ):
        self.Time = Time
        self.prn = int(prn)
        self.SatXYZ = SatXYZ

    def GetPrn(self):
        return self.prn

    def GetXYZ(self):
        return self.SatXYZ

    def GetTime(self):
        return self.Time