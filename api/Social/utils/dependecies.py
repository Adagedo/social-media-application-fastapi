from api.Social.utils.database import sessionLocals
def get_db():
    Db = sessionLocals()
    try:
        yield Db
    finally:
        Db.close()
