SELECT
    name
FROM
    sqlite_master
WHERE
    type = 'index'
AND
    name
NOT LIKE
    'sqlite_%';