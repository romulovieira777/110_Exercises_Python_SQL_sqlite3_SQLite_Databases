SELECT
    app_comment.user_id
  , app_user.first_name
  , app_user.last_name
  , app_user.email
  , COUNT(*) AS cnt
FROM
    app_comment
LEFT JOIN
    app_user
ON
    app_comment.user_id = app_user.id
GROUP BY
    app_comment.user_id
ORDER BY
    cnt DESC
  , app_user.first_name
LIMIT 10;