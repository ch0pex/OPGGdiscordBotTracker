import json
import aux
import cassiopeia as cass
ACCOUNTS_PATH = "/home/acbsu/json_files/accounts.json"
CHAMPS_PATH = "/home/acbsu/json_files/champs_ids.json"
class Storage:

    def __init__(self):
        self.accounts = self.__accounts_list()
        self.number_accounts = len(self.accounts)



    def __load(self,path):
        with open(path, "r",encoding="utf-8", newline="") as file:
            return json.load(file)


    def __write(self,data,path):
        with open(path, "w", encoding="utf-8", newline="") as file:
            json.dump(data, file, indent=2)

    async def add_summoner(self,name,region = "EUW"):
        data = self.__load(ACCOUNTS_PATH)
        if name in self.accounts:
            raise
        data[name] = [False,region]
        self.__write(data,ACCOUNTS_PATH)
        self.accounts = self.__accounts_list()


    async def delete_summoner(self,name):
        data = self.__load(ACCOUNTS_PATH)
        if name not in self.accounts:
            raise
        data.pop(name)
        self.__write(data,ACCOUNTS_PATH)
        self.accounts = self.__accounts_list()

    async def get_champion_name(self,id):
        file = self.__load(CHAMPS_PATH)
        return file.get(id)

    def __accounts_list(self):
        return list(self.__load(ACCOUNTS_PATH).keys())


    async def check_bool(self,summoner) -> bool:
        data = self.__load(ACCOUNTS_PATH)
        current_game = data[summoner][0]
        for i in data:
            if current_game == data[i][0] and i != summoner:
                return True
        return False


    async def set_bool(self,summ,game_id):
        data = self.__load(ACCOUNTS_PATH)
        if data[summ][0] == game_id:
            raise
        data[summ][0] = game_id
        self.__write(data,ACCOUNTS_PATH)

    def __str__(self):
        data = self.__load(ACCOUNTS_PATH)
        return str(data)

