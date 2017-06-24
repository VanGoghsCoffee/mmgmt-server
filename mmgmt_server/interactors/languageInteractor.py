from mmgmt_server.models import Lang


class LanguageInteractor(object):
    def __init__(self, logger):
        self.logger = logger

    def write_from_json(self, langs_dic, db):
        for lang in langs_dic:
            db.session.add(Lang(lang["name"], lang["iso_code"]))
        db.session.commit()
        self.logger.info('Langs written to DB - {}'.format(langs_dic))
