# Importando librerías
import numpy as np
import matplotlib.pyplot as plt

# Creando base de datos para su posterior graficación
horas_de_sueno = np.array([5.5, 6, 7.5, 8, 6.5, 9, 7])
rendimiento = np.array([4, 5, 8, 9, 6, 8, 7])
base_datos = np.column_stack((rendimiento, horas_de_sueno))

# Creación de la ventana de gráficos
fig, ax = plt.subplots()

# Título de la ventana
fig.canvas.manager.set_window_title("Mi gráfico de sueño y rendimiento")

# Título del gráfico
plt.title("Relación entre horas de sueño y rendimiento laboral", fontsize=14, fontweight="bold")

# Barra con configuración
plt.bar(rendimiento, horas_de_sueno, color="skyblue")

# Etiquetas
plt.ylabel("Horas de sueño", labelpad=30, rotation=0)
plt.xlabel("Rendimiento laboral (1-10)")
plt.xticks(rendimiento, rotation= 0)



# Ajuste de diseño
plt.subplots_adjust(left=0.2)

# Cuadrícula
plt.grid(True, linestyle="--", alpha=0.5)

# Mostrar gráfico
plt.show()