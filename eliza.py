"""Eliza homework. Relationship Advisor"""
__author__ = "Paulina Morales"
# # -*- coding: utf-8 -*-
import re
import random

emotions = [[r'([mM]y name is\w*)', "How are you today, x?", "How are you, x?", "How are you feeling, x?"],
            [r'\w*mother|mom|dad|father|brother|brothers|sister|sisters|cousin|cousins|aunt|aunts|friend|friends\w*', 'Tell me more about your x', 'What is your relationship like with your x?'],
            [r'\w*[Ss]ad|[Mm]ad|[Hh]appy|[Jj]oy|[Bb]ad|[Gg]ood|[Nn]umb\w*', 'Why are you x?', 'x. Tell me more.', 'What makes you feel x?'],
            [r'\w*(okay|\s+ok|fine)\w*', 'Why just "x"?'],
            [r'\w*start|\s+end+\s\w*', 'When did it x?', 'Why did it x?'],
            [r'\w*talk|cry|scream|read|shout|laugh|fight\w*', 'Why did you x?', 'How does xing make you feel?'],
            [r'(cook|watch|eat)', 'What do you like xing?', 'What did you x?'],
            ["no match", 'Tell me more', 'Can you elaborate?']]
intro = "Hi my name is Eliza. What's your name?"
greetings = ["How are you today, name?", "How are you, name?", "How are you feeling?"]

def eliza():
    global flag
    user_ans = input(intro)
    matched = re.findall(emotions[0][0], user_ans)
    if matched:
        matched = user_ans.split(" ")
        response = re.sub("x", matched[3], emotions[0][2])
        user_ans = input(response)
        while (user_ans != 'Bye' and user_ans != 'bye'):
            for i in range(len(emotions)):
                flag = False
                match = re.findall(emotions[i][0], user_ans)
                if match:
                    flag = True
                    user_ans = input(talk(i, match))
                    break
            if not flag:
                match = "no match"
                user_ans = input(talk(len(emotions) - 1, match))
        if user_ans == 'bye' or user_ans == 'Bye':
            print("Goodbye!")


def talk(i, match):
    new_emo = emotions[i][1:]
    response = random.choice(new_emo)
    response = re.sub("x", match[0], response) #if the string contains x.
    return(response)

if __name__ == "__main__":
    eliza()