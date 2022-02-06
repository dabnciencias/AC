# AC
  Repositorio de [mi curso de Algoritmos Computacionales en la Facultad de Ciencias (UNAM)](https://www.fciencias.unam.mx/docencia/horarios/presentacion/333034).

## ¿Cómo puedo correr los _notebooks_ desde mi computadora?

Para poder correr los _notebooks_ localmente en tu computadora es necesario instalar [Julia](https://julialang.org/), [Jupyter](https://jupyter.org/), [Git](https://git-scm.com/doc), [IJulia](https://julialang.github.io/IJulia.jl/stable/) y [Pluto](https://github.com/fonsp/Pluto.jl):
* **Julia** es el lenguaje en el cual están escritos los programas del repositorio,
* **Jupyter** es un entorno cómodo para aprender a programar con el cual podremos abrir los _notebooks_ de Jupyter del repositorio (archivos con formato .ipynb),
* **Git** nos servirá para "clonar" (es decir, descargar) el repositorio y actualizarlo cuando sea necesario (en el caso particular de sistemas operativos basados en Arch Linux, también nos ayudará a poder instalar los programas anteriores),
* **IJulia** nos permitirá correr código de Julia en los _notebooks_ de Jupyter y 
* **Pluto** es un entorno reactivo con el cual podremos abrir y correr los _notebooks_ de Pluto del repositorio (archivos con formato .jl, el formato estándar de los programas escritos en Julia).

A continuación, detallamos los pasos que debes seguir en distintos sistemas operativos para poder correr los _notebooks_ del curso localmente en tu computadora. 

### GNU/Linux

#### Instalar Julia, Jupyter y Git...

* **...en distribuciones basadas en Debian** ([Mint](https://linuxmint.com/)/[Ubuntu](https://ubuntu.com/)/[Debian](https://www.debian.org/))
1. Próximamente.
1. Espéralo...

* **...en distribuciones basadas en Arch** ([Manjaro](https://manjaro.org/)/[Endeavour](https://endeavouros.com/)/[Arch](https://archlinux.org/))
1. Abre una terminal virtual y sincroniza las bases de datos de las paqueterías de Arch con el comando `sudo pacman -Syyu` **antes de instalar cualquier cosa**.
1. Instala `git` con el comando `sudo pacman -S git`.
1. Corre los comandos `cd ~` y `git clone https://aur.archlinux.org/yay.git`; después de que el segundo comando haya terminado, corre el comando `cd yay`.
1. Instala `yay` con el comando `makepkg -si`; después de que haya terminado, corre el comando `cd ~`, y luego el comando `rm -rf yay/`.
1. Sincroniza las bases de datos de las paqueterías del [AUR](https://wiki.archlinux.org/title/Arch_User_Repository_(Español)) con el comando `yay -Syyu` **antes de instalar cualquiera de los programas siguientes**.
1. Instala `julia` y `jupyter` con el comando `yay -S julia-bin jupyter` 

* **...en distribuciones basadas en Red Hat Enterprise Linux** ([Fedora](https://getfedora.org/)/[CentOS](https://www.centos.org/)/[RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux))

1. Próximamente.
1. Espéralo...

#### Instalar IJulia y Pluto (para cualquier distribución GNU/Linux)
1. Abre una terminal virtual y corre el comando `julia` -el _prompt_ de la terminal virtual debería cambiar al texto `julia>` en verde.
1. Teclea `]` -el _prompt_ ahora debería cambiar a algo en azul que diga `pkg>`- y, después, corre el comando `add IJulia Pluto`.

#### Decargar y actualizar repositorio (para cualquier distribución GNU/Linux)
1. Para descargar todo el repositorio (en su forma actual) a la carpeta "home" de tu computadora, abre una terminal virtual y corre los comandos `cd ~` y después `git clone https://github.com/dabnciencias/AC`. Esto creará una carpeta `AC` con todos los contenidos del repositorio.
1. Para actualizar el repositorio (a como se encuentra en esta página de GitHub), abre una terminal virtual y corre los comandos `cd ~/AC` y después `git pull`.

#### Correr _notebooks_ localmente (para cualquier distribución GNU/Linux)
1. Para correr _notebooks_ de Jupyter (archivos del repositorio con formato .ipynb) localmente, abre una terminal virtual y corre el comando `jupyter-notebook`.
1. Para correr _notebooks_ de Pluto (archivos del repositorio con formato .jl, el formato estándar de código de Julia) localmente, abre una terminal virtual y corre el comando `julia`; después, corre el comando `using Pluto & Pluto.run()`.

### Mac

1. Próximamente.
1. Espéralo...

### Windows

1. Próximamente.
1. Espéralo...
