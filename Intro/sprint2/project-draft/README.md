# Car dataset normalization and ingestion

## Project Overview

This repository contains the notebook and post-ingestion scripts for ingesting harvested data from last year. The purpose of this project is to establish dedicated postgreSQL instance and data warehouse-like repository for data analysis department.

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Data](#data)
- [Data Preprocessing](#data-preprocessing)
- [Conclusion](#conclusion)

## Getting Started

### Prerequisites

To start the process one needs to have pqsl installed and active with default setting - runnning on localhost on port 5432 and with postgres username and password.

Required python packages are:
- ipython==8.14.0
- numpy==1.25.0
- pandas==2.0.3
- SQLAlchemy==2.0.19

## Project Structure

Project consists of:
1. `data.csv` - scraped data
2. `ingestion.ipynb` - notebook holding the processes for reading, cleaning and normalizing the data. Finally it writes it to two tables in the db.
3. `script.sql` - The script should take care of establishing primary keys and their non-nullability (1NF) as well as create a `data_analyst_01` user with sufficient privilages.

## Usage

1. Install the required dependencies:
pip install -r requirements.txt
2. Run the following script in the project folder:
```
ipython -c "%run ingestion.ipynb"
psql cars -h 127.0.0.1 -U postgres -p 5432
```
and execute the following command inside psql:
```
\i script.sql
```

## Data

The car data was harvested last one by one of the interns. It contains quite few problematic format and entries that are addressed as much as possible in the notebook.

Remarks:

- it was detected that KMPL column contains mainly numeric values, however there were 3 entries containing irrelevant text data. This resulted in conversion of the text entry to NaN value, hence KMPL column in the DB needs to allow null values.
- original `engine_type` column held information about the engine in a format that resembled a description (commas, full sentences, non-consitent attributes of the engine enlisted). Hence it was not considered a violation of 1NF (due to many commas that could indicate multiple entries in one cell) and treated more as TEXT datatype and converted to `engine_description`.

## Data preprocessing
To conform with 2NF - "Each non-key attribute depends solely on the primary key." - it was decided to split the dataset into two tables. Moreover data contained explicit duplicates (all attributes the same), which were removed from the original dataset.

1. `sold_cars` holding information about about specific cars and their customized settings (fx. gearbox, color, price). Primary key is the `ìndex` and references with foreign key to the specific `model_details` entry. 
2. `model_details` holding information that are solely dictated by the car model (fx. shape, power, producer). Primary key is the unique `series`-name resulting in 376 unique car series available at the shop.
