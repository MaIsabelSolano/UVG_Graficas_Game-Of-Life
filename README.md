# UVG_Graficas_Game-Of-Life
Univeridad del Valle de Guatemala <br>
Facultad de Ingeniería <br>
Departamento de Ciencias de la Computación <br>
Graficas por computador <br>

## Objetivos
Practicar los conceptos aprendidos sobre renderizado en tiempo real

## Sobre el laboratorio
El [archivo Game.py](https://github.com/MaIsabelSolano/UVG_Graficas_Game-Of-Life/blob/master/Game.py) contiene la programación del algorítmo de Conway's Game of Life, el cual es " un autómata celular diseñado por el matemático británico John Horton Conway en 1970. Es un juego de cero jugadores, en el que su evolución es determinada por un estado inicial, sin requerir intervención adicional. Se considera un sistema Turing completo que puede simular cualquier otra Máquina de Turing " (*fragmento obtenido de wikipedia*)

Este juego consiste en 4 reglas:
1. Cualquier célula viva con menos de 2 células vecinas vivas, muere por subpoblación
2. Cualquier célula viva con 2 o 3 células vecinas vivas, vive a la siguiente generación
3. Cualquier célula viva con más de 3 células vecinas vivas, muere por sobrepoblación
4. Cualquier célula muerta con exactamente 3 célula vecinas vivas, cambia a estar viva como si fuera por reproducción

## Capturas de pantalla
400px x 400px Life: <br>
![life1](https://user-images.githubusercontent.com/60373842/203758773-181d2c49-cec2-4a81-800a-a42d517e5846.png)

Entrada para la primera generación en el archivo: <br>
![life_firstgen](https://user-images.githubusercontent.com/60373842/203759259-a73fe8ac-f3e5-4f05-93fe-29c322129dfa.png)

## Tecnologías
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Referencias
Juego de la vida. (2022, 7 de noviembre). Wikipedia, La enciclopedia libre. Fecha de consulta: 10:10, noviembre 24, 2022 desde https://es.wikipedia.org/w/index.php?title=Juego_de_la_vida&oldid=147158850.
Wikipedia contributors. (2022, November 18). Conway's Game of Life. In Wikipedia, The Free Encyclopedia. Retrieved 10:11, November 24, 2022, from https://en.wikipedia.org/w/index.php?title=Conway%27s_Game_of_Life&oldid=1122604694
