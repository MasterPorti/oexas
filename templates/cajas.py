import matplotlib.pyplot as plt

# Datos de ejemplo: pesos de gemas en gramos
data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 100]  

# Crear el boxplot 
plt.boxplot(
    data, 
    patch_artist=True, 
    notch=True, 
    boxprops=dict(facecolor='pink', color='deeppink'),
    medianprops=dict(color='purple'),
    whiskerprops=dict(color='hotpink'),
    capprops=dict(color='hotpink'),
    flierprops=dict(marker='o', color='magenta', markersize=8)
)

plt.title('Distribución de Pesos de Gemas (Boxplot)')
plt.ylabel('Peso (gramos)')
plt.grid(axis='y', linestyle='--', alpha=0.7)  

# Mostrar el gráfico
plt.show()
