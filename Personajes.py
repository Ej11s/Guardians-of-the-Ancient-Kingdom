from abc import ABC, abstractmethod
from math import floor

class Personaje(ABC):
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("el nombre no puede estar vacio")
        self._nombre = valor
        
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, valor):
        if not isinstance(valor, int):
            raise TypeError("la vida debe ser un numero entero")
        if valor < 0 or valor > 100:
            raise ValueError("la vida debe estar entre 0 y 100")
        self._vida = valor
        
    @property
    def ataque(self):
        return self._ataque
    
    @ataque.setter
    def ataque(self, valor):
        if not isinstance(valor, int):
            raise TypeError("el ataque debe ser un numero entero")
        if valor <= 0:
            raise ValueError("el ataque debe ser positivo")
        self._ataque = valor
        
    @property
    def defensa(self):
        return self._defensa
    
    @defensa.setter
    def defensa(self, valor):
        if not isinstance(valor, int):
            raise TypeError("la defensa debe ser un numero entero")
        if valor < 0:
            raise ValueError("la defensa no puede ser negativa")
        self._defensa = valor
        
    def recibir_danio(self, cantidad):
        if cantidad < 0:
            raise ValueError("el daño no puede ser negativo")
        
        vida_anterior = self.vida
        self._vida = max(0, self.vida - cantidad)
        return vida_anterior - self.vida
    
    def esta_vivo(self):
        return self.vida > 0
    
    def mostrar_estado(self):
        print(
            f"Nombre: {self.nombre} | Vida: {self.vida} | "
            f"Ataque: {self.ataque} | Defensa: {self.defensa}"
        )
        
    @abstractmethod
    def atacar(self, objetivo):
        pass

class Guerrero(Personaje):
    def atacar(self, objetivo):
        if not isinstance(objetivo, Personaje):
            raise TypeError("objetivo invalido")
        
        if not self.esta_vivo():
            raise ValueError(
                f"{self.nombre} esta derrotado"
            )
            
        if not objetivo.esta_vivo():
            raise ValueError(" ya fue derrotado no se puede atacar")
        
        ataque_potenciado = floor(self.ataque * 1.20)
        dano = max(0, ataque_potenciado - objetivo.defensa)
        return objetivo.recibir_danio(dano)
    
class Mago(Personaje):
    def atacar(self, objetivo):
        if not isinstance(objetivo, Personaje):
            raise TypeError("objetivo invalido")
        
        if not self.esta_vivo():
            raise ValueError(
                f"{self.nombre} esta derrotado"
            )
            
        if not objetivo.esta_vivo():
            raise ValueError(" ya fue derrotado no se puede atacar")
        
        dano = self.ataque
        return objetivo.recibir_danio(dano)
    
class Arquero(Personaje):
    def atacar(self, objetivo):
        if not isinstance(objetivo, Personaje):
            raise TypeError("objetivo invalido")
        
        if not self.esta_vivo():
            raise ValueError(
                f"{self.nombre} esta derrotado"
            )
            
        if not objetivo.esta_vivo():
            raise ValueError(" ya fue derrotado no se puede atacar")
        
        if self.ataque > objetivo.defensa:
            dano_base = (self.ataque - objetivo.defensa)
            dano = dano_base * 2
        else:
            dano = 0
            
        return objetivo.recibir_danio(dano)
    
class Combate:
    def __init__(self, personaje1, personaje2):
        if not isinstance(personaje1, Personaje):
            raise TypeError("el primer participante es invalido, este debe ser un objeto de tipo Personaje")
        
        if not isinstance(personaje2, Personaje):
            raise TypeError("el segundo participante es invalido, este debe ser un objeto de tipo Personaje")
        
        
        self.personaje1 = personaje1
        self.personaje2 = personaje2
        
        self.turno_actual = personaje1
        self.ganador = None
        
    def cambiar_turno(self):
        if self.turno_actual == self.personaje1:
            self.turno_actual = self.personaje2
        else:
            self.turno_actual = self.personaje1
    
    def verificar_ganador(self):
        if not self.personaje1.esta_vivo():
            self.ganador = self.personaje2
        elif not self.personaje2.esta_vivo():
            self.ganador = self.personaje1
        
        return self.ganador
    
    def mostrar_resultado(self):
        if self.ganador:
            print(f"el ganador es: {self.ganador.nombre}")
        else:
            print("empate")
            
    def iniciar(self):
        
        ronda = 1
        
        while ronda <= 50:
            
            dano_ronda = 0
            
            for _ in range(2):
                atacante = self.turno_actual
                
                if atacante == self.personaje1:
                    defensor = self.personaje2
                else:
                    defensor = self.personaje1
                
                dano = atacante.atacar(defensor)
                dano_ronda += dano
                
                print(
                    f"ronda {ronda}: {atacante.nombre} ataca a {defensor.nombre} "
                    f"y causa {dano} de daño, vida restante de {defensor.nombre}: {defensor.vida}"
                )
                
                self.personaje1.mostrar_estado()
                self.personaje2.mostrar_estado()
                
                if self.verificar_ganador():
                    self.mostrar_resultado()
                    return
                
                self.cambiar_turno()
                
            if dano_ronda == 0:
                print(" empate tecnico")
                return
            
            ronda += 1
            
        print("limite de rondas alcanzado, el combate termina en empate")
        
        
