ALTER TABLE
    app_user
ADD COLUMN
    is_banned INTEGER DEFAULT 0;


DROP TABLE IF EXISTS
    app_membership;

ALTER TABLE
    app_group_user
RENAME TO app_membership;
