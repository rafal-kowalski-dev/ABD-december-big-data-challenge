<img src="task_03.png" alt="task image">

[English version](#basic-task-en)

# Podstawowe polecenie:
Przed nami być może najtrudniejsze zadanie. Mamy już dane surowe, które są uporządkowane i dostarczone w formie, jaką chcemy uzyskać. Teraz Twoim zadaniem jest poddać te dane modyfikacji, transformacji i uzyskać finalny kształt. Chodzi o to, żebyśmy mogli na końcu uzyskać z nich informacje. Całość zapisz do osobnych plików typu parquet w wybranym przez Ciebie miejscu. Przykładowe rzeczy, które można uzyskać:

- Zbiór najważniejszych danych dla wszystkich miast w ramach jednego zbioru.
- Zbiór z rankingiem miast z najwyższą temperaturą, najwyższą wilgotnością itd.
- Zestawienie średnich temperatur dla danego miasta (może też byc przygotowany mechanizm dla średnich temperatur dla danego miesiąca w konkretnym miescie)

## Data zakończenia:
22.12.2024

## Proponowane narzędzia:
Apache Spark (język obojętny)

## Dodatkowo dla ambitnych:
Cokolwiek przyjdzie Ci do głowy. Pomyśl jakie dane chcesz mieć finalnie i… działaj!

## Input (zasoby):
paczka z przykładowymi plikami wejściowymi typu Parquet dostępna w komentarzu

## Uzasadnienie (co ćwiczymy i dlaczego):

1. Transform to drugi etap architektury ETL. Wewnątrz niego łączymy zbiory, filtrujemy, przetwarzamy, wyciągamy statystyki. I właśnie nad tym etapem pracujemy w tym zadaniu.
2. Pracujemy tutaj nad umiejętnościami budowania operacji logicznych w sparku.
3. Dodatkowo pracujemy nad umiejętnością spojrzenia częściowo "z lotu ptaka", aby określić czego dokładnie potrzebujemy i gdzie to ma się znaleźć.

---

## Basic task (EN)
This might be our most challenging task yet. We already have raw data that is organized and delivered in the format we want. Now your task is to modify and transform this data to achieve its final shape. The goal is to extract meaningful information from it. Save everything to separate Parquet files in a location of your choice. Here are some examples of what you can achieve:

- A collection of the most important data for all cities in a single dataset.
- A dataset ranking cities by highest temperature, highest humidity, etc.
- A compilation of average temperatures for a given city (can also include a mechanism for average temperatures for a specific month in a specific city)

## Completion date:
22.12.2024

## Suggested tools:
Apache Spark (language is optional)

## Additional challenge:
Whatever comes to your mind. Think about what data you want to have in the end and... go for it!

## Input (resources):
A package with sample input Parquet files available in the comments

## Rationale (what we're practicing and why):

1. Transform is the second stage of ETL architecture. Within it, we combine datasets, filter, process, and extract statistics. And this is exactly what we're working on in this task.
2. We're working on building logical operations skills in Spark.
3. Additionally, we're practicing the ability to look at things from a "bird's eye view" to determine exactly what we need and where it should go.