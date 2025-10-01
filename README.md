# 🌿 Eco-Afinidade: Análise Preditiva de Engajamento em ESG (Itaú)

## 🎯 Descrição do Projeto

O projeto **Eco-Afinidade** desenvolveu um modelo de Machine Learning (XGBoost) para prever a probabilidade de um cliente Itaú aderir a ofertas de **Finanças Sustentáveis** e **ESG** (Environmental, Social, and Governance).

O objetivo principal é transformar a estratégia de marketing de segmentação ampla para **hiperpersonalização preditiva**, garantindo máxima eficiência no uso do capital e acelerando as metas do Itaú.

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

*Atenção: Adicione a imagem do seu gráfico Barplot do XGBoost aqui!*

```markdown
