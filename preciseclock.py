# Read and store precise precise satellites clock
# Author: Maninder Gill
# Date Created: Feb 07 2021
# Date modified: Feb 07 2021

import re

from SatelliteBias import SatelliteBias
from correctiontime import CorrectionTime


class ClockReader:

    def __init__(self,file_name,clockBias):
        clockBias['G'] = []; clockBias['C'] = []; clockBias['R'] = []
        clockBias['E'] = []; clockBias['J'] = []

        self.readandstore(file_name,clockBias)

    def readandstore(self,file_name,clockBias):
        ft = open(file_name, "r")

        for col in (raw.strip().split() for raw in ft):
            if col != []:
                if re.search("[GRECJ]+", col[1][0]) and col[0][0] == 'A':
                    if re.search("[0-9]+", col[1][1]):
                        my_Time = CorrectionTime(col[5], col[6], col[7])
                        my_satelliteBias = SatelliteBias(col[1][1:3], my_Time, col[9], col[10])
                        clockBias[col[1][0]].append(my_satelliteBias)



