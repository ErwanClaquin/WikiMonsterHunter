import json


class Monster:
    """Deafult class of monster which will be display on screen.
    Contain all informtations about them
    TODO : add image, rarity """

    def __init__(self, name=""):
        self.name = name.capitalize()
        self.displayName = None
        self.desciption = None

        self.__assertNameValid()

        self.updateAllMonster()

    def __del__(self):
        print("Deleted {obj} named as {name}".format(obj=self, name=self.name))

    def __assertNameValid(self):
        with open("DataMonster") as dataMonster:
            data = json.load(dataMonster)
            dataName = []
        for monster in data:
            dataName.append(monster)
        if self.name not in dataName:
            raise NotImplementedError("Name is not valid")

    def __assertLanguageValid(self, languageToCheck=""):
        with open("DataMonster") as dataMonster:
            data = json.load(dataMonster)
            dataLanguage = []
        for language in data[self.name]["Language"]:
            dataLanguage.append(language)
        if languageToCheck in dataLanguage:
            return languageToCheck
        else:
            return "EN"

    def updateAllMonster(self, language=""):
        """This is the main method to update the monster
        It will check language and change displayName and description
        TODO : change image"""

        if language == "":
            with open("Settings") as fileUserSettings:
                userSettings = json.load(fileUserSettings)
                languageUser = userSettings["language"]
        else:
            languageUser = language
        languageValid = self.__assertLanguageValid(languageToCheck=languageUser)

        with open("DataMonster") as fileDataMonster:
            self.updateLanguage(language=languageValid, fileDataMonster=fileDataMonster)

    def updateLanguage(self, language="EN", fileDataMonster=None):
        """This is a sub method to only change what is needed with language
        For exemple, image (TODO)
        will not be changed"""

        dataMonster = json.load(fileDataMonster)
        self.displayName = dataMonster[self.name]["Language"][language]["displayName"]
        self.desciption = dataMonster[self.name]["Language"][language]["description"]
