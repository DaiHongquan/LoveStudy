# 项目实操
'''
【问题拆解】在做一件事或面对一个问题的时候，将其拆解成多个步骤或多个层次，
逐步执行和解决问题，直至达到最终效果
项目流程：
1. 明确项目目标：达成什么目的，实现什么功能
2. 分析过程、拆解项目
3. 逐步执行、代码实现
解题流程
1.分析问题，明确结果
2.思考需要的知识，或者搜索新知识
3.思考切入点
4.尝试解决问题的一部分
5.重复1~4步
'''

# pk小游戏，自动生成人机属性，自动攻击

import time,random
# 游戏开始

def pkGame(pknum):
    playerWin = 0
    computerWin = 0
    print('===============')
    print('==PK小游戏======')
    print('===============')
    for i in range(1,pknum + 1):
        print("=====第{0}局=====".format(i))

        player={}
        player['血量']=random.randint(1,100)
        player['攻击']=random.randint(40,60)
        computer={}
        computer['血量']=random.randint(1,100)
        computer['攻击']=random.randint(40,60)
        time.sleep(1)
        print('''【玩家】
血量：{0}   
攻击：{1}'''.format(player['血量'],player['攻击']))
        time.sleep(1)
        print("===============")
        print('''【敌人】
血量：{0}   
攻击：{1}'''.format(computer['血量'],computer['攻击']))
        while True:
            time.sleep(1)
            print("===============")
            computer['血量'] = computer['血量'] - player['攻击']
            print('玩家发起了攻击,敌人剩余血量{0}'.format(computer['血量']))
            if computer['血量'] > 0:
                pass
            else:
                time.sleep(1)
                playerWin += 1
                print('恭喜，玩家把敌人干掉了')
                break
            player['血量'] = player['血量'] - computer['攻击']
            print('敌人发起了攻击,玩家剩余血量{0}'.format(player['血量']))
            if player['血量'] > 0:
                pass
            else:
                time.sleep(1)
                computerWin += 1
                print('悲催，敌人把玩家干掉了')
                break
    else:
        time.sleep(1)
        print("===============")
        print("玩家共获胜{0}局".format(playerWin))
        print("敌人共获胜{0}局".format(computerWin))
        time.sleep(1)
        if playerWin > computerWin:
            print('玩家是冠军')
        elif playerWin < computerWin:
            print('敌人是冠军')
        else:
            print('双方平手')
        print("===============")
pkGame(3)