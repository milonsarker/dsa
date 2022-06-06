--https://leetcode.com/problems/the-number-of-users-that-are-eligible-for-discount/

CREATE FUNCTION getUserIDs(startDate IN DATE, endDate IN DATE, minAmount IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    SELECT COUNT(DISTINCT user_id) INTO result
    FROM Purchases
    WHERE amount >= minAmount
    AND time_stamp BETWEEN startDate AND endDate;
    RETURN result;
END;