from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
from InstruccionesPL.TablaSimbolosPL.ArbolPL import Cuadruplo

class CreateOrReplacePL(InstruccionPL):
    def __init__(self, id , parametros, retornos,declare, begin, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id = id
        self.parametros = parametros
        self.retornos = retornos
        self.begin = begin
        self.declare = declare

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        ret = ''
        arbol.declararDiccionario(self.id)

        arbol.setDefEtiqueta(self.id)

        if self.parametros != None:
            for par in self.parametros:
                par.traducir(tabla, arbol)
                
        ret += 'def {0}():\n'.format(self.id)
        arbol.add3D(['def {0}():\n'.format(self.id)])
        arbol.agregarGeneral(0,'Metodo', self.id, '')
        
        if self.retornos !=None:
            for rets in self.retornos:
                rets.traducir(tabla, arbol)
                #Definir el modelo de return variable a regresar aqui se obtiene el tipo de variable pero no se define su ID
        if self.declare != None:
            for declas in self.declare:
                declas.traducir(tabla, arbol)
                
        if self.begin != None:
            for begs in self.begin:
                if type(begs) == list:
                    for beg in begs:
                        beg.traducir(tabla, arbol)
                else:
                    begs.traducir(tabla, arbol)
        
        #print(ret)
        # 
        # def -> no se puede ingresar a tripletas solo se podria ingresar ID de la funcion
        # por lo tanto la tripleta quedaria indice          Tripleta
        #                                      (0)          () 
        # lista actual -> 5 elementos 
        # enviamos la listatermporal -> llenado que se van en momento -> se generaron 11 elementos 
        #lista actual-> ()('op', op1, indice 11)-> agregar a la actual
        # recorremos la termporal
        #agregamos todos los elementos de la temporal
        # segunda opcion
        # mandar las lista

        '''

        (op,op1,op2, resultado )
        resultado = iD o una etiqueta tn
        '''