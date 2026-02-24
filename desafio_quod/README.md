Teste de Analytics - Quod 🧴📊

Olá! Este repositório contém a minha resolução para o teste de Estagiário de Analytics da Quod. Aqui, busquei não apenas resolver os problemas técnicos, mas também trazer uma visão analítica sobre os dados de um negócio de Skincare(tema por mim escolhido).

🚀 O que você vai encontrar aqui?

O projeto foi dividido em três grandes etapas, cada uma com seu foco e ferramentas:

1. Programação em Python (Simulação e Limpeza)

Nesta parte, criei um script que simula o dia a dia de uma loja de Skincare em 2023.

•
analise_vendas_limpeza.py: Gera o dataset, trata valores nulos (usando média/mediana) e remove duplicatas.

•
analise_exploratoria_vendas.py: Aqui gerei o gráfico de tendência mensal e identifiquei os primeiros padrões de comportamento dos "clientes".

2. Consultas SQL (PostgreSQL)

Utilizei o DataGrip para rodar consultas em PostgreSQL e extrair insights.

•
consultas_sql.sql: Contém as consultas que respondem aos desafios do teste e também alguns "extras" que fiz para entender melhor o faturamento e a sazonalidade dos produtos.

•
Nota: Como o dataset simulado é de 2023, a consulta para Junho de 2024 (conforme o enunciado) retorna vazia, mas a lógica está 100% correta e pronta para dados reais!

3. Interpretação de Resultados

•
relatorio_insights.pdf: Um breve relatório onde traduzi os números em ações práticas para o negócio.

🛠️ Como rodar o projeto?

Se você quiser ver os scripts em ação, basta seguir estes passos:

1.
Instale as bibliotecas necessárias:

Bash


pip install pandas matplotlib





2.
Execute a limpeza e geração de dados:

Bash


python dataset.py





3.
Gere as visualizações:

Bash


python analise_exploratoria.py





💡 Minhas Descobertas

Durante o teste, percebi que o Hidratante Facial é o grande motor do faturamento, e que o mês de Março foi o período de maior sucesso da operação. Essas descobertas me ajudaram a sugerir ações reais, como a criação de kits promocionais.

Espero que gostem da minha abordagem! Estou à disposição para conversarmos sobre qualquer detalhe do projeto. 😊

Candidato: Juliana Pereira Costa

