from matplotlib import pyplot as plt 

#Creacion de la grafica de lineas

inventario = [10,14,8,12,20],
ventas = [6,8,4,12,9],
plt.plot(inventario,ventas, color="pink", marker="o", linestyle="solid"),
plt.title("Comparacion de inventario/ventas"),
plt.ylabel("Ventas")
plt.show()