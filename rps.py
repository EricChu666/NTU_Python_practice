#剪刀石頭布小遊戲
import random
dic_player = {'1': '剪刀', '2': '石頭', '3': '布'}
dic_cpu = {1: '剪刀', 2: '石頭', 3: '布'}
name = input('歡迎來到猜拳的世界! 請輸入您的名稱: ')
game_count = [0, 0, 0, 0] # 0 is total, 1 is win, 2 is lose, 3 is draw

if name:
    while True:
        print('-' * 50)
        cpu = random.randint(1, 3)
        player = input('請出拳 (1) 剪刀 (2) 石頭 (3) 布, 退出請輸入q: ')

        if player == 'q' or player == 'Q':
            print('感謝', name, '的遊玩! 歡迎下次再來!')
            break

        elif player == '1' or player == '2' or player == '3':
            if int(player) == int(cpu):
                print(name, '出了:', dic_player[player], ', 電腦出了:', dic_cpu[cpu])
                print('你們平手!')
                game_count[0] += 1
                game_count[3] += 1

            elif (int(player) == 1 and int(cpu) == 2) or (int(player) == 2 and int(cpu) == 3) or (int(player) == 3 and int(cpu) == 1):
                print(name, '出了:', dic_player[player], ', 電腦出了:', dic_cpu[cpu])
                print('您輸了!')
                game_count[0] += 1
                game_count[2] += 1

            elif (int(player) == 1 and int(cpu) == 3) or (int(player) == 3 and int(cpu) == 2) or (int(player) == 2 and int(cpu) == 1):
                print(name, '出了:', dic_player[player], ', 電腦出了:', dic_cpu[cpu])
                print('您贏了!')
                game_count[0] += 1
                game_count[1] += 1
        else:
            print('請輸入 "1-3" 或是 "q"。')
            continue
            

        again = input('您還想再玩一局嗎?(y/n): ')

        if again == 'n' or again == 'N':
            print('=' * 50)
            print(name, '玩了', game_count[0], '局\n贏了', game_count[1], '局\n輸了', game_count[2], '局\n平手', game_count[3], '局')
            print('感謝', name, '的遊玩! 歡迎下次再來!')
            break
        elif again == 'y' or again == 'Y':
            pass
        else:
            print('請輸入 "Y" or "y" 或是 "N" or "n"。')
            break