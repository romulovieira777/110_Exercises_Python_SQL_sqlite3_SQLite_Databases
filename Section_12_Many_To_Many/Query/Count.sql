SELECT
    esmartdata_user.first_name
  , esmartdata_user.last_name
  , esmartdata_developer.level
  , COUNT(esmartdata_developer_techs.tech_id) AS num_techs
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
    esmartdata_developer_techs.tech_id = esmartdata_tech.id
GROUP BY
    esmartdata_user.first_name
  , esmartdata_user.last_name
  , esmartdata_developer.level
ORDER BY
    num_techs DESC
  , esmartdata_user.first_name ASC