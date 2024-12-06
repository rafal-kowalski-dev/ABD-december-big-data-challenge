<img src="task_01.png" alt="task image">

# Podstawowe polecenie: 
Napisz aplikację, która pobiera dane z API pogodowego i zapisuje na dysk. Aplikacja powinna być parametryzowana, aby można było łatwo uruchomić, pobierając z różnych miast czy dat. W podstawie można zrobić pobieranie z określonych miast, z aktualnego momentu. Docelowo warto dodać też historię.

## Data zakończenia: 
10.12.2024

## Proponowane narzędzia: 
Scala, Python, biblioteki: requests (w obu przypadkach)

## Dodatkowo dla ambitnych:
 Całość można zapisywać na którymś z systemów plików, chmurowych lub on-premise. Proponowane to: HDFS, MinIO, AWS S3, Azure ADLS gen 2 (blob)

## Input (zasoby):
Link do proponowanego API pogodowego (można wybrać swoje), do tego dwa konkretne linki (wszystko w komentarzu)

## Uzasadnienie (co ćwiczymy i dlaczego):

1. Zapoznawanie się z API: Big Data to nie tylko logiczne transformacje. To także konieczność pracy z zewnętrznymi źródłami. Pierwszym etapem jest umiejętność wczytania się w to jak ktoś inny przygotował to co mamy pobrać.
2. Pobieranie z API: jak wyżej:-). Tyle, że tu już budujemy warsztat techniczny do pobierania danych.
3. Umiejętność budowania ETL (pierwszy etap – Extract).
4. Praca z surowymi danymi
5. Tworzenie kodu, który nie jest jednorazowym ćwiczeniem. Poprzez parametryzację chcemy dać możliwość wielokrotnego, a nawet częstego wykorzystania