### A Pluto.jl notebook ###
# v0.17.7

using Markdown
using InteractiveUtils

# ╔═╡ 610ac7dc-84f0-11ec-0293-d5aea54961f4
md"# Solución numérica de ecuaciones diferenciales ordinarias (Método de Euler)

Una _ecuación diferencial ordinaria_ (EDO) es una ecuación de la forma

$$f(t,x(t),\dot{x}(t),\ddot{x}(t),...,x^{(n)}(t)) = 0, \quad (*)$$

donde $f$ es una función arbitraria, $t$ es una _variable independiente_, $x$ es una función de $t$ llamada _función incógnita_ y $\dot{x},\ddot{x},...,x^{(n)}$ son derivadas de la función incógnita $x$ con respecto a la variable independiente $t$.

Observemos que, si consideramos que $t$ es la función identidad y $0$ es la función constante cero, entonces una EDO es una igualdad entre funciones; por esto es que la incógnita de una EDO es, precisamente, una **función**.

En este curso, nos enfocaremos en ecuaciones diferenciales donde la función incógnita es una función real de variable real. En este caso, una función $x(t)$ es una _solución_ a la ecuación diferencial $(*)$ _en un intervalo_ $I\subseteq\mathbb{R}$ si tanto $x(t)$ como sus derivadas cumplen la ecuación $(1)$ para todo $t\in I$.
"

# ╔═╡ c1d72411-519c-4c4a-9fe5-5f9929d1e586
md"
**Ejemplo**
Consideremos la EDO (observemos que cumple la definición)

$$\dot{x} - x = 0. \quad (1)$$

Despejando y reescribiendo en notación de Leibnitz, tenemos que

$$\frac{d}{dt}x = x.$$

¿Qué función de real de variable real conocemos que es igual a su propia derivada?  La función exponencial:

$$x(t) = e^{t}.$$

¿Para qué valores reales de $t$ tenemos que $x$ y $\dot{x}$ cumplen la ecuación $(1)$? Para todo $t\in\mathbb{R}$, como se ve en un curso de cálculo diferencial de una variable.

Por lo tanto, $x(t) = e^t$ es una solución a la ecuación diferencial $(1)$ en el intervalo $\mathbb{R}$.
"

# ╔═╡ 0aacbcb0-30dd-4241-aac1-7db4ca76200b
md"
En el ejemplo anterior, obtuvimos como solución a una **función continua** que pudimos expresar matemáticamente mediante una regla de correspondencia sencilla. A esto se le conoce como una _solución analítica_.

Desafortunadamente, dado que la ecuación $(*)$ es muy general, la mayoría de las EDOs existentes **no tienen solución analítica**. _Afortunadamente_, existen métodos numéricos que nos permiten **aproximar** la solución de casi cualquier EDO mediante una **función discreta**; a esto se le conoce como una _solución numérica_ de una EDO. Uno de los más simples es el **Método de Euler**.
"

# ╔═╡ 0bf8be91-fdec-455f-b419-848451ef686e
md" ## Método de Euler

"

# ╔═╡ 173daae4-fdac-4f72-8332-0c501ae0f455
md""" ## Métodos de Runge-Kutta
El **Método de Euler** forma parte de una familia de métodos numéricos para aproximar soluciones numéricas de EDOs conocidos como **Métodos de Runge-Kutta**, siendo el más sencillo; por ende, en este curso decidimos introducir los Métodos de Runge-Kutta usando el Método de Euler. Seguramente aprenderás más métodos de Runge-Kutta en tu curso de **Física Computacional**, incluyendo el método más "clásico", conocido como _RK4_.
"""

# ╔═╡ fc7efcf9-70ca-4c3d-9822-720c67dcc7f7
md""" ### Créditos
Este notebook de Pluto fue basado parcialmente en el notebook de Jupyter `13. Ecuaciones diferenciales ordinarias - metodo de Euler.ipynb` del repositorio [`FisicaComputacional2019_3`](https://github.com/dpsanders/FisicaComputacional2019_3/) del Dr. David Philip Sanders. 
"""

# ╔═╡ 00000000-0000-0000-0000-000000000001
PLUTO_PROJECT_TOML_CONTENTS = """
[deps]
"""

# ╔═╡ 00000000-0000-0000-0000-000000000002
PLUTO_MANIFEST_TOML_CONTENTS = """
# This file is machine-generated - editing it directly is not advised

julia_version = "1.7.1"
manifest_format = "2.0"

[deps]
"""

# ╔═╡ Cell order:
# ╟─610ac7dc-84f0-11ec-0293-d5aea54961f4
# ╟─c1d72411-519c-4c4a-9fe5-5f9929d1e586
# ╟─0aacbcb0-30dd-4241-aac1-7db4ca76200b
# ╠═0bf8be91-fdec-455f-b419-848451ef686e
# ╟─173daae4-fdac-4f72-8332-0c501ae0f455
# ╟─fc7efcf9-70ca-4c3d-9822-720c67dcc7f7
# ╟─00000000-0000-0000-0000-000000000001
# ╟─00000000-0000-0000-0000-000000000002
