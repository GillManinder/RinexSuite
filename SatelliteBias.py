speedOfLight = 299792458.0

class SatelliteBias():
    def __init__(self, prn, time, bias, accuracy):
        self.prn = int (prn)
        self.bias = float(bias) * speedOfLight
        self.accuracy = float(accuracy) * speedOfLight
        self.decimalHour = int(time.hour) + float(time.minute) / 60.0 + float(time.second) / 3600.0

    def GetPrn(self):
        return self.prn

    def GetBias(self):
        return self.bias

    def GetTime(self):
        return self.decimalHour