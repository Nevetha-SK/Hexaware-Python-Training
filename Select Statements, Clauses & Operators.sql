--Select Table Information and Column Information from Schema
SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Screen';
SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'FoodItem';

--Select Top 3 rows
SELECT * FROM Screen;
SELECT TOP 3 * FROM Screen;

--Normal Select Statements
SELECT * FROM Seat;
SELECT * FROM Movie;
SELECT * FROM Review;
SELECT * FROM FoodItem;

--Select Specific Columns from the Table
SELECT [Name], [Description] FROM FoodItem;

--WHERE Clauses
SELECT * FROM Review WHERE Review_id IN (1, 3);
SELECT * FROM Review WHERE Review_id NOT IN (2,3);

-- ORDER BY
SELECT * FROM Show ORDER BY Show_datetime ASC;
SELECT * FROM Show ORDER BY Show_datetime DESC;
SELECT * FROM Booking ORDER BY Total_cost ASC;
SELECT * FROM Booking ORDER BY Booking_datetime DESC;
SELECT [Name] FROM FoodItem ORDER BY [Name] ASC

--Is NULL, NOT NULL
SELECT * FROM Membership WHERE User_id IS NULL;
SELECT * FROM Membership WHERE User_id IS NOT NULL;

--GROUP BY with HAVING and ORDER BY
SELECT User_id, SUM(Current_points) AS TotalPoints FROM Membership WHERE User_id IS NOT NULL GROUP BY User_id HAVING SUM(Current_points) > 400;
SELECT User_id, SUM(Current_points) AS TotalPoints FROM Membership WHERE User_id IS NOT NULL GROUP BY User_id ORDER BY TotalPoints DESC;

--Count 
SELECT COUNT(*) AS TotalTickets FROM Ticket;
SELECT COUNT(*) AS DownloadedTickets FROM Ticket
WHERE Is_downloaded = 1;

--IN, NOT IN
SELECT * FROM FoodOrder WHERE Booking_id IN (1, 3);
SELECT * FROM FoodOrder WHERE Screen_id NOT IN (3);

--BETWEEN...AND
SELECT * FROM FoodOrder WHERE Total_cost BETWEEN 250 AND 260;

--DISTINCT
SELECT DISTINCT Delivery_method FROM FoodOrder;

--WITH Keyword
WITH HighCostOrders AS (
    SELECT * FROM FoodOrder
    WHERE Total_cost > 300
)
SELECT * FROM HighCostOrders;

--Like, Wildcard Operator
SELECT * FROM FoodItem
WHERE Name LIKE 'C%';

