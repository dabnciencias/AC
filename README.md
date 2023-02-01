# AC

![](https://github.com/dabnciencias/AC/blob/main/misc/AC_2023-II.gif)

Repositorio de [mi curso de Algoritmos Computacionales en la Facultad de Ciencias (UNAM)](https://www.fciencias.unam.mx/docencia/horarios/presentacion/343139).

## ¿Cómo puedo ejecutar los _notebooks_ del curso desde mi computadora?

Para poder ejecutar los _notebooks_ localmente en tu computadora es necesario instalar [Julia](https://julialang.org/), [Jupyter](https://jupyter.org/), [Git](https://git-scm.com/doc), [IJulia](https://julialang.github.io/IJulia.jl/stable/) y [Pluto](https://github.com/fonsp/Pluto.jl):
* **Julia** es el lenguaje de programación en el cual están escritos la mayoría de los programas del repositorio,
* **Jupyter** es un entorno cómodo para aprender a programar con el cual podremos abrir los _notebooks_ (cuadernos interactivos) de Jupyter del repositorio (archivos con formato `.ipynb`),
* **Git** nos servirá para "clonar" (es decir, descargar) el repositorio y actualizarlo cuando sea necesario (en el caso particular de sistemas operativos basados en Arch Linux, también nos ayudará a poder instalar los programas anteriores),
* **IJulia** nos permitirá ejecutar código de Julia en los _notebooks_ de Jupyter y 
* **Pluto** es un entorno reactivo con el cual podremos abrir y ejecutar los _notebooks_ de Pluto del repositorio (archivos con formato `.jl`, el formato estándar de los programas escritos en Julia).

A continuación, detallamos los pasos que debes seguir en distintos sistemas operativos para poder ejecutar los _notebooks_ del curso localmente en tu computadora. 

**Si utilizas alguna otra distribución de Linux u otro sistema operativo distinto a los mencionados a continuación y necesitas soporte técnico, contacta al ayudante del curso.**

### GNU/Linux y MacOS

#### Instalar Julia, Jupyter y Git...

* **...en distribuciones basadas en Debian** ([Mint](https://linuxmint.com/)/[Ubuntu](https://ubuntu.com/)/[Debian](https://www.debian.org/))
1. Abre una terminal virtual y actualiza las bases de datos de paquetes de Debian con el administrador de paquetes [Aptitude](https://wiki.debian.org/Aptitude) corriendo el comando `sudo apt update && sudo apt -y upgrade`.
1. Instala `julia` y `git` con el comando `sudo apt-get install julia git`.
1. Para instalar `jupyter`, instala primero Python3 y `pip` con el comando `apt-get install python3 python3-pip python3-dev -y`; después de que haya terminado, ejecuta el comando `pip install jupyter`.

**Nota**
* No es posible actualizar versiones de Python2 a Python3; por ende, aunque ya tengas instalado Python2, tendrás que instalar Python3 para poder instalar Jupyter.
* Si tu computadora tiene [ChromeOS](https://www.google.com/chromebook/chrome-os/), puedes [activar las opciones de desarrollador](https://www.androidauthority.com/how-to-enable-developer-mode-on-a-chromebook-906688/) y luego [activar Linux](https://support.google.com/chromebook/answer/9145439?hl=en). De esta manera, una vez que tengas acceso a una terminal virtual de Linux, podrás seguir las instrucciones para distribuciones basadas en Debian para instalar Julia, Jupyter y Git.

* **...en distribuciones basadas en Arch** ([Manjaro](https://manjaro.org/)/[Endeavour](https://endeavouros.com/)/[Arch](https://archlinux.org/))
1. Abre una terminal virtual y actualiza las bases de datos de paquetes de Arch con el administrador de paquetes [`pacman`](https://wiki.archlinux.org/title/Pacman) corriendo el comando `sudo pacman -Syyu` **antes de instalar cualquier cosa**.
1. Instala `git` con el comando `sudo pacman -S git`.
1. Ejecuta los comandos `cd ~` y `git clone https://aur.archlinux.org/yay.git`; después de que el segundo comando haya terminado, ejecuta el comando `cd yay`.
1. Instala el programa auxiliar`yay` con el comando `makepkg -si`; después de que haya terminado, ejecuta el comando `cd ~`, y luego el comando `rm -rf yay/`.
1. Actualiza las bases de datos de los paquetes del [AUR](https://wiki.archlinux.org/title/Arch_User_Repository_(Español)) con [`yay`](https://wiki.archlinux.org/title/AUR_helpers#Pacman_wrappers) corriendo el comando `yay -Syyu` **antes de instalar cualquiera de los programas siguientes**.
1. Instala `julia` y `jupyter` con el comando `yay -S julia-bin jupyter`. 

* **...en MacOS**
1. Abre una terminal e instala el administrador de paquetes [hombrew](https://brew.sh/) corriendo el comando `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`.
1. Instala `jupyter` y `git` con el comando `brew install jupyter git`.
1. Instala `julia` con el comando `brew install --cask julia`.

#### Instalar IJulia y Pluto (para cualquier distribución GNU/Linux y MacOS)
1. Abre una terminal virtual y ejecuta el comando `julia` -el _prompt_ de la terminal virtual debería cambiar al texto `julia>` en verde.
1. Teclea `]` -el _prompt_ ahora debería cambiar a algo en azul que diga `pkg>`; después, escribe `add IJulia Pluto` y teclea `ENTER`.

#### Decargar y actualizar actualizar el repositorio del curso (para cualquier distribución GNU/Linux y MacOS)
1. Para descargar todo el repositorio (en su forma actual) a la carpeta "home" de tu computadora, abre una terminal virtual y ejecuta los comandos `cd ~` y después `git clone https://github.com/dabnciencias/AC`. Esto creará una carpeta `AC` con todos los contenidos del repositorio.
1. Para más adelante actualizar el repositorio (a como se encuentra en esta página de GitHub), abre una terminal virtual y ejecuta los comandos `cd ~/AC` y después `git pull`.

#### Ejecutar _notebooks_ localmente (para cualquier distribución GNU/Linux y MacOS)
1. Para ejecutar _notebooks_ de Jupyter (archivos del repositorio con formato .ipynb) localmente, abre una terminal virtual y ejecuta el comando `jupyter-notebook`.
1. Para ejecutar _notebooks_ de Pluto (archivos del repositorio con formato .jl, el formato estándar de código de Julia) localmente, abre una terminal virtual y ejecuta el comando `julia`; después, ejecuta el comando `using Pluto & Pluto.run()`.

### Windows

#### Julia
1. Descarga Julia utilizando el instalador desde su [página oficial](https://julialang.org/downloads/). Selecciona `64-bit (installer)` en la sección de Windows.
1. Al instalar, asegúrate de marcar la casilla 'Add Julia to PATH'.
1. Da click en el ícono de la aplicación de Julia que se creó en tu escritorio para abrir una terminal, deberás ver que el _prompt_ de la terminal virtual tiene el texto `julia>` en color verde.
1. Teclea `]` para ingresar al modo Pkg (Package), el _prompt_ ahora debería cambiar a algo en azul que diga `pkg>`; después, escribe `add IJulia Pluto` y teclea `ENTER` para instalar las paqueterías correspondientes. Para salir del modo Pkg, usa la tecla `DEL`.
1. Para ejecutar _notebooks_ de Pluto usa la terminal de julia (asegurate que el _prompt_ sea `julia>` en color verde) y ejecuta el comando `using Pluto & Pluto.run()`, esto deberá crear una ventana emergente en tu navegador con la interfaz de Pluto.

#### Jupyter
1. Instala Python3 utilizando el instalador desde su página oficial descargando el [siguiente archivo](https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe).
1. **Al instalar asegurate de marcar la casilla 'Add Python 3 to PATH'.**
1. Da click en la aplicación de Power Shell para abrir una terminal virtual en Windows.
1. Utiliza pip para instalar `jupyter` copiando y pegando el siguiente comando en tu terminal de PowerShell: `python -m pip install jupyter`.
1. Para abrir un notebook de Jupyter utiliza el siguiente comando en la terminal de PowerShell: `jupyter notebook` y espera a que se abra una ventana emergente en tu navegador.
1. Para terminar la sesión de Jupyter, cierra la ventana correspondiente de tu navegador y usa `Ctrl-C` dos veces en la terminal de PowerShell para terminar el proceso.

#### Git/GitHub
1. Crea una cuenta en la [página oficial de GitHub](https://github.com) usando tu correo @ciencias.
1. Descarga Git desde la [página oficial de Git](https://git-scm.com/download/win) (download for Windows).
1. Ejecuta el instalador para Windows descargado (archivo con extensión `.exe`).
1. Acepta los términos y revisa las configuraciones durante la instalación. Se recomienda que selecciones las configuraciones predeterminadas.
1. Selecciona tu IDE de preferencia para integrar Git. Si no tienes preferencia, elige cualquiera.
1. Para clonar el repositorio del curso, abre Git Bash desde tu buscador de Windows,
navega hasta la carpeta donde quieres clonar el repositorio y ejecuta el siguiente comando: `git clone https://github.com/dabnciencias/AC`.

### Alternativas para cualquier sistema operativo
1. Google Colab  
Si no cuentas con una computadora personal o tu computadora no tiene los suficientes recursos suficientes para soportar la instalación, puedes usar google colab como alternativa.  
Google Colab es un servicio que ofrece notebooks de Jupyter de manera gratuita con recursos de cómputo totalmente gestionados en la nube sin necesidad de instalar nada en tu computadora local.  
Los notebooks están desarrollados para ejecutar en Python por default, sin embargo se pueden hacer manipulaciones para utilizar otros programas como julia.  
Para utilizarlo, ve directamente a la [página oficial de Google Colab](https://colab.research.google.com/), una vez allí verás un recuadro que te pedirá seleccionar un archivo para abrir, selecciona la ventana Google Drive y da click en 'New notebook' para crear un notebook en blanco. Nota: Los archivos que crees de esta manera se almacenarán en una carpeta llamada 'Colab Notebooks' en la página principal de tu carpeta de Google Drive.

También puedes abrir los notebooks del repositorio del curso yendo a la pestaña de 'GitHub', copiando y pegando la siguiente liga `https://github.com/dabnciencias/AC.git` y seleccionando el archivo que quieras abrir.  

En la [siguiente liga](https://colab.research.google.com/github/ageron/julia_notebooks/blob/master/Julia_for_Pythonistas.ipynb#scrollTo=f_1dr-2W5iSU) puedes encontrar un ejemplo de como usar julia desde google colab.

1. Anaconda  
Una forma más sencilla (pero menos recomendada por el peso de descarga) para hacer la instalación es utilizando Anaconda Navigator.
Puedes descargar Anaconda directamente desde [su página web](https://www.anaconda.com/products/individual). Si decides utilizar esta opción de descarga y necesitas soporte técnico, contacta directamente al ayudante del curso.
