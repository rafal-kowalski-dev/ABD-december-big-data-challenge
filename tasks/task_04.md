<img src="task_04.png" alt="task image">

[English version](#basic-task-en)

# Podstawowe polecenie: 
Za nami ogrom pracy! Dane z surowych, nieorkrzesanych, są już nam podporządkowane i niewiele brakuje, aby zaczęły być użyteczne;-). Czas na załadowanie danych do relacyjnej bazy danych!

1. Zainstaluj PostgreSQL (lub jakąkolwiek inną bazę chcesz)
2. Utwórz schematy tabel które są odpowiednie dla Twoich parquetów
3. Stwórz joba sparkowego, który będzie indeksował dane do bazy danych

## Data zakończenia: 
29.12.2024

## Proponowane narzędzia: 
PostgreSQL (można wykorzystać dockera), Apache Spark + JDBC

## Dodatkowo dla ambitnych:
Przemyśl dokładnie jakie tabele mają być jak tworzone pod kątem optymalności. Nie tylko stwórz tabele, ale także napisz skrypt który je tworzy, aby można było zbudować zawsze "na nowo".

## Input (zasoby):
Tym razem brak. Pracujemy na tym co zostało z poprzedniego zadania;-)

## Uzasadnienie (co ćwiczymy i dlaczego):
1. Ćwiczymy setup technologii
2. Ćwiczymy kontakt z relacyjnymi bazami danych
3. Ćwiczymy ostatni etap ETL, czyli Load / indeksację

---

## Basic task (EN)
We've done a lot of work! The data has gone from raw and unprocessed to being under our control, and it's almost ready to become useful ;-). Time to load the data into a relational database!

1. Install PostgreSQL (or any other database of your choice)
2. Create table schemas appropriate for your parquet files
3. Create a Spark job that will index data into the database

## Completion date:
29.12.2024

## Suggested tools:
PostgreSQL (Docker can be used), Apache Spark + JDBC

## Additional challenge:
Think carefully about how the tables should be created for optimal performance. Don't just create the tables, but also write a script that creates them so they can always be built "from scratch".

## Input (resources):
None this time. We're working with what's left from the previous task ;-)

## Rationale (what we're practicing and why):
1. Practicing technology setup
2. Practicing interaction with relational databases
3. Practicing the final stage of ETL, namely Load / indexing