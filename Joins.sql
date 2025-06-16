--Inner Join
SELECT 
    m.Membership_id,
    m.Current_points,
    u.User_id,
    u.Name,
    u.Email
FROM Membership m
INNER JOIN [User] u ON m.User_id = u.User_id;

--Left Join
SELECT 
    m.Membership_id,
    m.Current_points,
    u.User_id,
    u.Name,
    u.Email
FROM Membership m
LEFT JOIN [User] u ON m.User_id = u.User_id;

--Right Join
SELECT 
    m.Membership_id,
    m.Current_points,
    u.User_id,
    u.Name,
    u.Email
FROM Membership m
RIGHT JOIN [User] u ON m.User_id = u.User_id;

--Full Outer Join
SELECT 
    m.Membership_id,
    m.Current_points,
    m.User_id AS Membership_UserID,
    u.User_id AS User_UserID,
    u.Name,
    u.Email
FROM Membership m
FULL OUTER JOIN [User] u ON m.User_id = u.User_id;

-- total points and membership count for each user with their names
SELECT 
    u.Name AS user_name,
    COUNT(m.Membership_id) AS total_memberships,
    SUM(m.Current_points) AS total_points
FROM Membership m
JOIN [User] u ON m.User_id = u.User_id
GROUP BY u.Name;

--Calculate the average membership points per user.
SELECT 
    u.Name AS user_name, 
    AVG(m.Current_points) AS avg_membership_points
FROM [User] u
JOIN Membership m ON u.User_id = m.User_id
GROUP BY u.Name;

--Retrieve distinct users who have made at least one booking
SELECT DISTINCT u.Name
FROM [User] u
JOIN Booking b ON u.User_id = b.User_id;

