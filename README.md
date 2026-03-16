# Bockathom 2026: Hero of the Hogar

## Descripción
"Hero of the Hogar" es una aventura conversacional y simulador en arte ASCII desarrollado exclusivamente para la Bockathom 2026. El jugador debe encarnar a un valiente compañero de piso y gestionar su energía para completar las tareas del hogar (poner la lavadora, fregar los platos, barrer el salón) y evitar que el caos domine la casa. ¡El simulador definitivo de supervivencia doméstica!

## Funcionamiento
El juego se basa en un sistema de gestión de recursos (energía) y exploración de entornos:
* **Navegación:** El jugador puede moverse libremente entre el Exterior, el Salón, la Cocina y el Lavadero.
* **Energía:** Comienzas con un 60% de vitalidad. Cada tarea doméstica consume puntos.
* **Descanso:** Si te quedas sin energía, fracasas en tu misión. Puedes sentarte en el sofá a ver el fútbol en el salón para recuperar fuerzas (+40 de energía).
* **Victoria:** Completa todas las tareas para ganar de forma normal. 

## Tecnologías Utilizadas
[cite_start]Cumpliendo con la libertad de stack tecnológico[cite: 18]:
* **Lenguaje:** Python 3.
* **Librerías:** `os` y `time` (Nativas del lenguaje, no requiere instalaciones adicionales).
* **Interfaz:** Consola/Terminal de comandos con renderizado de arte ASCII personalizado.

## Instrucciones de Instalación y Ejecución
[cite_start]Para probar la aplicación en tu máquina local[cite: 26]:
1. [cite_start]Clona o descarga los archivos de este repositorio público[cite: 23].
2. Asegúrate de tener Python 3 instalado en tu sistema.
3. Abre una terminal o consola de comandos en la carpeta del proyecto.
4. Ejecuta el juego usando el comando: `python juego_hogar.py` (o `python3 juego_hogar.py` dependiendo de tu sistema operativo).

## Licencia y Autoría
[cite_start]El proyecto es de código abierto (Open Source) y se distribuye bajo la licencia **MIT**[cite: 19]. 

---

## 🤫 EASTER EGG (Spoiler)
El juego cuenta con un final secreto y un objeto legendario oculto. Si eres parte del jurado y quieres encontrarlo por ti mismo, ¡no despliegues el siguiente texto!

<details>
<summary><b>Haz clic aquí para ver cómo desbloquear el Easter Egg (Manulleta Cósmica)</b></summary>
<br>
Para desbloquear la victoria secreta:
1. Entra a la casa y dirígete a la <b>Cocina</b>.
2. Selecciona la opción <b>"Fregar los platos"</b>.
3. Una vez frente al fregadero, ignora tu tarea y selecciona la opción <b>"Mirar a la izquierda"</b>.
4. Vuelve a seleccionar <b>"Mirar a la izquierda"</b> por segunda vez consecutiva.
5. Encontrarás la Manulleta oculta tras el escurreplatos. Al consumirla, obtendrás poderes cósmicos y la casa se limpiará sola, desbloqueando el final secreto.
</details>
