# AC
  Repositorio de [mi curso de Algoritmos Computacionales en la Facultad de Ciencias (UNAM)](https://www.fciencias.unam.mx/docencia/horarios/presentacion/333034).

## Instalación

A continuación, detallamos los pasos que debes seguir en distintos sistemas operativos para poder correr los _notebooks_ del curso localmente en tu computadora.

### GNU/Linux

#### Distribuciones basadas en Debian ([Mint](https://linuxmint.com/)/[Ubuntu](https://ubuntu.com/)/[Debian](https://www.debian.org/))

1. Próximamente.
1. Espéralo...

#### Distribuciones basadas en Arch ([Manjaro](https://manjaro.org/)/[Endeavour](https://endeavouros.com/)/[Arch](https://archlinux.org/))

1. Abre una terminal virtual, corre el comando `cd ~` y sincroniza las bases de datos de las paqueterías con el comando `sudo pacman -Syyu` **antes de instalar cualquier cosa**.
1. Instala [`Git`](https://git-scm.com/doc) con el comando `sudo pacman -S git`.
1. Corre el comando `git clone https://aur.archlinux.org/yay.git` y, después de que haya terminado, corre el comando `cd yay`.
1. Instala `yay` con el comando `makepkg -si` y, después de que haya terminado, corre el comando `cd ~`, y luego el comando `rm -rf yay`.
1. Sincroniza las bases de datos de las paqueterías del [AUR](https://wiki.archlinux.org/title/Arch_User_Repository_(Español)) con el comando `yay -Syyu` **antes de instalar cualquiera de los programas siguientes**.
1. Instala [Julia](https://julialang.org/) y [Jupyter](https://jupyter.org/) con el comando `yay -S julia-bin jupyter` y, después de que haya terminado, corre el comando `julia` y teclea `]`; al presionar esta tecla, el texto en verde `julia>` debería cambiar a algo como `(@v1.7) pkg>` en azul.
1. Corre el comando `add IJulia` y, después de que haya terminado, presiona la tecla `BACKSPACE` para volver al texto verde `julia>` y  corre el comando `exit()` para volver a la terminal virtual.
1. Corre el comando `git clone https://github.com/dabnciencias/AC` para clonar este repositorio localmente a tu computadora.
1. Corre el comando `jupyter-notebook`.

#### Distribuciones basadas en Red Hat Enterprise Linux ([Fedora](https://getfedora.org/)/[CentOS](https://www.centos.org/)/[RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux))

1. Próximamente.
1. Espéralo...

### Mac

1. Próximamente.
1. Espéralo...

### Windows

1. Próximamente.
1. Espéralo...
