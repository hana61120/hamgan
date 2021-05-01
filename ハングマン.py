
answer_list=["rose","cosmoss","rily","banana"]
 
import random
n=random.choice(answer_list)

def humgman(n):
    wrong=0
    stages =["",
             "_________         ",
             "|                 ",
             "|                 ",
             "|        |        ",
             "|        0        ",
             "|       /|\       ",
             "|       / \       ",
             "|                 ",
             ]
    rletters= list(n)
    board=["_"]*len(n)
    win=False
    print("ハングマンへようこそ！")

    while wrong <len(stages)-1:
        print("\n")
        msg="1文字をよそうしてね"
        char= input(msg)
        if char in rletters:
            cind= rletters.index(char)
            board[cind]=char
            rletters[cind]="$"
            
        else:
            wrong+=1
        print(" ".join(board))
        e= wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち!")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け!正解は{}.".format(n))


humgman(n)
