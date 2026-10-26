from sqlalchemy import create_engine, text


db_connection_string = \
    "postgresql://myuser:mypassword@localhost:5432/mydatabase"
db = create_engine(db_connection_string)

SHARED_SUBJECT_ID = None


def test_1_create_subject():
    global SHARED_SUBJECT_ID
    title = "Жопа горит"

    connection = db.connect()

    max_id_sql = text("SELECT MAX(subject_id) FROM subject")
    current_max = connection.execute(max_id_sql).scalar()

    SHARED_SUBJECT_ID = current_max + 1

    insert_sql = text(
        "INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)")
    connection.execute(insert_sql, {"id": SHARED_SUBJECT_ID, "title": title})
    connection.commit()

    select_sql = text("SELECT * FROM subject WHERE subject_id = :id")
    result = connection.execute(select_sql, {"id": SHARED_SUBJECT_ID})
    row = result.mappings().one_or_none()

    connection.close()

    assert row is not None
    assert row["subject_title"] == title
    print("[INFO] Здесь могла бы быть ваша реклама.")


def test_2_edit_subject():
    new_title = "Очень больно красноглазить"

    connection = db.connect()

    update_sql = text(
        "UPDATE subject SET subject_title = :title WHERE subject_id = :id")
    connection.execute(update_sql,
                       {"title": new_title, "id": SHARED_SUBJECT_ID})
    connection.commit()

    select_sql = text("SELECT * FROM subject WHERE subject_id = :id")
    result = connection.execute(select_sql, {"id": SHARED_SUBJECT_ID})
    row = result.mappings().one_or_none()

    connection.close()

    assert row is not None
    assert row["subject_title"] == new_title


def test_3_delete_subject():
    connection = db.connect()

    delete_sql = text("DELETE FROM subject WHERE subject_id = :id")
    connection.execute(delete_sql, {"id": SHARED_SUBJECT_ID})
    connection.commit()

    select_sql = text("SELECT * FROM subject WHERE subject_id = :id")
    result = connection.execute(select_sql, {"id": SHARED_SUBJECT_ID})
    row = result.mappings().one_or_none()

    connection.close()

    assert row is None
