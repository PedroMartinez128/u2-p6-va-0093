import matplotlib.pyplot as plt
import numpy as np
# Pedro Martinez NC 0093
cant_producto = [100,150,200,300,500]
precio = [4000,7000,9000,12000,18000]

plt.plot(cant_producto,precio)
plt.show()

## Personalizar grafico
plt.plot(cant_producto,precio,color="green",marker="o",linestyle="dashed",linewidth=2,markersize = 12)
plt.title("Ventas de walmart 0093")
plt.xlabel("cantidad de productos 0093")
plt.ylabel("precio 0093")


plt.show()