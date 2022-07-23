SELECT
    *
FROM
    app_comment
WHERE
    user_id IN (
                SELECT
                    id
                FROM
                    app_user
                WHERE
                    is_banned = 1)
ORDER BY
    created;


-- Another way to get the same result:
SELECT
    app_comment.*
FROM
    app_comment
INNER JOIN
	app_user
ON
	app_comment.user_id = app_user.id
WHERE
    app_user.is_banned = 1
ORDER BY
    created;
