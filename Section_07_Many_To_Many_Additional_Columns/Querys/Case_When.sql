SELECT
    created
  , CAST(strftime('%m', created) AS INTEGER) AS month
  , CASE
        WHEN CAST(strftime('%m', created) AS INTEGER) IN(0, 1, 2) THEN 'Q1'
        WHEN CAST(strftime('%m', created) AS INTEGER) IN(3, 4, 5) THEN 'Q2'
        WHEN CAST(strftime('%m', created) AS INTEGER) IN(6, 7, 8) THEN 'Q3'
        WHEN CAST(strftime('%m', created) AS INTEGER) IN(10, 11, 12) THEN 'Q4'
    END AS quarter
FROM
    esmartdata_membership;