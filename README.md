# AC
  Repositorio de [mi curso de Algoritmos Computacionales en la Facultad de Ciencias (UNAM)](https://www.fciencias.unam.mx/docencia/horarios/presentacion/333034).

## ¿Cómo puedo correr los _notebooks_ del curso desde mi computadora?

Para poder correr los _notebooks_ localmente en tu computadora es necesario instalar [Julia](https://julialang.org/), [Jupyter](https://jupyter.org/), [Git](https://git-scm.com/doc), [IJulia](https://julialang.github.io/IJulia.jl/stable/) y [Pluto](https://github.com/fonsp/Pluto.jl):
* **Julia** es el lenguaje en el cual están escritos los programas del repositorio,
* **Jupyter** es un entorno cómodo para aprender a programar con el cual podremos abrir los _notebooks_ de Jupyter del repositorio (archivos con formato .ipynb),
* **Git** nos servirá para "clonar" (es decir, descargar) el repositorio y actualizarlo cuando sea necesario (en el caso particular de sistemas operativos basados en Arch Linux, también nos ayudará a poder instalar los programas anteriores),
* **IJulia** nos permitirá correr código de Julia en los _notebooks_ de Jupyter y 
* **Pluto** es un entorno reactivo con el cual podremos abrir y correr los _notebooks_ de Pluto del repositorio (archivos con formato .jl, el formato estándar de los programas escritos en Julia).

A continuación, detallamos los pasos que debes seguir en distintos sistemas operativos para poder correr los _notebooks_ del curso localmente en tu computadora. 

**Si utilizas alguna otra distribución de Linux u otro sistema operativo distinto a los mencionados a continuación y necesitas soporte, contacta al profesor o al ayudante.**

### GNU/Linux y MacOS

#### Instalar Julia, Jupyter y Git...

* **...en distribuciones basadas en Debian** ([Mint](https://linuxmint.com/)/[Ubuntu](https://ubuntu.com/)/[Debian](https://www.debian.org/))
1. Abre una terminal y actualiza el administrador de paquetes apt con el siguiente comando: `sudo apt update && sudo apt -y upgrade`
1. Usa apt para instalar git. En la terminal corre el comando: `sudo apt-get install git`
1. Usa apt nuevamente para instalar julia: `sudo apt-get install julia`
1. Finalmente para instalar jupyter, instala primero python con el siguiente comando: `apt-get install python3 python3-pip python3-dev -y` y luego instala jupyter usando pip con: `pip install jupyter`

* **...en distribuciones basadas en Arch** ([Manjaro](https://manjaro.org/)/[Endeavour](https://endeavouros.com/)/[Arch](https://archlinux.org/))
1. Abre una terminal virtual y sincroniza las bases de datos de paqueterías de Arch con el comando `sudo pacman -Syyu` **antes de instalar cualquier cosa**.
1. Instala `git` con el comando `sudo pacman -S git`.
1. Corre los comandos `cd ~` y `git clone https://aur.archlinux.org/yay.git`; después de que el segundo comando haya terminado, corre el comando `cd yay`.
1. Instala `yay` con el comando `makepkg -si`; después de que haya terminado, corre el comando `cd ~`, y luego el comando `rm -rf yay/`.
1. Sincroniza las bases de datos de las paqueterías del [AUR](https://wiki.archlinux.org/title/Arch_User_Repository_(Español)) con el comando `yay -Syyu` **antes de instalar cualquiera de los programas siguientes**.
1. Instala `julia` y `jupyter` con el comando `yay -S julia-bin jupyter` 

* **...en MacOS**
1. Abre una terminal e instala el administrador de paquetes [hombrew](https://brew.sh/) corriendo el siguiente comando:  
```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```
1. Usa homebrew para instalar git. En la terminar corre el comando `brew install git`
1. Usa homebrew nuevamente para instalar jupyter: `brew install jupyter`
1. Finalmente para instalar julia utiliza: `brew install --cask julia`

#### Instalar IJulia y Pluto (para cualquier distribución GNU/Linux y MacOS)
1. Abre una terminal virtual y corre el comando `julia` -el _prompt_ de la terminal virtual debería cambiar al texto `julia>` en verde.
1. Teclea `]` -el _prompt_ ahora debería cambiar a algo en azul que diga `pkg>`; después, escribe `add IJulia Pluto` y teclea `ENTER`.

#### Decargar y actualizar repositorio (para cualquier distribución GNU/Linux y MacOS)
1. Para descargar todo el repositorio (en su forma actual) a la carpeta "home" de tu computadora, abre una terminal virtual y corre los comandos `cd ~` y después `git clone https://github.com/dabnciencias/AC`. Esto creará una carpeta `AC` con todos los contenidos del repositorio.
1. Para actualizar el repositorio (a como se encuentra en esta página de GitHub), abre una terminal virtual y corre los comandos `cd ~/AC` y después `git pull`.

#### Correr _notebooks_ localmente (para cualquier distribución GNU/Linux y MacOS)
1. Para correr _notebooks_ de Jupyter (archivos del repositorio con formato .ipynb) localmente, abre una terminal virtual y corre el comando `jupyter-notebook`.
1. Para correr _notebooks_ de Pluto (archivos del repositorio con formato .jl, el formato estándar de código de Julia) localmente, abre una terminal virtual y corre el comando `julia`; después, corre el comando `using Pluto & Pluto.run()`.

### Windows

Julia
1. Descarga julia utilizando el instalador desde su [página oficial](https://julialang.org/downloads/). Selecciona `64-bit (installer)` en la sección de Windows.
1. Da click en el icono de la applicación de julia para abrir una terminal, deberás ver que el _prompt_ de la terminal virtual tiene el texto `julia>` en color verde.
1. Teclea `]`, el _prompt_ ahora debería cambiar a algo en azul que diga `pkg>`; después, escribe `add IJulia Pluto` y teclea `ENTER`.

Jupyter
1. Instala python utilizando el instalador desde su página oficial, accediendo a la siguiente [liga](https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe).
1. Da click en la applicación de Power Shell para abrir una terminal virtual en Windows.
1. Utiliza pip para instalar jupyter corriendo el siguiente comando: `python -m pip install jupyter`
1. Para abrir un notebook de jupyter utiliza el siguiente comando en la terminal: `jupyter notebook` y espera a que se abra una ventana en tu navegador

Git/GitHub
1. Descarga [GitHub Desktop](https://desktop.github.com/) desde la página oficial.
1. Para clonar el repositorio del curso en tu computadora sigue los pasos descritos en la [siguiente página](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop).


### Alternativas para cualquier sistema operativo
1. Anaconda  
Una forma más sencilla (pero menos recomendada por el peso de descarga) para hacer la instalación es utilizando Anaconda Navigator.
Puedes descargar anaconda directamente desde [su página web](https://www.anaconda.com/products/individual).


1. Google Colab  
Si no cuentas con una computadora personal o tu computadora no tiene los suficientes recursos suficientes para soportar la instalación, puedes usar google colab como alternativa.  
Google Colab es un servicio que ofrece notebooks de Jupyter de manera gratuita con recursos de cómputo totalmente gestionados en la web sin necesidad de instalar nada en tu computadora local.  
Los notebooks están desarrollados para correr en Python por default, sin embargo se pueden hacer manipulaciones para utilizar otros programas, en la [siguiente liga](https://colab.research.google.com/github/ageron/julia_notebooks/blob/master/Julia_for_Pythonistas.ipynb#scrollTo=f_1dr-2W5iSU) puedes encontrar un ejemplo de como hacer esta configuración y usar julia desde google colab.

