SELECT
    name
FROM
    sqlite_master
WHERE
    type='table'
AND
    name LIKE 'app_%'
ORDER BY
    name;
