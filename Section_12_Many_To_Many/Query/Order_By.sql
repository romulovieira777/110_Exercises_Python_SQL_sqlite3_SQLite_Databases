SELECT
    esmartdata_developer.level
  , COUNT(esmartdata_developer.level) AS num_developers
FROM
    esmartdata_developer
GROUP BY
    esmartdata_developer.level
ORDER BY
    esmartdata_developer.level ASC;