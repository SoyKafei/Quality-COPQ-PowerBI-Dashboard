An end‑to‑end analytics project for Manufacturing Quality (Claims) and COPQ (Cost of Poor Quality) using a clean Star Schema, SQL analysis, Python automation, and a reusable Power BI dashboard template.
This repository is designed as a complete data portfolio project for Data Analyst / BI Analyst / Quality Engineering roles.

---

## 📌 Key Features

### ✔ Quality Issue Analysis
- Total claims overview  
- Monthly claims trend  
- Claims by program  
- Claims by harness (product family)  
- Claims by failure mode (Issue A–F)  
- Item/connector/component frequency chart  

### ✔ COPQ (Cost of Poor Quality) Analysis
- Monthly COPQ trend  
- Total annual COPQ  
- Paid vs. unpaid invoices  
- COPQ by program  
- COPQ by failure mode (Pareto-friendly)  

### ✔ Interactivity
- Slicers for Program, Product (Harness), Issue, Status, and Month  
- Dynamic tooltips  
- Dynamic titles  
- Clean reusable theme via custom `PortfolioTheme.json`  
- Works with ANY dataset following the same structure  

---

## 📐 Data Model (Star Schema)

This project uses a **professional dimensional model**, which improves performance, filtering logic, and scalability.

### **Dimension Tables**
- **DimDate** → complete calendar table  
- **DimProgram** → Program A, Program B  
- **DimProduct** → Harness A, Harness B, Harness C  
- **DimIssue** → Issue A–F  
- **DimStatus** → PAID / UNPAID  

### **Fact Tables**
- **FactClaims** → claim-level quality issue records  
- **FactInvoices** → invoice-level COPQ amounts  

---

## 🧩 Files Included

| File | Description |
|------|-------------|
| `Quality_COPQ_Portfolio.pbit` | Main template (recommended for reuse) |
| `Quality_COPQ_Portfolio.pbix` | Optional demo version with sample data |
| `/screenshots/` | Report preview images |

---

## 📊 Screenshots

| Overview | COPQ Page | About Page |
|----------|-----------|------------|
| screenshots/Quality Screenshot.png | screenshots/COPQ Screenshot.png | screenshots/About this



## 🛠 Skills Demonstrated
- Power BI Desktop  
- DAX (Measures & Calculated Logic)  
- Power Query (ETL / Data Shaping)  
- Dimensional Modeling (Star Schema)  
- Dashboard UX & Visual Design  
- Quality Engineering & COPQ Analytics  

---

## 📥 How to Use This Template

1. Download the `.pbit` file  
2. Open it in Power BI Desktop  
3. Load your own tables  
4. The visuals, measures, and model will automatically adapt  
5. You now have a reusable Quality & COPQ dashboard  

---

## 👤 Author
**Armando Barron**  
Quality Lead Engineering / Data Analyst  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Armando%20Barron-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/armando-barron-garcia-7777a91b1/)
[![Email](https://img.shields.io/badge/Email-manzanerobarron%40gmail.com-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:manzanerobarron@gmail.com)


---
``
