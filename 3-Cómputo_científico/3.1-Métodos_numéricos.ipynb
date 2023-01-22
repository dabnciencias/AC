{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "47de2803",
   "metadata": {},
   "source": [
    "# Métodos numéricos\n",
    "\n",
    "En muchas ramas de la ciencia existen problemas cuya solución _se asume_ que es una función **continua**, por ejemplo:\n",
    "* modelación de fuerzas naturales que dependen del tiempo en Física,\n",
    "* modelación de poblaciones en Biología,\n",
    "* ecuaciones diferenciales ordinarias y parciales en matemáticas.\n",
    "\n",
    "En efecto, la teoría de ecuaciones diferenciales es más sensata cuando busca condiciones bajo las cuales la solución de una ecuación sea una función **continua** (y, más aún, **única**). Por la _suposición_ de que muchos problemas en Física y Biología _deben tener_ soluciones que sean funciones continuas y únicas es que dichos problemas se modelan usando ecuaciones diferenciales, e inclusive algunos problemas para los cuales esto no aplica (por ejemplo, modelado de poblaciones, las cuales son discretas y cambian de forma discontinua) son más fáciles de aproximar si cambiamos nuestro enfoque y los modelamos con funciones continuas.\n",
    "\n",
    "Este tipo de suposiciones son comunes debido a que la continuidad es un requerimiento mínimo para tener un comportamiento predecible, pues las funciones discontinuas pueden tener \"saltos\" aleatorios que, por ejemplo, **no se ajusten** a un conjunto de datos experimentales; además, pedir que la solución sea una función _continua_ acota enormemente la cantidad de soluciones que se ajustan a un conjunto de datos experimentales.\n",
    "\n",
    "La mayoría de los problemas conocidos de este tipo _no tienen soluciones analíticas_; esto es, sus soluciones **no** se pueden describir a través de reglas de correspondencia usando funciones polinomiales, exponenciales, trigonométricas, etcétera, por lo que hoy en día existe una rama de las matemáticas dedicada a aprovechar las capacidades de cálculo de las computadoras para _aproximar_ soluciones para este tipo de problemas y estudiar los métodos con los que se obtienen dichas aproximaciones. Dado que el error numérico **inherente** a los sistemas de punto flotante vuelve prácticamente imposible la tarea de encontrar una función _única_, se desecha esta suposición.\n",
    "\n",
    "La rama de las matemáticas que se enfoca en problemas relacionados con funciones continuas es el **análisis matemático** (e incluye el cálculo diferencial e integral), por lo que el estudio de algoritmos que dan soluciones aproximadas a problemas de análisis matemático se conoce como **análisis numérico**, y a estos algoritmos se les conoce como **métodos numéricos**."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "42ad2a19",
   "metadata": {},
   "source": [
    "## Estabilidad\n",
    "\n",
    "El estudio de diferentes métodos numéricos lleva a que estos sean caracterizados de varias maneras bajo las cuales podamos compararlos. Un primer criterio de comparación es considerar la _forma_ en que el resultado es modificado cuando hacemos cambios \"pequeños\" en los datos de entrada.\n",
    "\n",
    "En Física, a los cambios \"pequeños\" les llamamos _perturbaciones_ y solemos modelarlos con una $\\varepsilon>0$ que suponemos lo \"suficientemente pequeña\" para el problema tratado, expresando la solución al sistema perturbado en términos de $\\varepsilon$. Sin embargo, dado que en Computación hemos visto que existe un error **inherente** a la mayoría de los cálculos numéricos, el cual se propaga al hacer operaciones, podemos comparar métodos numéricos en términos de cómo evoluciona su error.\n",
    "\n",
    "Sean $E_0>0$ un error introducido en alguna etapa de los cálculos de un método numérico y $E_n$ la magnitud del error después de $n$ operaciones.\n",
    "* Si $E_n\\approx (Cn)E_0$, con $C>0$ una constante independiente de $n$, decimos que el error evoluciona de forma **lineal**.\n",
    "* Si $E_n\\approx (C^n)E_0$, con $C>1$ una constante independiente de $n$, decimos que el error evoluciona de forma **exponencial**.\n",
    "\n",
    "Un método numérico es **estable** si su error evoluciona de forma **lineal**, lo cual generalmente produce resultados aceptables. Por otro lado, un método numérico es **inestable** si su error evoluciona de forma **exponencial** pues, independientemente de $E_0$ y $n$, suele producir errores inaceptabes. En la práctica, casi todos los métodos numéricos caen dentro de una de estas dos categorías."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "98682289",
   "metadata": {},
   "source": [
    "## Convergencia\n",
    "\n",
    "### Dependencia de la maquinaria\n",
    "\n",
    "Ingenuamente, podemos pensar que otro criterio para comparar métodos numéricos podría ser el _tiempo_ que tardan en obtener un resultado a partir de que fueron ejecutados. El principal problema con querer medir el _tiempo_ de ejecución para hacer comparaciones es que esta cantidad puede variar enormemente de computadora a computadora dependiendo, por ejemplo, de la velocidad del procesador o la capacidad de memoria. Más aún, puede variar a los largo de ejecuciones distintas en una **misma computadora** dependiendo de la cantidad de procesos que esté ejecutando el procesador o la cantidad de memoria disponible para la computadora al momento de ejecutar el método.\n",
    "\n",
    "Por ello, resulta más útil buscar un criterio que sea lo más independiente posible de la maquinaria que ejecutará las instrucciones. Un primer acercamiento sería comparar dos métodos diferentes por la cantidad de veces que cada uno ejecuta ciertas _instrucciones específicas_, por ejemplo:\n",
    "* cuántas sumas, restas, multiplicaciones, divisiones y potenciaciones ejecuta cada método,\n",
    "* cuántas declaraciones condicionales ejecuta cada método,\n",
    "* cuántas iteraciones de ciclos `for`/`while` ejecuta cada método, o\n",
    "* cuántas asignaciones de variables ejecuta cada método.\n",
    "\n",
    "Dado que resulta complicado llevar la cuenta de _todas_ las instrucciones que ejecutan diferentes métodos numéricos, se acostumbra dar una aproximación enfocándonos en el tipo de instrucción más relevante para un conjunto de métodos numéricos específicos.\n",
    "\n",
    "### Dependencia de la entrada\n",
    "\n",
    "La idea anterior suena bien, pero hay otro punto importante que no hemos considerado aún. Generalmente, los métodos numéricos requieren un valor de entrada, y la cantidad de veces que un método numérico _tendrá_ que ejecutar asignaciones de variables, iteraciones de ciclos, declaraciones condicionales, etc. **dependerá de dicho valor de entrada**. Además, como vimos en el _notebook_ [`1.2-Sistemas_numéricos_de_punto_flotante_y_error_numérico.ipynb`](../1-Estructura_básica_de_la_programación/1.2-Sistemas_numéricos_de_punto_flotante_y_error_numérico.ipynb), **las computadoras tardan más tiempo en procesar números representados con más _bits_**.\n",
    "\n",
    "Por esto es que, en la práctica, después de haber elegido el tipo de instrucción preponderante para un conjunto de métodos numéricos específicos, se hacer una gráfica de la cantidad de veces que dicha instrucción se ejecuta en función del valor de entrada para cada método. Después, se le ajustan a dichas gráficas funciones polinomial o logarítmicas, y se considera que dichas funciones caracterizan la **tasa de convergencia** de cada método; en el caso particular de los polinomios, se suele considerar sólo a la mayor potencia del polinomio, pues es el término dominante en el límite cuando $n$ crece arbitrariamente. Un ejemplo de este proceso se muestra en el video enlistado en la sección de **Recursos complementarios**."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "53c9b95a",
   "metadata": {},
   "source": [
    "**Nota** En este _notebook_, hemos discutido la variabilidad existente al momento de ejecutar un método numérico. Para comparar dos métodos numéricos de la forma más \"honesta\" posible, se suelen tomar como puntos de comparación a los _peores escenarios posibles_ para cada método; es decir que se comparan, por ejemplo, las **máximas cotas de error** de cada método en vez de buscar una medida de \"error promedio\" o algo similar."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "01a7ec8a",
   "metadata": {},
   "source": [
    "## Recursos complementarios\n",
    "* Sección \"1.3 Algorithms and Convergence\" de Burden, Faires y Burden, _Numerical Analysis_ (2016).\n",
    "* Video [What Is Big O Notation?](https://www.youtube.com/watch?v=Q_1M2JaijjQ) del canal de YouTube [Reducible](https://www.youtube.com/c/Reducible)."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Julia 1.8.4",
   "language": "julia",
   "name": "julia-1.8"
  },
  "language_info": {
   "file_extension": ".jl",
   "mimetype": "application/julia",
   "name": "julia",
   "version": "1.8.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
