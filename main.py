from supermercado import Supermercado


super1=Supermercado("LiChi", "Baru 1954", )

super1.cargarCatalogo("Harina 000", 15, 1, 1)
super1.cargarCatalogo("Psitol de Agua", 5, 0, 0)

Total=super1.sumPrecio()
print(Total)
print("Evaluando")