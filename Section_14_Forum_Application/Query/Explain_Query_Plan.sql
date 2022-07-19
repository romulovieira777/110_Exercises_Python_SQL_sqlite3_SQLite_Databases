EXPLAIN QUERY PLAN
    SELECT
        *
    FROM
        app_user
    WHERE
        id = 3;


EXPLAIN QUERY PLAN
    SELECT
        *
    FROM
        app_group_user
    WHERE
        group_id = 2
    AND
        user_id = 41;
