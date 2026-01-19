
# Python – Quality & COPQ Analytics

This module reproduces the key Quality & COPQ insights using the same datasets used by SQL and Power BI.

## 📂 Inputs
CSV files:
- `fact_invoices.csv` → columns: `invoice_id, invoice_name, created_date, program, product, issue, supplier, cost, status, payment_date`
- `fact_claims.csv`   → columns: `claim_id, claim_date, program, product, issue, color_status`

> In this repo, these CSVs live under `sql/data/` (see the main README).  
> The script can also run when both CSVs are in the same folder as the `.py`.

## 🧮 Analyses
- COPQ per month (line)
- Paid vs Unpaid (bar)
- Claims Pareto by Issue (bar)
- COPQ by Issue (bar)
- Simple integration: Claims ↔ Invoices (join by Program + Issue + Month), exported as CSV sample

## 🖼 Outputs
Saved in `./outputs/`:
- `copq_month.png`
- `paid_vs_unpaid.png`
- `claims_pareto.png`
- `copq_by_issue.png`
- `claims_invoices_sample.csv`

## ▶️ How to Run
```bash
# option A — CSVs in the SAME folder as the script
python python_copq_analysis.py

# option B — CSVs in ../sql/data/ (recommended repo structure)
# use the version that builds paths via Path(__file__) → HERE/REPO_ROOT/DATA_DIR
python python_copq_analysis.py
