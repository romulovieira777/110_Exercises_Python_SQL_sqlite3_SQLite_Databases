SELECT
    esmartdata_user.first_name
  , esmartdata_user.last_name
  , esmartdata_developer.level
FROM
    esmartdata_user
LEFT JOIN
    esmartdata_developer
ON
    esmartdata_user.id = esmartdata_developer.user_id;