INSERT INTO hotels (id, name, location, services, room_quantity) VALUES
(1, 'Grand Astana Hotel', 'Astana, Kazakhstan', '{"wifi": true, "pool": true, "breakfast": true}', 120),
(2, 'Almaty Plaza Hotel', 'Almaty, Kazakhstan', '{"wifi": true, "gym": true, "spa": true}', 95),
(3, 'Shymkent Luxury Inn', 'Shymkent, Kazakhstan', '{"wifi": true, "parking": true}', 60),
(4, 'Burabay Resort', 'Burabay, Kazakhstan', '{"wifi": true, "lake_view": true, "spa": true}', 80),
(5, 'Nomad Comfort Hotel', 'Astana, Kazakhstan', '{"wifi": true, "restaurant": true}', 110),
(6, 'Skyline Almaty', 'Almaty, Kazakhstan', '{"wifi": true, "pool": true, "gym": true}', 140),
(7, 'Central Park Hotel', 'Karaganda, Kazakhstan', '{"wifi": true, "parking": true, "breakfast": true}', 70),
(8, 'Zhetysu Palace', 'Taldykorgan, Kazakhstan', '{"wifi": true, "spa": false, "restaurant": true}', 55),
(9, 'Rixos Elite Astana', 'Astana, Kazakhstan', '{"wifi": true, "pool": true, "spa": true, "gym": true}', 200),
(10, 'Mountain View Lodge', 'Almaty Region, Kazakhstan', '{"wifi": true, "hiking_tours": true}', 40);

INSERT INTO rooms (id, hotel_id, name, description, price, quantity) VALUES
(1, 1, 'Standard Room', 'Cozy room with basic amenities', 50.00, '2'),
(2, 1, 'Deluxe Room', 'Spacious room with city view', 80.00, '3'),
(3, 1, 'Suite', 'Luxury suite with living area', 150.00, '1'),

(4, 2, 'Standard Room', 'Comfortable room with WiFi', 60.00, '4'),
(5, 2, 'Business Room', 'Ideal for business travelers', 90.00, '2'),
(6, 2, 'Luxury Suite', 'Premium suite with spa access', 200.00, '1'),

(7, 3, 'Economy Room', 'Affordable small room', 40.00, '5'),
(8, 3, 'Standard Room', 'Clean and simple room', 55.00, '3'),
(9, 3, 'Family Room', 'Large room for families', 100.00, '2'),

(10, 4, 'Lake View Room', 'Room with beautiful lake view', 120.00, '2');