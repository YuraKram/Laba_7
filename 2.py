import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scp


arr = np.genfromtxt('data1.csv', delimiter=';')
time = arr[1:, 0]
data1 = arr[1:, 3]
data2 = arr[1:, 17]

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(time, data1)
ax.plot(time, data2)
plt.title('Графики зависимостей положения дроссельной заслонки (%) и контрольной суммы ПЗУ (hех) от времени')
plt.xlabel('time (столбик 1)')
plt.ylabel('data')
plt.legend(('Положение дроссельной заслонки (%)', 'Контрольная сумма ПЗУ (hех)'))

fig2, ax2 = plt.subplots()
plt.title('График корреляции положения дроссельной заслонки (%)')
slope_1, intercept_1, r_1, p_1, stderr_1 = scp.linregress(time, data1)
line_1 = f'Regression line: y={intercept_1:.2f}+{slope_1:.2f}x, r={r_1:.2f}'
ax2.plot(time, data1, linewidth=0, marker='s', label='Data points')
ax2.plot(time, intercept_1 + slope_1 * time, label=line_1)
ax2.set_xlabel('time')
ax2.set_ylabel('data')
ax2.legend(facecolor='white')

fig3, ax3 = plt.subplots()
plt.title('Графики корреляции контрольной суммы ПЗУ (hех)')
slope_2, intercept_2, r_2, p_2, stderr_2 = scp.linregress(time, data2)
line = f'Regression line: y={intercept_2:.2f}+{slope_2:.2f}x, r={r_2:.2f}'
ax3.plot(time, data2, linewidth=0, marker='s', label='Data points')
ax3.plot(time, intercept_2 + slope_2 * time, label=line)
ax3.set_xlabel('time')
ax3.set_ylabel('data')
ax3.legend(facecolor='white')

plt.show()

