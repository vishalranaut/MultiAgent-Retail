-- Table for storing product demand data
CREATE TABLE IF NOT EXISTS Demand (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductID INTEGER,
    StoreID INTEGER,
    SalesQuantity INTEGER,
    SalesDate DATE
);

-- Table for inventory monitoring
CREATE TABLE IF NOT EXISTS Inventory (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductID INTEGER,
    StoreID INTEGER,
    StockLevels INTEGER,
    ReorderPoint INTEGER
);

-- Table for pricing optimization
CREATE TABLE IF NOT EXISTS Pricing (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductID INTEGER,
    StoreID INTEGER,
    Price REAL,
    CompetitorPrices REAL
);
