import pandas as pd
import random
from random import randint
import seaborn as sns
import matplotlib.pyplot as plt


segmento = ['VAREJO', 'UNICLASS', 'PERSONALITE']

uf = ['SP', 'RJ', 'PA', 'MG', 'BA', 'CE', 'DF', 'ES', 'AC', 'AL', 'AP', 'AM', 'GO', 'MA', 'MT', 'MS','PB', 'PR', 'PE', 'PI', 'RN', 'RS', 'RO', 'RR', 'SC', 'SE', 'TO']
peso_adesao = [0.9,0.1]
adesao_esg = [0,1]

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
    'ADESAO_ESG':random.choices(adesao_esg, weights=peso_adesao, k=amostras)
}

df = pd.DataFrame(data)

rendas = []
scores = []
for seg in df['SEGMENTO']:
    if seg =='VAREJO':
        rendas.append(randint(2000, 8000))
        scores.append(randint(400, 700))
    elif seg == 'UNICLASS':
        rendas.append(randint(8000, 25000))
        scores.append(randint(650, 850))
    elif seg == 'PERSONALITE':
        rendas.append(randint(25000, 150000))
        scores.append(randint(800, 1000))   
    else:
        rendas.append(0)
        scores.append(0)         
df['RENDA_MENSAL'] = rendas
df['SCORE_RISCO_CREDITO'] = scores


quantidade_adesao = df['ADESAO_ESG'] 
contagem_adesao = quantidade_adesao.sum()
quantidade_investimento = df['POSSUI_INVESTIMENTO']
contagem_investimento = quantidade_investimento.sum()
media_renda = df.groupby('SEGMENTO')['RENDA_MENSAL'].mean()
media_uso_digital = df.groupby('UF')['TAXA_USO_CANAL_DIGITAL'].mean()
distribuicao_adesao_segmento = df.groupby('SEGMENTO')['ADESAO_ESG'].count()
adesao_uf = df.groupby('UF')['ADESAO_ESG'].mean()
adesao_investimento = df.groupby('POSSUI_INVESTIMENTO')['ADESAO_ESG'].mean()
adesao_of = df.groupby('COMPARTILHA_OPEN_FINANCE')['ADESAO_ESG'].mean()
adesao_conteudo_esg = df.groupby('INTERESSE_CONTEUDO_ESG')['ADESAO_ESG'].mean()


plt.figure(figsize=(12,7))
plt.bar(
    x=adesao_of.index.map({0: 'Não Compartilha', 1: 'Compartilha'}),
    height=adesao_of.values,
    color=['#FFCD00', '#003366'],
)
plt.title('Taxa de Adesão ESG por Compartilhamento de Open Finance', fontsize=14)
plt.xlabel('Compartilha Dados via Open Finance', fontsize=12)
plt.ylabel('Taxa Média de Adesão ESG', fontsize=12)
plt.ylim(0, max(adesao_of.values) * 1.2)
plt.grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(adesao_of.values):
    plt.text(i, v + 0.005, f'{v:.2%}', ha='center', fontsize=10)




plt.figure(figsize=(12,7))
x= df['ADESAO_ESG']
sns.countplot(
    x=x,
    data=df
)


plt.figure(figsize=(12,7))
x = df['IDADE']
y= df['SCORE_RISCO_CREDITO']
data = df
sns.boxplot(
    x=x, y=y, data=data
)
plt.title("Score Por Idade")
plt.xlabel("Idade")
plt.ylabel("Score")




plt.figure(figsize=(12,7))
x = df['RENDA_MENSAL']
y= df['SCORE_RISCO_CREDITO']
sns.scatterplot(
    x='RENDA_MENSAL',
    y='SCORE_RISCO_CREDITO',
    hue='SEGMENTO',
    alpha=0.6,
    palette='viridis',
    data=df
)
plt.title('Relação entre renda e score de credito, Separada por segmento')
plt.xlabel('Renda Mensal')
plt.ylabel('Risco Score credito')

plt.show()


print(distribuicao_adesao_segmento)



