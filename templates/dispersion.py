from matplotlib import pyplot as plt 

#Creacion de grafica de dispersion.
entidad= ['CDMX','Hidalgo','Yucatan','EDOMEX','Los Cabos']
envios = [30,45,10,50,20]

plt.scatter(entidad, envios)
plt.title("Envios realizados a cada entidad")
plt.xlabel("# de envios")
plt.ylabel("Entidad que recibio el envio")
plt.show()