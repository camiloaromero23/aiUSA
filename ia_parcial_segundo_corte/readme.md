# ia-parcial_segundo_corte

## Installing dependencies

[//]:#[Google](google.com)
Take into account this is are instructions for Ubuntu

``` console
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-tk
sudo pip3 install pipenv
pipenv install
```

---

To avoid messing up the OS, run all files using the pipenv shell:

``` console
pipenv shell
```

---

## To Do

1. [x] Sudoku 6x6 hill climbing
   - [x] Steepest hill climbing
   - [x] Stochastic hill climbing
   - [x] First choice
   - [x] Random restart
2. [x] Sudoku 6x6 simulated annealing
   - [x] 3 Diferentes funciones de temperatura. Variar parámetros de temperatura inicial y factor de enfriamiento
   - [x] Función diferente la distribución de Boltzmann para la función de probabilidad aceptación.
   - [x] Grafique y analice cada uno de los versiones desarrolladas (Por ej. ¿No iter vs costo) ¿cuál es mejor? ¿por qué?
3. [x] Triqui mini max
4. [x] Triqui mini max poda alfa beta
   - [x] Compare el rendimiento entre los dos algoritmos de Mini Max con y sin poda, en varias ejecuciones y presente una gráfica
