# =======================================================
#                   Alfonso Kim Quezada
#                 Analisis de Algoritmos
#         ---------------------------------------
# Mucho codigo, pero es lo mas parecido al metodo 
# visto en clase.
# No use librerias de calculo numerico como numpy,  
# todo se calcula con listas de python normales
# =======================================================

# =======================================================
class Ecuacion():
    """ Modela una entrada de la tabla, no se me ocurrio un mejor nombre =(
    """

    # ---------------------------------------------------
    def __init__(self, coeficientes, igual):
        """ Crea la ecuacion.
            :param coeficientes: Una lista con los coeficientes de la ecuacion
            :param igual: El lado derecho o el resultado
        """
        self.coeficientes = [float(c) for c in coeficientes]
        self.igual = float(igual)

    # ---------------------------------------------------
    def __str__(self):
        """ Para generar el string de la ecuacion y poder imprimir la tabla
        """
        coefs = '%.3f\t' * len(self.coeficientes)
        return '%s=\t%.3f' % ((coefs % tuple([d for d in self.coeficientes]), self.igual))

    # ---------------------------------------------------
    def divide(self, num):
        """ Divide la ecuacion entre el numero dado
        """
        self.coeficientes = [(c / num) for c in self.coeficientes]
        self.igual = (self.igual / num)

    # ---------------------------------------------------
    def pivotear(self, otra, col_idx):
        """ Hace el pivoteo de una ecuacion con otra
            :param otra: La otra ecuacion a pivotear
            :col_idx El indice del coeficiente donde esta el pivote
        """
        self.igual = self.igual - (self.coeficientes[col_idx] * otra.igual)
        self.coeficientes = [coef - (self.coeficientes[col_idx] * otro_val) 
                             for coef, otro_val in zip(self.coeficientes, otra.coeficientes)]


# =======================================================
class Simplex():
    """ Ejecuta el algoritmo Simplex mediante listas de
        ecuaciones. 
    """

    # ---------------------------------------------------
    def __init__(self, objetivo):
        """ Crea Simplex con la funcion a maximizar
        """
        self.objetivo = objetivo
        self.restricciones = []
        self.iteraciones = 0
        self.listo = False

    # ---------------------------------------------------
    def __str__(self):
        """ Para imprimir la tabla a la consola
            La tabla debe de cerrarse para poder escribir la tabla
        """
        if not self.listo:
            raise Error('No se ha cerrado la tabla')
        eqs = list(self.restricciones)
        eqs.append('_'*50)
        eqs.append(self.objetivo)
        return '\n'.join([str(eq) for eq in eqs])

    # ---------------------------------------------------
    def add_restriccion(self, restriccion):
        """ Agrega una restriccion a la tabla
        """
        if self.listo:
            raise Error('La tabla esta cerrada')
            return
        self.restricciones.append(restriccion)

    # ---------------------------------------------------
    def cerrar(self):
        """ Este metodo esta feo, pero fue como me salio
            Al "cerrar" la tabla se agregan las variables de
            holgura a las restricciones y al objetivo. 
        """
        r = self.restricciones
        objetivos = []
        for i in range(len(r)):
            self.objetivo.coeficientes.append(0)
            objetivos.append(r[i].igual)
            for j in range(len(r)):
                r[i].coeficientes.append(0 if i != j else 1)
        self.objetivos = objetivos
        self.listo = True

    # ---------------------------------------------------
    def columna_pivote(self):
        """ Obtiene la columna pivote
        """
        min_c = min(self.objetivo.coeficientes)
        if min_c > 0: return -1 ## Ya acabamos
        return self.objetivo.coeficientes.index(min_c)

    # ---------------------------------------------------
    def columna(self, col_idx):
        """ Obtiene los coeficientes de una columna dada
            :param col_idx El indice de columna a buscar
        """
        return [coef.coeficientes[col_idx] for coef in self.restricciones]

    # ---------------------------------------------------
    def fila_pivote(self, col_pivote):
        """ Busca la fila a la que se va a pivotear
            :param col_pivote La columna con el pivote encontrado
        """
        valores = self.columna(col_pivote)
        return valores

    # ---------------------------------------------------
    def pivotear(self, fila, col_idx):
        """ Pivotea la tabla
            :param fila La fila pivote
            :param col_idx La columna pivote
        """
        fila_operacional = self.restricciones[fila] 
        fila_operacional.divide(fila_operacional.coeficientes[col_idx])
        for res_idx in range(len(self.restricciones)):
            if res_idx == fila: continue  # Ya esta transformada
            restriccion = self.restricciones[res_idx]
            restriccion.pivotear(fila_operacional, col_idx)
        self.objetivo.pivotear(fila_operacional, col_idx)

    # ---------------------------------------------------
    def resolver(self, debug=False):
        """ Resuelve el problema de maximizacion generado
            La tabla debe estar cerrada
            :param debug Bandera para escribir a consola el proceso
        """
        if not self.listo:
            raise Error('No se ha cerrado la tabla')
        if len(self.restricciones) == 0:
            raise Error('No se han insertado restricciones')
        iteracion = 0
        while not min(self.objetivo.coeficientes) >= 0:
            iteracion += 1
            col_pivote = self.columna_pivote()
            fila_pivote = self.fila_pivote(col_pivote)
            valores_pivote = [(i / f) if f != 0 else 9999999999 
                              for f, i in zip(fila_pivote, self.objetivos)]
            idx_val_salida = valores_pivote.index(min(valores_pivote))
            self.pivotear(idx_val_salida, col_pivote)
            if debug:
                print '--'*10 + ' iteracion %i ' % iteracion + '--'*10
                print self
            if iteracion > 1000:
                self.objetivo.igual = -1
                raise Error('Ups, algo salio mal. Parece que se ciclo')
        self.iteraciones = iteracion


# =======================================================
if __name__ == '__main__':
    """ Punto de entrada a la consola
    """
    s = Simplex(Ecuacion([-21, -31], 0))
    s.add_restriccion(Ecuacion([2, 3], 25))
    s.add_restriccion(Ecuacion([4, 1], 32))
    s.add_restriccion(Ecuacion([2, 9], 54))
    s.cerrar()
    print s
    print '---'*10 + ' solucion ' + '---'*10
    s.resolver(debug=True)
    print 'Maximo encontrado: %.3f en %i iteraciones' % (s.objetivo.igual, s.iteraciones)
    print '\n'*3
    
    s = Simplex(Ecuacion([-6, -5, -4], 0))
    s.add_restriccion(Ecuacion([2, 1, 1], 180))
    s.add_restriccion(Ecuacion([1, 3, 2], 300))
    s.add_restriccion(Ecuacion([2, 1, 2], 240))
    s.cerrar()
    print s
    print '---'*10 + ' solucion ' + '---'*10
    s.resolver()
    print s
    print 'Maximo encontrado: %.3f en %i iteracione' % (s.objetivo.igual, s.iteraciones)
    print '\n'*3

    s = Simplex(Ecuacion([-95, -85], 0))
    s.add_restriccion(Ecuacion([18, 19], 110))
    s.add_restriccion(Ecuacion([11, 10], 48))
    s.add_restriccion(Ecuacion([15, 14], 95))
    s.add_restriccion(Ecuacion([4, 0], 17))
    s.cerrar()
    print s
    print '---'*10 + ' solucion ' + '---'*10
    s.resolver()
    print s
    print 'Maximo encontrado: %.3f en %i iteracione' % (s.objetivo.igual, s.iteraciones)
    print '\n'*3
