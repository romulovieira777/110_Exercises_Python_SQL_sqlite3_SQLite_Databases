DROP INDEX IF EXISTS
    app_thread_creator_id_idx;

CREATE INDEX
    app_thread_creator_id_idx
ON
    app_thread (creator_id);

DROP INDEX IF EXISTS
    app_comment_thread_id_idx;

CREATE INDEX
    app_comment_thread_id_idx
ON
    app_comment (thread_id);

DROP INDEX IF EXISTS
    app_comment_user_id_idx;

CREATE INDEX
    app_comment_user_id_idx
ON
    app_comment (user_id);

DROP INDEX IF EXISTS
    app_group_user_group_id_idx;

CREATE INDEX
    app_group_user_group_id_idx
ON
    app_group_user (group_id);

DROP INDEX IF EXISTS
    app_group_user_user_id_idx;

CREATE INDEX
    app_group_user_user_id_idx
ON
    app_group_user (user_id);

DROP INDEX IF EXISTS
    app_group_user_group_id_user_idx_uniq;

CREATE UNIQUE INDEX
    app_group_user_group_id_user_idx_uniq
ON
    app_group_user (group_id, user_id);
