SELECT
    esmartdata_user.first_name
  , esmartdata_user.last_name
  , esmartdata_developer.level
FROM
    esmartdata_user
INNER JOIN
    esmartdata_developer
ON
    esmartdata_user.id = esmartdata_developer.user_id;


SELECT
    esmartdata_user.first_name
  , esmartdata_user.last_name
  , esmartdata_developer.level
  , esmartdata_tech.name
FROM
    esmartdata_user
INNER JOIN
    esmartdata_developer
ON
    esmartdata_user.id = esmartdata_developer.user_id
INNER JOIN
    esmartdata_developer_techs
ON
    esmartdata_developer.user_id = esmartdata_developer_techs.developer_id
INNER JOIN
    esmartdata_tech
ON
    esmartdata_developer_techs.tech_id = esmartdata_tech.id;