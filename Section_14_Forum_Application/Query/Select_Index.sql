SELECT
    type
  , name
FROM
    sqlite_master
WHERE
    type='index'
ORDER BY
    name;
