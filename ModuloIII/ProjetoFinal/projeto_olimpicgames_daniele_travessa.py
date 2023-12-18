'''                             Projeto Final - Banco de Dados
- Utilizar a base de dados dos Jogos Olímpicos mostrada em sala de aula, e que pode ser acessada pelo link abaixo:
https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results
- Carregar o dataset utilizando o Python (usando parte do código mostrado em sala), ou seja, CREATE TABLEs e INSERTs serão feitos através do código, e seguindo a modelagem de dados disponível no drive da turma;'''
import psycopg2
import csv
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory

conn = psycopg2.connect("host=localhost dbname=projeto_olimpicgames_danieletravessa user=postgres password=1234")
qry = conn.cursor()

qry.execute("""
    CREATE TABLE IF NOT EXISTS region (
        id SERIAL PRIMARY KEY,
        noc CHAR(3),
        region VARCHAR(150),
        notes VARCHAR(150),
        CONSTRAINT unique_noc_region UNIQUE (noc, region)
    );
""")

try:
    with open('ModuloIII\\ProjetoFinal\\noc_regions.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            qry.execute("""
                INSERT INTO region (noc, region, notes)
                VALUES (%s, %s, %s)
                ON CONFLICT ON CONSTRAINT unique_noc_region DO NOTHING;
                """, (row[0], row[1], row[2]))
except FileNotFoundError:
    msg = "O arquivo mencionado não foi encontrado!"
    print(msg)

qry.execute("""
    CREATE TABLE IF NOT EXISTS team (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        noc CHAR(3),
        CONSTRAINT unique_team_noc UNIQUE (name, noc)
        );
    """)

qry.execute("""
    CREATE TABLE IF NOT EXISTS athlete (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        gender CHAR(1),
        age INTEGER,
        height NUMERIC,
        weight NUMERIC,
        noc CHAR(3),
        team_id INTEGER REFERENCES team(id),
        CONSTRAINT unique_name_noc UNIQUE (name, noc)
        );
    """)

qry.execute("""
    CREATE TABLE IF NOT EXISTS sport (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        season CHAR(6),
        region_id INTEGER REFERENCES region(id),
        CONSTRAINT unique_name_season_region_id UNIQUE (name, season, region_id)
        );
    """)

qry.execute("""
    CREATE TABLE IF NOT EXISTS event (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        sport_id INTEGER REFERENCES sport(id),
        CONSTRAINT unique_name_sport_id UNIQUE (name, sport_id)
    );
""")

qry.execute("""
    CREATE TABLE IF NOT EXISTS medal (
        id SERIAL PRIMARY KEY,
        athlete_id INTEGER REFERENCES athlete(id),
        event_id INTEGER REFERENCES event(id),
        medal VARCHAR(10),
        year INTEGER,
        CONSTRAINT unique_athlete_event UNIQUE (athlete_id, event_id)
    );
""")
try:
    with open('ModuloIII\\ProjetoFinal\\athlete_events.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Pular o cabeçalho
        for row in reader:
        # Verificar se há "NA" em colunas específicas
            if 'NA' not in [row[3], row[4], row[5]]:
                age = int(row[3]) if row[3] != 'NA' else None

                qry.execute("""
                    INSERT INTO team (name, noc)
                    VALUES (%s, %s)
                    ON CONFLICT ON CONSTRAINT unique_team_noc DO NOTHING;
                    """, (row[6], row[7]))

                qry.execute("""
                    INSERT INTO athlete (name, gender, age, height, weight, noc, team_id)
                    VALUES (%s, %s, %s, %s, %s, %s, (SELECT id FROM team WHERE name = %s AND noc = %s LIMIT 1))
                    ON CONFLICT ON CONSTRAINT unique_name_noc DO NOTHING;
                    """, (row[1], row[2], age, row[4], row[5], row[7], row[6], row[7]))

                qry.execute("""
                    INSERT INTO sport (name, season, region_id)
                    VALUES (%s, %s, (SELECT id FROM region WHERE noc = %s LIMIT 1))
                    ON CONFLICT ON CONSTRAINT unique_name_season_region_id DO NOTHING;
                    """, (row[12], row[10], row[7]))

                qry.execute("""
                    INSERT INTO event (name, sport_id)
                    VALUES (%s, (SELECT id FROM sport WHERE name = %s AND season = %s LIMIT 1))
                    ON CONFLICT ON CONSTRAINT unique_name_sport_id DO NOTHING;
                    """, (row[13], row[12], row[10]))

                qry.execute("""
                    INSERT INTO medal (athlete_id, event_id, medal, year)
                    VALUES (
                        (SELECT id FROM athlete WHERE name = %s AND noc = %s LIMIT 1),
                        (SELECT id FROM event WHERE name = %s AND sport_id = (SELECT id FROM sport WHERE name = %s AND season = %s LIMIT 1) LIMIT 1),
                        %s, %s
                        ) ON CONFLICT ON CONSTRAINT unique_athlete_event DO NOTHING;
                    """, (row[1], row[7], row[13], row[12], row[10], row[14], row[9]))
            
except FileNotFoundError:
    msg = "O arquivo mencionado não foi encontrado!"
    print(msg)

conn.commit()
qry.close()
conn.close()