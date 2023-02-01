{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "95b518e4",
   "metadata": {},
   "source": [
    "# Solución de sistemas lineales de ecuaciones algebráicas\n",
    "\n",
    "## Motivación\n",
    "\n",
    "Los sistemas lineales de ecuaciones algebráicas son útiles para modelar muchos problemas científicos tales como el balanceo de ecuaciones químicas, el cálculo de corrientes en circuitos electrónicos, además de tener muchísimas aplicaciones dentro de la computación y las mismas matemáticas. Por ello, es de gran utilidad saber cómo se pueden implementar métodos numéricos que resuelvan este tipo de sistemas."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bef591a1",
   "metadata": {},
   "source": [
    "## Sistemas lineales de ecuaciones algebráicas\n",
    "\n",
    "Un _sistema de ecuaciones_ es un grupo de ecuaciones que deben cumplirse simultáneamente. En general, podemos expresar un sistema de $m$ ecuaciones y $n$ incógnitas como\n",
    "\n",
    "$$f_1(x_1,x_2,\\dots,x_n) = 0,$$\n",
    "\n",
    "$$f_2(x_1,x_2,\\dots,x_n) = 0,$$\n",
    "\n",
    "$$\\vdots$$\n",
    "\n",
    "$$f_m(x_1,x_2,\\dots,x_n) = 0,$$\n",
    "\n",
    "donde $f_j$ es una función arbitraria, con $1\\leq j\\leq m$. Una _solución_ al sistema es una $n$-tupla de valores $(x_1,x_2,\\dots,x_n)$ para los cuales todas las ecuaciones del sistema se verifican. Un _sistema de ecuaciones algebráicas_ es aquel donde todas las funciones $f_j$ son **polinomios** en las variables $x_1,x_2,\\dots,x_n$; más aún, un sistema de este tipo es _lineal_ si en todas las ecuaciones del sistema las incógnitas $x_1,x_2,\\dots,x_n$ **no aparecen elevadas a una potencia mayor que uno** y **tampoco aparecen productos entre las diferentes incógnitas**.\n",
    "\n",
    "En este _notebook_ veremos un método para solucionar sistemas lineales de ecuaciones algebráicas de $n$ ecuaciones y $n$ variables, donde todas las ecuaciones son _linealmente independientes_. En general, este tipo de sistemas se pueden escribir de la siguiente forma (verifica que cumpla las definiciones anteriores):\n",
    "\n",
    "$$ a_{11}x_1 + a_{12}x_2 + \\dots + a_{1n}x_n = b_1, $$\n",
    "\n",
    "$$ a_{21}x_1 + a_{22}x_2 + \\dots + a_{2n}x_n = b_2, $$\n",
    "\n",
    "$$ \\vdots $$\n",
    "\n",
    "$$ a_{n1}x_1 + a_{n2}x_2 + \\dots + a_{nn}x_n = b_n. $$\n",
    "\n",
    "### Operaciones elementales\n",
    "\n",
    "Existen tres \"operaciones elementales\" que le podemos aplicar a este sistema **sin cambiar su conjunto de soluciones**:\n",
    "1. multiplicar una ecuación (de ambos lados) por una constante no nula;\n",
    "1. sumarle a una ecuación alguna de las otras ecuaciones multiplicada por una constante arbitraria;\n",
    "1. intercambiar dos ecuaciones de lugar.\n",
    "\n",
    "El hecho de que la operación 1 no cambie al conjunto de soluciones del sistema se sigue de que, para todo $1\\leq i\\leq n$, si $c\\neq0$, entonces\n",
    "\n",
    "$$c(a_{i1}x_1 + a_{i2}x_2 + \\dots + a_{in}x_n - b_i) = 0 \\iff a_{i1}x_1 + a_{i2}x_2 + \\dots + a_{in}x_n - b_i = 0.$$\n",
    "\n",
    "Similarmente, el hecho de que la operación 2 no cambie al conjunto de soluciones del _sistema_ se sigue de que, para cualesquiera $1\\leq i,j\\leq n$ y para cualquier constante arbitraria $c'$,\n",
    "\n",
    "\\begin{align}\n",
    "    (a_{i1}x_1 + a_{i2}x_2 + \\dots + a_{in}x_n - b_i) = 0 \\ &\\land \\ (a_{j1}x_1 + a_{j2}x_2 + \\dots + a_{jn}x_n - b_j) = 0 \\\\\n",
    "    &\\iff \\\\\n",
    "    (a_{i1}x_1 + a_{i2}x_2 + \\dots + a_{in}x_n - b_i) \\ &+ \\ c'(a_{j1}x_1 + a_{j2}x_2 + \\dots + a_{jn}x_n - b_j) = 0.\n",
    "\\end{align}\n",
    "\n",
    "En efecto: La primera implicación es directa, mientras que la otra se sigue de que las ecuaciones son linealmente dependientes. Por último, es claro por qué la operación 3 no cambia el conjunto de soluciones pues, después de aplicarla, las ecuaciones del sistema siguen siendo las mismas."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "507ffad4",
   "metadata": {},
   "source": [
    "## Método de eliminación Gaussiana\n",
    "\n",
    "A continuación, veremos un algoritmo que aprovecha las operaciones elementales descritas anteriormente para obtener una solución a un sistema lineal de ecuaciones algebráicas.\n",
    "\n",
    "### Retropropagación\n",
    "\n",
    "Supongamos que, a través de operaciones elementales, podemos transformar el sistema lineal de ecuaciones algebráicas anterior en uno de la forma\n",
    "\n",
    "\\begin{align*}\n",
    "    a'_{11}x_1 \\ + \\ a'_{12}x_2 \\ + \\dots + \\ a'_{1n-1}x_{n-1} \\ + \\ a'_{1n}x_n &= b'_1, \\\\\n",
    "    0 \\ + a'_{22}x_2 + \\dots + a'_{1n-1}x_{n-1} \\ + \\ a'_{1n}x_n &= b'_2, \\\\\n",
    "    & \\ \\vdots \\\\\n",
    "    0 + 0 + \\dots + a'_{n-1,n-1} x_{n-1} + a'_{n-1n}x_n &= b'_{n-1}, \\\\\n",
    "    0 \\ + \\ 0 \\ + \\ \\dots \\ + \\ \\ 0 \\ \\ + \\ \\ \\ a'_{nn}x_n &= b'_n,\n",
    "\\end{align*}\n",
    "\n",
    "con $a'_{ii}\\neq0$ para $1\\leq 1\\leq n$ (en la sección **Reducción** explicaremos por qué es posible lograr esto). Observemos que la última ecuación tiene sólo una incógnita, que podemos despejar para obtener\n",
    "\n",
    "$$x_n = \\frac{b'_n}{a'_{nn}}.$$\n",
    "\n",
    "**Ejercicio** Despeja a $x_{n-1}$ de la penúltima ecuación y sustituye en valor de $x_n$."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "27b76adf",
   "metadata": {},
   "source": [
    "_Escribe tu procedimiento aquí._"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2d2a55c4",
   "metadata": {},
   "source": [
    "Iterativamente, por cada ecuación que solucionamos, podemos sustituir todos los valores obtenidos hasta el momento en la ecuación _anterior_ para solucionarla también, hasta haber encontrado valores $(x_1,x_2,\\dots,x_n)$ que solucionen todo el sistema. A este procedimiento se le conoce como _retropropagación_.\n",
    "\n",
    "**Ejercicio** Da una fórmula general para el valor de $x_i$, con $1\\leq i<n$, en términos de los $x_j$ para $i < j \\leq n$."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "07ebfddf",
   "metadata": {},
   "source": [
    "_Escribe tu respuesta aquí._"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a0407b0e",
   "metadata": {},
   "source": [
    "**Nota** Lo que nos asegura que los coeficientes $a_{ii}$ con $1\\leq i\\leq n$ son distintos de cero y, por lo tanto, que nuestras soluciones para $x_n, x_{n-1},\\dots,x_1$ están bien definidas es que las ecuaciones del sistema sean linealmente independientes. Esto es equivalente a que la matriz cuadrada tenga un determinante distinto de cero. A este tipo de matrices se les llama _matrices no singulares_."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "70c87c91",
   "metadata": {},
   "source": [
    "### Reducción\n",
    "\n",
    "Al proceso de tomar un sistema lineal de $n$ ecuaciones algebráicas y $n$ incógnitas\n",
    "\n",
    "$$ a_{11}x_1 + a_{12}x_2 + \\dots + a_{1n}x_n = b_1, $$\n",
    "\n",
    "$$ a_{21}x_1 + a_{22}x_2 + \\dots + a_{2n}x_n = b_2, $$\n",
    "\n",
    "$$ \\vdots $$\n",
    "\n",
    "$$ a_{n1}x_1 + a_{n2}x_2 + \\dots + a_{nn}x_n = b_n, $$\n",
    "\n",
    "y transformarlo a través de operaciones elementales en uno de la forma\n",
    "\n",
    "\\begin{align*}\n",
    "    a'_{11}x_1 \\ + \\ a'_{12}x_2 \\ + \\dots + \\ a'_{1n-1}x_{n-1} \\ + \\ a'_{1n}x_n &= b'_1, \\\\\n",
    "    0 \\ + a'_{22}x_2 + \\dots + a'_{1n-1}x_{n-1} \\ + \\ a'_{1n}x_n &= b'_2, \\\\\n",
    "    & \\ \\vdots \\\\\n",
    "    0 + 0 + \\dots + a'_{n-1,n-1} x_{n-1} + a'_{n-1n}x_n &= b'_{n-1}, \\\\\n",
    "    0 \\ + \\ 0 \\ + \\ \\dots \\ + \\ \\ 0 \\ \\ + \\ \\ \\ a'_{nn}x_n &= b'_n.\n",
    "\\end{align*}\n",
    "\n",
    "se le conoce como _reducción_, y esto último se conoce como la _forma reducida_ del sistema. Una _transformación elemental_ es la transformación de una ecuación del sistema en otra a través de operaciones elementales.\n",
    "\n",
    "Sea $E_i$ la $i$-ésima ecuación del sistema no reducido. Si $E_1$ tiene un coeficiente $a_{11}$ distinto de cero, definimos\n",
    "\n",
    "$$ E_1 =: E'_1; \\quad (1) $$\n",
    "\n",
    "de lo contrario, primero intercambiemos a $E_1$ por alguna ecuación $E_j$ con el coeficiente $a_{j1}$ de $x_1$ distinto de cero\n",
    "\n",
    "$$E_1 \\leftrightarrow E_j$$\n",
    "\n",
    "y después definimos a $E_1'$ usando la ecuación (1). En ambos casos, redefinamos sus coeficientes como $a'_{11}:= a_{j1}, a'_{12}:= a_{j2},\\dots, b'_1:=b_j$, obteniendo la ecuación\n",
    "\n",
    "$$E'_1: a'_{11}x_1 + a'_{12}x_2 + ... + a'_{1n} x_n = b'_1,$$\n",
    "\n",
    "con $a'_{11}\\neq0$.\n",
    "\n",
    "Ahora, observemos que, si $E_2$ tiene un coeficiente $a_{22}$ distinto de cero, entonces al aplicar la transformación elemental\n",
    "\n",
    "$$E_2 \\to E_2 - \\frac{a_{21}}{a'_{11}} E_1' =: E'_2 \\quad (2)$$\n",
    "\n",
    "la ecuación resultante $E'_2$ tendrá un coeficiente nulo en $x_1$ y no nulo en $x_2$ (Escríbela a mano y verifícalo); en cambio, si $a_{22} = 0$, primero debemos intercambiar a $E_2$ por alguna ecuación $E_k$ con el coeficiente $a_{k2}$ de $x_2$ distinto de cero\n",
    "\n",
    "$$ E_2 \\leftrightarrow E_k $$\n",
    "\n",
    "y después definir a $E'_2$ con la ecuación (2) para que la ecuación resultante tenga un coeficiente nulo en $x_1$ y no nulo en $x_2$. En ambos casos, definimos a los coeficientes de la ecuación $E'_2$, obteniendo\n",
    "\n",
    "$$E'_2: a'_{21}x_1 + a'_{22}x_2 + ... + a'_{2n} x_n = b'_2,$$\n",
    "\n",
    "con $a'_{21}=0$ y $a'_{22}\\neq0$.\n",
    "\n",
    "Luego, si $E_3$ tiene un coeficiente $a_{33}$ distinto de cero, entonces al aplicar la transformación elemental\n",
    "\n",
    "$$ E_3 \\to E_3 - \\frac{a_{31}}{a'_{11}} E_1' - \\frac{a_{32}}{a'_{22}} E_2' =: E'_3 \\quad (3) $$\n",
    "\n",
    "la ecuación resultante $E'_3$ tendrá coeficientes nulos en $x_1$ y $x_2$, y un coeficiente no nulo en $x_3$; en cambio, si $a_{33} = 0$, primero debemos intercambiar a $E_3$ por alguna ecuación $E_m$ con el coeficiente $a_{l3}$ de $x_3$ distinto de cero\n",
    "\n",
    "$$ E_3 \\leftrightarrow E_l $$\n",
    "\n",
    "y después definir\n",
    "\n",
    "y después definir a $E'_3$ con la ecuación (3) para que la ecuación resultante tenga un coeficiente nulo en $x_1$ y $x_2$, y no nulo en $x_3$. En ambos casos, definimos a los coeficientes de la ecuación $E'_3$, obteniendo\n",
    "\n",
    "$$E'_3: a'_{31}x_1 + a'_{32}x_2 + ... + a'_{3n} x_n = b'_3,$$\n",
    "\n",
    "con $a'_{31}=a'_{32}=0$ y $a'_{33}\\neq0$. (¿Observas un patrón? En serio, es muy importante que escribas al menos estos dos primeros pasos a mano, para que realmente lo _observes_.).\n",
    "\n",
    "Podemos seguir aplicando el mismo procedimiento iterativamente hasta haber obtenido ecuaciones $E'_1, E'_2, \\dots, E'_n$, las cuales forman un sistema _reducido_ al cual le podemos aplicar _retropropagación_.\n",
    "\n",
    "**Nota** La razón por la que **debe existir** una ecuación $E_j$ con coeficiente $a_{j1}\\neq0$ con el cual podamos definir a $E'_1$ y empezar el proceso de reducción es que, de lo contrario, ¡el sistema tendría $n-1$ incógnitas en vez de $n$!\n",
    "\n",
    "Observemos que las transformaciones elementales **no afectan a las incógnitas** $x_1,x_2\\dots,x_n$, sino que **sólo afectan a los coeficientes** $a_{ij}, b_i$, con $1\\leq i,j\\leq n$. Por lo tanto, podemos hacer reducción _sólo considerando a los coeficientes del sistema_. Similarmente, notemos que, para hacer retropropagación, _sólo necesitamos a los coeficientes del sistema reducido_. Esto nos lleva desechar los sistemas en favor de una representación más sencilla de visualizar y de implementar en código."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0cf2ebb0",
   "metadata": {},
   "source": [
    "### Representación matricial\n",
    "\n",
    "\n",
    "Consideremos, nuevamente, un sistema lineal de ecuaciones algebráicas\n",
    "\n",
    "$$ a_{11}x_1 + a_{12}x_2 + \\dots + a_{1n}x_n = b_1, $$\n",
    "\n",
    "$$ a_{21}x_1 + a_{22}x_2 + \\dots + a_{2n}x_n = b_2, $$\n",
    "\n",
    "$$ \\vdots $$\n",
    "\n",
    "$$ a_{n1}x_1 + a_{n2}x_2 + \\dots + a_{nn}x_n = b_n. $$\n",
    "\n",
    "Como tal vez sospeches por la notación de los coeficientes, podemos escribir este sistema como una sola ecuación vectorial\n",
    "\n",
    "$$ \\begin{pmatrix} a_{11} &a_{12} &\\dots &a_{1n} \\\\ a_{21} &a_{22} &\\dots &a_{2n} \\\\ \\vdots &\\vdots &\\ddots &\\vdots \\\\ a_{n1} &a_{n2} &\\dots &a_{nn} \\end{pmatrix} \\begin{pmatrix} x_1 \\\\ x_2 \\\\ \\vdots \\\\ x_n \\end{pmatrix} = \\begin{pmatrix} b_1 \\\\ b_2 \\\\ \\vdots \\\\ b_n \\end{pmatrix}; $$\n",
    "\n",
    "o, de forma más sucinta,\n",
    "\n",
    "$$ A \\vec{x} = \\vec{b}. $$\n",
    "\n",
    "Observemos que podemos representar a nuestro sistema de ecuaciones con la matriz aumentada\n",
    "\n",
    "$$ \\big( A\\mid\\vec{b} \\ \\big) = \\begin{pmatrix} a_{11} &a_{12} &\\dots &a_{1n} &\\mid &b_1 \\\\ a_{21} &a_{22} &\\dots &a_{2n} &\\mid &b_2 \\\\ \\vdots &\\vdots &\\ddots &\\vdots &\\mid &\\vdots \\\\ a_{n1} &a_{n2} &\\dots &a_{nn} &\\mid &b_n \\end{pmatrix}. $$\n",
    "\n",
    "De esta forma, cada renglón de la matriz aumentada representa una ecuación de nuestro sistema... ¡y las operaciones elementales que vimos para sistemas lineales de ecuaciones _coinciden completamente_ con operaciones elementales de matrices! (De hecho, de ahí viene el nombre.) Recordando que las transformaciones elementales sólo afectan a los **coeficientes** de un sistema lineal de ecuaciones, entonces podemos aplicarle **reducción** a la matriz aumentada para llevarla a su forma reducida\n",
    "\n",
    "$$ \\begin{pmatrix} a'_{11} &a'_{12} &\\dots &a'_{1n} &\\mid &b'_1 \\\\ 0 &a'_{22} &\\dots &a'_{2n} &\\mid &b'_2 \\\\ \\vdots &\\vdots &\\ddots &\\vdots &\\mid &\\vdots \\\\ 0 &0 &\\dots &a'_{nn} &\\mid &b'_n \\end{pmatrix}. $$\n",
    "\n",
    "Luego, recordando que la retropropagación se puede llevar a cabo sólo con los coeficientes del sistema reducido, ¡podemos utilizar esta matriz reducida para encontrar la solución de nuestro sistema!"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "139f4699",
   "metadata": {},
   "source": [
    "## Implementación\n",
    "\n",
    "Para este punto, ya debes tener motivación para resolver un problema importante y ubicuo, así como un plan de acción respaldado por una teoría sensata. Ahora sí, ¡te toca implementarlo!\n",
    "\n",
    "Como sugerencia general, te recomiendo recordar que puedes crear celdas de Jupyter libremente para experimentar con tu código, probarlo con diferentes parámetros, ver si funciona como esperas, e irlo corrigiendo en caso de que no. Además, si así lo deseas, puedes empezar resolviendo sistemas pequeños (por ejemplo, de dos ecuaciones) y, ya que tengas una noción de los procedimientos y cómo implementarlos, generalizar tu código para que también pueda resolver sistemas más grandes. \n",
    "\n",
    "**Ejercicio** Crea una función `retropropagación` con un argumento `M`, que puedes suponer que es una matriz aumentada de la forma\n",
    "\n",
    "$$ \\begin{pmatrix} a'_{11} &a'_{12} &\\dots &a'_{1n} &\\mid &b'_1 \\\\ 0 &a'_{22} &\\dots &a'_{2n} &\\mid &b'_2 \\\\ \\vdots &\\vdots &\\ddots &\\vdots &\\mid &\\vdots \\\\ 0 &0 &\\dots &a'_{nn} &\\mid &b'_n \\end{pmatrix} $$\n",
    "\n",
    "-es decir, aquella formada por una matriz triangulada superior y un vector $\\vec{b}'$-, que aplique retropropagación a la matriz `M` y devuelva como resultado un arreglo con el vector solución $\\vec{x}$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8afe23d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Tu código (comentado) va aquí :D"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dc0c2af6",
   "metadata": {},
   "source": [
    "Ya hemos implementado un algoritmo capaz de solucionar matrices reducidas. Ahora, implementaremos otro que realice el proceso de reducción de una matriz aumentada. Como este proceso depende de que las entradas que van quedando en la diagonal sean no nulas -para poder dividir entre ellas-, primero implementaremos una función que se asegure de que esto suceda.\n",
    "\n",
    "**Ejercicio** Crea una función `pivote` que tome tres argumentos `M`, `i` y `j`, y revise si la entrada del renglón `i` y columna `j` de la matriz `M` es igual a cero. En caso que sí lo sea, debe buscar la primera entrada distinta de cero entre los siguientes renglones de la misma columna y, al encontrarla, intercambiar el renglón correspondiente a la entrada no nula con el renglón `i`.\n",
    "\n",
    "Sugerencias: Recuerda que puedes aplicar la función `length` a un vector columna de una matriz para obtener la cantidad de renglones de esa matriz. Además, puedes crear una variable temporal para no perder información durante el intercambio de los renglones."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82a63dc1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Tu código (comentado) va aquí :D"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cb419e2e",
   "metadata": {},
   "source": [
    "**Ejercicio** Crea una función `reducción` que tome un argumento `M`, que puedes suponer que es una matriz aumentada de la forma\n",
    "\n",
    "$$ \\begin{pmatrix} a_{11} &a_{12} &\\dots &a_{1n} &\\mid &b_1 \\\\ a_{21} &a_{22} &\\dots &a_{2n} &\\mid &b_2 \\\\ \\vdots &\\vdots &\\ddots &\\vdots &\\mid &\\vdots \\\\ a_{n1} &a_{n2} &\\dots &a_{nn} &\\mid &b_n \\end{pmatrix} $$\n",
    "\n",
    "que representa un sistema de ecuaciones algebráicas linealmente independientes -y que, por ende, le podemos aplicar reduccion-, que devuelva la matriz reducida correspondiente.\n",
    "\n",
    "Sugerencia: Usa la función `pivote` que creaste anteriormente."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0829fed7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Tu código (comentado) va aquí :D"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "725fb2a7",
   "metadata": {},
   "source": [
    "**Ejercicio** Crea una función `solución` con un argumento `M`, que puedes suponer que es una matriz aumentada que representa un sistema de ecuaciones algebráicas linealmente independientes, que integre las funciones `reducción` y `retropropagación` y devuelva un arreglo con el vector solución $\\vec{x}$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3870ac0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Tu código (comentado) va aquí :D"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "462f6ff3",
   "metadata": {},
   "source": [
    "## Cálculo de matrices inversas\n",
    "\n",
    "Una de las características más importantes de las matrices no singulares (esto es, matrices cuadradas con determinante no nulo) es que son invertibles. Es decir que, si $A\\in M_{n\\times n}(\\mathbb{R})$ es tal que $\\text{det}(A)\\neq 0$, entonces existe $C\\in M_{n\\times n}(\\mathbb{R})$ tal que\n",
    "\n",
    "$$ AC = I_{n\\times n} = CA,$$\n",
    "\n",
    "donde $I_{n\\times n}$ es la matriz identidad con $n$ renglones y $n$ columnas. Observemos que, si esto sucede, entonces de la ecuación $AC = I_{n\\times n}$ tenemos que el producto del primer vector columna de $C$ con la matriz $A$ es igual al vector\n",
    "v\n",
    "$$ \\begin{pmatrix} 1 \\\\ 0 \\\\ \\vdots \\\\ 0 \\end{pmatrix}. $$\n",
    "\n",
    "Más generalmente, el producto del $j$-ésimo vector columna de $C$ con la matriz $A$ dará como resultado un vector con $1$ en la $j$-ésima entrada y $0$ en todas las demás.\n",
    "\n",
    "A raíz de esta observación, podemos armar y solucionar $n$ sistemas lineales de ecuaciones distintos y juntar los vectores solución en una matriz, obteniendo así una matriz _inversa por la derecha_ de $A$. Más aún, se puede ver sencillamente con un poquito de álgebra que esta matriz inversa por la derecha debe ser _la_ inversa. En efecto: sea $A\\in M_{n\\times n}(\\mathbb{R})$ una matriz no singular (invertible), $A^{-1}$ su inversa y $C$ una matriz inversa de $A$ por la derecha; entonces\n",
    "\n",
    "$$ \\begin{align*} C &= I_{n\\times n} C \\\\ &= (A^{-1}A)C  \\\\ &= A^{-1}(AC) \\\\ &= A^{-1}I_{n\\times n} \\\\ &= A^{-1}.\\end{align*} $$\n",
    "\n",
    "**Ejercicio** Crea una función `invertir` con un argumento `M`, que puedes suponer que es una matriz cuadrada no singular (invertible), que devuelva la matriz inversa de `M`.\n",
    "\n",
    "Sugerencia: Utiliza la función `solución` que creaste anteriormente."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "519373a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Tu código (comentado) va aquí :D"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "70597fba",
   "metadata": {},
   "source": [
    "## El método de propagación\n",
    "\n",
    "Existe otro método para solucionar sistemas lineales de ecuaciones algebráicas **totalmente análogo al que hemos visto**. En efecto, esto se sigue de observar que, si en vez de tener un sistema cuya matriz asociada sea triangular superior, fuese triangular _inferior_\n",
    "\n",
    "$$ \\begin{pmatrix} a'_{11} &0 &\\dots &0 \\\\ a'_{21} &a'_{22} &\\dots &0 \\\\ \\vdots &\\vdots &\\ddots &\\vdots \\\\ a'_{n1} &a'_{n2} &\\dots &a'_{nn} \\end{pmatrix} \\begin{pmatrix} x_1 \\\\ x_2 \\\\ \\vdots \\\\ x_n \\end{pmatrix} = \\begin{pmatrix} b'_1 \\\\ b'_2 \\\\ \\vdots \\\\ b'_n \\end{pmatrix} $$\n",
    "\n",
    "entonces podríamos solucionarlo de principio a fin, obteniendo primero a\n",
    "\n",
    "$$x_1 = \\frac{b'_{1}}{a'_{11}}$$\n",
    "\n",
    "y luego la fórmula general\n",
    "\n",
    "$$ x_i = \\frac{1}{a'_{ii}} \\bigg( b'_i - \\sum_{j=1}^{i-1} a'_{ij}x_j \\bigg) $$\n",
    "\n",
    "para $1<i\\leq n$. A este método se le conoce como _propagación_, pues solucionamos la primera entrada del vector incógnita y después propagamos esa solución iterativamente hacia adelante. Asimismo, podemos reducir una matriz aumentada de la forma\n",
    "\n",
    "$$ \\begin{pmatrix} a_{11} &a_{12} &\\dots &a_{1n} &\\mid &b_1 \\\\ a_{21} &a_{22} &\\dots &a_{2n} &\\mid &b_2 \\\\ \\vdots &\\vdots &\\ddots &\\vdots &\\mid &\\vdots \\\\ a_{n1} &a_{n2} &\\dots &a_{nn} &\\mid &b_n \\end{pmatrix} $$\n",
    "\n",
    "a una de la forma\n",
    "\n",
    "$$ \\begin{pmatrix} a'_{11} &0 &\\dots &0 &\\mid &b'_1 \\\\ a'_{21} &a'_{22} &\\dots &0 &\\mid &b'_2 \\\\ \\vdots &\\vdots &\\ddots &\\vdots &\\mid &\\vdots \\\\ a'_{n1} &a'_{n2} &\\dots &a'_{nn} &\\mid &b'_n \\end{pmatrix} $$\n",
    "\n",
    "haciendo un proceso inverso al que vimos anteriormente -siempre y cuando, nuevamente, la matriz cuadrada sea no singular.\n",
    "\n",
    "En inglés, este segundo método (propagación) se conoce como _forward substitution_, mientras que el primero que vimos (retropropagación) se conoce como _backward substitution_."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9864317a",
   "metadata": {},
   "source": [
    "## Recursos complementarios\n",
    "\n",
    "* Capítulo 6 \"Direct Methods for Solving Linear Systems\" de Burden, Faires y Burden, _Numerical Analysis_ (2016).\n",
    "* Secciones 3.2 \"Solution of Triangular Systems\" y 3.3 \"The Gaussian Elimination Method (GEM) and LU Factorization\" de Quarteroni, Sacco y Saleri, _Numerical Mathematics_ (2000).\n",
    "* Capítulo 2 \"Systems of Linear Equations\" de Poole, _Linear Algebra: A Modern Introduction_ (2015)."
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
