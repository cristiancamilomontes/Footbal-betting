#--------------inicio CLASES-----------------------------------

class aventura():
  empresa='NINTENDO'
  def recuerdo(self):
      print('nostalgia por haberlo jugado en la infancia')

class accion():
  empresa='SONY'
  def recuerdo(self):
      print('nostalgia porque mis hermanos fueron quienes los jugaron')

zelda=aventura()
metal_gear=accion()

#print('Zelda es un juego creado por',zelda.empresa)
#print('Metal Gear es un juego creado por',metal_gear.empresa)
#print('Las razones por la que me gustan estos juegos es:')
#print('Zelda por')
#zelda.recuerdo()
#print('Metal Gear por')
#metal_gear.recuerdo()

#-------------metodo constructor y metodo string------------------

class shooter():
    def __init__(self,empresa,consola):
        self.empresa=empresa
        self.consola=consola

    def __str__(self):
        return """\
                empresa perro: {}
                consola cabron: {}""".format(self.empresa, self.consola)

COD=shooter('MICROSOFT','XBOX-360')
#print('CALL OF DUTY es un juego de la empresa {} y es de la consola {}'.format(COD.empresa,COD.consola))
print('')
#print(COD)

#------------------Encapsulacion----------------------------------

class RPG():
    def __init__(self):
        #self.musica='Nobuo Uematsu'
        self.__virtud='La musica de los RPG es bella'
    def publico(self):
        return 'publico perros!!'
    def __privado(self):
        print ('prrrrivado cabrones')

    def get_virtud(self):
        return self.__virtud
    def set_cambiar_virtud(self):
        self.__virtud='lo hemos cambiado cabrones'

FFVII=RPG()
print(FFVII.publico())
print(FFVII._RPG__privado())
print(FFVII.get_virtud())
FFVII.set_cambiar_virtud()
print(FFVII.get_virtud())
#print(FFVII.musica)


print('')
print ('amor, tranquilo')


