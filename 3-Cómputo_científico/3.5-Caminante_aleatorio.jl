### A Pluto.jl notebook ###
# v0.19.4

using Markdown
using InteractiveUtils

# ╔═╡ 6f5f31aa-2941-42f5-aceb-bedb2bd30ea2
md"# Caminante aleatorio
Un caminante aleatorio (o _random walk_, en inglés) es un tipo de modelo estocástico en el cual la posición de una partícula en cierto instante depende de su posición en el instante previo y alguna variable aleatoria que determina su subsecuente dirección y la longitud de paso.

Este tipo de modelo es muy útil para hacer simulaciones en Física Estadística; por ejemplo, se puede utilizar para modelar el movimiento browniano de moléculas en un gas.
"

# ╔═╡ 62816dec-c81a-40cb-aebd-8bda77d5e389
md" ## Caminante aleatorio en una dimensión
El modelo más sencillo de un caminante aleatorio es aquel en el que una partícula:
* se mueve en un tiempo discreto y en intervalos de tiempo uniformes;
* se mueve en una sola dimensión espacial;
* tiene igual probabilidad de moverse en cualquiera de los dos sentidos posibles.

Los primeros dos puntos son fáciles de modelar: para el primer punto, podemos modelar el tiempo con los números naturales y, para el segundo, podemos modelar el espacio con los números enteros, suponiendo -por simplicidad- que la posición inicial de la partícula es el origen (`0`). En otras palabras, para simular el paso del tiempo podemos iterar sobre un arreglo de números naturales consecutivos y, para registar cada posición, podemos crear un arreglo que inicialmente sólo contenga la posición inicial, (`[0]`) y posteriormente añadir las posiciones subsecuentes como entradas a este arreglo.

La cuestión ahora es, ¿cómo modelamos el tercer punto?
"

# ╔═╡ 6dd575bd-5ee7-49ab-8234-ab83eff83ebf
md"### La función `rand`
Julia tiene varias funciones para generar números aleatorios (puedes consultar su documentación [aquí](https://docs.julialang.org/en/v1/stdlib/Random/#Random-generation-functions)). Una de ellas es `rand`. Para conocer lo que hace esta función a través de ejemplos, crea celdas individuales para cada uno de los siguientes comandos y corre cada una de ellas varias veces hasta que tengas una idea de qué es lo que hacen:
* `rand()`
* `rand(Int)`
* `rand(Bool)`"

# ╔═╡ d3e89523-095f-4f2f-aa2c-b38887c187eb
md"Ahora, haz lo mismo para los siguientes comandos, creando las nuevas celdas _debajo_ de la celda que define a la variable `n=1` y cambiando el valor de `n` (corriendo la celda en la que se define) varias veces antes de revisar la documentación de nuevo:
* `rand(n)`
* `rand(Int,n)`
* `rand(Bool,n)`"

# ╔═╡ 712bfc18-334c-470f-8809-1a1388be7b66
n=1

# ╔═╡ 5eedcedb-7dd6-45b0-8a06-238bf6b358f7
md"Como estamos modelando el espacio con los números enteros, cada paso sucesivo de nuestro caminante aleatorio debería sumar o restar `1` a la posición anterior con igual probabilidad. 

**Ejercicio** Utiliza alguna de las funciones anteriores para crear un programa que devuelva los valores `1` y `-1` con igual probabilidad."

# ╔═╡ f2bb54fd-ccb9-4e8d-b8c4-3a4058ffbe4c
md" **Ejercicio** Crea un programa que:
* tome como entrada un número de pasos `n` y
* devuelva como salida un arreglo con `n+1` posiciones, incluyendo la posición inicial `0`, siguiendo una caminata aleatoria."

# ╔═╡ 1e68a5ca-d78e-4371-a63c-d329d11b187f
md"**Ejercicio** Crea una función que:
* tome como entrada un número de pasos `n` y
* devuelva como salida una gráfica que muestre una caminata aleatoria de `n` pasos, a partir de una posición inicial `0`."

# ╔═╡ 5553d1a5-62e9-4a29-bb8e-e4e752ef0cea
md"**Ejercicio** Crea un programa que:
* tome como entrada un número de pasos `n` y un número de caminantes `m`
* devuelva como salida una gráfica que muestre `m` caminatas aleatorias de `n` pasos, a partir de una posición inicial `0`."

# ╔═╡ 75d3a337-a3b2-4319-bd1b-72d2642caef7
md"**Ejercicio** Crea un programa que:
* tome como entrada un arreglo que simule una caminata aleatoria en una dimensión y
* devuelva como salida una *animación* de la caminata sobre la recta numérica."

# ╔═╡ 4179e801-10e6-4ad3-97f1-7ddb8f90bd87
md" https://github.com/dpsanders/metodos-computacionales/blob/master/notas/aleatorios-funciones-caminatas.tex

"

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
# ╟─6f5f31aa-2941-42f5-aceb-bedb2bd30ea2
# ╟─62816dec-c81a-40cb-aebd-8bda77d5e389
# ╟─6dd575bd-5ee7-49ab-8234-ab83eff83ebf
# ╟─d3e89523-095f-4f2f-aa2c-b38887c187eb
# ╠═712bfc18-334c-470f-8809-1a1388be7b66
# ╟─5eedcedb-7dd6-45b0-8a06-238bf6b358f7
# ╟─f2bb54fd-ccb9-4e8d-b8c4-3a4058ffbe4c
# ╟─1e68a5ca-d78e-4371-a63c-d329d11b187f
# ╟─5553d1a5-62e9-4a29-bb8e-e4e752ef0cea
# ╟─75d3a337-a3b2-4319-bd1b-72d2642caef7
# ╟─4179e801-10e6-4ad3-97f1-7ddb8f90bd87
# ╟─00000000-0000-0000-0000-000000000001
# ╟─00000000-0000-0000-0000-000000000002
