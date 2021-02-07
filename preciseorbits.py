# Read, store and plot precise RINEX satellites position
# Author: Maninder Gill
# Date Created: Jan 17 2021
# Date modified: Feb 07 2021

import re

from correctiontime import CorrectionTime
from satelliteposition import SatXYZ
from satelliteposition import SatellitePosition


class Sp3Reader:

    def __init__(self, file_name, satellitePosition):
        satellitePosition['G'] = []; satellitePosition['C'] = []; satellitePosition['R'] = []
        satellitePosition['E'] = []; satellitePosition['J'] = []

        self.readandstore(file_name, satellitePosition)

    def readandstore(self,file_name,satellitePosition):
        ft = open(file_name, "r")
        for col in (raw.strip().split() for raw in ft):
            if col != []:
                if col[0] == '*':
                    my_Time = CorrectionTime(col[4], col[5], col[6])
                    continue

            if re.search("[P]", col[0][0]):
                my_satXYZ = SatXYZ(col[1], col[2], col[3])
                my_SatellitePosition = SatellitePosition(my_Time, col[0][2:4], my_satXYZ)
                satellitePosition[col[0][1]].append(my_SatellitePosition)
                continue

