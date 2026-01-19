
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

---

## 🗂 Project Structure
