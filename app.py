import numpy as np
import matplotlib.pyplot as plt

# Generate sample data with NumPy
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

print("NumPy version:", np.__version__)
print("Creating a sine curve with Matplotlib...")

# Create and save a plot
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Python + NumPy + Matplotlib in Docker")
plt.grid(True)
plt.savefig("sine_curve.png")

print("Done. Plot saved as sine_curve.png")
