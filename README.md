# Guardians of the Ancient Kingdom

## 1- Descripción del proyecto

Guardians of the Ancient Kingdom es un sistema de combate por turnos desarrollado en Python, que simula combates entre tres clases de guardianes del reino de Eldoria: Los Guerreros, Los Magos y Los Arqueros.

El proyecto resuleve la necesidad de automatizar los combates, donde cada personaje tiene atributos comunes como nombre, vida, ataque y defensa, pero cada tipo de personaje cuenta con una habilidad especial que modifica la forma en que realiza sus ataques, por ende, el sistema administra automanticamente los turnos, calcula el daño causado y actualiza la vida de los personajes y determina el resultado de la batalla, por lo tanto, se puede decir que el sistema controla de forma segura las reglas que rigen el orden de los combates entre los personajes de las tres ordenes del reino.


## 2- Estructura del repositorio

El proyecto está compuesto por tres archivos principales:
**personajes.py:**Contiene toda la implementación del sistema, en esta encontraremos la clase base abstracta "Personaje" y las siguientes sub clases:
- Personaje
- Guerrero
- Mago
- Arquero
- Combate
Además, contiene la lógica del combate, los métodos, las validaciones y las reglas de funcionamiento.

**main.py:**Es el archivo encargado de ejecutar el programa, en este archivo se crean los personajes, se realizan enfrentamientos y se ejecutan los casos de prueba solicitados para verificar el correcto funcionamiento del sistema.

**README.md:**Este contiene la documentación del proyecto, explicando la organización del programa y la aplicación de los conceptos de Programación Orientada a Objetos.

## 3- Clases 

**Personaje:**Es la clase abstracta del sistema y representa las características comunes de todos los personajes, esta se encarga de almacenar los atributos de los personajes como:
- Nombre
- Vida
- Ataque
- Defensa

Además, proporciona los metodos para recibir daño, verificar si el personaje sigue vivo y mostrar su estado actual, por otra parte, también incluye el método abstracto atacar(), que obliga a las clases hijas a implementar su propia forma de ataque.

**Guerrero:** Representa a un guerrero que se especializa en combate fisico, este cuenta con una habilidad especial que es un Golpe Poderozo, que aumenta su ataque en 20% antes de descontar la defensa del enemigo.

**Mago:** Representa a un mago que se especializa en hechizos penetrantes, este cuanta con una habilidad especial que ignora la defensa del oponente.

**Arquero:** Representa a un personaje que se especializa en ataques a distancia tiene una habilidad especial que dispara un disparo critico que duplica el daño cuando su ataque supera la defensa del oponente.

**Combate:** Es la clase que se encarga de administrar los combates entre los personajes, este controla:
- Los turnos.
- Los ataques.
- La verificación del ganador.
- Los empates.
- La finalización del combate.

## 4- Relaciones entre clases

**Herencia:** Esta se aplica porque los tres tipos de pesonajes, Guerreros, Magos y Arqueros son tipos especificos de personaje, por lo tanto, debido a esta relacion se reutilizan atributos y metodos comunes sin necesidad de repetir el codigo

**Asociación:** Esta ocurre cuando un personaje interactua con otro durante un ataque, por ejemplo, que un personaje ataque a otro guerrero.atacar(mago).

**Agregación:**Esta se utiliza en la clase combate, debido a que un combate recibe personajes ya creados previamente y una ves que estos esten en batalla y esta se de por finalizada, los personajes pueden reguir existiendo, por lo tanto, esta relacion corresponderia a una agregacion

## 5- Conceptos de Programación Orientada a Objetos

**Abstracción:**Esta se aplica mediante la clase abstracta Personaje, esta clase define las caracteriticas y comportamientos que deben tener todos los personajes sin especificar exactamente como atacan, delegando esta tarea a la subclases

**Encapsulamiento:** se aplica en atributos y propiedades usando getter y setters, permitiendo que se controlen y validen los datos antes de modificarlos.

**Herencia:**Se utiliza cuando las clases Guerrero, Mago y Arquero heredan de Personaje, gracias a esto se reutilizan características comunes y se evita la necesidad de duplicar partes del codigo.

**Polimorfismo:** Esta se aplica mediante el metodo atacar(), cada personaje implementa el metodo de modo diferente.

## 6- Lógica del combate y reglas del daño

El sistema desarrolla el combate por turnos, durante cada turno ocurre lo siguiente:
1. Se identifica el atacante y el defensor.
2. El atacante ejecuta su método atacar().
3. Se calcula el daño correspondiente.
4. El defensor recibe el daño mediante recibir_danio().
5. Se actualiza la vida del defensor.
6. Se muestra el estado de ambos participantes.
7. Se verifica si existe un ganador.

**Daño del Guerrero:** Daño = max(0, ataque × 1.20 − defensa)

**Daño del Mago:**Daño = ataque (Ignora la defensa del enemigo).

**Daño del Arquero:**
Daño base = ataque − defensa
Daño final = daño base × 2 (se aplica si supera la defensa del enemigo)
**Empates:**El combate finaliza en empate cuando:
- Ninguno de los personajes consigue causar daño durante una ronda completa.
- Se alcanzan 50 rondas sin que exista un ganador.

## 7- Ejecución

Para ejecutar el proyecto se debe tener Python instalado en el equipo.

Pasos para ejecutar el programa:

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el archivo principal:

```bash
python main.py
```

El programa ejecutará el combate principal y posteriormente mostrará todos los casos de prueba.

## 8- Pruebas realizadas

Se realizaron los siguientes casos de prueba:

1. Creación correcta de Guerrero, Mago y Arquero.
2. Validación de vida superior a 100.
3. Validación de vida negativa.
4. Validación de nombres vacíos.
5. Validación de ataques inválidos.
6. Validación de defensas inválidas.
7. Comprobación de la habilidad especial del Guerrero.
8. Comprobación del ataque del Mago ignorando defensa.
9. Comprobación del disparo crítico del Arquero.
10. Verificación de que la vida nunca sea negativa.
11. Verificación de que un personaje derrotado no pueda atacar.
12. Ejecución completa de un combate e identificación del ganador.
13. Comprobación del empate técnico cuando ninguno de los participantes puede causar daño.

Los resultados obtenidos fueron los esperados, demostrando que las validaciones, habilidades especiales y reglas del combate funcionan correctamente.