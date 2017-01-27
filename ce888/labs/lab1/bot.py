from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()
counter = [0] * 6
numOfmessages = 0

@module.rule('')
def hi(bot, trigger):
    global numOfmessages
    numOfmessages +=1
    print(trigger, trigger.nick)
    triggeredEmo = emo.detect_emotion_in_raw_np(trigger)
    messageIndex = 0
    for i,val in enumerate(triggeredEmo):
        if(val!=0):
            counter[i] += 1
            messageIndex = i
    for i, val in enumerate(counter):
        if(i == 0):
            print('anger: '  + str(val / numOfmessages))
        if (i == 1):
            print('disgust: ' +  str(val / numOfmessages))
        if (i==2):
            print('fear: ' + str(val / numOfmessages))
        if (i == 3):
            print('joy: ' + str(val / numOfmessages))
        if (i == 4):
            print('sadness: ' + str(val / numOfmessages))
        if (i == 5):
            print('surprise: ' + str(val / numOfmessages))



    print(counter)

    #bot.say('Hi, ' + trigger.nick)
