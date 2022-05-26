### A Pluto.jl notebook ###
# v0.19.4

using Markdown
using InteractiveUtils

# ╔═╡ f4a77582-9121-4881-8139-fcb01d4ef6b9
html"""
<style>
	main {
		margin: 0 auto;
		max-width: 2000px;
    	padding-left: max(160px, 10%);
    	padding-right: max(160px, 10%);
	}
</style>
"""

# ╔═╡ 6f5f31aa-2941-42f5-aceb-bedb2bd30ea2
md"# Caminante aleatorio
Un caminante aleatorio (o _random walk_, en inglés) es un tipo de modelo estocástico en el cual la posición de una partícula en cierto instante depende de su posición en el instante previo y alguna variable aleatoria que determina su subsecuente dirección y la longitud de paso.

Este tipo de modelo es muy útil para hacer simulaciones en Física Estadística; por ejemplo, se puede utilizar para modelar el movimiento browniano de moléculas en un gas.
"

# ╔═╡ 62816dec-c81a-40cb-aebd-8bda77d5e389
md" ## Caminante aleatorio en una dimensión
El modelo más sencillo de un caminante aleatorio es aquel en el que una partícula:
* se mueve en un tiempo discreto y en intervalos de tiempo uniformes;
* se mueve en un espacio discreto de una sola dimensión con tamaño de paso uniforme;
* en cada paso, tiene igual probabilidad de moverse en cualquiera de los dos sentidos posibles.

Los primeros dos puntos son fáciles de modelar: para el primer punto, podemos modelar el tiempo con los números naturales y, para el segundo, podemos modelar el espacio con los números enteros, suponiendo -por simplicidad- que la posición inicial de la partícula es el origen (`0`) y que el tamaño de casa paso es `1`. En otras palabras, para simular el paso del tiempo podemos iterar sobre un arreglo de números naturales consecutivos y, para registar cada posición, podemos crear un arreglo que inicialmente sólo contenga la posición inicial, (`[0]`) y posteriormente añadir las posiciones subsecuentes como entradas a este arreglo.

La cuestión ahora es, ¿cómo modelamos el tercer punto?
"

# ╔═╡ 6dd575bd-5ee7-49ab-8234-ab83eff83ebf
md"### La función `rand`
Julia tiene varias funciones para generar números aleatorios (puedes consultar su documentación [aquí](https://docs.julialang.org/en/v1/stdlib/Random/#Random-generation-functions)). Una de ellas es `rand`. Para conocer lo que hace esta función a través de ejemplos, crea celdas individuales para cada uno de los siguientes comandos y ejecuta cada una de ellas varias veces hasta que tengas una idea de qué es lo que hacen:
* `rand()`
* `rand(Int)`
* `rand(Bool)`"

# ╔═╡ d3e89523-095f-4f2f-aa2c-b38887c187eb
md"Ahora, haz lo mismo para los siguientes comandos, creando las nuevas celdas _debajo_ de la celda que define a la variable `n=1` (y arriba del **Ejercicio**) y cambiando el valor de `n` (ejecutando la celda en la que se define) varias veces antes de revisar la documentación de nuevo:
* `rand(n)`
* `rand(Int,n)`
* `rand(Bool,n)`"

# ╔═╡ 712bfc18-334c-470f-8809-1a1388be7b66
n=1

# ╔═╡ 97ec59e8-2d0d-43d3-b2c8-dd74c7020352
md"**Ejercicio** Crea una función `aleatorioUniforme` que tome como argumentos dos números `a` y `b`, y devuelva como salida un número aleatorio distribuido uniformemente en el intervalo $[a,b]\subset\mathbb{R}$. (Sugerencia: Utiliza `rand()` y un poco de aritmética.)"

# ╔═╡ d4caf15c-4f99-44e4-9222-519433799348
# Tu código va aquí :)

# ╔═╡ 737eb77d-ce3f-4eac-9f38-5cbae8bd2636
md"**Ejercicio** Verifica con un histograma que tu función `aleatorioUniforme` realmente cumpla la propiedad desada. (Pista: ¿Cómo debería verse el histograma?)"

# ╔═╡ 41a80720-ab01-4931-b86f-1c72cf48c993
# Tu código (comentado) va aquí :)

# ╔═╡ 5eedcedb-7dd6-45b0-8a06-238bf6b358f7
md" ### Modelando una caminata aleatoria

Como estamos modelando el espacio con los números enteros, cada paso sucesivo de nuestro caminante aleatorio debería sumar o restar `1` a la posición anterior con igual probabilidad. 

**Ejercicio** Crea una función `unPaso` que no tome argumentos de entrada y devuelva sólamente los valores `1` y `-1` con igual probabilidad. (Pista: La forma más sencilla de hacerlo es usando `rand(Bool)` y un poco de aritmética...)"

# ╔═╡ fc77bf6a-1864-431a-bd9b-0e3a471d81b7
# Tu código va aquí :)

# ╔═╡ d3a7fcb3-b0a5-4b41-bf95-ac3ffdce7fb6
md" **Ejercicio** Crea una función `variosPasos` que tome como argumento un número entero positivo `n` y devuelva un arreglo con `n` entradas, donde cada una de ellas tiene la misma probabilidad de ser `1` ó `-1`. (Pista: Recuerda que colocar un punto (`.`) antes de un operador aritmético hace que funcione con arreglos.)"

# ╔═╡ 544fdf8f-fb78-40be-8618-f071c47f00b2
# Tu código va aquí :)

# ╔═╡ f2bb54fd-ccb9-4e8d-b8c4-3a4058ffbe4c
md" **Ejercicio** Crea una función `caminataAleatoria` que
* tome como entrada un número de pasos `n` y
* devuelva como salida un arreglo con `n+1` posiciones, incluyendo la posición inicial `0`, simulando una caminata aleatoria. (Sugerencia: Puedes usar cualquiera de las funciones `unPaso` o `variosPasos`; la que te resulte más cómoda.)"

# ╔═╡ 9d09fc0f-ccba-477d-9968-82b9554f44e2
# Tu código (comentado) va aquí :)

# ╔═╡ 1e68a5ca-d78e-4371-a63c-d329d11b187f
md"""**Ejercicio** Crea una función `graficaCaminata` que

* tome como entrada un arreglo -que supondremos que simula una caminata aleatoria en una dimensión- y 
* devuelva como salida una gráfica de posición contra número de pasos, usando _puntos_ (`scatter`) y con etiquetas en los ejes.

(Sugerencia: Crea un bloque de código con `begin` y `end` para poder hacer todo en una sola celda de Pluto.)

Luego, en una celda aparte, define una variable `n2` como un número entero positivo y aplica tu función `graficaCaminata` a `caminataAleatoria(n2)` para generar gráficas de caminatas aleatorias.
"""

# ╔═╡ 1ed85ab5-476d-4851-a0ab-c627f972b2c9
# Tu código (comentado) va aquí :)

# ╔═╡ 07edca52-f4bc-478f-b823-9811c320e171
md"**Ejercicio** Crea una función `graficaCaminata!` que sea una versión modificadora de la función anterior y utilice gráficas con líneas rectas punteadas (pues esto nos ayudará a discernir las trayectorias de distintos puntos más fácilmente). Luego, genera una gráfica con 5 caminatas aleatorias.
"

# ╔═╡ 896d6213-105b-403f-8aed-632303c7ba2b
# Tu código (comentado) va aquí :)

# ╔═╡ 75d3a337-a3b2-4319-bd1b-72d2642caef7
md"**Ejercicio** Crea una función `animaCaminata` que
* tome como entrada un arreglo -que supondremos que simula una caminata aleatoria en una dimensión- y
* devuelva como salida una *animación* de la caminata. (Sugerencia: Usa tu función `graficaCaminata`.)"

# ╔═╡ 7a0b1904-17e8-4cce-af17-70182a27da49
# Tu código (comentado) va aquí :)

# ╔═╡ 24490a53-4b2b-49bd-bf9d-f8994ed6a3a7
md"""### Caminante aleatorio en dos dimensiones

Generalicemos nuestro modelo de caminante aleatorio suponiendo que ahora nuestra partícula se mueve en un espacio _continuo_ de _dos_ dimensiones espaciales; con tamaño de paso _continuo_ y _variable_. Es decir que, a pesar de que seguiremos modelando con un tiempo discreto e intervalos de tiempo uniformes, ahora el espacio será _continuo_ y tendrá _dos_ dimensiones espaciales.
"""

# ╔═╡ 09361d57-7c4c-4832-afc4-edf6f8819368
md""" **Ejercicio** Crea una función `caminataAleatoria2D` que
* tome como entrada un número de pasos `n` y
* devuelva como salida un arreglo con dos subarreglos que tengan `n+1` "posiciones" cada uno -uno de posiciones horizontales y otro de posiciones verticales, incluyendo las posiciones iniciales `0` en cada caso-, simulando una caminata aleatoria.
Utiliza tu función `aleatorioUniforme` para generar números aleatorios en el intervalo $[-1,1]$ y suma números generados por esta función a las posiciones horizontales y verticales para simular un paso continuo en dos dimensiones."""

# ╔═╡ d1c6a096-583d-4f85-b2cd-89d227311c1d
# Tu código (comentado) va aquí :)

# ╔═╡ 893d49c4-ab84-4c57-a9e3-54116575ade3
md"""**Ejercicio** Crea una función `graficaCaminata2D` que

* tome como entrada un arreglo con dos subarreglos -que, supondremos, simulan una caminata aleatoria en dos dimensiones- y 
* devuelva como salida una gráfica bidimensional que muestre la trayectoria de la caminata con una línea punteada.

(Sugerencia: Crea un bloque de código con `begin` y `end` para poder hacer todo en una sola celda de Pluto.)

Luego, en una celda aparte, define una variable `n3` como un número entero positivo y aplica tu función `graficaCaminata2D` a `caminataAleatoria2D(n3)` para generar gráficas de caminatas aleatorias en dos dimensiones.
"""

# ╔═╡ d292165a-b37b-47a6-a61e-dbdafbf1f928
# Tu código (comentado) va aquí :)

# ╔═╡ eb7afba3-6d48-4406-8ac7-75521a965a14
md"**Ejercicio** Crea una función `graficaCaminata2D!` que sea una versión modificadora de la función anterior. Luego, genera una gráfica con 5 caminatas aleatorias en dos dimensiones (espaciales).
"

# ╔═╡ ff3c8595-0466-412e-b20b-30336916f573
# Tu código (comentado) va aquí :)

# ╔═╡ ec2b4750-3522-4c26-87ff-06b0b2e3b5d6
md"**Ejercicio** Crea una función `animaCaminata2D` que
* tome como entrada un arreglo con dos subarreglos -que, supondremos, simulan una caminata aleatoria en dos dimensiones- y 
* devuelva como salida una *animación* de la caminata. (Sugerencia: Usa tu función `graficaCaminata2D`.)"

# ╔═╡ f08b6ef6-65c1-4b53-ba50-128e589f70ee
# Tu código (comentado) va aquí :)

# ╔═╡ ef1706ee-85dc-422b-98fa-aa43f75ae098
md"**Ejercicio** ¡Haz una caminata aleatoria en tres dimensiones espaciales y grafícala! (Así se modelan, por ejemplo, las partículas en un gas)." 

# ╔═╡ 48e666c6-3a29-4ebb-993f-06696a49b025
# Tu código (comentado) va aquí :)

# ╔═╡ 9bdee65a-5b90-4e1f-aec8-9939ba1c32e3
md""" #### Nota final

Como aclaración, la razón por la cual en los **Ejercicios** de los _notebooks_ de este curso generalmente se definen muchas funciones "pequeñas" que luego se unen en una función "grande" _no es necesariamente porque esto sea **siempre** la mejor práctica_, sino por una cuestión pedagógica. Cuando estamos aprendiendo a programar y queremos implementar la solución a un problema, es mucho más fácil dividirlo en problemas más pequeños y fáciles de atacar que, después de solucionar, podamos integrar en una solución al problema principal. Sin embargo, para hacer un uso eficiente de los recursos computacionales, generalmente no es recomendable crear funciones que hagan _cada pequeña cosa_, pues todas ellas ocupan espacio en la memoria, por lo que es preferible hacer una implementación más deliberada una vez resuelto el problema usando la estrategia anterior. Recordemos que la principal utilidad de las funciones está en crear bloques de código _reutilizables_ por lo que, una vez implementado un programa, debe encontrarse un punto medio entre cuántas funciones _realmente necesitamos_ por su reutilizabilidad y cuántos recursos computacionales  tenemos a nuestra disposición.

"""

# ╔═╡ 8a5ab06a-12c5-4966-ba10-6d33e920f730
md""" ## Recursos complementarios
* Documentación de [funciones de generación aleatoria](https://docs.julialang.org/en/v1/stdlib/Random/#Random-generation-functions) en Julia.
"""

# ╔═╡ 74e480de-ae20-46ca-a65a-6fb8db3fc202
md""" ## Créditos
Este _notebook_ de Pluto fue basado parcialmente en los _notebooks_ de Jupyter `4. Caminatas aleatorias.ipynb` y `Tarea 1.ipynb` del repositorio [`FisicaComputacional2019_3`](https://github.com/dpsanders/FisicaComputacional2019_3/) del Dr. David Philip Sanders. 
"""

# ╔═╡ 00000000-0000-0000-0000-000000000001
PLUTO_PROJECT_TOML_CONTENTS = """
[deps]
"""

# ╔═╡ 00000000-0000-0000-0000-000000000002
PLUTO_MANIFEST_TOML_CONTENTS = """
# This file is machine-generated - editing it directly is not advised

julia_version = "1.7.2"
manifest_format = "2.0"

[deps]
"""

# ╔═╡ Cell order:
# ╟─f4a77582-9121-4881-8139-fcb01d4ef6b9
# ╟─6f5f31aa-2941-42f5-aceb-bedb2bd30ea2
# ╟─62816dec-c81a-40cb-aebd-8bda77d5e389
# ╟─6dd575bd-5ee7-49ab-8234-ab83eff83ebf
# ╟─d3e89523-095f-4f2f-aa2c-b38887c187eb
# ╠═712bfc18-334c-470f-8809-1a1388be7b66
# ╟─97ec59e8-2d0d-43d3-b2c8-dd74c7020352
# ╠═d4caf15c-4f99-44e4-9222-519433799348
# ╟─737eb77d-ce3f-4eac-9f38-5cbae8bd2636
# ╠═41a80720-ab01-4931-b86f-1c72cf48c993
# ╟─5eedcedb-7dd6-45b0-8a06-238bf6b358f7
# ╠═fc77bf6a-1864-431a-bd9b-0e3a471d81b7
# ╟─d3a7fcb3-b0a5-4b41-bf95-ac3ffdce7fb6
# ╠═544fdf8f-fb78-40be-8618-f071c47f00b2
# ╟─f2bb54fd-ccb9-4e8d-b8c4-3a4058ffbe4c
# ╠═9d09fc0f-ccba-477d-9968-82b9554f44e2
# ╟─1e68a5ca-d78e-4371-a63c-d329d11b187f
# ╠═1ed85ab5-476d-4851-a0ab-c627f972b2c9
# ╟─07edca52-f4bc-478f-b823-9811c320e171
# ╠═896d6213-105b-403f-8aed-632303c7ba2b
# ╟─75d3a337-a3b2-4319-bd1b-72d2642caef7
# ╠═7a0b1904-17e8-4cce-af17-70182a27da49
# ╟─24490a53-4b2b-49bd-bf9d-f8994ed6a3a7
# ╟─09361d57-7c4c-4832-afc4-edf6f8819368
# ╠═d1c6a096-583d-4f85-b2cd-89d227311c1d
# ╟─893d49c4-ab84-4c57-a9e3-54116575ade3
# ╠═d292165a-b37b-47a6-a61e-dbdafbf1f928
# ╟─eb7afba3-6d48-4406-8ac7-75521a965a14
# ╠═ff3c8595-0466-412e-b20b-30336916f573
# ╟─ec2b4750-3522-4c26-87ff-06b0b2e3b5d6
# ╠═f08b6ef6-65c1-4b53-ba50-128e589f70ee
# ╟─ef1706ee-85dc-422b-98fa-aa43f75ae098
# ╠═48e666c6-3a29-4ebb-993f-06696a49b025
# ╟─9bdee65a-5b90-4e1f-aec8-9939ba1c32e3
# ╟─8a5ab06a-12c5-4966-ba10-6d33e920f730
# ╟─74e480de-ae20-46ca-a65a-6fb8db3fc202
# ╟─00000000-0000-0000-0000-000000000001
# ╟─00000000-0000-0000-0000-000000000002
