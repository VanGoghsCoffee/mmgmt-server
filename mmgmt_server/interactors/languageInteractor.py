from mmgmt_server.interactors import Interactor
from mmgmt_server.models import Lang


class LanguageInteractor(Interactor):
    def write_from_json(self, langs_dic, db):
        added_languages = []
        for lang in langs_dic:
            added_languages.append(Lang(lang["name"], lang["iso_code"]))
            db.session.add(added_languages[len(added_languages) - 1])
        db.session.commit()
        self.logger.info('Langs written to DB - {}'.format(langs_dic))
        return added_languages
