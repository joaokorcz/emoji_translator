'''
Emoji translator by joao otavio
'''

import emoji

def comparator_n_translator(phrase):
    phrase = phrase.lower()
    phrase_=''
    for i in range(len(phrase)):
        if phrase[i]=='p':
            phrase_+=emoji.emojize(':parking:', use_aliases=True)
        elif phrase[i]=='a':
            phrase_+=emoji.emojize(':a:', use_aliases=True)
        elif phrase[i]=='t':
            phrase_+=emoji.emojize(':latin_cross:', use_aliases=True)
        elif phrase[i]=='o':
            phrase_+=emoji.emojize(':o2:', use_aliases=True)
        elif phrase[i]=='r':
            phrase_+=emoji.emojize(':registered:', use_aliases=True)
        elif phrase[i]=='d':
            phrase_+=emoji.emojize(':leftwards_arrow_with_hook:', use_aliases=True)
        elif phrase[i]=='c':
            phrase_+=emoji.emojize(':copyright:', use_aliases=True)
        elif phrase[i]=='m':
            phrase_+=emoji.emojize(':scorpius:', use_aliases=True)
        elif phrase[i]=='b':
            phrase_+=emoji.emojize(':b:', use_aliases=True)
        elif phrase[i]=='i':
            phrase_+=emoji.emojize(':information:', use_aliases=True)
        elif phrase[i]=='v':
            phrase_+=emoji.emojize(':aries:', use_aliases=True)
        elif phrase[i]=='x':
            phrase_+=emoji.emojize(':x:', use_aliases=True)
        elif phrase[i]=='s':
            phrase_+=emoji.emojize(':heavy_dollar_sign:', use_aliases=True)
        elif phrase[i]=='n':
            phrase_+=emoji.emojize(':capricorn:', use_aliases=True)
        elif phrase[i]=='l':
            phrase_+=emoji.emojize(':call_me_hand:', use_aliases=True)
        elif phrase[i]=='h':
            phrase_+=emoji.emojize(':pisces:', use_aliases=True)
        elif phrase[i]=='u':
            phrase_+=emoji.emojize(':ophiuchus:', use_aliases=True)
        elif phrase[i]=='j':
            phrase_+=emoji.emojize(':heavy_check_mark:', use_aliases=True)
        elif phrase[i]=='z':
            phrase_+=emoji.emojize(':zzz:', use_aliases=True)
        elif phrase[i]=='g':
            phrase_+=emoji.emojize(':cyclone:', use_aliases=True)
        elif phrase[i]=='e':
            phrase_+=emoji.emojize(':three:', use_aliases=True)
        elif phrase[i]=='w':
            phrase_+=emoji.emojize(':trident:', use_aliases=True)
        elif phrase[i]=='f':
            phrase_+=emoji.emojize(':joker:', use_aliases=True)
        elif phrase[i]=='k':
            phrase_+=emoji.emojize(':joker:', use_aliases=True)
        elif phrase[i]=='q':
            phrase_+=emoji.emojize(':pretzel:', use_aliases=True)
        elif phrase[i]=='y':
            phrase_+=emoji.emojize(':person_cartwheeling:', use_aliases=True)
        elif phrase[i]=='?':
            phrase_+=emoji.emojize(':question:', use_aliases=True)
        elif phrase[i]==' ':
            phrase_+='\n\n'
        else:
            phrase_+=phrase[i]
    return phrase_

def main():
    phrase = input('pinto: ')
    phrase = comparator_n_translator(phrase)
    print('toma:', phrase)
main()
