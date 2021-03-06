

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

fA = open('ave_A.dat', 'r')
fB = open('ave_B.dat', 'r')
fC = open('sub_A.dat', 'r')
fD = open('sub_B.dat', 'r')

linesA = fA.readlines()
fA.close()
linesB = fB.readlines()
fB.close()
linesC = fC.readlines()
fC.close()
linesD = fD.readlines()
fD.close()

xA = []
xB = []
xC = []
xD = []

for line in linesA:
    pA = line.split()
    xA.append(pA)

for line in linesB:
    pB = line.split()
    xB.append(pB)
for line in linesC:
    pC = line.split()
    xC.append(pC)

for line in linesD:
    pD = line.split()
    xD.append(pD)

xAv = np.array(xA)
xBv = np.array(xB)
xCv = np.array(xC)
xDv = np.array(xD)

y = range(len(xA))
yv = np.array(y)

gs = gridspec.GridSpec(11, 1)
fig = plt.figure()

ax1 = plt.subplot(gs[0:7,:])
ax1.plot(y,xAv,y,xBv)
ax1.set_xlabel('Generations')
ax1.set_ylabel('Objective Fitness')
ax1.set_ylim([0,100])
ax1.set_xlim([0,600])

ax2 = plt.subplot(gs[8,:])
ax2.plot(y,xCv)
ax2.set_ylabel('Subj A')
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_ylim([-20, int(max(xCv)[0])*4])

ax3 = plt.subplot(gs[10,:])
ax3.plot(y,xDv)
ax3.set_ylabel('Subj B')
ax3.set_xticks([])
ax3.set_yticks([])
ax3.set_ylim([-20, int(max(xDv)[0])*4])

plt.show()

