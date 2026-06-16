# Data Pipeline Dataflow Diagram

```mermaid
graph TD
    A["📥 PostgreSQL<br/>Database"]
    B["📥 CSV<br/>Files"]
    C["📥 API<br/>Data"]
    
    D["⚙️ Data Ingestion<br/>Python"]
    E["⚙️ Data Transformation<br/>PySpark"]
    
    F["💾 Data Lake<br/>Parquet Format"]
    
    G["📊 Data Warehouse"]
    H["📊 BI/Reporting"]
    I["📊 Analytics"]
    
    A -->|Raw Data| D
    B -->|Raw Data| D
    C -->|Raw Data| E
    
    D -->|Cleaned Data| E
    E -->|Transformed Data| F
    
    F -->|Processed Data| G
    F -->|Processed Data| H
    F -->|Processed Data| I
    
    style A fill:#E1D5F7,stroke:#9673A6,stroke-width:2px
    style B fill:#E1D5F7,stroke:#9673A6,stroke-width:2px
    style C fill:#E1D5F7,stroke:#9673A6,stroke-width:2px
    
    style D fill:#D4E6F1,stroke:#5499C7,stroke-width:2px
    style E fill:#D4E6F1,stroke:#5499C7,stroke-width:2px
    
    style F fill:#FCF3CF,stroke:#D4AF37,stroke-width:2px
    
    style G fill:#D5F4E6,stroke:#52BE80,stroke-width:2px
    style H fill:#D5F4E6,stroke:#52BE80,stroke-width:2px
    style I fill:#D5F4E6,stroke:#52BE80,stroke-width:2px
```

## Legend

| Component | Color | Description |
|-----------|-------|-------------|
| 📥 **Data Sources** | Purple | Raw data inputs (DB, files, APIs) |
| ⚙️ **Processing** | Blue | Data processing/transformation logic |
| 💾 **Storage** | Gold | Intermediate data storage |
| 📊 **Output** | Green | Final data destinations |

## Data Flow Steps

1. **Ingestion** → PostgreSQL, CSV, and API data are collected
2. **Processing** → Python cleans the data, PySpark transforms it
3. **Storage** → Transformed data lands in Data Lake (Parquet)
4. **Distribution** → Data flows to Warehouse, BI tools, and Analytics
