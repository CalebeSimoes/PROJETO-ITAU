# 🌿 Eco-Afinidade: Análise Preditiva de Engajamento em ESG

## 🎯 Descrição do Projeto

O projeto **Eco-Afinidade** desenvolveu um modelo de Machine Learning (XGBoost) para prever a probabilidade de um cliente aderir a ofertas de **Finanças Sustentáveis** e **ESG** (Environmental, Social, and Governance).

O objetivo principal é transformar a estratégia de marketing de segmentação ampla para **hiperpersonalização preditiva**, garantindo máxima eficiência no uso do capital.

## 📈 Resultados Chave do Modelo (XGBoost)

O modelo foi treinado e calibrado com um *threshold* de **0.60**, mostrando um excelente equilíbrio entre Precisão e Recall nas previsões de adesão.

| Métrica de Performance | Valor | Avaliação de Negócio |
| :--- | :--- | :--- |
| **AUC-ROC Score** | **0.6725** | Capacidade preditiva estável e superior ao acaso. |
| **F1-Score (Adesão)** | **0.62** | Excelente equilíbrio, ideal para implantação em um projeto piloto. |
| **Recall (Adesão)** | **0.63** | O modelo captura 63% dos clientes que realmente aderem (ótimo para capturar oportunidades). |

---

## 🌟 Insights Estratégicos: Drivers de Adesão

A análise de importância de *features* revela que a **Afinidade Digital** é o motor de adesão, superando fatores puramente financeiros.

| Rank | Feature | Importância | Ação de Marketing Recomendada |
| :--- | :--- | :--- | :--- |
| **1º** | **COMPARTILHA_OPEN_FINANCE** | **25.2%** | **Estratégia Prioritária:** Focar a aquisição de *leads* ESG em clientes que utilizam o **Open Finance**, pois demonstram alta confiança e engajamento. |
| **2º** | **INTERESSE_CONTEUDO_ESG** | 13.0% | **Personalização:** Usar o consumo prévio de conteúdo como *trigger* imediato para a oferta (Funil: Conteúdo $\rightarrow$ Oferta). |
| **3º** | **HISTORICO_ADESAO_SUSTENTAVEL** | 10.0% | **Fidelidade e Upsell:** Priorizar estes clientes para ofertas de produtos ESG mais sofisticados. |

### Visualização: Importância das Features

<img width="1440" height="795" alt="image" src="https://github.com/user-attachments/assets/c51f49d8-0986-45da-bd49-3fca0565e444" />


```markdown

🛠️ Como Rodar o Projeto
Pré-requisitos
Certifique-se de ter o ambiente Python configurado com as seguintes bibliotecas:

Bash

pip install pandas numpy scikit-learn xgboost matplotlib seaborn
Execução
Salve o código principal do modelo (eco_afinidade.py).

Execute o script via terminal:

Bash

python eco_afinidade.py
O script irá gerar o dataset simulado, treinar o modelo e imprimir as métricas finais.
