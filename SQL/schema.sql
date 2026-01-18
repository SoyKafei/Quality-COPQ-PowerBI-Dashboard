
-- Star schema (generic). Tested for SQLite/MySQL compatibility.

CREATE TABLE DimProgram (
  ProgramKey INTEGER PRIMARY KEY,
  Program VARCHAR(100) UNIQUE
);

CREATE TABLE DimProduct (
  ProductKey INTEGER PRIMARY KEY,
  Product VARCHAR(100) UNIQUE
);

CREATE TABLE DimIssue (
  IssueKey INTEGER PRIMARY KEY,
  Issue VARCHAR(100) UNIQUE
);

CREATE TABLE DimStatus (
  StatusKey INTEGER PRIMARY KEY,
  Status VARCHAR(50) UNIQUE
);

CREATE TABLE FactClaims (
  ClaimID VARCHAR(64) PRIMARY KEY,
  ClaimDate DATE,
  Program VARCHAR(100),
  Product VARCHAR(100),
  Issue VARCHAR(100),
  ColorStatus VARCHAR(50)
);

CREATE TABLE FactInvoices (
  InvoiceID VARCHAR(64) PRIMARY KEY,
  CreatedDate DATE,
  InvoiceName VARCHAR(255),
  Program VARCHAR(100),
  Issue VARCHAR(100),
  Supplier VARCHAR(100),
  Cost DECIMAL(18,2),
  Status VARCHAR(50),
  PaymentDate DATE
);

-- Optional: Views to expose star-joined facts using natural keys
CREATE VIEW vw_FactClaims_Star AS
SELECT c.ClaimID, c.ClaimDate,
       dp.ProgramKey, dprod.ProductKey, di.IssueKey,
       c.Program, c.Product, c.Issue, c.ColorStatus
FROM FactClaims c
LEFT JOIN DimProgram dp ON dp.Program = c.Program
LEFT JOIN DimProduct dprod ON dprod.Product = c.Product
LEFT JOIN DimIssue di ON di.Issue = c.Issue;

CREATE VIEW vw_FactInvoices_Star AS
SELECT i.InvoiceID, i.CreatedDate, i.InvoiceName,
       dp.ProgramKey, di.IssueKey, ds.StatusKey,
       i.Program, i.Issue, i.Status, i.Supplier,
       i.Cost, i.PaymentDate
FROM FactInvoices i
LEFT JOIN DimProgram dp ON dp.Program = i.Program
LEFT JOIN DimIssue di ON di.Issue = i.Issue
LEFT JOIN DimStatus ds ON ds.Status = i.Status;
