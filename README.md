# RetailXpress_datawarehouse

## Project Overview
RetailXpress is a mid-sized retail company aiming to centralize data from multiple silos, reduce reliance on operational databases, and improve agility in decision-making. This project implements a dimensional warehouse using the Kimball methodology, ensuring scalability and efficiency for analytics.

## Objectives
- Enable unified insights across customer behavior, sales trends, and inventory management.
- Empower business teams with self-service analytics using BI tools like Tableau or Power BI.

## Architecture
The project follows a multi-layered architecture:

- Staging Layer: Raw data ingestion and transformation.
- Warehouse Layer: Dimensional modeling with star schemas.
- OBT Layer: Denormalized tables for optimized reporting.

## Key Features
- Centralized Dimensional Modeling: Star schemas for streamlined analytics.
- ETL/ELT Pipeline: Built with dbt and orchestrated for scalability.
- Error Handling: Automated tests and notifications for pipeline health.
- Self-Service BI Enablement: Pre-aggregated data for dashboards.

## Technologies Used
- Cloud Platform: Google BigQuery
- Data Transformation: dbt
- Orchestration: Apache Airflow
- Visualization: Tableau / Power BI
- Version Control: Git/GitHub

## Setup Instructions
- Clone the repository: `git clone https://github.com/NeonStone7/RetailXpress_datawarehouse.git`
`cd RetailXpress_datawarehouse`
- Configure profiles.yml to connect dbt to BigQuery.
- Run the dbt pipeline: `dbt run --select staging`
- Connect your BI tool (e.g., Tableau or Power BI) to the OBT layer for visualization.