
# python_copq_analysis.py
# -------------------------------------------
# Quality & COPQ Analytics (Python module)
# Lee los CSV del MISMO folder y guarda gráficas en ./outputs
# Autor: Armando Barron

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# ---------- Paths: todo en el mismo directorio ----------
HERE = Path(__file__).resolve().parent          # carpeta donde está el .py
OUT_DIR = HERE / 'outputs'                      # /outputs (se crea si no existe)
OUT_DIR.mkdir(parents=True, exist_ok=True)

INVOICES_CSV = HERE / 'fact_invoices.csv'
CLAIMS_CSV   = HERE / 'fact_claims.csv'

print('[INFO] Loading CSVs ...')
print(f'[DEBUG] Invoices file exists? {INVOICES_CSV.exists()} -> {INVOICES_CSV}')
print(f'[DEBUG] Claims file   exists? {CLAIMS_CSV.exists()} -> {CLAIMS_CSV}')

# ---------- Load ----------
# Ajusta los nombres si tus encabezados difieren.
invoices = pd.read_csv(INVOICES_CSV, parse_dates=['created_date', 'payment_date'])
claims   = pd.read_csv(CLAIMS_CSV,   parse_dates=['claim_date'])

print(f'[INFO] Invoices shape: {invoices.shape}')
print(f'[INFO] Claims   shape: {claims.shape}')

# Normaliza nombres
invoices.columns = [c.strip().lower() for c in invoices.columns]
claims.columns   = [c.strip().lower() for c in claims.columns]

# Si 'cost' trae comas como miles, descomenta:
# invoices['cost'] = (invoices['cost'].astype(str)
#                                   .str.replace(',', '', regex=False)
#                                   .astype(float))

# ---------- Transformaciones ----------
invoices['month'] = invoices['created_date'].dt.to_period('M').astype(str)
claims['month']   = claims['claim_date'].dt.to_period('M').astype(str)

# ---------- 1) COPQ por mes ----------
copq_month = (invoices.groupby('month', as_index=False)['cost'].sum()
                         .sort_values('month'))
print('\n[INFO] COPQ per month (head):')
print(copq_month.head())

plt.figure(figsize=(10,4))
plt.plot(copq_month['month'], copq_month['cost'], marker='o', color='#2F5597')
plt.title('COPQ per Month'); plt.xlabel('Month'); plt.ylabel('Total COPQ')
plt.xticks(rotation=45, ha='right'); plt.grid(axis='y', alpha=0.2)
plt.tight_layout(); plt.savefig(OUT_DIR / 'copq_month.png', dpi=160); plt.close()

# ---------- 2) Paid vs Unpaid ----------
paid_unpaid = (invoices.groupby('status', as_index=False)['cost'].sum()
                         .sort_values('cost', ascending=False))
print('\n[INFO] Paid vs Unpaid:')
print(paid_unpaid)

plt.figure(figsize=(6,4))
plt.bar(paid_unpaid['status'].astype(str), paid_unpaid['cost'], color=['#3FA34D','#E76F51'])
plt.title('Paid vs Unpaid (COPQ)')
plt.xlabel('Status'); plt.ylabel('Total Cost'); plt.grid(axis='y', alpha=0.2)
plt.tight_layout(); plt.savefig(OUT_DIR / 'paid_vs_unpaid.png', dpi=160); plt.close()

# ---------- 3) Claims Pareto (por Issue) ----------
claims_pareto = (claims.groupby('issue', as_index=False)['claim_id'].count()
                        .rename(columns={'claim_id':'total_claims'})
                        .sort_values('total_claims', ascending=False))
print('\n[INFO] Claims Pareto (head):')
print(claims_pareto.head())

plt.figure(figsize=(9,4))
plt.bar(claims_pareto['issue'].astype(str), claims_pareto['total_claims'], color='#264653')
plt.title('Claims Pareto (Issue)')
plt.xlabel('Issue'); plt.ylabel('Total Claims')
plt.xticks(rotation=30, ha='right'); plt.tight_layout()
plt.savefig(OUT_DIR / 'claims_pareto.png', dpi=160); plt.close()

# ---------- 4) COPQ por Issue ----------
copq_by_issue = (invoices.groupby('issue', as_index=False)['cost'].sum()
                          .sort_values('cost', ascending=False))
print('\n[INFO] COPQ by Issue (head):')
print(copq_by_issue.head())

plt.figure(figsize=(9,4))
plt.bar(copq_by_issue['issue'].astype(str), copq_by_issue['cost'], color='#8AB17D')
plt.title('COPQ by Issue')
plt.xlabel('Issue'); plt.ylabel('Total COPQ')
plt.xticks(rotation=30, ha='right'); plt.tight_layout()
plt.savefig(OUT_DIR / 'copq_by_issue.png', dpi=160); plt.close()

# ---------- 5) Integración simple: join por Program + Issue + Month ----------
merged = (claims[['claim_id','program','product','issue','month']]
          .merge(invoices[['invoice_id','program','issue','cost','status','month']],
                 on=['program','issue','month'], how='left'))

sample = merged.head(200)
sample_path = OUT_DIR / 'claims_invoices_sample.csv'
sample.to_csv(sample_path, index=False)
print(f'\n[INFO] Saved merged sample to: {sample_path}')

print('\n[DONE] Charts saved to ./outputs:')
for f in ['copq_month.png','paid_vs_unpaid.png','claims_pareto.png','copq_by_issue.png']:
    print(f' - {f}')
