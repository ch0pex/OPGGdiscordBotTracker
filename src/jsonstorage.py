import json
ACCOUNTS_PATH = "/home/acbsu/json_files/accounts.json"
CHAMPS_PATH = "/home/acbsu/json_files/champs_ids.json"
class Storage():

    def __init__(self):
        self.number_accounts = self.__lenght()
        self.accounts = self.__accounts_list()

    def __load(self,path):
        with open(path, "r",encoding="utf-8", newline="") as file:
            return json.load(file)


    def __write(self,data,path):
        with open(path, "w", encoding="utf-8", newline="") as file:
            json.dump(data, file, indent=2)

    def __lenght(self) -> int:
        list_summs = self.__load(ACCOUNTS_PATH)
        return len(list_summs["accounts"])

    def add_summoner(self,name,region = "EUW"):
        data = self.__load(ACCOUNTS_PATH)
        data.get(region).append(name)
        self.__write(data,ACCOUNTS_PATH)


    def delete_summoner(self,name):
        data = self.__load(ACCOUNTS_PATH)
        data.remove(name)
        self.__write(data,ACCOUNTS_PATH)

    def get_champion_name(self,id):
        file = self.__load(CHAMPS_PATH)
        return file.get(id)

    def __accounts_list(self):
        return self.__load(ACCOUNTS_PATH).get("EUW")
