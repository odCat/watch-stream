#!python

import os

streams = ['shinmiri2']
twitch_link = 'https://www.twitch.tv/'

if __name__ == '__main__':
    command = 'streamlink ' + twitch_link + streams[0] + ' best'
    os.system(command)

