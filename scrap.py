import requests
from bs4 import BeautifulSoup

class ScrapComp():

    def get_data(self):

        url = "https://www.codechef.com/contests"

        root = requests.get(url=url)
        soup = BeautifulSoup(root.text, "html.parser")
        # print(soup.prettify())

        present = {}
        counter = 0
        data = {}
        past = {}
        future = {}
        ic = 0
        for i in soup.find_all("tbody"):
            # print(i.text)
            ic += 1
            counter = 0
            # ic+=1
            present = {}
            for j in i.find_all("tr"):
                counter += 1
                subdata = {}
                subdata["CODE"] = str(j.contents[1].text)
                subdata["NAME"] = str(j.contents[3].text)
                subdata["END_TIME"] = str(j.contents[7].text)
                subdata["START_TIME"] = str(j.contents[5].text)
                subdata["URL"] = "https://www.codechef.com/" + str(j.contents[1].text)
                present[str(counter)] = subdata
            if ic == 1:
                data["PRESENT"] = present
            elif ic == 2:
                data["FUTURE"] = present
            elif ic == 3:
                data["PAST"] = present
        return data
# ss=ScrapComp()
# print(ss.get_data())