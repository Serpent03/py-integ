import csv

import numpy as np
import matplotlib.pyplot as plt

#! Without Gravity
ax = [0.0]
ay = [0.0]
az = [0.0]

vx = [0.0]
vy = [0.0]
vz = [0.0]

px = [0.0]
py = [0.0]
pz = [0.0]

timeStamp = []

with open('filesdata.csv', 'r') as f:
    iterCount = 0
    csvData = csv.reader(f)
    for lines in csvData:
        iterCount += 1
        if iterCount > 2:
            ax.append(float(lines[0]))
            ay.append(float(lines[1]))
            az.append(float(lines[2]))
            timeStamp.append(float(lines[3]))
    f.close()

def integrator(ax, ay, az, ts):
    #* V(t) = V(t-1) + A*Δt
    #* P(t) = P(t-1) + V*Δt + 0.5*A*Δt^2

    global vx, vy, vz
    global px, py, pz

    for i in range(1, len(ts)):
        delta = (ts[i] - ts[i-1]) / 1000
        print(delta)
        vx.append(vx[-1] + (ax[i] * delta)) 
        vy.append(vy[-1] + (ay[i] * delta)) 
        vz.append(vz[-1] + (az[i] * delta)) 

        px.append(px[-1] + vx[-1] * delta + (0.5 * ax[i] * delta)) 
        py.append(py[-1] + vy[-1] * delta + (0.5 * ay[i] * delta)) 
        pz.append(pz[-1] + vz[-1] * delta + (0.5 * az[i] * delta))

integrator(ax, ay, az, timeStamp)

print(px)
print(py)
print(pz)


ax = plt.axes(projection='3d')
ax.plot3D(px, py, pz, 'gray')

ax.scatter3D(px[0], py[0], pz[0], color='green')
ax.text(px[0], py[0], pz[0], "START", color='green')
ax.scatter3D(px[-1], py[-1], pz[-1], color='red')

ax.set_xlim(-1.8, 1.8)
ax.set_ylim(-1.8, 1.8)
ax.set_zlim(-1.8, 1.8)

ax.set_title('Android IMU')
plt.show()

