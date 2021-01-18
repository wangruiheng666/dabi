from tkinter import messagebox as m
from tkinter import Tk
from random import randint
from time import sleep

welcome = '欢迎游玩大臂！ \n版本：v0.1.2\n' \
        'v0.1.2主要更新内容：\n' \
        '1.修复了已知错误。'
print(welcome)
shuoming = '0.1.2版本游戏可用招式：大臂、攒钱、方盾、圆盾、超闪、刀、ber、J刀、防J刀、闪电盾、泡沫盾、锤锤锤。\n'
a = input('输入1开始游戏，输入2查看说明。请输入：')
playerxy = False
robotxy = False#眩晕


def main():
    global a, shuoming, playerxy, robotxy
    tk = Tk()
    tk.withdraw()
    if a == '2':
        print(shuoming)
    elif a == '1':
        pass
    else:
        print('输入有误，直接开始！')
    sleep(1)
    a = '1'
    #开始游戏
    print('输入对应数字以出对应的招式：')
    print('大臂:1、攒钱:2、方盾:3、圆盾:4、超闪:5、刀:6、ber:7、J刀:8、防J刀:9、闪电盾：10、泡沫盾：11、锤锤锤：12.')
    zhaoshi={0:'本局眩晕，无法出招',1:'大臂',2:'攒钱',3:'方盾',4:'圆盾',5:'超闪',6:'刀',7:'ber',8:'J刀',9:'防J刀',10:'闪电盾',11:'泡沫盾',12:'锤锤锤'}
    player=[]#玩家出招的列表
    playerhave = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 10: 0, 11: 0}  # 玩家有的东西
    robot=[]
    robothave = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 10: 0, 11: 0}
    defend = {6: 3, 7: 4, 8: 9, 12: 1}  # 防御列表
    attack = [6, 7, 8, 12]  # 攻击招式
    hurt = {6: 1.0, 7: 0.8, 8: 2.4, 12: 1.8}
    round=0
    while True:
        #b是玩家出招，c是机器出招
        round=round+1
        print('第{}回合'.format(round))

        #玩家出招
        if not playerxy:
            b = input('玩家出招：（输入数字）')
        else:#第50行代码
            b = 0
            print('玩家本回合眩晕！')
        #判断输入是否有效，无效就算大臂
        try:
            b = int(b)
        except:
            print('出招无效，就算大臂，接着来！')
            b = 1
        if b < 13 and b > -1:
            pass
        else:
            print('出招无效，就算大臂，接着来！')
            b = 1
        #加入player,playerhave
        player.append(b)
        if 0<b<6 or 9<b<12:
            playerhave[b]=playerhave[b]+1



        #判断玩家是否自爆,并且扣除playerhave中对应的数量
        if round != 1 and b == 5 and player[-2] == 5:
            m.showinfo('你被J刀了！','由于你连续出2个超闪，所以你自爆了！\n由于自爆=被J刀劈，所以，你被J刀了！')
            return 0
        elif b == 6:
            if playerhave[1] == 0:
                m.showinfo('你被J刀了！', '由于你没有大臂而出刀，所以你自爆了！\n由于自爆=被J刀劈，所以，你被J刀了！')
                return 0
            else:
                playerhave[1] = playerhave[1]-1
        elif b==7:
            if playerhave[2] == 0:
                m.showinfo('你被J刀了！', '由于你没有攒钱而出ber，所以你自爆了！\n由于自爆=被J刀劈，所以，你被J刀了！')
                return 0
            else:
                playerhave[2] = playerhave[2]-1
        elif b == 8:
            if playerhave[1] < 2 or playerhave[4] == 0:
                m.showinfo('你被J刀了！', '由于你没有集齐2大臂1圆盾而出J刀，所以你自爆了！\n由于自爆=被J刀劈，所以，你被J刀了！')
                return 0
            else:
                playerhave[1] = playerhave[1]-2
                playerhave[4] = playerhave[4]-1
        elif b == 11:
            if playerhave[3] == 0 or playerhave[4] == 0:
                m.showinfo('你被J刀了！', '由于你没有集齐1方盾1圆盾而出泡沫盾，所以你自爆了！\n由于自爆=被J刀劈，所以，你被J刀了！')
                return 0
            else:
                playerhave[3] = playerhave[3]-1
                playerhave[4] = playerhave[4]-1#第100行代码
        elif b == 10:
            if playerhave[3] == 0 or playerhave[5] == 0:
                m.showinfo('你被J刀了！', '由于你没有集齐1方盾1超闪而出闪电盾，所以你自爆了！\n由于自爆=被J刀劈，所以，你被J刀了！')
                return 0
            else:
                playerhave[3] = playerhave[3]-1
                playerhave[5] = playerhave[5]-1
        elif b == 12:
            if playerhave[1] == 0 or playerhave[2] == 0:
                m.showinfo('你被J刀了！', '由于你没有集齐1大臂1攒钱而出锤锤锤，所以你自爆了！\n由于自爆=被J刀劈，所以，你被J刀了！')
                return 0
            else:
                playerhave[1] = playerhave[1]-1
                playerhave[2] = playerhave[2]-1

        if b != 0:
            print('玩家出招：{}'.format(zhaoshi[b]))

        #机器出招

        c = 0
        if robotxy:
            pass
        #玩家有2个大臂、1个圆盾，则：
        #1.机器能出闪电盾，若玩家出不了锤锤锤则100%闪电盾，否则机器60%闪电盾
        #2.机器能出J刀，则80%出J刀
        #3.机器能出超闪则90%超闪
        #4.否则机器80%防J刀
        elif playerhave[1] > 1 and playerhave[4] > 0 and robothave[3] > 0 and robothave[5] > 0 and (playerhave[2] == 0 or randint(1,5) < 4):
            c = 10
        elif playerhave[1] > 1 and playerhave[4] > 0 and robothave[1] > 1 and robothave[5] > 0 and randint(1,5) < 5:
            c = 8
        elif playerhave[1] > 1 and playerhave[4] > 0 and robot[-1] != 5 and randint(1,10) < 10:
            c = 5
        elif playerhave[1] > 1 and playerhave[4] > 0 and randint(1, 5) < 5:
            c = 9
        #如果有2个大臂1个圆盾，则70%出J刀
        elif robothave[1] > 1 and robothave[4] > 0 and randint(1, 10) < 8:
            c = 8
        #如果有大臂攒钱，则50%出锤锤锤
        elif robothave[1] > 0 and robothave[2] > 0 and randint(1, 2) != 1:
            c = 12
        #如果有大臂，则30%出刀；攒钱同理
        elif robothave[1] > 0 and randint(1, 10) < 4:
            c = 6
        elif robothave[2] > 0 and randint(1, 10) < 4:
            c = 7
        #如果能出闪电盾，则60%出闪电盾
        elif robothave[3] > 0 and robothave[5] > 0 and randint(1, 5) < 4:
            c = 10
        #如果能出泡沫盾，则30%出
        elif robothave[3] > 0 and robothave[4] > 0 and randint(1, 10) < 4:
            c = 11
        #上局玩家集齐锤锤锤，60%出大臂，否则30%
        elif playerhave[1] > 0 and playerhave[2] > 0 and round > 1 and playerhave[player[-2]] == 0 and randint(1,5) < 4:
            c = 1
        elif playerhave[1] > 0 and playerhave[2] > 0 and randint(1,10)<4:
            c = 1
        #否则不是第一局且能出超闪，30%超闪
        elif robot[-1:] != [5] and randint(1,10) < 4 and round != 1:
            c = 5
        #上局玩家大臂，如果第一局，则90%出方盾，则40%；攒钱同理
        elif round == 2 and player[-2] in [1,2] and randint(1,10) != 7:
            c = player[-1] + 2
        elif round > 1 and[-2] in [1,2] and randint(1,5) < 3:
            c = player[-1] + 2
        #否则1-4随机
        else:
            c = randint(1,4)

        if c == 6:
            robothave[1] = robothave[1] - 1
        elif c == 7:
            robothave[2] = robothave[2] - 1
        elif c == 8:
            robothave[1] = robothave[1] - 2
            robothave[4] = robothave[4] - 1
        elif c == 10:
            robothave[3] = robothave[3] - 1
            robothave[5] = robothave[5] - 1
        elif c == 11:
            robothave[3] = robothave[3] - 1
            robothave[4] = robothave[4] - 1
        elif c == 12:
            robothave[1] = robothave[1] - 1
            robothave[2] = robothave[2] - 1

        if c != 0:
            print('机器出招：{}'.format(zhaoshi[c]))
        else:
            print('机器本回合眩晕！')
        # 加入robot,robothave
        robot.append(c)
        if 0 < c < 6 or 9 < c < 12:
            robothave[c] += 1


        playerxy = False
        robotxy = False

        #判断卒
        #伤害一样，抵消
        if c == b:
            pass
        #可以防的招式
        elif c in attack and b in [5,defend[c]]:
            pass
        elif b in attack and c in [5,defend[b]]:
            pass
        #锤锤锤穿透
        elif c == 12 and b not in attack:
            if playerhave[10] + playerhave[11] > 3:
                if playerhave[11] > 3:
                    playerhave[11] = playerhave[11] - 3
                    print('掉3层闪电盾，接着来！')
                else:
                    print('掉{}层闪电盾和{}层泡沫盾，接着来！'.format(playerhave[11],3-playerhave[11]))
                    playerhave[10] = playerhave[10] + playerhave[11] - 3
                    playerhave[11] = 0
            else:

                sleep(1)
                msg = '你被{}了,卒一根！'.format(zhaoshi[c])
                m.showinfo(msg, msg)
                return 0
        elif b == 12 and c not in attack:
            if robothave[10] + robothave[11] > 3:
                if robothave[11] > 3:
                    robothave[11] = robothave[11] - 3
                else:
                    robothave[10] = robothave[10] + robothave[11] - 3
                    robothave[11] = 0
            else:
                sleep(1)
                msg = '机器被你{}了,你胜利了！'.format(zhaoshi[b])
                m.showinfo(msg, msg)
                return 0
        #都是攻击招式且不相同的伤害计算
        elif b in attack and c in attack:
            if hurt[b] != hurt[c]:
                if hurt[b] > hurt[c]:
                   if robothave[10] == 0 and robothave[11] == 0:
                       msg = '机器被你{}了,你胜利了！'.format(zhaoshi[b])
                       m.showinfo(msg, msg)
                       return 0
                   elif robothave[10] != 0:
                       robothave[10] = robothave[10] - 1
                       playerxy = True
                       print('掉个闪电盾，眩晕一回合，接着来！')
                       sleep(2)
                   else:
                       robothave[11] = robothave[11] - 1
                       print('掉个泡沫盾，接着来！')
                       sleep(2)
                else:
                    if playerhave[10] == 0 and playerhave[11] == 0:
                        msg = '你被{}了,卒一根！'.format(zhaoshi[c])
                        m.showinfo(msg, msg)
                        return 0
                    elif playerhave[10] != 0:
                        playerhave[10] -= 1
                        robotxy = True
                        print('掉个闪电盾，眩晕一回合，接着来！')
                        sleep(2)
                    else:
                        robothave[11] -= 1
                        print('掉个泡沫盾，接着来！')
                        sleep(2)

        #闪电盾防御和眩晕效果
        elif robothave[10] != 0 and b in attack[:-1]:
            robothave[10] = robothave[10] - 1
            playerxy = True
            print('掉个闪电盾，眩晕一回合，接着来！')
            sleep(2)
        elif playerhave[10] != 0 and c in attack[:-1]:
            playerhave[10] = playerhave[10] - 1
            robotxy = True
            print('掉个闪电盾，眩晕一回合，接着来！')
            sleep(2)
        #泡沫盾防御
        elif robothave[11] != 0 and b in attack[:-1]:#第250行代码
            robothave[11] = robothave[10] - 1
            print('掉个泡沫盾，接着来！')
            sleep(2)
        elif playerhave[11] != 0 and c in attack[:-1]:
            playerhave[11] = playerhave[11] - 1
            print('掉个泡沫盾，接着来！')
            sleep(2)
        elif c in attack and b not in [defend[c],5]+attack:
            sleep(2.5)
            msg = '你被{}了，卒一根！'.format(zhaoshi[c])
            m.showinfo(msg,msg)
            return 0
        elif b in attack and c not in [defend[b],5]+attack:
            sleep(2.5)
            msg = '机器被你{}了，你胜利了！'.format(zhaoshi[b])
            m.showinfo(msg, msg)
            return 0



if __name__ == '__main__':
    while True:
        main()
        if m.askyesno('是否重新开始？','本局游戏已结束，是否重新开始？'):
            print('\n重新开始！\n')
            sleep(1)
        else:
            exit()#268行