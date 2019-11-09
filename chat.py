import bot
import time

if __name__ == '__main__':

    while True:
        try:
            user_input = input('>')

            time_begin=time.time()
            # response_time = utils.get_response_time(bot.little_white, user_input)

            bot_response = bot.little_white.get_response(user_input)

            time_end=time.time()
            response_time=time_end-time_begin

            print(f'{bot_response} [uses {response_time}]')

        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
