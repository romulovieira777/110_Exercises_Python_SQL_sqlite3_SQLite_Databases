SELECT
    esmartdata_membership.created
  , esmartdata_course.title
FROM
    esmartdata_course
LEFT JOIN
    esmartdata_membership
ON
    esmartdata_course.id = esmartdata_membership.course_id
WHERE
    esmartdata_membership.created BETWEEN '2021-02-01' AND '2021-03-31';