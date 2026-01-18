
-- 1) Total Claims per Issue (Pareto)
SELECT Issue, COUNT(*) AS TotalClaims
FROM FactClaims
GROUP BY Issue
ORDER BY TotalClaims DESC;

-- 2) COPQ per month
SELECT strftime('%Y-%m', CreatedDate) AS Month, SUM(Cost) AS TotalCOPQ
FROM FactInvoices
GROUP BY Month
ORDER BY Month;

-- 3) Claims by Program and Month
SELECT Program, strftime('%Y-%m', ClaimDate) AS Month, COUNT(*) AS Claims
FROM FactClaims
GROUP BY Program, Month
ORDER BY Program, Month;

-- 4) Paid vs Unpaid COPQ
SELECT Status, SUM(Cost) AS COPQ
FROM FactInvoices
GROUP BY Status;

-- 5) COPQ by Issue (Top contributors)
SELECT Issue, SUM(Cost) AS COPQ
FROM FactInvoices
GROUP BY Issue
ORDER BY COPQ DESC;

-- 6) Join Claims to Invoices (when IDs are related)
SELECT c.ClaimID, c.Program, c.Issue, i.Cost, i.Status
FROM FactClaims c
LEFT JOIN FactInvoices i ON i.Issue = c.Issue AND i.Program = c.Program;
