import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# dy / dt = -y, y(0) = 1
# Analytical y(t) = exp(-t)

def deriv_kp(t, y):
   return -y + 27

def deriv_ki(t, y):
   return [y[1], 27-y[0]]

def deriv_kd(t, y):
   return 0

t = np.arange(0, 10, 0.001)
result_kp = solve_ivp(deriv_kp, (t[0], t[-1]), [32], t_eval=t)
result_ki = solve_ivp(deriv_ki, (t[0], t[-1]), [32, 0], t_eval=t)
result_kd = solve_ivp(deriv_kd, (t[0], t[-1]), [27/2], t_eval=t)

plt.axhline(y=27, xmin=0.0, xmax=10, color='r', label="Refrence line", linestyle='dashed')
plt.plot(result_kp.t, result_kp.y[0], label='Solution KP')
plt.plot(result_ki.t, result_ki.y[0], label='Solution KI')
plt.plot(result_kd.t, result_kd.y[0], label='Solution KD')

# Set the axis labels
plt.set_xlabel('Time')
plt.set_ylabel('Temperature')

plt.legend()
plt.show()

