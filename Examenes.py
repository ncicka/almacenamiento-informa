
class Pregunta:
    
    def __init__(self,texto,respuesta,dificultad=0):
        self.texto = texto
        self.respuesta = respuesta
        self.dificultad = dificultad
    
    def __eq__(self, otro):
        return self.texto == otro

    def __str__(self):
        return self.texto

class Enunciado:

    def __init__(self, nombre):
        self.nombre = nombre
        self.preguntas = []
    
    def agregarPregunta(self,preg):
        self.preguntas.append(preg)

    def obtenerPregunta(self,nro_pregunta):
        if nro_pregunta <= self.numeroPreguntas():
            return self.preguntas[nro_pregunta-1]
        return None
    
    def permutarPregunta(self,nro_pregunta, mover_a):
        c = nro_pregunta -1
        a = mover_a -1
        if c <= self.numeroPreguntas()-1 and a <= self.numeroPreguntas()-1:
            self.preguntas [c], self.preguntas[a] = self.preguntas [a], self.preguntas[c]
            return True
        return False
    
    def borrarPregunta(self,valor,nro=True):
        if nro:
            if valor <= self.numeroPreguntas():
                self.preguntas.pop(valor-1)
                return True
        else:
            if self.contienePregunta(valor):
                self.preguntas.remove(valor)
                return True
        return False

    def contienePregunta(self,textoPregunta):
        if textoPregunta in self.preguntas:
            return True
        return False
    
    def numeroPreguntas(self):
        return len(self.preguntas)
    
    def mostrarPreguntas(self):
        for i in range(self.numeroPreguntas()):
            print(f"{i+1}) {self.preguntas[i]}")

class Examen:
    def __init__(self, enunciado):
        self.enunciado = enunciado
        self.respuestas = dict(map(lambda x: (x+1,''), range(enunciado.numeroPreguntas())))

    def responder(self, nro_pregunta, respuesta):
        if nro_pregunta <=self.enunciado.numeroPreguntas():
            self.respuestas[nro_pregunta]= respuesta
            return True
        return False
    
    def mostrarRespuesta(self):
        print(self.respuestas)

if __name__ == '__main__':
    p1 = Pregunta("¿Que es una Tupla?", "A")
    p2 = Pregunta("¿Que tipo de lenguaje es Python?","B")
    p3 = Pregunta("¿Que es Pep 8?","C")

    e = Enunciado("Examen Python")
    e.agregarPregunta(p1)
    e.agregarPregunta(p2)
    e.agregarPregunta(p3)

    print(p1)
    print(p2)
    print(p3)
    #e.mostrarPreguntas()
    #e.borrarPregunta("¿Que es una Tupla?",nro=False)
    #e.mostrarPreguntas()
    print(e.obtenerPregunta(4))
    exa = Examen(e)

    exa.responder(1,"B")
    exa.responder(2,"B")
    exa.responder(3,"C")
    exa.responder(4,"C")
    exa.mostrarRespuesta()
    exa.responder(1,"A")
    exa.mostrarRespuesta()