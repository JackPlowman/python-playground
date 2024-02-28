INSERT INTO brands (id, name) VALUES (1, 'Toyota') ON CONFLICT DO NOTHING;
INSERT INTO brands (id, name) VALUES (2, 'Nissan') ON CONFLICT DO NOTHING;
INSERT INTO brands (id, name) VALUES (3, 'Ford') ON CONFLICT DO NOTHING;
INSERT INTO brands (id, name) VALUES (4, 'Chevrolet') ON CONFLICT DO NOTHING;
INSERT INTO brands (id, name) VALUES (5, 'Honda') ON CONFLICT DO NOTHING;

INSERT INTO models (name, price, brand_id) VALUES ('Corolla', 18000, 1) ON CONFLICT DO NOTHING;
INSERT INTO models (name, price, brand_id) VALUES ('Camry', 24000, 1) ON CONFLICT DO NOTHING;
INSERT INTO models (name, price, brand_id) VALUES ('Prius', 25000, 1) ON CONFLICT DO NOTHING;
INSERT INTO models (name, price, brand_id) VALUES ('Sentra', 22000, 2) ON CONFLICT DO NOTHING;
INSERT INTO models (name, price, brand_id) VALUES ('Altima', 24000, 2) ON CONFLICT DO NOTHING;
INSERT INTO models (name, price, brand_id) VALUES ('Maxima', 30000, 2) ON CONFLICT DO NOTHING;
