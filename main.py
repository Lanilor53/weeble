import os
from bot.bot import DiscordBot

if __name__ == '__main__':

    bot = DiscordBot()

    if not os.path.exists('{0}\{1}'.format(os.getcwd(), 'config.ini')):
        print('Creating base configuration file...')
        bot.create_config()
    else:
        bot.get_token()

    bot.run()