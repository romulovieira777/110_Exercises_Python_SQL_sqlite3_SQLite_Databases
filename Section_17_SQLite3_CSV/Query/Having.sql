SELECT
    age
  , COUNT(age) AS cnt_users
FROM
    app_user
GROUP BY
    age
HAVING
    COUNT(age) > 1  -- or put having cnt_users > 1
ORDER BY
    cnt_users DESC
  , age DESC;
