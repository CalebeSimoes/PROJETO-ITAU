🌿 Eco-Afinidade: Análise Preditiva de Engajamento em ESG (Itaú)
🎯 Objetivo do Projeto
Construir um modelo de Machine Learning para prever a probabilidade de um cliente Itaú aderir a uma iniciativa ou produto de Sustentabilidade/ESG (ex: Fundos Verdes, Programas de Impacto Social).

A missão é hiperpersonalizar a comunicação, reduzindo o custo de marketing e acelerando a meta do Itaú de mobilizar 1 Trilhões em finanças sustentáveis até 2030.

📈 Sumário dos Resultados do Modelo
O modelo de classificação XGBoost foi treinado com um dataset sintético de 10.000 amostras, simulando características financeiras, comportamentais e dados de Open Finance.

Métrica de Performance

Valor

Insights

AUC-ROC Score

0.6725

Capacidade moderada e estável de discriminação entre as classes.

F1-Score (Adesão/Classe 1)

0.62

Indica um bom equilíbrio entre Precisão e Recall, ideal para um rollout piloto.

🌟 Principais Drivers de Negócio (Feature Importance)
O modelo revelou que a Afinidade Digital é o principal fator de adesão ESG, superando Renda e Segmento.

Rank

Feature

Importância

Ação Estratégica Sugerida

1º

COMPARTILHA_OPEN_FINANCE

25.2%

Prioridade Máxima: Incentivar o uso do Open Finance como funil de entrada para ofertas ESG.

2º

INTERESSE_CONTEUDO_ESG

13.0%

Usar o histórico de consumo de conteúdo para personalizar a comunicação de venda.

3º

HISTORICO_ADESAO_SUSTENTAVEL

10.0%

Direcionar upsells e novas ofertas a clientes com engajamento ESG comprovado.

📊 EDA Principal: Taxa de Adesão por Compartilhamento de Open Finance
O gráfico gerado na Análise Exploratória (EDA) demonstra visualmente o insight mais importante: clientes que compartilham dados Open Finance possuem uma taxa de adesão a ESG significativamente maior, validando o Rank 1 da Importância de Features.

<img width="1440" height="798" alt="image" src="https://github.com/user-attachments/assets/182582b4-ecbb-45cf-9f59-7f988f869f70" />


🛠️ Como Rodar o Código (Simulação)
Pré-requisitos
Python 3.8+

Bibliotecas: pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn.

Passos
Clone o repositório:

# Se estivesse no GitHub:
# git clone <link-do-seu-repo>
# cd eco-afinidade

Instale as dependências:

pip install pandas numpy scikit-learn xgboost matplotlib seaborn

Execute o script principal (eco_afinidade.py - simulado neste ambiente):

python eco_afinidade.py

O script irá gerar o dataset simulado, realizar a engenharia de features, treinar o modelo XGBoost, e imprimir todas as métricas de performance (AUC, F1-Score) e o ranking de Importância de Features.
