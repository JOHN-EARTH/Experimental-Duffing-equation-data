import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib.animation as animation
from scipy.fft import fft, ifft, fftfreq
from findiff import FinDiff

# Define the oscillator

G = 0.59
beta = 300
alpha = np.cbrt(beta*G)
print("alpha =", str(alpha), "; beta =", str(beta), "; G =", str(G))

x_osci = np.linspace(-0.295, 0.295, 500)
y_osci = (-alpha * x_osci**2)/2 + (beta * x_osci**4)/4

# Import and store data into lists

data_features = ['time', 'color', 'cx', 'cy']
data_pts = pd.DataFrame(data=None, columns=data_features, dtype=float)

data_pts = pd.read_csv("C:\path\Video.csv") #change for your path to the video

start_vid = 350  # Removes the first few points when the oscillator doesn’t move

ball_x = ((data_pts[data_pts['color'] == 'green']['cx']).to_numpy())[start_vid:]
ball_y = ((data_pts[data_pts['color'] == 'green']['cy']).to_numpy())[start_vid:]

ref_x = ((data_pts[data_pts['color'] == 'red']['cx']).to_numpy())[start_vid:]
ref_y = ((data_pts[data_pts['color'] == 'red']['cy']).to_numpy())[start_vid:]

time = ((data_pts[data_pts['color'] == 'red']['time']).to_numpy())[start_vid:] - (
        (data_pts[data_pts['color'] == 'red']['time']).to_numpy())[start_vid]


# Adjust the ball’s position to the oscillator’s frame of reference
# Position (x, y) = (0, 0) corresponds to the unstable equilibrium position
x = (ball_x - ref_x) / 0.136  # we divide by 0.166 to scale the system (0.166m being the position of the equilibrium)
y = (-ball_y + ref_y - 0.09) / 0.136  # 0.09 being the y distance between the origin of the axis and the red dot

# Plot positions as a function of time

plt.figure(1)
plt.scatter(time, ball_x, 0.5, color='green', label='Green ball')
plt.scatter(time, ref_x, 0.5, color='red', label='Reference')
plt.scatter(time, x, 0.5, color='black', label='Duffing oscillator')
plt.xlabel('Time (seconds)')
plt.ylabel('Horizontal position (units)')
plt.legend()
plt.grid()

plt.figure()
plt.scatter(time, ball_y, 0.5, color='green', label='green ball')
plt.scatter(time, ref_y, 0.5, color='red', label='reference point')
plt.scatter(time, y, 0.5, color='black', label='Duffing oscillator')
plt.xlabel('Time (seconds)')
plt.ylabel('Vertical position (units)')
plt.legend()
plt.grid()

# FOURIER TRANSFORM

def porte(x, lim_inf, lim_sup):
    return np.where((x >= lim_inf) & (x <= lim_sup), 1, 0)

fourier_x = fft(x)
fourier_y = fft(y)

N = len(x)  # Number of sample points
T = (time[1] - time[0])  # Sample spacing
xf = fftfreq(N, T)

plt.figure()
plt.plot(xf, 2.0/N * np.abs(fourier_x), color='c', linewidth=2, label="TF{x}")
plt.plot(xf, 2.0/N * np.abs(fourier_y), color='y', linewidth=2, label="TF{y}")
plt.title("Fourier Transform of the ball’s position")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.xlim(-10, 10)
plt.grid()
plt.legend()

# Low-pass filter to remove high frequencies
x_filtering = fourier_x * porte(xf, -6, 6)
y_filtering = fourier_y * porte(xf, -6, 6)

# Inverse fourier transform
x_filtered = np.real(ifft(x_filtering))  # abs to remove complex values
y_filtered = np.real(ifft(y_filtering))

# Removes the firsts and lasts values due to filtering errors at extremities
plot_lim = 10

# Plot position as a function of time (in the oscillator’s frame of reference)

plt.figure()
plt.scatter(time, x, 0.5, color='black', label='Position x')
plt.plot(time[plot_lim:-plot_lim], x_filtered[plot_lim:-plot_lim], color='#889fdb', linewidth=2, label='Data filtered')
plt.xlabel('Time (seconds)')
plt.ylabel('Horizontal position (units)')
plt.legend()
plt.grid()

plt.figure()
plt.scatter(time, y, 0.5, color='black', label='Position y')
plt.plot(time[plot_lim:-plot_lim], y_filtered[plot_lim:-plot_lim], color='#889fdb', linewidth=2, label='Data filtered')
plt.xlabel('Time (seconds)')
plt.ylabel('Vertical position (units)')
plt.legend()
plt.grid()

# Plot the ball’s position in the oscillator

plt.figure()
plt.plot(x_osci / 0.136, y_osci / 0.136, color='black')
plt.scatter(x, y, 0.5, color='black')
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(-0.295 / 0.136, 0.295 / 0.136)
plt.ylim(-0.075 / 0.136, 0.1 / 0.136)
plt.xlabel('Horizontal position (units)')
plt.ylabel('Vertical position (units)')
plt.grid()

# DERIVATION
# Deprecation of scipy derivation function => use of FinDiff (to be installed beforehand)

dt = time[1] - time[0]
d_dt = FinDiff(0, dt)

dx_dt = d_dt(x_filtered)
dy_dt = d_dt(y_filtered)

# Plot phase portraits

plt.figure()
plt.plot(x_filtered[plot_lim:-plot_lim], dx_dt[plot_lim:-plot_lim], color='black')
plt.xlabel('Position (units)')
plt.ylabel('Speed (units/seconds)')
plt.grid()

plt.figure()
plt.plot(y_filtered[plot_lim:-plot_lim], dy_dt[plot_lim:-plot_lim], color='black')
plt.xlabel('Position (units)')
plt.ylabel('Speed (units/seconds)')
plt.grid()

# ANIMATE

fig = plt.figure(layout="constrained", figsize=(6, 4.2))

# Position subplots on the figure
gs = GridSpec(3, 3, figure=fig)
axu = fig.add_subplot(gs[0, :-1])
axd = fig.add_subplot(gs[1:, :-1])
axr = fig.add_subplot(gs[:, 2])

# Set x(y) plot
axu.set(xlim=[-0.295, 0.295], ylim=[-0.075, 0.1], xlabel='Position x', ylabel='Position y')
axu.grid()
scat_u = axu.scatter(x_filtered[plot_lim:-plot_lim], y_filtered[plot_lim:-plot_lim], color="green", s=15)
line_u = axu.plot(x_osci[plot_lim:-plot_lim], y_osci[plot_lim:-plot_lim], color='black', linewidth=1.2)

# Set phase portrait plot
axd.set(xlim=[-0.24, 0.24], ylim=[-1.1, 1.1], xlabel='Position', ylabel='Speed')
axd.grid()
scat_d = axd.scatter(x[plot_lim:-plot_lim], dx_dt[plot_lim:-plot_lim], color="green", s=15)
line_d = axd.plot(x[plot_lim:-plot_lim], dx_dt[plot_lim:-plot_lim], color='black', linewidth=1.2)

# Set x(t) plot
axr.set(xlim=[-0.23, 0.23], ylim=[time[plot_lim], time[-plot_lim]], xlabel='Position', ylabel='Time')
axr.grid()
axr.yaxis.tick_right()
axr.yaxis.set_label_position("right")
scat_r = axr.scatter(x[plot_lim:-plot_lim], time[plot_lim:-plot_lim], color="green", s=15)
line_r = axr.plot(x[plot_lim:-plot_lim], time[plot_lim:-plot_lim], color='black', linewidth=1.2)

def animate(i):  # For each frame, update the data stored on each artist
    data_u = np.stack([x_filtered[plot_lim:-plot_lim][i], y_filtered[plot_lim:-plot_lim][i]]).T
    scat_u.set_offsets(data_u)

    data_d = np.stack([x[plot_lim:-plot_lim][i], dx_dt[plot_lim:-plot_lim][i]]).T
    scat_d.set_offsets(data_d)

    data_r = np.stack([x[plot_lim:-plot_lim][i], time[plot_lim:-plot_lim][i]]).T
    scat_r.set_offsets(data_r)

    return scat_r, scat_d, scat_u

ani = animation.FuncAnimation(fig, animate, interval=0.1, blit=False, frames=len(x[plot_lim:-plot_lim]))
ani.save(filename="./Video_RCG.gif", writer="pillow")

plt.show()
