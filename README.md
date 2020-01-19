# Para que serve?

Você pode definir por quanto tempo uma função deverá se repetir.


# Como usar:

Primeiramente baixe o whilefreezed.py e importe-o no seu programa da seguinte maneira:

```
from whilefreezed import *
```

Os parâmetros do whilefreezed são (h=0, m=0, s=0, f=None).

h -> hora <br />
m -> minutos <br />
s -> segundos <br />
f -> função (onde deverá ser posta a função sem fazer a chamada da mesma, ou seja, sem o "()" no final. <br />


``````
>>> from whilefreezed import *


>>> def exemplo():
        print('Exemplo de uso')
    
>>>> whilefreezed(s=10, f=exemplo)
 
Exemplo de uso
Exemplo de uso
Exemplo de uso
Exemplo de uso
Exemplo de uso
...
```
