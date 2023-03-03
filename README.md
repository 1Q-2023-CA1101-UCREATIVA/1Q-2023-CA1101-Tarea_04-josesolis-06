# Tarea 04

## Ejercicio 01

### Descripción

Escribe una función que devuelva los puntos ganados en un solo lanzamiento de un juego de Dardos. La función se llama `puntaje` (recuerden la identación es muy importante).

Los dardos son un juego en el que los jugadores lanzan dardos a una diana.

En nuestro caso particular del juego, la diana recompensa con 4 cantidades diferentes de puntos, dependiendo de dónde caiga el dardo:

- Si el dardo cae fuera de la diana, el jugador no gana puntos (0 puntos).
- Si el dardo cae en el círculo exterior de la diana, el jugador gana 1 punto. Es decir, si $r$ está entre 5 abierto y 10 cerrado, o sea: 

    $5 < r <= 10$
- Si el dardo cae en el círculo central de la diana, el jugador gana 5 puntos. Es decir, si $r$ está entre 1 abierto y 5 cerrado, o sea: 

    $1 < r <= 5$
- Si el dardo cae en el círculo interior de la diana, el jugador gana 10 puntos. Es decir, si $r$ es menor o igual que 1, o sea: 

    $r <= 1$

¿A qué les suena esto? ¿Tendrá que ver algo con `if`, `elif`?

El círculo exterior tiene un radio de 10 unidades (esto equivale al radio total de toda la diana), el círculo central un radio de 5 unidades, y el círculo interior un radio de 1. Por supuesto, todos están centrados en el mismo punto (es decir, los círculos son concéntricos definidos por las coordenadas (0, 0)).

Escriba una función que dado un punto en la diana (definido por sus coordenadas cartesianas x e y, donde x e y son reales), devuelva la cantidad correcta ganada por un dardo que caiga en ese punto.

## Tips

### ¿Cómo determinar si un punto pertenece a una circunferencia?

Para determinar si un punto ($x$, $y$) pertenece a una circunferencia con centro ($a$, $b$) y radio $r$, se prueba que la distancia entre ($x$, $y$) y el centro ($a$, $b$) es:

$\sqrt{(x - a)^2 + (y - b)^2} = r$

Esta es la fórmula general para los puntos ($x$, $y$) que pertenecen a una circunferencia con centro ($a$, $b$) y radio $r$.

### ¿Cómo averiguar la raíz cuadrada en Python?

Vayan a este enlace: [Funciones matemáticas](https://docs.python.org/es/3/library/math.html#math.sqrt)


### Recomendaciones del profe

- Recuerden la identación.

- Usen la variable `puntos_ganados` para guardar el puntaje, ya sea: 0, 1, 5, 10...
