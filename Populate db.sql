--Insert Screen
INSERT INTO Screen (Screen_id, Screen_name, Class_type, Capacity)
VALUES 
(1, 'Screen A', 'Standard', 160),
(2, 'Screen B', 'Premium', 180),
(3, 'Screen C', 'VIP', 90),
(4, 'Screen D', 'Deluxe', 120),
(5, 'Screen E', 'Recliner', 140);

--Insert Seats
INSERT INTO Seat (seat_id, seat_number)
VALUES
(1, 'A1'),
(2, 'A2'),
(3, 'A3'),
(4, 'B1'),
(5, 'B2'),
(6, 'B3');

--Insert Movies
INSERT INTO Movie (Movie_id, Title, Genre, Rating, Status, Poster_image_url)
VALUES
(1, 'Inception', 'Sci-Fi', 8.8, 'Now Showing', 'https://img.com/inception.jpg'),
(2, 'The Dark Knight', 'Action', 9.0, 'Now Showing', 'https://img.com/darkknight.jpg'),
(3, 'Coco', 'Animation', 8.4, 'Coming Soon', 'https://img.com/coco.jpg'),
(4, 'Interstellar', 'Sci-Fi', 8.6, 'Now Showing', 'https://img.com/interstellar.jpg'),
(5, 'La La Land', 'Romance', 8.0, 'Coming Soon', 'https://img.com/lalaland.jpg');

--Insert Reviews
INSERT INTO Review (Review_id, Content, Review_date, Reviewer_name)
VALUES
(1, 'Amazing movie with brilliant visuals!', '2024-12-10 14:30:00', 'Ajay'),
(2, 'Good storyline, but could be shorter.', '2024-12-11 10:15:00', 'Ragavi'),
(3, 'Loved the acting and direction!', '2024-12-12 18:45:00', 'Shivani');

--Insert Show
INSERT INTO Show (Show_id, Show_datetime, Screen_id, Movie_id)
VALUES 
(1, '2025-06-11 10:00:00', 1, 2),
(2, '2025-06-11 14:30:00', 2, 3),
(3, '2025-06-11 09:00:00', 1, 1);

--Insert Users
INSERT INTO [User] (User_id, Name, Email, Phone)
VALUES
(1, 'Alice Johnson', 'alice.johnson@example.com', '9876543210'),
(2, 'Bob Smith', 'bob.smith@example.com', '9123456789'),
(3, 'Charlie Brown', 'charlie.brown@example.com', '9988776655'),
(4, 'Diana Prince', 'diana.prince@example.com', '9001122334');

 --Insert Membership     
INSERT INTO Membership (Membership_id, Current_points, User_id)
VALUES
(1, 100, 1),    
(2, 250, 2),   
(3, 150, NULL),
(4, 300, NULL);
INSERT INTO Membership (Membership_id, Current_points, User_id)
VALUES
(5, 220, 2),
(6, 390, 1),
(7, 400, 3),
(8, 450, 3),
(9, 120, 4);

--Insert Bookings
INSERT INTO Booking (Booking_id, Booking_datetime, Total_cost, User_id, Show_id)
VALUES
(1, '2025-06-01 14:00:00', 500.00, 1, 1),
(2, '2025-06-02 18:30:00', 350.00, 2, 2),
(3, '2025-06-03 11:00:00', 450.00, 3, 3);

--Insert Tickets
INSERT INTO Ticket (Ticket_id, Qr_code, Delivery_method, Is_downloaded, Scanned_at, Booking_id, Show_id)
VALUES
(1, 'QR12345', 'Email', 1, '2025-06-01 14:10:00', 1, 1),
(2, 'QR67890', 'Mobile App', 0, NULL, 2, 2),
(3, 'QR54321', 'Email', 1, '2025-06-03 11:15:00', 3, 3);

--Insert Food Items
INSERT INTO FoodItem (Item_id, [Name], [Description], Is_Combo)
VALUES
(1, 'Veg Burger', 'A burger with lettuce, tomato, and cheese', 0),
(2, 'Chicken Combo', 'Grilled chicken with fries and drink', 1),
(3, 'French Fries', 'Crispy golden potato fries', 0),
(4, 'Family Meal', 'Meal for 4 including pizzas and sides', 1),
(5, 'Cold Coffee', 'Chilled coffee with whipped cream', 0);

--Insert Food Orders
INSERT INTO FoodOrder (Order_id, Order_datetime, Total_cost, Delivery_method, Booking_id, Screen_id)
VALUES
(1, '2025-06-10 12:00:00', 300.00, 'Counter', 1, 1),
(2, '2025-06-10 12:15:00', 450.00, 'App', 2, 2),
(3, '2025-06-10 12:30:00', 250.00, 'Counter', 3, 3);

--Insert Food Order items
INSERT INTO FoodOrderItem (order_item_id, quantity, price_at_time, order_id, item_id)
VALUES
(1, 2, 150.00, 1, 1),
(2, 1, 120.00, 2, 2),
(3, 3, 100.00, 1, 3);


