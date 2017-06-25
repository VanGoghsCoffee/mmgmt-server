class DatabaseInteractor(object):
    def __init__(self, logger):
        self.logger = logger

    def drop_reset(self, db):
        try:
            db.reflect()
            db.drop_all()
            self.logger.info("db reset")
        except exc.SQLAlchemyError as e:
            self.logger.error("couldn't drop db: {}".format(e))
        else:
            try:
                db.create_all()
                self.logger.info("db created")
            except exc.SQLAlchemyError as e:
                self.logger.error("db creat error: {}".format(e))
