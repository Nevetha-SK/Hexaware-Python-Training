--referral

ALTER TABLE Membership
ADD referred_by INT;

-- Set Membership ID 1 as the root (no one referred it)
UPDATE Membership
SET referred_by = NULL
WHERE Membership_id = 1;

-- Set Membership 1 as the referrer for 2 and 3
UPDATE Membership
SET referred_by = 1
WHERE Membership_id IN (2, 3);

-- Set Membership 2 as the referrer for 4
UPDATE Membership
SET referred_by = 2
WHERE Membership_id = 4;

-- Set Membership 3 as the referrer for 5
UPDATE Membership
SET referred_by = 3
WHERE Membership_id = 5;

--Using Recursive Query
--Anchor Part
WITH membership_tree AS (
    SELECT 
        Membership_id,
        Current_points,
        referred_by,
        0 AS level
    FROM Membership
    WHERE referred_by IS NULL

    UNION ALL
--Recursive Part
    SELECT 
        m.Membership_id,
        m.Current_points,
        m.referred_by,
        mt.level + 1
    FROM Membership m
    JOIN membership_tree mt ON m.referred_by = mt.Membership_id
)
-- Final query to retrieve the referral hierarchy
SELECT * 
FROM membership_tree
ORDER BY level, Membership_id;

