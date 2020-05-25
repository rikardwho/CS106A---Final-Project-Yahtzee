import random
from tkinter import *
from tkinter import Canvas

NUM_DICE = 5
NUM_SIDES = 6
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 700
SIDE_LENGTH = 40
BG_COLOR1 = '#dc94ff'
BG_COLOR2 = '#ffb5dc'
BG_COLOR3 = '#ffb5dc'
DICE_COLOR = '#60e6c2'
BG_COLOR4 = '#ffd596'
HOLD_COLOR = '#cb63ff'
HOLD_BG = '#eabfff'
BUTTON_Y_PADDING = 3
BUTTON_Y_PADDING2 = 3
LIME = '#ccffcd'
PEACH = '#ffa1a1'
ORANGE = '#ff925c'
SCORE_RELIEF = 'ridge'


def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Yahtzee')

    # Aesthetics -----------------------------------------------------------------------------------

    scoreboardUpper = Frame(canvas,
                            bg=BG_COLOR1,
                            highlightbackground='black',
                            highlightthickness=1)
    scoreboardUpper.columnconfigure(1, minsize=151)
    scoreboardUpper.grid(column=0, row=0, sticky=W)

    scoreboardLower = Frame(canvas,
                            bg=BG_COLOR1,
                            highlightbackground='black',
                            highlightthickness=1)
    scoreboardLower.columnconfigure(1, minsize=150)
    scoreboardLower.grid(column=0, row=1, sticky=NW)

    # Dice board widgets -----------------------------------------------------------------------------------

    diceboard = Canvas(canvas,
                       bg=BG_COLOR2,
                       highlightbackground="black",
                       highlightthickness=1,
                       width=CANVAS_WIDTH,
                       height=80)
    diceboard.grid(column=0, row=3, columnspan=10, sticky=W)

    # Check Button widgets -----------------------------------------------------------------------------------

    cbFrame = Frame(canvas,
                    highlightbackground="black",
                    highlightthickness=1,
                    width=CANVAS_WIDTH,
                    bg=HOLD_BG)
    for i in range(5):
        cbFrame.columnconfigure(i, minsize=80)
    cbFrame.grid(column=0, row=4, columnspan=10, sticky=W)

    # Set Button widgets -------------------------------------------------------------------------------------

    setButtonFrameUpper = Frame(canvas, highlightbackground="black",
                                highlightthickness=1, bg=BG_COLOR4, pady=32)
    setButtonFrameUpper.columnconfigure(0, minsize=111)
    setButtonFrameUpper.grid(column=2, row=0, sticky=N)

    setButtonFrameLower = Frame(canvas, highlightbackground="black",
                                highlightthickness=1, bg=BG_COLOR4, pady=26)
    setButtonFrameLower.grid(column=2, row=1, sticky=N)

    # Player score widgets -------------------------------------------------------------------------------------

    playerscoreUpper = Frame(canvas,
                             bg=BG_COLOR3,
                             highlightbackground='black',
                             highlightthickness=1)
    playerscoreUpper.grid(column=1, row=0, sticky=NW)
    for i in range(10):
        playerscoreUpper.rowconfigure(i, minsize=27)
    # for i in range(2):
    # playerscoreUpper.grid_columnconfigure(i, weight=1, uniform='uprScr')

    playerscoreLower = Frame(canvas,
                             highlightbackground='black',
                             highlightthickness=1,
                             bg=BG_COLOR3)
    playerscoreLower.grid(column=1, row=1, sticky=NW)
    for i in range(10):
        playerscoreLower.rowconfigure(i, minsize=27)
    for i in range(2):
        playerscoreLower.columnconfigure(i, minsize=57)

    # Button Frame -----------------------------------------------------------------------------------

    buttonFrame = Frame(canvas, highlightbackground='black',
                        highlightthickness=1, bg=PEACH)
    buttonFrame.grid(column=2, row=3, rowspan=2, sticky=NW)

    # Game Score widgets -----------------------------------------------------------------------------------

    # make_gamescore(playerscoreUpper, "Player 1", 0, 0)
    # make_gamescore(playerscoreLower, "Player 1", 0, 0)

    playerOneLabel = Label(playerscoreUpper, text='Player 1', font=('helvetica', 16, 'bold'), borderwidth=1,
                           relief='raised')
    playerTwoLabel = Label(playerscoreUpper, text='Player 2', font=('helvetica', 16, 'bold'), borderwidth=1,
                           relief='raised')

    playerOneLabel.grid(column=0, row=0)
    playerTwoLabel.grid(column=1, row=0)

    aceScoreLbl = Label(playerscoreUpper, text='0', font=('helvetica', 16, 'bold'), borderwidth=2, relief=SCORE_RELIEF)
    twoScoreLbl = Label(playerscoreUpper, text='0', font=('helvetica', 16, 'bold'), borderwidth=2, relief=SCORE_RELIEF)
    threeScoreLbl = Label(playerscoreUpper, text='0', font=('helvetica', 16, 'bold'), borderwidth=2,
                          relief=SCORE_RELIEF)
    fourScoreLbl = Label(playerscoreUpper, text='0', font=('helvetica', 16, 'bold'), borderwidth=2, relief=SCORE_RELIEF)
    fiveScoreLbl = Label(playerscoreUpper, text='0', font=('helvetica', 16, 'bold'), borderwidth=2, relief=SCORE_RELIEF)
    sixScoreLbl = Label(playerscoreUpper, text='0', font=('helvetica', 16, 'bold'), borderwidth=2, relief=SCORE_RELIEF)
    aceScoreLbl.grid(column=0, row=1)
    twoScoreLbl.grid(column=0, row=2)
    threeScoreLbl.grid(column=0, row=3)
    fourScoreLbl.grid(column=0, row=4)
    fiveScoreLbl.grid(column=0, row=5)
    sixScoreLbl.grid(column=0, row=6)

    totalLbl = Label(playerscoreUpper, text=0, font=('helvetica', 16, 'bold'), borderwidth=2, relief=SCORE_RELIEF)
    totalLbl.grid(column=0, row=7)

    bonusScoreLbl = Label(playerscoreUpper, text='0', font=('helvetica', 16, 'bold'),
                          borderwidth=2, relief=SCORE_RELIEF)
    bonusScoreLbl.grid(column=0, row=8)

    totalOfUpperSectionLbl = Label(playerscoreUpper, text=0, font=('helvetica', 16, 'bold'),
                                   borderwidth=2, relief=SCORE_RELIEF)
    totalOfUpperSectionLbl.grid(column=0, row=9)

    playerOneLabelLower = Label(playerscoreLower, text='Player 1', font=('helvetica', 16, 'bold'), borderwidth=1,
                                relief='raised')
    playerTwoLabelLower = Label(playerscoreLower, text='Player 2', font=('helvetica', 16, 'bold'), borderwidth=1,
                                relief='raised')

    playerOneLabelLower.grid(column=0, row=0)
    playerTwoLabelLower.grid(column=1, row=0)

    threeOfKindScoreLbl = Label(playerscoreLower, text='0', font=('helvetica', 16, 'bold'), borderwidth=2,
                                relief=SCORE_RELIEF)
    fourOfKindScoreLbl = Label(playerscoreLower, text='0', font=('helvetica', 16, 'bold'), borderwidth=2,
                               relief=SCORE_RELIEF)
    fullHouseScoreLbl = Label(playerscoreLower, text='0', font=('helvetica', 16, 'bold'), borderwidth=2,
                              relief=SCORE_RELIEF)
    lowStraightScoreLbl = Label(playerscoreLower, text='0', font=('helvetica', 16, 'bold'), borderwidth=2,
                                relief=SCORE_RELIEF)
    highStraightScoreLbl = Label(playerscoreLower, text='0', font=('helvetica', 16, 'bold'), borderwidth=2,
                                 relief=SCORE_RELIEF)
    yahtzeeScoreLbl = Label(playerscoreLower, text='0', font=('helvetica', 16, 'bold'), borderwidth=2,
                            relief=SCORE_RELIEF)
    chanceScoreLbl = Label(playerscoreLower, text='0', font=('helvetica', 16, 'bold'), borderwidth=2,
                           relief=SCORE_RELIEF)
    yahtzeeBonusScoreLbl = Label(playerscoreLower, text='0', font=('helvetica', 16, 'bold'), borderwidth=2,
                                 relief=SCORE_RELIEF)
    totalOfLowerSectionLbl = Label(playerscoreLower, text='0', font=('helvetica', 16, 'bold'), borderwidth=2,
                                   relief=SCORE_RELIEF)
    grandTotalScoreLbl = Label(playerscoreLower, text='0', font=('helvetica', 16, 'bold'), borderwidth=2,
                               relief=SCORE_RELIEF)
    # playerscoreLowerFillerLbl = Label(playerscoreLower, bg=BG_COLOR3)

    threeOfKindScoreLbl.grid(column=0, row=1)
    fourOfKindScoreLbl.grid(column=0, row=2)
    fullHouseScoreLbl.grid(column=0, row=3)
    lowStraightScoreLbl.grid(column=0, row=4)
    highStraightScoreLbl.grid(column=0, row=5)
    yahtzeeScoreLbl.grid(column=0, row=6)
    chanceScoreLbl.grid(column=0, row=7)
    yahtzeeBonusScoreLbl.grid(column=0, row=8)
    totalOfLowerSectionLbl.grid(column=0, row=9)
    grandTotalScoreLbl.grid(column=0, row=10)
    # playerscoreLowerFillerLbl.grid(column=0, row=11)
    playerscoreLower.rowconfigure(11, minsize=3)
    # make_gamescore(playerscoreUpper, "Player 2", 1, 0)
    # make_gamescore(playerscoreLower, "Player 2", 1, 0)

    scoreLabels = [aceScoreLbl,
                   twoScoreLbl,
                   threeScoreLbl,
                   fourScoreLbl,
                   fiveScoreLbl,
                   sixScoreLbl,
                   totalLbl,
                   bonusScoreLbl,
                   totalOfUpperSectionLbl,
                   threeOfKindScoreLbl,
                   fourOfKindScoreLbl,
                   fullHouseScoreLbl,
                   lowStraightScoreLbl,
                   highStraightScoreLbl,
                   yahtzeeScoreLbl,
                   chanceScoreLbl,
                   yahtzeeBonusScoreLbl]

    # Upper Section Widgets in frame ----------------------------------------------------------------------
    uppersectionLbl = Label(scoreboardUpper, text='Upper Section', font=('helvetica', 16, 'bold'), bg=BG_COLOR1)
    onesLbl = Label(scoreboardUpper, text='Count and add only Aces', font=('helvetica', 16), bg=BG_COLOR1)
    twosLbl = Label(scoreboardUpper, text='Count and add only Twos', font=('helvetica', 16), bg=BG_COLOR1)
    threesLbl = Label(scoreboardUpper, text='Count and add only Threes', font=('helvetica', 16), bg=BG_COLOR1)
    foursLbl = Label(scoreboardUpper, text='Count and add only Fours', font=('helvetica', 16), bg=BG_COLOR1)
    fivesLbl = Label(scoreboardUpper, text='Count and add only Fives', font=('helvetica', 16), bg=BG_COLOR1)
    sixesLbl = Label(scoreboardUpper, text='Count and add only Sixes', font=('helvetica', 16), bg=BG_COLOR1)
    totalUpr1Lbl = Label(scoreboardUpper, text='Total', font=('helvetica', 16, 'bold'), bg=BG_COLOR1)
    bonusLbl = Label(scoreboardUpper, text='63 + scores a 35 Bonus', font=('helvetica', 16, 'bold'), bg=BG_COLOR1)
    totalUpr2Lbl = Label(scoreboardUpper, text='Total of Upper Section', font=('helvetica', 16, 'bold'), bg=BG_COLOR1)

    uppersectionLbl.grid(column=0, row=0, sticky=W)
    onesLbl.grid(column=0, row=2, columnspan=4, sticky=E)
    twosLbl.grid(column=0, row=4, columnspan=2, sticky=E)
    threesLbl.grid(column=0, row=6, columnspan=2, sticky=E)
    foursLbl.grid(column=0, row=8, columnspan=2, sticky=E)
    fivesLbl.grid(column=0, row=10, columnspan=2, sticky=E)
    sixesLbl.grid(column=0, row=12, columnspan=2, sticky=E)
    totalUpr1Lbl.grid(column=0, row=14, columnspan=2, sticky=E)
    bonusLbl.grid(column=0, row=16, columnspan=2, sticky=E)
    totalUpr2Lbl.grid(column=0, row=18, columnspan=2, sticky=E)

    # Lower Section Widgets in frame ----------------------------------------------------------------------

    lowersectionLbl = Label(scoreboardLower, text='Lower Section', font=('helvetica', 16, 'bold'), bg=BG_COLOR1)
    threeOfKindALbl = Label(scoreboardLower, text='3 of a kind', font=('helvetica', 16), bg=BG_COLOR1)
    threeOfKindBLbl = Label(scoreboardLower, text='Total of all dice', font=('helvetica', 16, 'bold'), bg=BG_COLOR1)
    fourOfKindALbl = Label(scoreboardLower, text='4 of a kind', font=('helvetica', 16), bg=BG_COLOR1)
    fourOfKindBLbl = Label(scoreboardLower, text='Total of all dice', font=('helvetica', 16, 'bold'), bg=BG_COLOR1)
    fullHouseALbl = Label(scoreboardLower, text='Full House', font=('helvetica', 16), bg=BG_COLOR1)
    fullHouseBLbl = Label(scoreboardLower, text='25', font=('helvetica', 16, 'bold'), bg=BG_COLOR1)
    lowStraightALbl = Label(scoreboardLower, text='Low Straight', font=('helvetica', 16), bg=BG_COLOR1)
    lowStraightBLbl = Label(scoreboardLower, text='30', font=('helvetica', 16, 'bold'), bg=BG_COLOR1)
    highStraightALbl = Label(scoreboardLower, text='High Straight', font=('helvetica', 16), bg=BG_COLOR1)
    highStraightBLbl = Label(scoreboardLower, text='40', font=('helvetica', 16, 'bold'), bg=BG_COLOR1)
    yahtzeeALbl = Label(scoreboardLower, text='Yahtzee', font=('helvetica', 16, 'bold'), bg=BG_COLOR1)
    yahtzeeBLbl = Label(scoreboardLower, text='50', font=('helvetica', 16, 'bold'), bg=BG_COLOR1)
    chanceALbl = Label(scoreboardLower, text='Chance', font=('helvetica', 16), bg=BG_COLOR1)
    chanceBLbl = Label(scoreboardLower, text='Total of all dice', font=('helvetica', 16, 'bold'), bg=BG_COLOR1)
    yahtzeeBonusALbl = Label(scoreboardLower, text='Yahtzee Bonus', font=('helvetica', 16), bg=BG_COLOR1)
    yahtzeeBonusBLbl = Label(scoreboardLower, text='100', font=('helvetica', 16, 'bold'), bg=BG_COLOR1)
    lowerTotalLbl = Label(scoreboardLower, text='Total of Lower Section', font=('helvetica', 16, 'bold'), bg=BG_COLOR1)
    grandTotalLbl = Label(scoreboardLower, text='Grand Total', font=('helvetica', 16, 'bold'), bg=BG_COLOR1)
    # scoreboardLowerFillerLbl = Label(scoreboardLower, bg=BG_COLOR1)

    lowersectionLbl.grid(column=0, row=10, sticky="w")
    threeOfKindALbl.grid(column=0, row=11, sticky=W)
    threeOfKindBLbl.grid(column=1, row=11, sticky=E)
    fourOfKindALbl.grid(column=0, row=12, sticky=W)
    fourOfKindBLbl.grid(column=1, row=12, sticky=E)
    fullHouseALbl.grid(column=0, row=13, sticky=W)
    fullHouseBLbl.grid(column=1, row=13, sticky=E)
    lowStraightALbl.grid(column=0, row=14, sticky=W)
    lowStraightBLbl.grid(column=1, row=14, sticky=E)
    highStraightALbl.grid(column=0, row=15, sticky=W)
    highStraightBLbl.grid(column=1, row=15, sticky=E)
    yahtzeeALbl.grid(column=0, row=16, sticky=W)
    yahtzeeBLbl.grid(column=1, row=16, sticky=E)
    chanceALbl.grid(column=0, row=17, sticky=W)
    chanceBLbl.grid(column=1, row=17, sticky=E)
    yahtzeeBonusALbl.grid(column=0, row=18, sticky=W)
    yahtzeeBonusBLbl.grid(column=1, row=18, sticky=E)
    lowerTotalLbl.grid(column=0, row=19, columnspan=2, sticky=E)
    totalUpr2Lbl.grid(column=0, row=20, columnspan=2, sticky=E)
    grandTotalLbl.grid(column=0, row=21, columnspan=2, sticky=E)
    # scoreboardLowerFillerLbl.grid(column=0, row=22, columnspan=2)
    scoreboardLower.rowconfigure(21, minsize=30)

    # Functionality --------------------------------------------------------------------------------

    dice = []
    upperSectionScores = {'Ones': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Bonus': 0}
    lowerSectionScores = {'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Low Straight': 0,
                          'High Straight': 0, 'Yahtzee': 0, 'Chance': 0, 'Yahtzee Bonus': 0}
    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()
    v5 = IntVar()

    # ----------------------------------------------------------------------------------------------
    # roll_button = Button(text='Roll Dice', command=lambda: clear_and_roll(diceboard, dice))
    # roll_button.pack(side='left')

    roll_button = Button(buttonFrame, text='Roll\nDice', padx=8, pady=2, highlightbackground=PEACH,
                         command=lambda: clear_and_roll(diceboard, dice))
    reroll_button = Button(buttonFrame, text='Reroll', padx=7, pady=10, highlightbackground=PEACH,
                           command=lambda: reroll(diceboard, dice, v1, v2, v3, v4, v5))
    setScore_button = Button(buttonFrame, text='Set\nScore', padx=5, pady=2, highlightbackground=PEACH,
                             command=lambda: set_scores(upperSectionScores, lowerSectionScores, totalLbl, bonusScoreLbl,
                                                        totalOfUpperSectionLbl, totalOfLowerSectionLbl,
                                                        grandTotalScoreLbl))
    clearScoreButton = Button(buttonFrame, text='Clear\n Score', padx=5, pady=2, highlightbackground=PEACH,
                              command=lambda: clear_both_scores(upperSectionScores, lowerSectionScores, scoreLabels))
    clearHold = Button(buttonFrame, text='Clear Hold', padx=19, pady=2, highlightbackground=ORANGE,
                       command=lambda: clear_hold(v1, v2, v3, v4, v5))

    roll_button.grid(column=0, row=0)
    reroll_button.grid(column=1, row=0)
    setScore_button.grid(column=0, row=1)
    clearScoreButton.grid(column=1, row=1)
    clearHold.grid(column=0, row=2, columnspan=2)

    setAces = Button(setButtonFrameUpper, text='Aces', padx=36, pady=BUTTON_Y_PADDING, highlightbackground=LIME,
                     command=lambda: count_ones(dice, aceScoreLbl, upperSectionScores))
    setTwos = Button(setButtonFrameUpper, text='Twos', padx=35, pady=BUTTON_Y_PADDING, highlightbackground=LIME,
                     command=lambda: count_twos(dice, twoScoreLbl, upperSectionScores))
    setThrees = Button(setButtonFrameUpper, text='Threes', padx=30, pady=BUTTON_Y_PADDING, highlightbackground=LIME,
                       command=lambda: count_threes(dice, threeScoreLbl, upperSectionScores))
    setFours = Button(setButtonFrameUpper, text='Fours', padx=34, pady=BUTTON_Y_PADDING, highlightbackground=LIME,
                      command=lambda: count_fours(dice, fourScoreLbl, upperSectionScores))
    setFives = Button(setButtonFrameUpper, text='Fives', padx=35, pady=BUTTON_Y_PADDING, highlightbackground=LIME,
                      command=lambda: count_fives(dice, fiveScoreLbl, upperSectionScores))
    setSixes = Button(setButtonFrameUpper, text='Sixes', padx=35, pady=BUTTON_Y_PADDING, highlightbackground=LIME,
                      command=lambda: count_sixes(dice, sixScoreLbl, upperSectionScores))
    fillerLbl = Label(setButtonFrameUpper, bg=BG_COLOR4)

    setAces.grid(column=0, row=0)
    setTwos.grid(column=0, row=1)
    setThrees.grid(column=0, row=2)
    setFours.grid(column=0, row=3)
    setFives.grid(column=0, row=4)
    setSixes.grid(column=0, row=5)
    fillerLbl.grid(column=0, row=6)
    setButtonFrameUpper.rowconfigure(6, minsize=50)

    setThreeOfKind = Button(setButtonFrameLower, text='3 of a kind', padx=18, pady=BUTTON_Y_PADDING2,
                            highlightbackground=LIME,
                            command=lambda: three_of_kind(dice, threeOfKindScoreLbl, lowerSectionScores))
    setFourOfKind = Button(setButtonFrameLower, text='4 of a kind', padx=18, pady=BUTTON_Y_PADDING2,
                           highlightbackground=LIME,
                           command=lambda: four_of_kind(dice, fourOfKindScoreLbl, lowerSectionScores))
    setFullHouse = Button(setButtonFrameLower, text='Full House', padx=18, pady=BUTTON_Y_PADDING2,
                          highlightbackground=LIME,
                          command=lambda: full_house(dice, fullHouseScoreLbl, lowerSectionScores))
    setLowStraight = Button(setButtonFrameLower, text='Low Straight', padx=12, pady=BUTTON_Y_PADDING2,
                            highlightbackground=LIME,
                            command=lambda: low_straight(dice, lowStraightScoreLbl, lowerSectionScores))
    setHighStraight = Button(setButtonFrameLower, text='High Straight', padx=9, pady=BUTTON_Y_PADDING2,
                             highlightbackground=LIME,
                             command=lambda: high_straight(dice, highStraightScoreLbl, lowerSectionScores))
    setYahtzee = Button(setButtonFrameLower, text='YAHTZEE', padx=22, pady=BUTTON_Y_PADDING2, highlightbackground=LIME,
                        command=lambda: yahtzee(dice, yahtzeeScoreLbl, lowerSectionScores))
    setChance = Button(setButtonFrameLower, text='chance', padx=29, pady=BUTTON_Y_PADDING2, highlightbackground=LIME,
                       command=lambda: chance(dice, chanceScoreLbl, lowerSectionScores))
    setYahtzeeBonus = Button(setButtonFrameLower, text='YAHTZEEEEEEE', pady=BUTTON_Y_PADDING2, highlightbackground=LIME,
                             command=lambda: yahtzee_bonus(dice, yahtzeeBonusScoreLbl, lowerSectionScores))
    fillerLbl2 = Label(setButtonFrameLower, bg=BG_COLOR4)

    setThreeOfKind.grid(column=0, row=0, pady=0)
    setFourOfKind.grid(column=0, row=1, pady=0)
    setFullHouse.grid(column=0, row=2, pady=0)
    setLowStraight.grid(column=0, row=3, pady=0)
    setHighStraight.grid(column=0, row=4, pady=0)
    setYahtzee.grid(column=0, row=5, pady=0)
    setChance.grid(column=0, row=6, pady=0)
    setYahtzeeBonus.grid(column=0, row=7, pady=0)
    fillerLbl2.grid(column=0, row=8)

    for i in range(8):
        setButtonFrameLower.rowconfigure(i, minsize=27)

    setButtonFrameLower.rowconfigure(8, minsize=32)

    # testbtn = Button(text='Test', command=lambda: test(bonusLbl))
    # testbtn.pack()

    # ----------------------------------------------------------------------------------------------

    hold1 = Checkbutton(cbFrame, text='Hold', variable=v1, bg=HOLD_COLOR, relief='raised')
    hold2 = Checkbutton(cbFrame, text='Hold', variable=v2, bg=HOLD_COLOR)
    hold3 = Checkbutton(cbFrame, text='Hold', variable=v3, bg=HOLD_COLOR)
    hold4 = Checkbutton(cbFrame, text='Hold', variable=v4, bg=HOLD_COLOR)
    hold5 = Checkbutton(cbFrame, text='Hold', variable=v5, bg=HOLD_COLOR)

    hold1.grid(column=0, row=0)
    hold2.grid(column=1, row=0)
    hold3.grid(column=2, row=0)
    hold4.grid(column=3, row=0)
    hold5.grid(column=4, row=0)

    # ----------------------------------------------------------------------------------------------
    # print(val)
    canvas.mainloop()


def clear_hold(v1, v2, v3, v4, v5):
    v1.set(0)
    v2.set(0)
    v3.set(0)
    v4.set(0)
    v5.set(0)


def three_of_kind(dice, label, score_dictionary):
    if hand(dice) == 'Three of a kind' or hand(dice) == 'Full House':
        label.configure(text=str(sum(dice)))
        score_dictionary['Three of a Kind'] = sum(dice)


def four_of_kind(dice, label, score_dictionary):
    if hand(dice) == 'Four of a kind':
        label.configure(text=str(sum(dice)))
        score_dictionary['Four of a Kind'] = sum(dice)


def full_house(dice, label, score_dictionary):
    if hand(dice) == 'Full House':
        label.configure(text=str(25))
        score_dictionary['Full House'] = 25


def low_straight(dice, label, score_dictionary):
    if hand(dice) == 'Low Straight':
        label.configure(text=str(30))
        score_dictionary['Low Straight'] = 30


def high_straight(dice, label, score_dictionary):
    if hand(dice) == 'High Straight':
        label.configure(text=str(40))
        score_dictionary['High Straight'] = 40


def yahtzee(dice, label, score_dictionary):
    if hand(dice) == 'Yahtzee':
        label.configure(text=str(50))
        score_dictionary['Yahtzee'] = 50


def chance(dice, label, score_dictionary):
    label.configure(text=sum(dice))
    score_dictionary['Chance'] = sum(dice)


def yahtzee_bonus(dice, label, score_dictionary):
    if score_dictionary['Yahtzee'] == 50 and hand(dice) == 'Yahtzee':
        label.configure(text=str(100))
        score_dictionary['Yahtzee Boonus'] = 100
    print(score_dictionary)
    return score_dictionary


def test(label):
    label.configure(text='test')


def clear_both_scores(dict1, dict2, scoreLabels):
    clear_score(dict1)
    clear_score(dict2)
    clear_score_labels(scoreLabels)


def clear_score(score_dictionary):
    for key in score_dictionary.keys():
        score_dictionary[key] = 0
    print(score_dictionary)


def clear_score_labels(scoreLabels):
    for item in scoreLabels:
        item.configure(text=0)


def count_ones(dice, label, score_dictionary):
    label.configure(text=str(dice.count(1)))
    score_dictionary['Ones'] = dice.count(1)


def count_twos(dice, label, score_dictionary):
    label.configure(text=str(dice.count(2) * 2))
    score_dictionary['Twos'] = dice.count(2) * 2


def count_threes(dice, label, score_dictionary):
    label.configure(text=str(dice.count(3) * 3))
    score_dictionary['Threes'] = dice.count(3) * 3


def count_fours(dice, label, score_dictionary):
    label.configure(text=str(dice.count(4) * 4))
    score_dictionary['Fours'] = dice.count(4) * 4


def count_fives(dice, label, score_dictionary):
    label.configure(text=str(dice.count(5) * 5))
    score_dictionary['Fives'] = dice.count(5) * 5


def count_sixes(dice, label, score_dictionary):
    label.configure(text=str(dice.count(6) * 6))
    score_dictionary['Sixes'] = dice.count(6) * 6


def upper_total(score_dictionary, label1, label2, label3):
    label1.configure(text=str(sum(list(score_dictionary.values()))))
    if sum(list(score_dictionary.values())) >= 63:
        score_dictionary['bonus'] = 35
        label2.configure(text=str(35))
    label3.configure(text=str(sum(list(score_dictionary.values()))))


def lower_total(score_dictionary, label1):
    label1.configure(text=str(sum(list(score_dictionary.values()))))


def grand_total(dict1, dict2, label):
    total = sum(list(dict1.values())) + sum(list(dict2.values()))
    label.configure(text=str(total))


def set_scores(dict1, dict2, label1, label2, label3, label4, label5):
    """
    This function set the score across the board at any point during the game. It does so by adding the values in both
    scoring dictionaries and configuring the appropriate labels.
    :param dict1: upperSectionScores
    :param dict2: lowerSectionScores
    :param label1: Total in Upper Section
    :param label2: Bonus in Upper Section
    :param label3: Total OF Upper Section
    :param label4: Total OF Lower Section
    :param label5: Grand Total
    :return:
    """
    upper_total(dict1, label1, label2, label3)
    lower_total(dict2, label4)
    grand_total(dict1, dict2, label5)


def make_gamescore(canvas, player, column, row):
    player1 = Label(canvas,
                    text=player,
                    font=('helvetica', 16, 'bold'),
                    borderwidth=1,
                    relief='solid')
    player1.grid(column=column,
                 row=row,
                 sticky=NW)
    for i in range(9):
        scoreLbl = Label(canvas,
                         text='0',
                         font=('helvetica', 16, 'bold'),
                         borderwidth=1,
                         relief='solid')
        scoreLbl.grid(column=column,
                      row=row + (1 + i))


def reroll(canvas, dice, v1, v2, v3, v4, v5):
    """
    Checks if any related checkbutton is set to false, in which it will reroll that die.
    """
    if not v1.get():
        roll_single_die(canvas, dice, 0)
    if not v2.get():
        roll_single_die(canvas, dice, 1)
    if not v3.get():
        roll_single_die(canvas, dice, 2)
    if not v4.get():
        roll_single_die(canvas, dice, 3)
    if not v5.get():
        roll_single_die(canvas, dice, 4)
    print(hand(dice))


def roll_single_die(canvas, dice, i):
    """
    This function clears the part of the canvas where the dice should be painted, throws a dice and adds it
    to the dice-list. It then paints the die-face to the canvas.
    :param canvas: The tkinter "parent" where the die is painted.
    :param dice: The list where the die is appended.
    :param i: The index of the die in the list.
    :return: The dice list.
    """
    whitebrush(canvas, i)
    dice.pop(i)
    dice.insert(i, roll_die())
    paint_dice(canvas, i, dice)
    return dice


def clear_and_roll(canvas, dice):
    dice.clear()
    for i in range(NUM_DICE):
        whitebrush(canvas, i)
    roll_all_dice(canvas, dice)


def roll_all_dice(canvas, dice):
    for i in range(NUM_DICE):
        dice.append(random.randint(1, NUM_SIDES))
        paint_dice(canvas, i, dice)
    return dice


def paint_dice(canvas, i, dice):
    if dice[i] == 6:
        dot_six(canvas, i)
    elif dice[i] == 5:
        dot_five(canvas, i)
    elif dice[i] == 4:
        dot_four(canvas, i)
    elif dice[i] == 3:
        dot_three(canvas, i)
    elif dice[i] == 2:
        dot_two(canvas, i)
    elif dice[i] == 1:
        dot_one(canvas, i)


def whitebrush(canvas, i):
    """
    This just paints the die on the canvas white.
    """
    x3 = 20 + (80 * i)
    y3 = 20
    x4 = 60 + (80 * i)
    y4 = 60

    canvas.create_rectangle(x3, y3, x4, y4, fill='white', outline='white')

    return canvas


"""
The following functions paints the dots in the dice.
"""


def dot_one(canvas, i):
    # x3 = 20 + (80 * i)
    # y3 = CANVAS_HEIGHT - 60
    # x4 = 60 + (80 * i)
    # y4 = CANVAS_HEIGHT - 20

    x3 = 20 + (80 * i)
    y3 = 20
    x4 = 60 + (80 * i)
    y4 = 60

    canvas.create_rectangle(x3, y3, x4, y4)

    x1 = 37 + (80 * i)
    y1 = 37
    x2 = 43 + (80 * i)
    y2 = 43

    canvas.create_oval(x1, y1, x2, y2, fill='black')
    return canvas


def dot_two(canvas, i):
    x3 = 20 + (80 * i)
    y3 = 20
    x4 = 60 + (80 * i)
    y4 = 60

    canvas.create_rectangle(x3, y3, x4, y4)

    canvas.create_oval(27 + (80 * i),
                       33,
                       33 + (80 * i),
                       27,
                       fill='black')

    canvas.create_oval(47 + (80 * i),
                       53,
                       53 + (80 * i),
                       47,
                       fill='black')
    return canvas


def dot_three(canvas, i):
    x3 = 20 + (80 * i)
    y3 = 20
    x4 = 60 + (80 * i)
    y4 = 60

    canvas.create_rectangle(x3, y3, x4, y4)

    dot_two(canvas, i)
    dot_one(canvas, i)
    return canvas


def dot_four(canvas, i):
    x3 = 20 + (80 * i)
    y3 = 20
    x4 = 60 + (80 * i)
    y4 = 60

    canvas.create_rectangle(x3, y3, x4, y4)

    dot_two(canvas, i)

    canvas.create_oval(27 + (80 * i),
                       53,
                       33 + (80 * i),
                       47,
                       fill='black')

    canvas.create_oval(47 + (80 * i),
                       33,
                       53 + (80 * i),
                       27,
                       fill='black')
    return canvas


def dot_five(canvas, i):
    x3 = 20 + (80 * i)
    y3 = 20
    x4 = 60 + (80 * i)
    y4 = 60

    canvas.create_rectangle(x3, y3, x4, y4)

    dot_four(canvas, i)
    dot_one(canvas, i)

    return canvas


def dot_six(canvas, i):
    x3 = 20 + (80 * i)
    y3 = 20
    x4 = 60 + (80 * i)
    y4 = 60

    canvas.create_rectangle(x3, y3, x4, y4)

    dot_four(canvas, i)

    canvas.create_oval(27 + (80 * i),
                       43,
                       33 + (80 * i),
                       37,
                       fill='black')

    canvas.create_oval(47 + (80 * i),
                       43,
                       53 + (80 * i),
                       37,
                       fill='black')
    return canvas


def hand(dice):
    pairs = 0
    tress = 0
    quad = 0
    fives = 0

    for i in range(NUM_SIDES):
        if dice.count(i + 1) == 5:
            fives += 1
        if dice.count(i + 1) == 4:
            quad += 1
        if dice.count(i + 1) == 3:
            tress += 1
        if dice.count(i + 1) == 2:
            pairs += 1

    if fives:
        return 'Yahtzee'
    elif tress and pairs:
        return 'Full House'
    elif quad:
        return 'Four of a kind'
    elif tress:
        return 'Three of a kind'
    elif pairs == 2:
        return 'Two pairs'
    elif pairs == 1:
        return 'One pair'
    elif dice.count(1) == 0:
        return 'High Straight'
    elif dice.count(6) == 0:
        return 'Low Straight'
    else:
        return "You've got nothing"


def roll_die():
    return random.randint(1, NUM_SIDES)


def make_canvas(width, height, title):
    top = Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


if __name__ == '__main__':
    main()
