# 🌿 Eco-Afinidade: Análise Preditiva de Engajamento em ESG (Itaú)

## 🎯 Descrição do Projeto

O projeto **Eco-Afinidade** desenvolveu um modelo de Machine Learning (XGBoost) para prever a probabilidade de um cliente Itaú aderir a ofertas de **Finanças Sustentáveis** e **ESG** (Environmental, Social, and Governance).

A missão é mover a estratégia de marketing de ESG de segmentação ampla para **hiperpersonalização preditiva**, garantindo máxima eficiência no uso do capital e acelerando as metas de mobilização de R$ 1 Tri.

## 📈 Resultados Chave do Modelo (XGBoost)

O modelo foi treinado com um dataset sintético de 10.000 amostras e calibrado com um *threshold* de **0.60** para otimizar o equilíbrio entre Precisão e Recall.

| Métrica de Performance | Valor | Avaliação de Negócio |
| :--- | :--- | :--- |
| **AUC-ROC Score** | **0.6725** | Capacidade estável e preditiva, superior ao acaso. |
| **F1-Score (Adesão)** | **0.62** | Excelente equilíbrio entre Precisão (0.61) e Recall (0.63). |
| **Recall (Adesão)** | **0.63** | O modelo captura 63% dos clientes que realmente aderem (ótimo para capturar oportunidades). |

## 🌟 Insights Estratégicos: Os Drivers de Adesão

A análise de importância de *features* revela quais fatores o modelo considera mais relevantes para a adesão, orientando as decisões de investimento em marketing.

| Rank | Feature | Importância | Ação de Marketing Recomendada |
| :--- | :--- | :--- | :--- |
| **1º** | **COMPARTILHA_OPEN_FINANCE** | **25.2%** | **Estratégia Prioritária:** Incentivar o uso do Open Finance como funil de entrada para ofertas ESG. É o preditor mais forte. |
| **2º** | **INTERESSE_CONTEUDO_ESG** | 13.0% | **Personalização:** Usar o consumo prévio de conteúdo (blog, vídeos) como *trigger* imediato para a oferta. |
| **3º** | **HISTORICO_ADESAO_SUSTENTAVEL** | 10.0% | **Fidelidade e Upsell:** Priorizar clientes com engajamento ESG comprovado para ofertas de maior valor. |

## 🛠️ Requisitos e Como Rodar o Projeto

### Pré-requisitos
Certifique-se de ter o ambiente Python configurado com as seguintes bibliotecas:
```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn
