from matplotlib import pyplot

piedras=('Zafiro','Esmeralda','Diamante','Rubi','Perla')
ventas=(6,12,20,4,8)
colores=('purple','pink','gold','silver','green')

pyplot.pie(ventas, colors=colores,labels=piedras)
pyplot.title("Piedras con mas ventas")
pyplot.show()