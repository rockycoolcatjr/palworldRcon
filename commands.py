from mcrcon import MCRcon
from time import sleep


class commands:
    def __init__(self, ip, password, additional, command):
        self.ip = ip
        self.password = password
        self.command = command
        self.additional = additional
        self.response = None
        print("Initialized")

    def commandSwitch(self):
        option = self.command
        print(option)
        match option:
            case 1:
                self.broadcast()
            case 2:
                self.shutdown()
            case 3:
                self.exit()
            case 4:
                self.kickPlayer()
            case 5:
                self.showPlayers()
            case 0:
                self.info()
            case 6:
                self.save()             


    def broadcast(self): #Sends message out to server
        print("Broadcast")
        with MCRcon(self.ip, self.password) as mcr:
            #print("|" + self.ip + "|")
            #print("|" +self.password+ "|")
            #print("Additional: " , self.additional)
            resp = mcr.command("broadcast " + self.additional)
            print(resp)
            self.response = resp
            
    def shutdown(self): #shutdoown server, in seconds and message text
        with MCRcon(self.ip, self.password) as mcr:
            resp = mcr.command("Shutdown " + self.additional)
            print(resp)
            self.response = resp

    def exit(self): #Hard exit
        with MCRcon(self.ip, self.password) as mcr:
            resp = mcr.command("DoExit")
            print(resp)
            self.response = resp

    def kickPlayer(self): #Kick player, and requires additional
        with MCRcon(self.ip, self.password) as mcr:
            print("Kick Player")
            resp = mcr.command("KickPlayer " + self.additional)
            print(resp)
            self.response = resp
    def showPlayers(self): #Show all players online, output to console needed
        with MCRcon(self.ip, self.password) as mcr:
            print("Show players")
            resp = mcr.command("ShowPlayers")
            self.response = resp
            print(resp)
            self.response = resp
 
    def info(self): #Gets server info, output to console needed
        with MCRcon(self.ip, self.password) as mcr:
            resp = mcr.command("Info")
            self.response = resp
            print(resp)
            self.response = resp

    def save(self):
        with MCRcon(self.ip, self.password) as mcr:
            resp = mcr.command("Save")
            self.response = resp
            print(resp)
            self.response = resp

    def sendRCON(self): #Defaul method to send stuff to server, just cuz i forget
        
        with MCRcon(self.ip, self.password) as mcr:
            resp = mcr.command("broadcast " + "message")
            print(resp)