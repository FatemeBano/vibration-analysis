import numpy as np
import matplotlib.pyplot as plt
import random
import csv

# تولید داده‌ی جعلی ارتعاشی (موج سینوسی با نویز)
time = np.linspace(0, 2, 500)  # ۲ ثانیه
frequency = 5  # هرتز
signal = np.sin(2 * np.pi * frequency * time)
noise = [random.uniform(-0.2, 0.2) for _ in range(len(time))]
data = signal + noise

# رسم نمودار
plt.plot(time, data)
plt.title("داده‌ی ارتعاشی جعلی (شتاب)")
plt.xlabel("زمان (ثانیه)")
plt.ylabel("شتاب (m/s^2)")
plt.grid(True)


# ذخیره‌سازی داده در فایل CSV
with open('vibration_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['زمان (ثانیه)', 'شتاب (m/s^2)'])
    for t, d in zip(time, data):
        writer.writerow([t, d])

print("داده‌ها در فایل vibration_data.csv ذخیره شدند.")
plt.show()