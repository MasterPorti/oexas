import pandas as pd
import matplotlib as plt

#Crear histograma 
import matplotlib.pyplot as plt

data = [10, 15, 20, 25, 30, 35, 40, 45, 50]

plt.hist(data, bins=5, color='skyblue', edgecolor='black')


plt.title('Distribución de Pesos de Gemas')
plt.xlabel('Peso (gramos)')
plt.ylabel('Frecuencia')

# Mostrar el gráfico
plt.grid(axis='y', linestyle='--', alpha=0.7)  
plt.show()