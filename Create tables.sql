-- Create the database
CREATE DATABASE IF NOT EXISTS InoxDB;
USE InoxDB;

--Create Screen Table
CREATE TABLE Screen (
    Screen_id INT PRIMARY KEY,
    Screen_name VARCHAR(100),
    Class_type VARCHAR(100),
    Capacity INT,
    Membership_id INT,
    FOREIGN KEY (Membership_id) REFERENCES Booking(Membership_id)
);

--Create Seat Table
CREATE TABLE Seat (
    seat_id INT PRIMARY KEY,
    seat_number VARCHAR(10)
);

--Create Movie Table
CREATE TABLE Movie (
     Movie_id INT PRIMARY KEY,
     Title VARCHAR(100),
     Genre VARCHAR(100),
     Rating DECIMAL(2,1),
     Status VARCHAR(100),
     Poster_image_url VARCHAR(100)
     );

--Create Review Table
CREATE TABLE Review (
       Review_id INT PRIMARY KEY,
       Content TEXT,
       Review_date DATETIME,
       Reviewer_name VARCHAR(100)
);

--Create Show Table
CREATE TABLE Show (
       Show_id INT PRIMARY KEY,
       Show_datetime DATETIME,
       Screen_id INT,
       Movie_id INT,
    FOREIGN KEY (Screen_id) REFERENCES Screen(Screen_id),
    FOREIGN KEY (Movie_id) REFERENCES Movie(Movie_id)
);

--Create User Table
CREATE TABLE [User] (
       User_id INT PRIMARY KEY,
       Name VARCHAR(100),
       Email VARCHAR(150),
       Phone VARCHAR(15)
);

--Create Membership Table
CREATE TABLE Membership (
       Membership_id INT primary key,
       Current_points INT,
       User_id INT,
    FOREIGN KEY (User_id) REFERENCES [User](User_id) 
);

--Create Booking Table
CREATE TABLE Booking (
       Booking_id INT PRIMARY KEY,
       Booking_datetime DATETIME,
       Total_cost DECIMAL(10,2),
       User_id INT,
       Show_id INT,
       FOREIGN KEY (User_id) REFERENCES [User](User_id),
       FOREIGN KEY (Show_id) REFERENCES Show(Show_id) 
);

--Create Ticket Table
CREATE TABLE Ticket (
    Ticket_id INT PRIMARY KEY,
    Qr_code VARCHAR(100),
    Delivery_method VARCHAR(50),
    Is_downloaded BIT,
    Scanned_at DATETIME,
    Booking_id INT,
    Show_id INT,
    FOREIGN KEY (Booking_id) REFERENCES Booking(Booking_id),
    FOREIGN KEY (Show_id) REFERENCES Show(Show_id)
);

--Create FoodIten Table
CREATE TABLE FoodItem (
       Item_id INT PRIMARY KEY,
       [Name] VARCHAR(100),
       [Description] TEXT,
       Is_Combo BIT
);

--Create FoodOrder Table
CREATE TABLE FoodOrder (
       Order_id INT PRIMARY KEY,
       Order_datetime DATETIME,
       Total_cost DECIMAL(10,2),
       Delivery_method VARCHAR(50),
       Booking_id INT,
       Screen_id INT,
       FOREIGN KEY (Booking_id) REFERENCES Booking(Booking_id),
       FOREIGN KEY (Screen_id) REFERENCES Screen(Screen_id)
);

--Create FoodOrderItem Table
create table FoodOrderItem (
             order_item_id int primary key,
             quantity int,
             price_at_time decimal(10,2),
             order_id INT,
             item_id INT,
             FOREIGN KEY (order_id) REFERENCES FoodOrder(Order_id),
             FOREIGN KEY (item_id) REFERENCES FoodItem(Item_id)
);



