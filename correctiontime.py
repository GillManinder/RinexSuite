class CorrectionTime():

    def __init__(self, hour,minute,second):
        self.hour = float(hour)
        self.minute= float(minute)
        self.second= float(second)
        self.decimalHour = int(hour) + float(minute) / 60.0 + float(second) / 3600.0

    def GetDecimalHour(self):
        return self.decimalHour
