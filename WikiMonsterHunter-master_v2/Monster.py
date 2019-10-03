import json


def createMonster():
    """Create all object monsters"""
    listMonsters = []
    with open("DataMonster") as dataMonster:
        data = json.load(dataMonster)
        for monster in data:
            listMonsters.append(Monster(monster))
    return listMonsters


class Monster:
    """Deafult class of monster which will be display on screen.
    Contain all informtations about them
    TODO : add image, rarity """

    def __init__(self, name=""):
        self.name = name.capitalize()
        self.displayName = None
        self.description = None
        self.picture = None
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
        self.description = dataMonster[self.name]["Language"][language]["description"]


class Search:
    def __init__(self, userSearch=None, listMonster=None):
        self.userSearch = userSearch.lower()
        self.listMonster = listMonster
        self.listMonsterSearch = []

    def __del__(self):
        print("Deleted {obj}".format(obj=self))

    def search(self):
        listTri = []
        listTri2 =[]
        verif = None
        #On récupère les monstres qui contiennent dans leur nom le message donné par l'utilisateur
        for monster in self.listMonster:
            if self.userSearch in monster.name.lower():
                listTri.append(monster.name)
            monster.name.capitalize()
        #On tri cette liste de telle sorte à obtenir les monstres ayant ce message au début de leur nom en premier
        for  monster in listTri:
            for i in range(0, len(self.userSearch)):
                if monster[i]==self.userSearch[i] :
                    verif = True
                else:
                    verif = False
                    break
            if verif :
                listTri2.append(monster)
                listTri.remove(monster)
                break
        for monster in listTri :
            listTri2.append(monster)


        #On copie les monstres qui corresponde à notre recherche dans la liste de recherche
        for monster in listTri2:
            for monsters in self.listMonster :
                if monster == monsters.name :
                    self.listMonsterSearch.append(monsters)

    def clean(self):
        self.listMonsterSearch = []


liste = createMonster()
search = Search("rath", liste)
search.search()
for monster in search.listMonsterSearch :
    print(monster.name)
