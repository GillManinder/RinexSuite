# Read, store and plot precise satellite clock and orbits
# Author: Maninder Gill
# Date Created: Feb 07 2021
# Date modified: Feb 07 2021

import matplotlib.pyplot as plt
import os
import matplotlib.cm as cm
import matplotlib.colors as colors

from preciseclock import ClockReader
from preciseorbits import Sp3Reader

clk_file = 'com18823.clk'
sp3_file = 'com18823.sp3'

clockBias = {}
satellitePosition ={}

ClockReader(clk_file,clockBias)
Sp3Reader(sp3_file,satellitePosition)


# Plot clock corrections
# for key in clockBias.keys():
#     for sat in range(1, 32):
#         ind = []
#         for i, j, in enumerate(clockBias[key]):
#             if j.GetPrn() == sat:
#                 ind.append(i)  # This stores the index of the satellite
#
#         satClock=[]; time=[]
#         for index in ind:
#             satClock.append(clockBias[key][index].GetBias())
#             time.append(clockBias[key][index].GetTime())
#
#         plt.plot(time, satClock, '.')
#         plt.grid(True)
#         plt.xlabel('Decimal Hour')
#         plt.ylabel('Satellite clock [m]')
#         plt.legend(["PRN: " + str(key)+ str(sat)])
#         plt.show()



#------------------PLOTTING--------------------------
for key in satellitePosition.keys():
    for sat in range(1, 5):
        ind = []
        for i, j, in enumerate(satellitePosition[key]):
            if j.GetPrn() == sat:
                ind.append(i)

        satX=[]; satY=[]; satZ=[]; time=[]
        for index in ind:
            satX.append(satellitePosition[key][index].GetXYZ().GetX())
            satY.append(satellitePosition[key][index].GetXYZ().GetY())
            satZ.append(satellitePosition[key][index].GetXYZ().GetZ())
            time.append(satellitePosition[key][index].GetTime().GetDecimalHour())


        plt.plot(time, satX, '.', label="X")
        plt.plot(time, satY, '.', label="Y")
        plt.plot(time, satZ, '.', label="Z")
        plt.grid(True)
        plt.xlabel('Decimal Hour')
        plt.ylabel('Satellite position [km]')
        plt.title( str(key)+ str(sat))
        os.mkdirs('orbit_plots')
        plt.legend()
        plt.close('all')