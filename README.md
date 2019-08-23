# Actionfreeze
Lib para executar funcões repetidamente por um tempo específico

# Usage:

Primeiramente instale a lib usando o pip:

```
pip install actionfreeze
```

Agora você pode importar a lib como o exemplo a seguir:

```
from actionfreeze import *

ice = timefreeze(5)
while actualseconds() != ice:
    print('Hello word!')
````

A variável ```ice``` está recebendo a função ```timefreeze(seconds)```, que retorna os segundos do horário atual somados aos segundos que você especificar.  

Depois é criado um while que compara os segundos atuais retornados pela função ```actualseconds()```

# Funções:

```timefreeze(10)``` retorna os segundos do horário atual somados aos segundos que você especificar

```actualseconds()``` Retorna os segundos do horário atual

Obs: O tempo de congelamento nao pode ultrapassar 60 segundos, ao menos, nao ainda. 

