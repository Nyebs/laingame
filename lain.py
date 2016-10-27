#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

from os import system
import random, progressbar, time
from colorama import init, Fore, Style

#welcome to lain

#initializes colorama
init()

#definitions - flags
lvlmail = 0
def lvlmailadd():
    global lvlmail
    lvlmail += 1
lvldatabasechisa = 0
def lvldatabasechisaadd():
    global lvldatabasechisa
    lvldatabasechisa += 1
lvldatabasecyberia = 0
def lvldatabasecyberiaadd():
    global lvldatabasecyberia
    lvldatabasecyberia += 1
lvldatabaseknights = 0
def lvldatabaseknightsadd():
    global lvldatabaseknights
    lvldatabaseknights += 1
lvlremote = 0
def lvlremoteadd():
    global lvlremote
    lvlremote += 1
lvldarkweb = 0
def lvldarkwebadd():
    global lvldarkweb
    lvldarkweb += 1

#intro
print("Welcome to Navi!")
print("Please Log In: ")

#definitions - names
username = ["lain","Lain"]
loginpassword = ["rilakkuma","Rilakkuma"]

#log in
user = input("Username: \n> ")
if any(user in s for s in username):
    password = input("Password: \n> ")
    if any(password in s for s in loginpassword):

#definitions - functions
        #mail
        def mailapp():
            if lvlmail == 0:
                print("Hello Lain!")
                print("You have one new mail!")
                input("Press enter to read: ")
                print("---------------------")
                print("Sender: Yomoda, Chisa")
                print("Subject: Hello Lain")
                print("Body: God is in here.")
                print("---------------------")
                system('say -v Kathy God is in here.')
                lvlmailadd()
            elif lvldatabasechisa == 1 and lvlmail == 1:
                print("Hello Lain!")
                print("You have one new mail!")
                input("Press enter to read: ")
                print("---------------------")
                print("Sender: Mizuki, Alice ")
                print("Subject: Cyberia")
                print("Body: Hello Lain! Juri, Reiko, and I were going to Cyberia! Why dont you come here?")
                print("---------------------")
                system('say -v Agnes Hello Lain! Juri, Reiko, and I were going to Cyberia! Why dont you come here?')
                lvlmailadd()
            elif lvldatabaseknights == 1 and lvlmail == 2:
                print("Hello Lain!")
                print("You have one new mail!")
                input("Press enter to read: ")
                print("---------------------")
                print("Sender: The Knights ")
                print("Subject: ...")
                print("Body: It begins.")
                print("Attachment: EncryptionKey.asc")
                print("---------------------")
                system('say -v Vicki It begins')
                lvldarkwebadd()
                lvlmailadd()
            else:
                print("Hello Lain!")
                print("You have no new mail!")
            input("Press Enter to continue...")
            functionapp()

        #database
        def databaseapp():
            #definitions
            chisa = ["Chisa Yomoda","Yomoda, Chisa","chisa","Chisa","Yomoda","yomoda","chisa yomoda","yomoda, chisa"]
            theknights = ["The Knights","Knights","knights"]
            exit = ["Exit","exit","return","homepage","back","start","quit","Quit"]
            god = ["god","God"]
            lain = ["lain","Lain","lain iwakura","Lain Iwakura","iwakura, lain","Iwakura, Lain"]
            cyberia = ["Cyberia","cyberia","cyberiachat","CyberiaChat"]
            navi = ["navi","Navi"]
            here = ["here","Here","localhost"]
            thewired = ["The Wired","thewired","wired","Wired","the wired"]
            #function
            searchtarget = input("Who or what would you like to look up? \n> ")
            if any(searchtarget in s for s in chisa):
                print("Searching...")
                time.sleep(3)
                print(Fore.RED + "四方田千砂: Please don't look for me.")
                system('say -v Kathy Please dont look for me.')
                print(Style.RESET_ALL)
                input("Press Enter to continue...")
                lvldatabasechisaadd()
            elif any(searchtarget in s for s in exit):
                functionapp()
            elif any(searchtarget in s for s in theknights):
                print("The Knights of the Eastern Calculus (often the Knights) is a group of pseudonymous, notorious and highly-skilled computer crackers. ")
            elif any(searchtarget in s for s in navi):
                print("The Knowledge Navigator or NAVI for short are high-powered computers designed around accessing The Wired with ease. While some aren't pretty to look at they are unmistakably powerful. NAVIs can come in almost any shape or form. ")
            elif any(searchtarget in s for s in cyberia):
                print("Club Cyberia, also Cyberia Café & Club, commonly referred to as Cyberia, is a nightclub with, oddly, no policy regarding underage visitors. It is located in Shibuya. ")
            elif any(searchtarget in s for s in lain):
                print("127.0.0.1")
            elif any(searchtarget in s for s in god):
                print("An omnipresent being who has at least one follower")
            elif searchtarget == here:
                print("127.0.0.1")
            elif searchtarget == thewired:
                print("The Wired is an internet-like communication system used by the majority of the world. 'There is the world around us, a world of people, tactile sensation, and culture. There is the wired world, inside a computer, of images, personalities, virtual experiences, and a culture all of its own.' The Wired is '...An advanced form of communication.' where people all around the world link to share thoughts, conversation, play games, and socialize. It has become such a meaningful and useful tool in modern society that modern society would almost cease to function without it. I guess you could call it a 'religion' of sorts, as people tend to worship it giving the Wired top priority in their daily lives. Many older citizens of society feel that there is a danger to the Wired. It, while being a very useful tool for life, can also become an obsession to those who do not secure themselves in the reality that no matter how real the Wired may be the true world will always be more real.")
            else:
                print("Target not found.")
                databaseapp()
            functionapp()

        #remote
        def remoteapp():
            #definitions
            cyberiachat = ["CyberiaChat","cyberiachat"]
            school = ["school","School"]
            other = ["random","Random"]
            darkweb = ["darkweb","darknet","deepweb","Deepweb","Darknet","Darkweb"]
            if lvldarkweb == 0:
                network = input("Which network would you like to connect to?: [CyberiaChat], [School], [Random], or [Exit] \n> ")
            else:
                network = input("Which network would you like to connect to?: [CyberiaChat], [School], [Random], [Darknet], or [Exit] \n> ")
            #function
            if lvlremote == 0:
                #cyberiachat
                if any(network in s for s in cyberiachat):
                    print("「Ｗｉｒｅｄ Ｓｏｕｎｄ Ｆｏｒ Ｗｉｒｅｄ Ｐｅｏｐｌｅ」")
                    print("\n")
                    join = input("W o u l d  y o u  l i k e  t o  l o o k  i n s i d e ? (Y/N) \n> ")
                    if join == "y" or "Y":
                        def cyberiachat():
                            print("\nForums:\n\nMusic\nCyber\nRumors\n")
                            forum = input("Please select a forum or [exit]\n> ")
                            #definitions
                            music = ["Music","music","mus"]
                            cyber = ["Cyber","cyber","tech"]
                            rumors = ["Rumors","rumors"]
                            exit = ["exit","Exit","Back","Home","home","homepage","return"]
                            #function
                            if any(forum in s for s in music):
                                print("(1) jj the dj")
                                print("(2) How to apply to DJ")
                                print("(3) ")
                                musthread = input("Please select a thread, or [exit]: \n> ")
                                if musthread == "1":
                                    print("---------------------")
                                    print("Poster: accelaboy")
                                    print("Thread: jj the dj")
                                    print("Post: yo jj is the best of all thime he keeps the groove flowing keeps the energy uppppp")
                                    print("---------------------")
                                    input("Press Enter to continue...")
                                    cyberiachat()
                                elif musthread == "2":
                                    print("---------------------")
                                    print("Poster: DJStylez")
                                    print("Thread: How to apply to DJ")
                                    print("Post: Hello! I was hoping that I could get in contact with whoever does the booking here, I would love to demo what I could do for Cyberia!")
                                    print("---------------------")
                                    input("Press Enter to continue...")
                                    cyberiachat()
                                elif musthread == "3":
                                    print("---------------------")
                                    print("Poster: ")
                                    print("Thread: ")
                                    print("Post: ")
                                    print("---------------------")
                                    input("Press Enter to continue...")
                                    cyberiachat()
                            elif any(forum in s for s in cyber):
                                print("(1) The Knights Sighting???")
                                cybthread = input("Please select a thread: ")
                                if cybthread == "1":
                                    print("---------------------")
                                    print("Poster: lostincyber")
                                    print("Thread: The Knights Sighting???")
                                    print("Post: Whats all this talk about Knights? I heard they were super hackers, but do they actually exist? Is it just another net rumor?")
                                    print("---------------------")
                                    lvldatabaseknightsadd()
                                    input("Press Enter to continue...")
                                    cyberiachat()
                            elif any(forum in s for s in rumors):
                                print("(1)'Lain?'")
                                print("(2) those damn kids")
                                rumthread = input("Please select a thread: \n> ")
                                if rumthread == "1":
                                    print("---------------------")
                                    print("Poster: ")
                                    print("Thread: 'Lain?'")
                                    print("Post: ")
                                    print("---------------------")
                                    input("Press Enter to continue...")
                                    cyberiachat()
                                elif rumthread == "2":
                                    print("---------------------")
                                    print("Poster: pissedpatron")
                                    print("Thread: those damn kids")
                                    print("Post: How are those punk brats here night after night? Are they even old enough to be in a club? Argh those kids cheese me off.")
                                    print("---------------------")
                                    print("Poster: myumyuthecute")
                                    print("Thread: re: those damn kids")
                                    print("Post: Get a life old man.")
                                    input("Press Enter to continue...")
                                    cyberiachat()
                                elif rumthread == "3":
                                    print("---------------------")
                                    print("Poster: truepatriot")
                                    print("Thread: WWIII")
                                    print("Post: WWIII:, is a great war needed for this generation of lazy bundles, SJWs, multiple pronouns, tranny loving, horse fucking young adults?")
                                    print("---------------------")
                                    print("Poster: freedomfriend")
                                    print("Thread: re: WWIII")
                                    print("Post: only soft and spoiled children who have never experience war can say things like that")
                                    print("---------------------")
                                    print("Poster: truepatriot")
                                    print("Thread: re: re: WWIII")
                                    print("Post: You are the soft one friend, and you and your ilk will be removed from our nation in the final days.")
                                    print("---------------------")
                                    input("Press Enter to continue...")
                                    cyberiachat()
                                elif any(forum in s for s in exit):
                                    functionapp()
                    else:
                        remoteapp()
                    cyberiachat()
                #school
                elif any(network in s for s in school):
                    print("Welcome to the Ouka Private Girls Academy network")
                    print("This site is still under development")
                    input("Press Enter to continue...")
                #other
                elif any(network in s for s in other):
                    site = int(random.randrange(1, 5, 1))
                    if site == 1:
                        print("Random Website: dota putin fóóbar weird anime putin Gene høi hallo fullfill the prophesy")
                    elif site == 2:
                        print("Random Website: Post-Apocalyptic is a member-driven directory of websites related to the post-apocalyptic genre!")
                    elif site == 3:
                        print("Random Website: Little dogs like you’ve never even seen them before.")
                    elif site == 4:
                        print("Random Website: Wave cheerio to the blues, any hour of any day.")
                    elif site == 5:
                        print("Random Website: Weirdness to infinity and back.")
                    functionapp()
                #darksites
                elif any(network in s for s in darkweb):
                    drugs = ["drugs","Drugs"]
                    farright = ["Far Right Ideology","Far-Right Ideology","fri","far","far right","farright","FarRight","Far Right","far right ideology","ideology","Ideology","/pol/"]
                    porn = ["Illegal Porn","illegal porn","porn","illegal","CP","cp","cheese pizza"]
                    if lvldarkweb == 0:
                        print("[The 'Top Of Relay' network obfuscation project is under development by the Computer Science department of Tokyo U!\nBe sure to check back regularly for updates!]")
                    elif lvldarkweb > 0:
                        print("Loading...")
                        bar = progressbar.ProgressBar()
                        for i in bar(range(100)):
                            time.sleep(0.02)
                        print("Drugs")
                        print("Far-right Ideology")
                        print("Illegal Porn")
                        print("\n")
                        darksite = input("Please select a site: \n> ")
                        if any(darksite in s for s in drugs):
                            print("Welcome to the Grand Trunk Road!\nThe site where you can buy anything!")
                        elif any(darksite in s for s in farright):
                            print("You're on '/Politically Observant Losers/', the last bastion of free speech on the internet.")
                            toppost = int(random.randrange(1, 5, 1))
                            if toppost == 1:
                                print("Top Post: What are some small redpills to casually drop on the normies?")
                            if toppost == 2:
                                print("Top Post: I can't wait to see the mass suicide of libtards. It's going to be beautiful.")
                            if toppost == 3:
                                print("Top Post: Do vaccines cause autism?")
                            if toppost == 4:
                                print("Top Post: What are some of your degenerate habits, how are you planning to stop them, or what have you stopped?")
                            if toppost == 5:
                                print("Top Post: People always say that Women crash their cars because they are horrible drivers, yet studies show that Women are better drivers than Men")
                        elif any(darksite in s for s in porn):
                            print("Chuckie's Cheese Pizza, delivered hot and fresh!")
                            pedologin = input("Username:\n> ")
                            if pedologin == "zippydoodah":
                                pedopassword = input("Password:\n> ")
                                if pedopassword == "puddinpops":
                                    print(Fore.RED + "מֹלֶךְ")
                                    print(Style.RESET_ALL)
                                    input("There is no way to go back...")
                                    exit()
                            input("Press Enter to return...")
                        else:
                            print("Site not found!")
            #post event remoting
            elif lvlremote == 1:
                if any(network in s for s in cyberiachat):
                    print("This website is experiencing issues")
                elif any(network in s for s in school):
                    print("")
                elif any(network in s for s in other):
                    print("")
            input("Press Enter to continue...")
            functionapp()

        #function director
        def functionapp():
            #definitions
            mail = ["mail","Mail"]
            remote = ["remote","Remote"]
            database = ["database","Database"]
            exit = ["Exit","exit","return","homepage","back","start","quit","Quit"]
            #function
            function = input("Which would you like [Mail], [Database], [Remote], or [Exit]?: \n> ")
            if any(function in s for s in mail):
                mailapp()
            elif any(function in s for s in database):
                databaseapp()
            elif any(function in s for s in remote):
                remoteapp()
            elif any(function in s for s in exit):
                system('exit')
            else:
                print("Function not found.")
                input("Press Enter to continue...")
                functionapp()
        #homepage
        def homepage():
            print("Welcome Lain~")
            input("Press Enter to continue...")
            functionapp()

#start
        system('say -v Whisper Weird: Layer zero one')
        homepage()

#error messages
    else:
        print("Login Failed")
else:
    print("Login Failed")
deinit()
