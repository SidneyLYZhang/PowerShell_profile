#################################################################################################
#                 _                                        _
#     __ _   ___ | |_         ___   ___   ___  _ __   ___ | |_
#    / _` | / _ \| __| _____ / __| / _ \ / __|| '__| / _ \| __|
#   | (_| ||  __/| |_ |_____|\__ \|  __/| (__ | |   |  __/| |_
#    \__, | \___| \__|       |___/ \___| \___||_|    \___| \__|
#    |___/
#
# =============================================================================================== 
#
#   Update : 2020-02-17
#   Coding by : SidneyZhang <zly@lyzhang.me>
#  
#################################################################################################

##########################
#        FOREWORD        #
##########################

"""
一个简单的密码管理的小程序，仅适合保存不怕泄密的密码内容。因为仅包含非必须的简单加密方法，所以：
        __请注意使用安全__。

A simple password management applet, only suitable for saving password contents that is
not afraid of leaking. Because it only includes non-essential simple encryption methods, 
        __BE CAREFUL ABOUT SECURITY__ .

如有修改建议，请直接在Github提交，如想了解我的情况请访问我的Blog ： https://lyzhang.me

Welcome to my website : https://lyzhang.me
"""

##########################
#        PACGAGES        #
##########################

import click
import json
import os
import hashlib
import random
import string
import fire
from pyfiglet import Figlet
from base64 import b64encode,b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

##########################
#        SETTING         #
##########################

SecretFile = "C:/Users/alfch/AppData/StaticData/secretwords.json" # file path and file name
CRYTOUSER = "SidneyZhang" # your name

##########################
#        CRYPTION        #
##########################

# ENCRYPTION
def encryption(text, key, current_info):
    thenonce = get_random_bytes(16)
    password = hashlib.blake2s(key.encode()).digest()
    cipher = AES.new(password, AES.MODE_EAX, nonce = thenonce)
    fixed = CRYTOUSER.encode() + current_info.encode()
    cipher.update(fixed)
    ciphText, tag = cipher.encrypt_and_digest(text.encode())
    re_key = ['nonce', 'fix', 'citext', 'tag']
    re_val = [ b64encode(x).decode('utf-8') for x in (cipher.nonce, CRYTOUSER.encode(), ciphText, tag) ]
    result = json.dumps(dict(zip(re_key,re_val)))
    return result

# DECRYPTION
def decryption(setext, key, current_info):
    password = hashlib.blake2s(key.encode()).digest()
    try:
        text64 = json.loads(setext)
        t_key = ['nonce', 'fix', 'citext', 'tag']
        t_val = { k : b64decode(text64[k]) for k in t_key }
        cihper = AES.new(password, AES.MODE_EAX, nonce = t_val['nonce'])
        cihper.update(t_val['fix'] + current_info.encode())
        result = cihper.decrypt_and_verify(t_val['citext'], t_val['tag'])
        result = result.decode()
    except :
        result = "Password is invalid!"
    return result

##########################
#        FUNCTIONS       #
##########################

# COLOR-PRINT
def lolcat(words, colors = "white", reverse = False, light = False, oneline = False):
    color = colors.lower()
    foreground = {
        "white" : 37,
        "cyan" : 36,
        "magenta" : 35,
        "blue" : 34,
        "yellow" : 33,
        "green" : 32,
        "red" : 31,
        "black" : 30
    }[color]
    if reverse :
        reout = 47 + 30 - foreground
    else :
        reout = 40
    if light :
        liout = 1
    else :
        liout = 0
    if oneline :
        print("\033[{};{};{}m{}\033[0m".format(liout,foreground,reout,words), end = "")
    else :
        print("\033[{};{};{}m{}\033[0m".format(liout,foreground,reout,words))

# FORMAT-PRINT
def output_info(secret_dick, password = None):
    thekey = list(secret_dick.keys())
    for i in thekey :
        if secret_dick[i] != "######" :
            title = i + " :"
            lolcat(title, colors = "yellow", oneline = True)
            if isinstance(password, str) and i in ["Username","Password"]:
                infos = decryption(secret_dick[i], password, i)
            else :
                infos = secret_dick[i]
            lolcat("\t\t" + infos)

# LOADING-FILES
def load_secret():
    #loading direct secretwords-file
    with open(SecretFile, encoding='utf8') as sf :
        sefile = json.load(sf)
    seWords = dict()
    for i in sefile :
        seWords[i["Name"]] = i["Value"]
    return seWords

# PREPROGRAM
def has_secret():
    #create secretwords file if there is no secretwords-file
    if not os.path.exists(SecretFile) :
        path_dir = os.path.dirname(SecretFile)
        if not os.path.exists(path_dir) :
            os.makedirs(path_dir)
        open(SecretFile,"w").close()
        lolcat("\nCreation is complete ...\n",color = 'yellow')
    else :
        lolcat("\nSecret File is exists, not to create one ...\n",color = 'yellow')

# SEARCH-INFOS
def search_secret(mode = "all", keywords = None, password = None):
    #search the file by four modes
    #mode:{all,title,curtype,exist}
    data = load_secret()
    if mode == "all" :
        lolcat("All information is listed below here :".upper(), colors = "red")
        lolcat("所有密码信息如下 :", colors = "red")
        for key in data.keys() :
            lolcat(key.upper(), colors = "blue")
            if isinstance(data[key], list) :
                nx = 1
                for od in data[key] :
                    lolcat(("(" + str(nx) + ")"), colors = "yellow", oneline = True)
                    output_info(od, password = password)
                    nx += 1
            else :
                output_info(data[key], password = password)
    elif mode == "title" :
        lolcat("The key information is shown below here :".upper(), colors = "red")
        lolcat("关键信息如下所示 :", colors = "red")
        for key in data.keys() :
            if isinstance(data[key], list) :
                tem = []
                for i in data[key] :
                    if i["Type"] == "######" :
                        tem.extend([i["Description"]])
                    else :
                        tem.extend([i["Type"]])
                lolcat((key.upper() + " :\t\t"), colors = "Yellow", oneline = True)
                lolcat(str(tem))
            else :
                lolcat((key.upper() + " :\t\t"), colors = "yellow", oneline = True)
                lolcat(data[key]["Description"])
    elif mode == "curtype" :
        if keywords in data.keys() :
            lolcat("Found information :".upper(), colors = "red")
            if isinstance(data[keywords], list) :
                nx = 1
                for od in data[keywords] :
                    lolcat(("(" + str(nx) + ")"), colors = "yellow", oneline = True)
                    output_info(od, password = password)
                    nx += 1
            else :
                output_info(data[keywords], password = password)
        else :
            nodata = True
            for key in data.keys() :
                if isinstance(data[key], list) :
                    for item in data[key] :
                        if keywords in item["Type"] :
                            output_info(item, password = password)
                            nodata = False
                        elif keywords in item["Description"] :
                            output_info(item, password = password)
                            nodata = False
            if nodata :
                lolcat("The keywords for searching is wrong...")
                lolcat("There is no informatin ahout your inputing-test.")
    elif mode == "exist" :
        if keywords in data.keys() :
            lolcat("The information is exists...", colors = "green")
        else :
            tydata = []
            for key in data.keys() :
                if isinstance(data[key], list) :
                    for item in data[key] :
                        tydata.append(item["Type"])
            if keywords in tydata :
                lolcat("The information is exists...", colors = "green")
            else :
                lolcat("No found your keywords...")
    else :
        lolcat("Selected a wrong mode...", colors = "red")
        lolcat("Supported Modes : ", colors = "Green")
        lolcat("  (1) all :\t\t getting all informations of passwords that you saved;")
        lolcat("  (2) title :\t\t getting the key informations of those passwords;")
        lolcat("  (3) curtype :\t\t getting the information that you need;")
        lolcat("  (4) exist :\t\t whether ther is an existed keywords in your secret-file.")

# ADD-SECRETS
def add_secret(name, username, password, type = "######", 
                description = "######", web = "######", secret_password = None):
    #add new information to the secret file
    oriData = load_secret()
    if secret_password :
        addData = {
            "Type" : type,
            "Description" : description,
            "Web" : web,
            "Username" : encryption(username,secret_password,"Username"),
            "Password" : encryption(password,secret_password,"Password")
        }
    else :
        addData = {
            "Type" : type,
            "Description" : description,
            "Web" : web,
            "Username" : username,
            "Password" : password
        }
    if name in oriData.keys() :
        if isinstance(oriData[name], list) :
            temp = oriData[name]
            temp.append(addData)
            oriData[name] = temp
        else :
            oriData[name]["Type"] = Name
            oriData[name] = [oriData[name] , addData]
    else :
        oriData[name] = addData
    result = json.dumps(oriData, indent = 4)
    with open(SecretFile,"w") as f :
        f.write(result)
    lolcat("\nAdding information is complete ...\n", colors = "green")

##########################
#        DO-PROGRAM      #
##########################

# COMMAND:ADD
class addness(object):
    def __init__(self, name = None, password = None):
        if name is None :
            named = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(8,15)))
        else :
            named = name
        self._name = named
        self._password = password
    
    def new(self, user = CRYTOUSER, keywords = "######", types = "######", web = "######",
                description = "######", multiple = None):
        if multiple is None:
            mds = [user,keywords,types,web,description]
            add_secret(name = self._name, username = mds[0], password = mds[1], type = mds[2], 
                        description = mds[4], web = mds[3], secret_password = self._password)
        else :
            mlen = len(multiple)
            if mlen >= 2 and mlen <= 5 :
                mds = list(multiple) + ["######"] * (5-mlen)
                add_secret(name = self._name, username = mds[0], password = mds[1], type = mds[2], 
                            description = mds[4], web = mds[3], secret_password = self._password)
            else :
                lolcat("ERROR : Multiple must have at least 2 items and no more than 5 items...", colors = "red")
    
    def help(self):
        lolcat("Usage : python getSecret.py add [--name <your name> --password <crytion-password>] new <user> <key>")
        lolcat("\t\tMore information by command \"python getSecret.py help\".")

# COMMAND:SEARCH
class searchness(object):
    def __init__(self, password = None):
        self._password = password
    
    def by(self, mode, text = None):
        search_secret(mode = mode, keywords = text, password = self._password)
    
    def help(self):
        lolcat("Usage : python getSecret.py search [--password <crytion-password>] by <mode> <text>")
        lolcat("\t\tMore information by command \"python getSecret.py help\".")

# COMMAND:GROUP
class CommandsNow(object) :
    # COMMAND-GROUP INIT
    def __init__(self):
        self.add = addness()
        self.search = searchness()
    
    # COMMAND:INIT
    def init(self):
        has_secret()
        lolcat("DONE", colors = "yellow")
    
    # COMMAND:HELP
    def help(self):
        figtoken = Figlet(font = "big")
        lolcat(figtoken.renderText("Secret-Applet"), colors = "Green")
        lolcat("\tCode by : \tSidney Zhang <zly@lyzhang.me>")
        lolcat("\tLast Update : \t2020-02-17 in Tianjin")
        lolcat("="*78, colors = "green")
        print("\n")
        lolcat(__doc__, colors = "magenta")
        print("\n")
        lolcat("-"*78 + "\n\n", colors = "green")
        lolcat("USAGE", colors = "yellow")
        lolcat("\n\tpython getSecret.py COMMAND [option] [...]\n", colors = "cyan")
        lolcat("\tCOMMAND :")
        lolcat("\t\thelp : \t\t\t\tShow this help message and exit")
        lolcat("\t\tversion : \t\t\t\tShow version infomation and exit")
        lolcat("\t\tinit : \t\t\t\tInitialize the secret-file")
        lolcat("\t\tadd [option] : \t\t\tAdd information of new password to the secret-file")
        lolcat("\t\tsearch [option] [...] : \tGet the information that you need\n")
        lolcat("\tAdd Argument :")
        lolcat("\t\tname : \t\t\t\tgive the topname for adding information")
        lolcat("\tAdd Option :")
        lolcat("\t\t--user : \t\t\tusername for the password")
        lolcat("\t\t--keyword : \t\t\tthe password")
        lolcat("\t\t--types : \t\t\ttype for Distinguishing between passwords")
        lolcat("\t\t--web : \t\t\tlogin web")
        lolcat("\t\t--description : \t\tinformation for the password")
        lolcat("\t\t--password : \t\tpassword for cryption")
        lolcat("\t\t--multiple : \t\tmultiple input by all things\n")
        lolcat("\tSearch Argument :")
        lolcat("\t\tmode : \t\t\t\tsearch mode, four type: all/title/curtype/exist")
        lolcat("\tSearch Option :")
        lolcat("\t\t--keywords : \t\tsearch by this word")
        lolcat("\t\t--password : \t\tpassword for cryption")
        lolcat("EXAMPLE", colors = "yellow")
        lolcat("\t(a) $python getSecret.py add blog new --user sidney --keywords 123456 --password 333333", colors = "cyan")
        lolcat("\t   Add a new topic that named blog, and this password is 123456 under username [sidney],")
        lolcat("\t   at the sametime the information will be encrypted by 333333.")
        lolcat("\t(b) $python getSecret.py search by all", colors = "cyan")
        lolcat("\t   Print all information in your secret-file.")
        lolcat("\t(c) $python getSecret.py add blog new --multiple \"('sidney','123456')\" --password 333333", colors = "cyan")
        lolcat("\t   Add a new topic that named blog, this is equal to the command (a).")
        lolcat("LICENSE", colors = "yellow")
        lolcat("\tThe MIT License (MIT)", colors = "blue")
        lolcat("\tcopyright (c) 2019-2020", colors = "blue")
        lolcat("\t\tSidney Zhang <zly@lyzhang.me>", colors = "blue")
        lolcat("\t(See full details of License in github/SidneyLYZhang/PowerShell_profile)", 
                colors = "blue", light = True)
    
    # COMMAND:VERSION
    def version(self, infos = "all"):
        if infos == "all" :
            lolcat("SECRET-APPLET \tin python", colors = "Green")
            lolcat("Coding by \tSidney Zhang <zly@lyzhang.me>", light = True)
            lolcat("Last Update : \t2020-02-17", colors = "yellow")
            lolcat("Version : \tv2.0.1", colors = "yellow")
        elif infos == "value" :
            return ("Secret-Applet version 2.0.1")
        elif infos == "jiangjiang" :
            figtoken = Figlet(font = "big")
            lolcat(figtoken.renderText("LOVE&PEACE"), colors = "red")
            lolcat("无论在哪，都可以写下这句话。\tby my wife - Jiangjiang ♥", colors = "red")
            lolcat("Secret-Applet version 2.0.1", colors = "yellow")
        elif infos == "email" :
            lolcat("About this script, touch me by my email <zly@lyzhang.me> ...", colors = "yellow")
            lolcat("BUT I don't often check my email ... Please be patient ...", colors = "yellow")
        else :
            lolcat("Secret-Applet version 2.0.1", colors = "yellow")
            

# COMMANDS-CLI
def cli():
    fire.Fire(CommandsNow)

##########################
#        MAINPROGRAM     #
##########################

if __name__ == '__main__':
    cli()

##########################
#        LICENSE         #
##########################
#
# Copyright © 2020 SidneyZhang<zly@lyzhang.me>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this 
# software and associated documentation files (the “Software”), to deal in the Software 
# without restriction, including without limitation the rights to use, copy, modify, 
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to 
# permit persons to whom the Software is furnished to do so, subject to the following 
# conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.