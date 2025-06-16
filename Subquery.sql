--Subquery
SELECT Membership_id, Current_points
FROM Membership
WHERE Current_points > (
    SELECT AVG(Current_points) FROM Membership
);

--subqery with distinct
SELECT DISTINCT User_id
FROM Membership
WHERE User_id IN (
    SELECT User_id
    FROM Membership
    WHERE User_id IS NOT NULL
    GROUP BY User_id
    HAVING COUNT(*) > 1
);
