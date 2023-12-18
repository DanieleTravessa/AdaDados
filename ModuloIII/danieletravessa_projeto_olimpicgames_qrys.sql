/*- Após todas as tabelas da base de dados terem sido criadas, executar as seguintes queries dentro do próprio PgAdmin. Lembrando que todas as respostas devem ser acompanhadas de comentários, indicando o raciocínio feito:
1 - Quantas medalhas cada país conseguiu no total desde 1990?
2 - TOP 3 atletas que ganharam mais medalhas de ouro? TOP 3 medalhas de prata? TOP3 medalhas de bronze?
3 - Qual a lista de todas as modalidades existentes? A partir de que ano elas foram introduzidas nas olimpíadas?
4 - Quantas medalhas de ouro, prata e bronze cada país ganhou no vôlei (tanto masculino, quanto feminino)? Não é necessário mostrar países que nunca ganharam uma medalha no esporte.
5 - Qual a média de atletas por ano a partir de 1920 (separar verão de inverno).
EXTRA (200XP)
6 - Proporção de homens e mulheres antes e depois de 1950 (compare e explique).*/

--Consultas:

--1. Quantas medalhas cada país conseguiu no total desde 1990?

SELECT
    athlete.noc,
    COUNT(*) AS medal_total
FROM
    medal
JOIN
    athlete ON medal.athlete_id = athlete.id
WHERE
    medal.year >= 1990
GROUP BY
    athlete.noc
ORDER BY
    meda_total DESC;
	
--2. TOP 3 atletas que ganharam mais medalhas de ouro? TOP 3 medalhas de prata? TOP3 medalhas de bronze?

--Top 3 Medalhas de Ouro:

SELECT
    athlete.name,
    COUNT(*) AS gold_total
FROM
    medal
JOIN
    athlete ON medal.athlete_id = athlete.id
WHERE
    medal.medal = 'Gold'
GROUP BY
    athlete.name
ORDER BY
    gold_total DESC
LIMIT 3;

--Top 3 Medalhas de Prata:

SELECT
    athlete.name,
    COUNT(*) AS silver_total
FROM
    medal
JOIN
    athlete ON medal.athlete_id = athlete.id
WHERE
    medal.medal = 'Silver'
GROUP BY
    athlete.name
ORDER BY
    silver_total DESC
LIMIT 3;

--Top 3 Medalhas de Bronze:

SELECT
    athlete.name,
    COUNT(*) AS bronze_total
FROM
    medal
JOIN
    athlete ON medal.athlete_id = athlete.id
WHERE
    medal.medal = 'Bronze'
GROUP BY
    athlete.name
ORDER BY
    bronze_total DESC
LIMIT 3;

--3. Qual a lista de todas as modalidades existentes? A partir de que ano elas foram introduzidas nas Olimpíadas?

SELECT
    event.name AS event,
    MIN(medal.year) AS ano_introducao
FROM
    modalidades
JOIN
    medalhas ON modalidades.id = medalhas.modalidades_id
GROUP BY
    modalidades.nome
ORDER BY
    ano_introducao;
	
--4. Quantas medalhas de ouro, prata e bronze cada país ganhou no vôlei (tanto masculino, quanto feminino)? Não é necessário mostrar países que nunca ganharam uma medalha no esporte.

SELECT
    atletas.noc,
    COUNT(CASE WHEN medalhas.medalha = 'Gold' THEN 1 END) AS ouro,
    COUNT(CASE WHEN medalhas.medalha = 'Silver' THEN 1 END) AS prata,
    COUNT(CASE WHEN medalhas.medalha = 'Bronze' THEN 1 END) AS bronze
FROM
    medalhas
JOIN
    atletas ON medalhas.atletas_id = atletas.id
JOIN
    modalidades ON medalhas.modalidades_id = modalidades.id
JOIN
    esportes ON modalidades.esportes_id = esportes.id
JOIN
    regioes ON esportes.regiao_id = regioes.id
WHERE
    esportes.nome = 'Volleyball'
GROUP BY
    atletas.noc
HAVING
    COUNT(CASE WHEN medalhas.medalha IN ('Gold', 'Silver', 'Bronze') THEN 1 END) > 0;
	
	
--5. Qual a média de atletas por ano a partir de 1920 (separar verão de inverno)?

SELECT
    temporada,
    ano,
    ROUND(AVG(total_atletas)) AS media_atletas
FROM (
    SELECT
        esportes.temporada,
        medalhas.ano,
        COUNT(DISTINCT atletas.id) AS total_atletas
    FROM
        medalhas
    JOIN
        atletas ON medalhas.atletas_id = atletas.id
    JOIN
        modalidades ON medalhas.modalidades_id = modalidades.id
    JOIN
        esportes ON modalidades.esportes_id = esportes.id
    WHERE
        medalhas.ano >= 1920
    GROUP BY
        esportes.temporada, medalhas.ano
) AS subquery
GROUP BY
    temporada, ano
ORDER BY
    temporada, ano;
	
	
-- 6. Proporção de homens e mulheres antes e depois de 1950 (compare e explique).

SELECT
    atletas.genero, #Seleciona a coluna gênero da tabela atletas.
    COUNT(CASE WHEN medalhas.ano < 1950 THEN 1 END) AS total_antes_1950, #Conta o número de casos em que o ano da medalha é anterior a 1950 por gênero.
    COUNT(CASE WHEN medalhas.ano >= 1950 THEN 1 END) AS total_depois_1950, #Conta o número de casos em que o ano da medalha é igual ou posterior a 1950 por gênero.
    ROUND(COUNT(CASE WHEN medalhas.ano < 1950 THEN 1 END) * 100.0 / NULLIF(COUNT(CASE WHEN medalhas.ano >= 1950 THEN 1 END), 0), 2) AS proporcao_antes_1950 #Calcula a proporção de medalhas antes de 1950 em relação ao total de medalhas após 1950.
FROM
    atletas #Da tabela atletas.
JOIN
    medalhas ON atletas.id = medalhas.atletas_id #Une as tabelas atletas e medalhas com base na correspondência entre atletas.id e medalhas.atletas_id.
WHERE
    atletas.genero IS NOT NULL #Filtra apenas registros com a informação de gênero.
GROUP BY
    atletas.genero; --Agrupa os resultados pela coluna gênero.