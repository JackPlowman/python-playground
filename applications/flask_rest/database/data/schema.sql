-- Create the brands table
CREATE TABLE IF NOT EXISTS brands (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);

-- Create the models table
CREATE TABLE IF NOT EXISTS models (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  price REAL NOT NULL,
  brand_id INTEGER NOT NULL,
  FOREIGN KEY (brand_id) REFERENCES brands (id)
);
