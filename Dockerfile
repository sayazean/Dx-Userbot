# Using Python Slim-Buster
Fromm kyyex/kyy-userbot:busterv2
#━━━━━ Userbot Telegram ━━━━━━
#━━━━━ By AbingxUserbot ━━━━━

RUN git clone -b AbingxUserbot https://github.com/SayaAbing/AbingxUserbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/SayaAbing/AbingxUserbot/AbingxUserbot/requirements.txt

EXPOSE 80 443

# Finalization
