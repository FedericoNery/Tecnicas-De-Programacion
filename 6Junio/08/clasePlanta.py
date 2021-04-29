class Planta:
    def __init__(self,alto,hojas):
        self.alto=alto
        self.hojas=hojas
    def crecer(self,sumar=1):
        self.alto=self.alto+sumar
    def crear_hoja(self):
        self.hojas=self.hojas+1

if __name__=='main':
    a=Planta(10,5)
    print("alto= ",a.alto)
    print("hojas= ",a.hojas)
    a.crecer()
    print("alto= ",a.alto)
    a.crecer(4)
    print("alto= ",a.alto)
    a.crear_hoja()
    print("hojas= ",a.hojas)


