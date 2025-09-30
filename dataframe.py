import pandas as pd
import random
from random import randint
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np
from sklearn.ensemble import RandomForestClassifier

segmento = ['VAREJO', 'UNICLASS', 'PERSONALITE']
uf = ['SP', 'RJ', 'PA', 'MG', 'BA', 'CE', 'DF', 'ES', 'AC', 'AL', 'AP', 'AM', 'GO', 'MA', 'MT', 'MS','PB', 'PR', 'PE', 'PI', 'RN', 'RS', 'RO', 'RR', 'SC', 'SE', 'TO']

peso_adesao = [0.95, 0.05]
adesao_esg = [0, 1]

amostras = 10000
random.seed(42)


data = {
    'IDADE': [randint(18, 69) for _ in range(amostras)],
    'RENDA_MENSAL': [0] * amostras,
    'SEGMENTO': [random.choice(segmento) for _ in range(amostras)],
    'UF': [random.choice(uf) for _ in range(amostras)],
    'SCORE_RISCO_CREDITO': [0] * amostras, 
    'POSSUI_INVESTIMENTO': [randint(0, 1) for _ in range(amostras)],
    'VALOR_MEDIO_INVESTIDO': [
        randint(500, 500000) if possui_inv else 0
        for possui_inv in [randint(0, 1) for _ in range(amostras)]
    ],
    'HISTORICO_ADESAO_SUSTENTAVEL': [randint(0, 9) for _ in range(amostras)],
    'DIAS_DESDE_ULTIMO_ACESSO_APP': [randint(1, 365) for _ in range(amostras)],
    'TAXA_USO_CANAL_DIGITAL': [round(random.random(), 4) for _ in range(amostras)],
    'COMPARTILHA_OPEN_FINANCE': [randint(0, 1) for _ in range(amostras)],
    'INTERESSE_CONTEUDO_ESG': [randint(0, 1) for _ in range(amostras)],
    'ADESAO_ESG': random.choices(adesao_esg, weights=peso_adesao, k=amostras)
}

df = pd.DataFrame(data)

p_map = {
    'VAREJO': 0.05,
    'UNICLASS': 0.10,
    'PERSONALITE': 0.20
}

df['PROB_BASE'] = df['SEGMENTO'].map(p_map)
df['PROB_FINAL'] = df['PROB_BASE']
df.loc[df['INTERESSE_CONTEUDO_ESG'] == 1, 'PROB_FINAL'] += 0.15
df.loc[df['HISTORICO_ADESAO_SUSTENTAVEL'] >= 1, 'PROB_FINAL'] += 0.06
df.loc[df['HISTORICO_ADESAO_SUSTENTAVEL'] >= 2, 'PROB_FINAL'] += 0.10
df.loc[df['HISTORICO_ADESAO_SUSTENTAVEL'] >= 3, 'PROB_FINAL'] += 0.12
df.loc[df['TAXA_USO_CANAL_DIGITAL'] == 1, 'PROB_FINAL'] += 0.09

df['PROB_FINAL'] = np.clip(df['PROB_FINAL'], 0, 1)

df['ADESAO_ESG'] = np.random.binomial(n=1, p=df['PROB_FINAL'])

rendas = []
scores = []
for seg in df['SEGMENTO']:
    if seg == 'VAREJO':
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



adesao_por_segmento = df.groupby('SEGMENTO')['ADESAO_ESG'].mean().sort_values(ascending=False)
adesao_investimento = df.groupby('POSSUI_INVESTIMENTO')['ADESAO_ESG'].mean()
adesao_of = df.groupby('COMPARTILHA_OPEN_FINANCE')['ADESAO_ESG'].mean()
adesao_conteudo_esg = df.groupby('INTERESSE_CONTEUDO_ESG')['ADESAO_ESG'].mean()
adesao_uf_top10 = df.groupby('UF')['ADESAO_ESG'].mean().nlargest(10)


plt.figure(figsize=(8, 6))
sns.countplot(
    x='ADESAO_ESG',
    data=df,
    palette=['#FFCD00', '#003366'],
    order=[0, 1]
)
plt.title('Distribuição de Adesão ESG (0=Não, 1=Sim)', fontsize=14)
plt.xlabel('Adesão ESG', fontsize=12)
plt.ylabel('Contagem de Clientes', fontsize=12)
plt.xticks([0, 1], ['Não Aderiu', 'Aderiu'])
plt.show()
print(f"Taxa total de Adesão ESG: {df['ADESAO_ESG'].mean():.2%}")

plt.figure(figsize=(10, 6))
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
    plt.text(i, v + 0.0005, f'{v:.2%}', ha='center', fontsize=10)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(
    x=adesao_por_segmento.index,
    y=adesao_por_segmento.values,
    palette=['#003366', '#4CAF50', '#FFCD00']
)
plt.title('Taxa Média de Adesão ESG por Segmento', fontsize=14)
plt.xlabel('Segmento', fontsize=12)
plt.ylabel('Taxa de Adesão ESG', fontsize=12)
for i, v in enumerate(adesao_por_segmento.values):
    plt.text(i, v + 0.0005, f'{v:.2%}', ha='center', fontsize=10)
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='RENDA_MENSAL',
    y='SCORE_RISCO_CREDITO',
    hue='SEGMENTO',
    alpha=0.6,
    palette='viridis',
    data=df
)
plt.title('Relação entre Renda e Score de Crédito, Separada por Segmento', fontsize=14)
plt.xlabel('Renda Mensal', fontsize=12)
plt.ylabel('Score Risco Crédito', fontsize=12)
plt.show()

corr_df = df.corr(numeric_only=True, method='pearson')

plt.figure(figsize=(14, 12)) # Aumentei o tamanho para melhor visualização
sns.heatmap(
    corr_df,
    annot=True,
    cmap='coolwarm',
    fmt=".2f",
    linewidths=.5,
    cbar_kws={'label': 'Coeficiente de Correlação'}
)
plt.title('Mapa de Calor da Correlação (Variáveis Numéricas)', fontsize=16)
plt.show()


y = df['ADESAO_ESG']
X_features = df.drop(['ADESAO_ESG', 'PROB_BASE', 'PROB_FINAL'], axis=1)
X = pd.get_dummies(
    X_features,
    columns=['SEGMENTO', 'UF'],
    dtype=int
) 
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)


modelo_rf = RandomForestClassifier(n_estimators=200, random_state=42, class_weight='balanced')

modelo_rf.fit(X_train, y_train)
y_pred_rf = modelo_rf.predict(X_test)

y_prob_rf = modelo_rf.predict_proba(X_test)
y_prob_classe1_rf = y_prob_rf[:, 1]
novo_threshold = 0.60
y_pred_rf_calibrado = (y_prob_classe1_rf >= novo_threshold).astype(int)

print(classification_report(y_test, y_pred_rf_calibrado))

cm = confusion_matrix(y_test, y_pred_rf_calibrado)
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    cbar=False,
    xticklabels=['Previsto Não aderencia (0)', 'Previsto aderencia (1)'],
    yticklabels=['Real não aderiu (0)', 'Real Aderiu (1)']
)
plt.title('Matriz de confusão', fontsize=12)
plt.xlabel('Previsao do modelo:')
plt.ylabel('Valor real:')
plt.show()


importancias = modelo_rf.feature_importances_
nomes_features = X.columns 

df_importancia = pd.DataFrame({
    'Feature': nomes_features,
    'Importancia': importancias
}).sort_values(by='Importancia', ascending=False)

print("\n--- Top 10 Features Mais Importantes ---")
print(df_importancia.head(10))

plt.figure(figsize=(10, 6))
sns.barplot(x='Importancia', y='Feature', data=df_importancia.head(10))
plt.title('Importância das Features (Random Forest)')
plt.show()