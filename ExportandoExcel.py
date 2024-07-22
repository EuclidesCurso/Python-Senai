#Criar uma tabela em python e mandar executar

import pandas as pd
import numpy as np

#exportando
col = 'Prova01 Prova02 Prova03 Prova04'.split()
lin = 'beatriz bianca bianca caio claudemir daniel deivid douglas emerson erika euclides fabio fabricio fernando floriano gary guilherme gustavo henrique jessica juan kauê lucas luciano duda matheus miriam sabrina'.split()
notas = np.random.randint(1,11,112).reshape(28,4)
print(notas)

dados = pd.DataFrame(data=notas,index=lin,columns=col)
print(dados)

dados.to_excel('Notas_TurmaPython.xlsx')