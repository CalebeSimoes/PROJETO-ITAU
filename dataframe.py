import pandas as pd
import random
from random import randint
import seaborn as sns
import matplotlib.pyplot as plt


segmento = ['VAREJO', 'UNICLASS', 'PERSONALITE']

uf = ['SP', 'RJ', 'PA', 'MG', 'BA', 'CE', 'DF', 'ES', 'AC', 'AL', 'AP', 'AM', 'GO', 'MA', 'MT', 'MS','PB', 'PR', 'PE', 'PI', 'RN', 'RS', 'RO', 'RR', 'SC', 'SE', 'TO']

amostras = 10000
random.seed(42)


data = {
    'IDADE': [randint(18,69) for _ in range(amostras)],
    'RENDA_MENSAL': [randint(2000, 150000) for _ in range(amostras)],
    'SEGMENTO': [random.choice(segmento) for _ in range(amostras)],
    'UF': [random.choice(uf) for _ in range(amostras)],
    'SCORE_RISCO_CREDITO': [randint(200, 1000) for _ in range(amostras)],
    'POSSUI_INVESTIMENTO': [randint(0,1) for _ in range(amostras)],
    'VALOR_MEDIO_INVESTIDO':[
        randint(500, 500000) if possui_inv else 0
        for possui_inv in [randint(0,1) for _ in range(amostras)]
        ],
    'HISTORICO_ADESAO_SUSTENTAVEL': [randint(0,9) for _ in range(amostras)],
    'DIAS_DESDE_ULTIMO_ACESSO_APP': [randint(1,365) for _ in range(amostras)],
    'TAXA_USO_CANAL_DIGITAL':[round(random.random(), 4) for _ in range(amostras)],
    'COMPARTILHA_OPEN_FINANCE': [randint(0,1) for _ in range(amostras)],
    'INTERESSE_CONTEUDO_ESG': [randint(0,1) for _ in range(amostras)],
    'ADESAO_ESG':[randint(0,1) for _ in range(amostras)]
}

df = pd.DataFrame(data)

quantidade_adesao = df['ADESAO_ESG'] 
contagem_adesao = quantidade_adesao.sum()
quantidade_investimento = df['POSSUI_INVESTIMENTO']
contagem_investimento = quantidade_investimento.sum()

media_renda = df.groupby('SEGMENTO')['RENDA_MENSAL'].mean()
media_uso_digital = df.groupby('UF')['TAXA_USO_CANAL_DIGITAL'].mean()



x = df['IDADE']
y= df['SCORE_RISCO_CREDITO']
data = df
sns.boxplot(x=x, y=y, data=data)

plt.title("Score Por Idade")
plt.xlabel("Idade")
plt.ylabel("Score")

plt.show()
