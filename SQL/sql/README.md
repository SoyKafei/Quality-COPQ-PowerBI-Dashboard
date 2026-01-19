
# SQL – Manufacturing Quality & COPQ Analysis

This project demonstrates data modeling, analytical SQL, and star‑schema design using real anonymized manufacturing data.  
It covers *Claims* (quality issues reported) and *COPQ* (Cost of Poor Quality).

All scripts and datasets are included to fully reproduce the project.

---

## 📐 Data Model – Star Schema

This project implements a clean star‑schema architecture:

### 🟩 Dimension Tables
- `DimProgram`  
- `DimProduct`  
- `DimIssue`  
- `DimStatus`

### 🟦 Fact Tables
- `FactClaims` — claim events reported in a manufacturing environment  
- `FactInvoices` — COPQ entries linked to issues and suppliers  

The full schema is defined in **`schema.sql`**.

---

## 📊 Analytical SQL Included

All analysis queries are stored in **`analysis_queries.sql`**.

### ✔ Claims Analysis (Quality Issues)
- Issue Pareto (Top failure modes)
- Claims per program  
- Monthly claims trend  
- Claims by product  

### ✔ COPQ Analysis (Cost of Poor Quality)
- COPQ per month  
- Paid vs Unpaid spend  
- COPQ by issue and by program  
- Supplier‑level cost contribution  

### ✔ Integrated Analysis
- Claims ↔ Invoices join (root‑cause cost tracing)
- Star‑schema views for simplified reporting

---

## 🖼 Screenshots (SQL Output)

| Claims Pareto | COPQ Monthly Trend | Paid vs Unpaid |
|---------------|--------------------|-----------------|
| `screenshots/claims_pareto.png` | `screenshots/copq_month_query.png` | `screenshots/paid_vs_unpaid.png` |

| Join Analysis | Star‑Schema View |
|---------------|------------------|
| `screenshots/join_claims_invoices.png` | `screenshots/view_star_model.png` |

## 🛠 How to Reproduce

1. Open **`schema.sql`** in MySQL Workbench.  
2. Execute the script to create all DIM and FACT tables.  
3. Import each CSV file using *Table Data Import Wizard*:
   - `fact_claims.csv` → `FactClaims`
   - `fact_invoices.csv` → `FactInvoices`
   - Dim CSV files → corresponding dimension tables  
4. Execute the queries in **`analysis_queries.sql`**.  
5. Review results or screenshots inside `sql/screenshots/`.

---

## 🎯 Purpose of the Project

This project demonstrates real‑world SQL skills required for:

- Data Analyst  
- Business Intelligence Analyst  
- Operations / Manufacturing Analyst  
- Quality Engineer (with data focus)  

Key skills demonstrated:

- Star‑schema design  
- Data cleaning and transformation  
- Analytical SQL (GROUP BY, JOINs, DATE functions)  
- Quality & COPQ metrics  
- Manufacturing performance analysis  
- Reproducible data project structure  

---

## 📩 Contact

Feel free to reach out if you want to run the dataset, extend the analysis, or integrate it with Python or Power BI.
