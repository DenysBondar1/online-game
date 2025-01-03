# імпортуємо необхідні модулі
import pygame 
import modules.data as m_data
import modules.images as m_images
import modules.clients_server as m_client
import modules.audio as m_audio
# список клітинок без кораблів
list_miss = "05"
# список клітинок з кораблями
list_explosion = "1234"
# метод з атакою
def attack(pos: tuple,multiplier_x,multiplier_y):
    # створення глобальних змінних
    global list_miss, list_explosion
    # умова для повора кораблів
    # blits = True
    if m_data.turn:
        # цикл для ряду
        for row in range(10):
            # цикл для клітинки
            for cell in range(10):
                # створюємо хіт-бокс
                rect = pygame.Rect((725+55.7*cell) * multiplier_x, 
                                (115+55.7*row) * multiplier_y,
                                55.7 * multiplier_x,
                                55.7 * multiplier_y)
                # перевірка на колізію
                if rect.collidepoint(pos):
                    image = m_images.Image(
                            progression = "game",
                            name = "",
                            x = 725+55.7*cell,
                            y = 115+55.7*row ,
                            width= 55.7,
                            height=55.7
                    )
                    # for rows in m_data.enemy_field:
                    #     print(rows)
                    # 6 - explosion 7 - miss
                    # змінна ім'я зі значенням нічого
                    name = None
                    
                    
                    # умова для клітинок заповнених ворожими кораблями
                    if str(m_data.enemy_field[row][cell]) in list_explosion:
                        m_data.enemy_field[row][cell] = 6
                        # відправляє закодовані данні
                        image.name = 'explosion'
                        image.update_image()
                        m_data.list_explosions.append([image, row, cell])
                       
                        # import time
                        # time.sleep(0.1)
                        # відповідає за те яка клітинка створиться
                        name = "explosion"
                        # клітинка з вибухнувшим кораблем
                        # for ship in m_data.enemy_ships:
                        # список з клітинками в яких є кораблі

                        explosions = []
                        for row2 in m_data.enemy_field:
                            print(row2,'the best')
                        # цикл для ворожих кораблів
                        for ship in m_data.enemy_ships:
                            # перевіряє ворожий корабль
                            ship.check_enemy()
                            # список з клітинками кораблів
                            cells = []
                          
                            # цикл для додавання всіх клітинок корабля до cells
                            for count in range(int(ship.name)):
                                # якщо корабель стоїть горизонтально то
                                if ship.rotate %180 == 0 and m_data.enemy_field[ship.row][ship.cell+count] != int(ship.name[0]):
                                    # додається клітика
                                    cells.append([ship.row, ship.cell+count])
                                # інакше якщо корабель стоїть вертикалюно то
                                elif ship.rotate %180 != 0 and m_data.enemy_field[ship.row+count][ship.cell] != int(ship.name[0]):
                                    # додається клітинка
                                    cells.append([ship.row+count, ship.cell])
                            # 
                            if int(ship.name) == len(cells):
                                # 
                                # blits = False
                                for explosion in m_data.list_explosions:
                                    #
                                    for celll in cells:
                                        #
                                        if explosion[1] == celll[0] and explosion[2] == celll[1]:
                                            #
                                            explosions.append(explosion[0])
                        
                        for ex in explosions:
                            try:
                                #
                                # del m_data.list_blits['game'][ex]
                                m_data.list_blits['game'].remove(ex)
                                
                            except:
                                print('reoeroreoreoreooeroeroreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
                                # pass
                    #
                    elif str(m_data.enemy_field[row][cell]) in list_miss:
                        #
                        m_data.enemy_field[row][cell] = 7
                        #
                        name = "miss"
                        image.name = 'miss'
                        image.update_image()
                        #
                        m_data.turn = False
                        #
                      
                    #
                    if name: 
                        m_client.send(f"attack:{row},{cell} {name}".encode())
                        #
                        m_audio.explosion.play()
                        #
                        # if name == 'explosion':
                        #     #
                        #     print(image, row, cell)
                            
                            # m_audio.track.play()
                    # for ship in m_data.enemy_ships:
                        # перевіряє ворожий корабль
                        # ship.check_enemy()
    win_lose()
def win_lose():
    yes_no = True
    print(m_data.enemy_ships, 153)
    
    for ship in m_data.enemy_ships:
        print(ship in m_data.enemy_ships, not ship.explosion)
        if not ship.explosion:
        #     pass
        # elif :
            yes_no = False
    if yes_no and m_data.enemy_ships:
        m_data.progression = "win"
        m_client.send("lose:?????".encode())