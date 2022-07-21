SELECT
    id
  , body
  , created
FROM
    app_comment
WHERE
    created BETWEEN '2021-05-23' AND '2021-05-25'
ORDER BY
    created DESC
LIMIT
    10;
