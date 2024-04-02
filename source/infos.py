class DocumentInfos:

    title = u'Wizard of the roast - projet jeu vidéo'
    first_name = 'Berreqia Akim,'
    last_name = 'Fanton Louis'
    author = f'{first_name} {last_name}'
    year = u'2024'
    month = u'Janvier'
    seminary_title = u'Projet OCI'
    tutor = u"Cédric Donner"
    release = "(Version finale)"
    repository_url = "https://github.com/<username>/<reponame>"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()