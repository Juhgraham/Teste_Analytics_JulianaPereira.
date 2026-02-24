-- Parte 2: Consultas SQL para Análise de Vendas


-- Usando o dataset já importado, caso gere outro, os insights podem mudar.
-- Criei uma tabela vendas apartir do dataset com as colunas :
-- ID (INTEGER), Data (TDATE), Produto (VARCHAR), Categoria (VARCHAR), Quantidade (INTEGER), Preco (NUMERIC)
-- Ferramenta usada : Datagrip. 
-- Linguagem usada : PostgreSQL

-- 1. Listar o nome do produto, categoria e a soma total de vendas (Quantidade * Preço) 
--    para cada produto. Ordene o resultado pelo valor total de vendas em ordem decrescente.
SELECT 
    produto, 
    categoria, 
    SUM(quantidade * preco) AS faturamento_total
FROM 
    vendas
GROUP BY 
    produto, 
    categoria
ORDER BY 
    faturamento_total DESC;

-- Saída: Hidradante facial foi o produto com maior faturamento e 
-- o Gel de limpeza foi o produto com menor faturamento

-- 2. Identificar os produtos que venderam menos no mês de junho de 2024.
-- Obs: Como o dataset simulado é de 2023, e o enunciado pede junho de 2024, a resposta será vazia.
SELECT 
    produto, 
    SUM(quantidade) AS total_unidades_junho
FROM 
    vendas
WHERE 
    data >= '2024-06-01' AND data <= '2024-06-30'
GROUP BY 
    produto
ORDER BY 
    total_unidades_junho ASC;

-- Resposta: Não teve saída de dados. 

-- EXPLICAÇÃO DA LÓGICA (POSTGRESQL):
-- 1. SUM(quantidade * preco): Realiza o cálculo do faturamento total por linha e soma.
-- 2. GROUP BY produto, categoria: Agrupa os resultados em valores por produto.
-- 3. ORDER BY ... DESC: Organiza do maior faturamento para o menor.
-- 4. WHERE data >= ... AND data <= ...: Filtra especificamente o intervalo de junho de 2024.
-- 5. ORDER BY ... ASC: Organiza da menor quantidade vendida para a maior, identificando os que venderam menos.


----------------------------------- EXTRA --------------------------------------------------

-- 3. Listar o nome do produto, categoria e a soma total de vendas 
--(Quantidade * Preço) para cada produto.
-- Qual o produto com maior faturamento ?
SELECT 
    Produto, 
    SUM(Quantidade * Preco) AS Faturamento_Total
FROM 
    vendas
GROUP BY 
    Produto
ORDER BY 
    Faturamento_Total DESC
LIMIT 1;
-- Resposta  : Hidratante facial foi o mais vendido com o total de R$ 10793.4


-- 4. Listar produto com maior quantidade vendida
-- Qual produto teve a maior quantidade total de unidades vendidas?
SELECT
    produto,
    SUM(quantidade) AS Total_Unidades
FROM
    vendas
GROUP BY
    produto
ORDER BY
    Total_Unidades DESC
LIMIT 1;
-- Resposta : Hidratante facial também foi o produto mais vendido,
-- além de ter gerado o maior faturamento


-- 5. Pico de vendas do protetor solar.
-- Em qual mês o 'Protetor Solar' teve seu maior volume de vendas?
SELECT
    produto,DATE_PART('month', data) AS Mes,
    SUM(quantidade) AS Quantidade_Vendida
FROM
    vendas
WHERE
    produto = 'Protetor Solar'
GROUP BY
    Mes, produto
ORDER BY
    Quantidade_Vendida DESC
LIMIT 1;
-- Resposta : A maior quantidade de vendas do Protetor Solar
-- foi em abril, com 16 vendas.


-- 6. Mês com maior quantidade de vendas
-- Qual mês registrou o maior volume total de vendas (todas as categorias)?
SELECT
    DATE_PART('month', data) AS Mes,
    SUM(quantidade) AS Volume_Total
FROM
    vendas
GROUP BY
    Mes
ORDER BY
    Volume_Total DESC
LIMIT 1;
-- Resposta: O mês de março foi o que teve maior quantidade de vendas,
-- com o total de 40 vendas.


-- 7. Mês com maior faturamento(extra)
-- Qual mês registrou o maior faturamento total de vendas (todas as categorias)?
SELECT
    DATE_PART('month', data) AS Mes,
    SUM(preco) AS Faturamento
FROM
    vendas
GROUP BY
    Mes
ORDER BY
    Faturamento DESC
LIMIT 1;
-- Resposta: Março também foi o maior mês de faturamento com o total de
--R$ 953,00 de faturamento






