'''
    >>> Відповідяє за створення всіх кнопок - клас Button
    >>> Відповідає за функції при натисканні кнопок - метод button_start 
'''
# імпорт чужих модулів для роботи
import pygame , socket, os
import threading, random
import getpass
# імпорт наших модулів
import modules.audio as m_audio
from modules.images import Image
import modules.transform as m_transform
import modules.data as m_data
import modules.clients_server as m_client 
import modules.achievements as m_achievements
import modules.attack as m_attack
# import modules.server as m_server
from modules.ships import Ship,fill_field
def stroke(screen,rect:pygame.Rect,color = (0,0,0),width = 5,multiplier_x = 1,multiplier_y = 1):
    '''
        >>> Малює обведення
    '''
    pygame.draw.line(screen,color,
                     (int(rect.x*multiplier_x),int(rect.y*multiplier_y)),
                     (int((rect.x+rect.width)*multiplier_x),int(rect.y*multiplier_y)),int(width*multiplier_x))
    pygame.draw.line(screen,color,
                     (int((rect.x+rect.width)*multiplier_x),int(rect.y*multiplier_y)),
                     (int((rect.x+rect.width)*multiplier_x),int((rect.y+rect.height)*multiplier_y)),int(width*multiplier_x))
    pygame.draw.line(screen,color,
                     (int((rect.x+rect.width)*multiplier_x),int(rect.y+rect.height)*multiplier_y),
                     (int(rect.x*multiplier_x),int((rect.y+rect.height)*multiplier_y)),int(width*multiplier_x))
    pygame.draw.line(screen,color,
                     (int((rect.x)*multiplier_x),int((rect.y+rect.height)*multiplier_y)),
                     (int(rect.x*multiplier_x),int(rect.y*multiplier_y)),int(width*multiplier_x))

# класс з кнопками
class Button(Image):
    '''
        >>> Додає параметри до класу зображень
    '''
    # метод з створенням параметрів
    def __init__(self, fun = None, width = 100, height = 100, x= 0, y= 0, name = "", progression = "menu", text: str ="Button", size = 65, color = (0, 0, 0),rotate = 0):
        # задаємо параметри в класс зображень
        Image.__init__(self, width=width, height=height, x=x, y=y, name=name, progression=progression,rotate=rotate)
        # переносимо параметри в змінні
        self.WIDTH_BUT = width
        self.HEIGHT_BUT = height
        self.X = x
        self.Y = y
        self.function = fun
        self.TEXT = text  
        self.render = None
        self.last_text = None
        self.activate = 0
        # створюємо параметри
        self.COLOR = color
        self.FONT = pygame.font.SysFont("algerian", size)
        self.rect = pygame.Rect(x,y,width,height)
        self.size = size 
        self.start_size = size
        self.current_size = self.size
    # метод з кнопкою старт
    def button_start(self, event):
        '''
            >>> Створює кнопку старт
            >>> Перевіряє чи кнопка натиснута
        '''
        if type(event) == pygame.event.Event:

            pos = event.pos
        else:
            pos = event
        # якщо кнопка натиснута
        if self.rect.collidepoint(pos):
            if type(self.function) == type("123") and self.function.split(":")[0] == "c_s":
                print(self.function.split(":")[1])
                m_data.client_server = self.function.split(":")[1]
                server.COLOR = (0,0,0)
                client.COLOR = (0,0,0)
                self.COLOR =(40,2,255)
            # якщо функція корабль то
            elif self.function == "ship":
                # цикл для всіх кораблів
                for ship in m_data.all_ships:
                    # якщо корабль виділен
                    if ship.select:
                        # поворот корабля   
                       ship.rotate_ship()
                        # виділення корабля
                       ship.select  = False
            elif self.function == "music":
                if m_audio.track.stoped:
                    m_audio.track.play()
                    # self.name = "music"
                else:
                    m_audio.track.stop()
                    # self.name = "music_off"
                # self.update_image()
            elif self.function == "win_lose":
                m_data.revenge = True
                m_transform.type_transform = random.randint(0,m_transform.count_types)
                m_data.progression = "pre-game"
                
                size_ship = "1"
                m_data.enemy_ships = []
                m_data.all_ships = []
                # Створення списку, у якому зберігаеться усе наше поле
                m_data.my_field = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]

                # Створення списку, у якому зберігаеться усе поле ворога
                m_data.enemy_field = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
                m_data.turn = True
                # list_count = []
                m_data.list_blits["game"] = []
                m_data.list_explosions = []
                play_field = Image(width = 1280, height = 851, x = 0, y = 0, name = "play_field", progression = "game", edit = False)
                # for count in range(len(m_data.list_blits["game"])):
                #     if m_data.list_blits["game"][count].name in "miss, explosion":
                #         list_count += [count]
                # for count in range(len(list_count)):
                #     del m_data.list_blits["game"][list_count[-(count + 1)]]
                for count in range(10):
                    ship = Ship(x=59, y=115, name=size_ship)
                    ship.select = True
                    ship.place((684, 220))
                    ship.select = False
                    if count == 3:
                        size_ship = "2"
                    if count == 6:
                        size_ship = "3"
                    if count == 8:
                        size_ship = "4"
            elif self.function == "check":
                return True
            elif self.function == "buy":
                try:
                    if not m_data.attack:
                        if m_data.cost_data[m_data.select_weapon] <= m_data.coins:
                            m_data.coins -= m_data.cost_data[m_data.select_weapon]
                            m_achievements.achievement('Hooked')
                            m_audio.buying.play()
                            if 'Energetic' == m_data.select_weapon:
                                m_data.buffs.append(['Energetic'])
                                # m_client.send('buff:Energetic')
                            elif "Anti_fire"== m_data.select_weapon:
                                add = ';pass'
                                for buff in m_data.buffs:
                                    if buff[0] == 'Energetic':
                                        add = ''
                                m_client.send('Anti_fire:'+add)
                                if add:
                                    m_data.turn = False
                                for row in range(10):
                                    if 8 in m_data.my_field[row]:
                                        for cell in range(10):
                                            if m_data.my_field[row][cell] == 8:
                                                m_data.my_field[row][cell] = 6
                                for explosion in m_data.list_explosions:
                                    if explosion[0].name == 'fire' and explosion[0].x < 725:
                                        explosion[0].name = 'explosion'
                                        explosion[0].update_image()
                                m_transform.type_transform = random.randint(0,m_transform.count_types)
                                m_data.progression = "game"
                                                        # m_attack.need_to_send.append('Anti_fire:')
                                                        
                            else:
                                m_data.attack = m_data.select_weapon
                                m_transform.type_transform = random.randint(0,m_transform.count_types)
                                m_data.progression = "game"
                except:
                    print('hhhhhhhhhhhhhhhhhhhho')
            elif self.function == 'shop':
                m_transform.type_transform = random.randint(0,m_transform.count_types)
                if m_data.progression == 'shop':
                    m_data.progression = "game"
                    m_data.select_weapon = None
                else:
                    m_data.progression = 'shop'
                    m_achievements.achievement("New Opportunities")
            elif self.function == 'achievements':
                m_transform.type_transform = random.randint(0,m_transform.count_types)
                if m_data.progression == 'achievements':
                    m_data.progression = "menu"
                else:
                    m_data.progression = 'achievements'
            # інакше функція гра
            elif self.function == "play":

                # змінна да_ні дорівнює правді
                yes_no = True
                # цикл для стандартних клітинок
                for row in m_data.cells:
                    # цикл для клітинок в ряду
                    for cell in m_data.cells[row]:
                        # якщо кораблі не розставлені
                        if cell[0]:
                            # змінна да_ні змінюється на неправду 
                            yes_no =  False
                # якщо всі кораблі розставлені
                if yes_no:
                    # переходимо в гру
                    m_transform.type_transform = random.randint(0,m_transform.count_types)
                    m_data.progression = "game"
                    icon = pygame.image.load(os.path.abspath(__file__ + "/../../images/icon_peaceful.png"))
                    pygame.display.set_icon(icon)
                    if not m_data.revenge:
                        # if m_data.client_server == "client" or not m_data.client_server:
                            # активує клієнта одночасно з роботою кода
                        threading.Thread(target = m_client.activate,daemon=True).start()
                        # if m_data.client_server == "server" or not m_data.client_server:
                            # активує сервер
                            # threading.Thread(target = m_server.activate,daemon=True).start()
                        # 
                    else:
                        ships = "field:"
                        for ship in m_data.all_ships:
                            ships += f"{ship.name},{ship.row},{ship.cell},{ship.rotate} "
                        # визиваємо функцію для відправки даних на сервер
                        m_client.send(ships.encode()) 

            elif self.function and 'set_achievement' in self.function:
                description_.TEXT = (self.name.split('/')[1]+': '+m_data.achievements_data[self.function.split('/')[1]]['description']).split(' ') +['                ', '           ']
                m_data.select_weapon = self.name.split('/')[1]
                print(description_.TEXT)
                size = description_.FONT.size(" ".join(description_.TEXT))
                if size[0] < description_.rect.width:
                    description_.TEXT = [" ".join(description_.TEXT)]
                elif len(description_.TEXT)-2:
                    list_text = []
                    text = ''
                    
                    for text_for in description_.TEXT:
                        print(description_.rect.width)
                        size = description_.FONT.size(text+text_for)
                        if size[0] < description_.rect.width:
                            text += text_for + ' '
                        elif size[0] > description_.rect.width:
                            list_text.append(text)
                            text = text_for + ' '
                        elif description_.TEXT[-1] == text_for + ' ':
                            list_text.append(text)
                    if text_for in list_text[-1]:
                        pass
                    else:
                        size = description_.FONT.size(text+text_for)
                        if size[0] < description_.rect.width:
                            text += text_for
                        elif size[0] > description_.rect.width:
                            list_text.append(text)
                            list_text.append(text_for)
                        elif description_.TEXT[-1] == text_for:
                            list_text.append(text)
                    description_.TEXT =  list_text
                    print(description_.TEXT)
            elif self.function and 'weapons' in self.function:
                # buff
                
                description.TEXT = m_data.weapon_data[self.function.split('/')[1]][self.function.split('/')[2]].split(' ') +['                ', '           ']
                m_data.select_weapon = self.function.split('/')[2]
                print(description.TEXT)
                multiplers = [
                    self.rect.width/self.width,
                    self.rect.height/self.height
                ]
                if multiplers[0] > multiplers[1]:
                    description.FONT = pygame.font.SysFont("algerian", int((40*multiplers[1])))
                else:
                    description.FONT = pygame.font.SysFont("algerian", int((40*multiplers[0])))
                size = description.FONT.size(" ".join(description.TEXT))
                if size[0] < description.width*multiplers[0]:
                    description.TEXT = [" ".join(description.TEXT)]
                elif len(description.TEXT)-2:
                    list_text = []
                    text = ''
                    
                    for text_for in description.TEXT:
                        print(description.width*multiplers[0])
                        size = description.FONT.size(text+text_for)
                        if size[0] < description.width*multiplers[0]:
                            text += text_for + ' '
                        elif size[0] > description.width*multiplers[0]:
                            list_text.append(text)
                            text = text_for + ' '
                        elif description.TEXT[-1] == text_for + ' ':
                            list_text.append(text)
                    if text_for in list_text[-1]:
                        pass
                    else:
                        size = description.FONT.size(text+text_for)
                        if size[0] < description.width*multiplers[0]:
                            text += text_for
                        elif size[0] > description.width*multiplers[0]:
                            list_text.append(text)
                            list_text.append(text_for)
                        elif description.TEXT[-1] == text_for:
                            list_text.append(text)
                    description.TEXT = [self.function.split('/')[2]+': '] +  list_text
                    print(description.TEXT)
                    # print(description.TEXT)
            else:
                if m_data.client_server and nickname.TEXT:
                    # for sprite in m_data.all_ships:
                    #     print(sprite.x,sprite.y,sprite.width,sprite.height,multiplier_x,multiplier_y,ship.name)
                    # записання ip
                    ip = input.TEXT.split(": ")
                    del ip[0]
                    ip = ": ".join(ip)
                    m_data.ip = ip
                    if m_data.ip == "":
                        m_data.ip = m_client.ip
                    with open(m_data.path+m_data.type+'data.txt', "w") as file:
                        file.write(f"{nickname.TEXT}\n{m_data.ip}\n{not m_audio.track.stoped}\n{m_data.client_server}")
                    # перехід в пре-гру"
                    m_transform.type_transform = random.randint(0,m_transform.count_types)
                    m_data.progression = "pre-game"
                    # if event.key == pygame.K_c:
                    # for row in m_data.my_field:
                    #     print(row)
    # метод відображення поверхні на головному окні
    def blit(self, screen,x,y,width,height,multiplier_x,multiplier_y):
        '''
            >>> Відображає картинку на екрані
        '''
        # якщо картинка задана 
        self.rect = pygame.Rect(x,y,width,height)
        if self.name != "":
            # відображення картинки 
            Image.blit(self, screen,x,y,width,height,multiplier_x,multiplier_y)
        if multiplier_x > multiplier_y and self.current_size !=int((self.size*multiplier_y)):
            self.FONT = pygame.font.SysFont("algerian", int((self.size*multiplier_y)))
            self.current_size= int((self.size*(multiplier_y/2)))
            # self.size = int((self.size*multiplier_y))
        elif self.current_size != int((self.size*multiplier_x)) and multiplier_x <= multiplier_y:
            self.FONT = pygame.font.SysFont("algerian", int((self.size*(multiplier_x))))
            self.current_size = int((self.size*multiplier_x))
            
        if type(self.TEXT) == type(""):
            size = self.FONT.size(self.TEXT) 
            # задаємо y для тексту
            y = y + height/2-size[1]/2
            # задаємо x для тексту
            x = x + width/2-size[0]/2
            # if self.TEXT != self.last_text:
                # screen.blit(self.FONT.render(self.TEXT,True,self.COLOR), (x, y))
            render = self.FONT.render(self.TEXT,True,self.COLOR)
            render.set_alpha(self.opasity)
            screen.blit(render, (x, y))
            # print(render,self.render)
            self.last_text = self.TEXT
            # print('hoh')
            # else:
            #     screen.blit(self.render, (x, y))
            # screen.blit(self.FONT.render(self.TEXT,True,self.COLOR), (x, y))
        elif type(self.TEXT) == type([]):
                
            count = 0
            # while True:
            for text in self.TEXT:
                if multiplier_x > multiplier_y:
                    self.FONT = pygame.font.SysFont("algerian", int((40*multiplier_y)))
                else:
                    self.FONT = pygame.font.SysFont("algerian", int((40*multiplier_x)))
                height = self.FONT.size(text)[1]
                size = self.FONT.size(text) 
                y = (self.rect.y+10+height*count) * multiplier_y
                # задаємо x для тексту 
                x = (self.rect.x)*multiplier_x
                # відображення тексту на екрані
                render = self.FONT.render(text,True,(0,0,0))
                render.set_alpha(self.opasity)
                screen.blit(render, (self.rect.x, y))
                count += 1
        # y = y + height/2-size[1]/2
        # # задаємо x для тексту 
        # x = x + width/2-size[0]/2
        # # відображення тексту на екрані
        # size = self.FONT.size(self.TEXT)

        # size[0] = multiplier_x * size[0]
        # size[1] = multiplier_y * size[1]
        # задаємо y для тексту

# button = Button()
class Input(Image):
    '''
        >>> Додає параметри до картинки
    '''
    def __init__(self, width: int, height: int,x = 0,y = 0, name = "", progression = "menu", color = (0,0,0), text = "ip: ", list = "0123456789."):
        self.start_width = width 
        self.start_height = height 
        Image.__init__(self, width=width, height=height, x=x, y=y, name=name, progression=progression)
        self.COLOR = color
        self.FONT = pygame.font.SysFont("algerian", 65)
        self.TEXT = text 
        self.RENDER_TEXT = None
        self.enter = False
        self.edit("ok")
        self.rect = pygame.Rect(x,y,width,height)
        self.list = list
        self.size = 65 
        self.current_size = self.size
    def blit(self, screen,x,y,width,height,multiplier_x,multiplier_y):
        '''
            >>> Відображає картинку на екрані
        '''
        if self.name != "":
            # відображення картинки
            Image.blit(self, screen,x,y,width,height,multiplier_x,multiplier_y)
        # s = pygame.time.get_ticks()
        # задання розміру для тексту
        self.rect = pygame.Rect(x,y,width,height)
        if self.list == 'any':
            self.x = 42
        if multiplier_x > multiplier_y and self.current_size !=int((self.size*multiplier_y)):
            self.FONT = pygame.font.SysFont("algerian", int((self.size*multiplier_y)))
            self.current_size= int((self.size*multiplier_y))
            # self.size = int((self.size*multiplier_y))
        elif self.current_size != int((self.size*multiplier_x)) and multiplier_x <= multiplier_y:
            self.FONT = pygame.font.SysFont("algerian", int((self.size*multiplier_x)))
            self.current_size = int((self.size*multiplier_x))
        size = self.FONT.size(self.TEXT)
        # задаємо y для тексту
        y = y + height/2-size[1]/2
        # задаємо x для тексту
        x = x + width/2-size[0]/2
        render = self.FONT.render(self.TEXT,True,self.COLOR)
        render.set_alpha(self.opasity)
        screen.blit(render, (x, y))
        self.rect = pygame.Rect(x,y,width,height)
        # e = pygame.time.get_ticks()
        # print(e-s,'input')
        # відображення тексту на екрані
    def activate(self, event):
        '''
            >>> Відповідає за виділення поля ввода
        '''
        # rect = pygame.Rect(self.x,self.y,self.width,self.height)
        if self.rect.collidepoint(event.pos):
            self.enter = True
            print('hallok')
        else:
            self.enter = False
        # print(self.enter)
    def edit(self,event):
        '''
            >>> Редагує текст
        '''
        if self.enter:
            key = pygame.key.name(event.key)
            if event.key == pygame.K_BACKSPACE and self.TEXT != "ip: ":
                # прибирає останній символ текста 
                self.TEXT = self.TEXT[:-1]
            elif key in self.list or self.list != "0123456789." and len(key) == 1:
                # 
                self.TEXT += key

        self.RENDER_TEXT = self.FONT.render(self.TEXT, True, self.COLOR)
class Auto(Image):
    '''
        >>> Випадково розставляє кораблі
    '''
    def __init__(self, width: int, height: int, x: int, y: int, name='', progression: str = "pre-game"):
        super().__init__(width, height, x, y, name, progression)
        self.rect = pygame.Rect(x,y,width,height)
        m_data.list_blits["pre-game"].append(self)
    def blit(self, screen,x,y,width,height,multiplier_x,multiplier_y):
        '''
            >>> Відображає кнопку на екрані
        '''
        self.rect = pygame.Rect(x,y,width,height)
        # pygame.draw.rect(screen,(255,25,25),self.rect)
    def randomship(self, cor):
        '''
            >>> Випадково розставляє кораблі
        '''
        if self.rect.collidepoint(cor):
            count = 0
            count_ships = 0  
            m_data.my_field = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
            m_data.all_ships = []
            for row in m_data.cells:
                for cell in m_data.cells[row]:
                    cell[0] =  False
            # for ship in m_data.all_ships:
                
            while True:
                row = random.randint(0, 9)
                cell = random.randint(0, 9)
                rotate = random.randint(0, 4)
                count += 1
                if m_data.my_field[row][cell] ==  0:
                    ship = Ship(x = 59, y = 115, cell = cell, row = row, rotate = rotate * 90)
                    count_ships += 1
                    m_data.my_field[row][cell] = 1
                    fill_field(m_data.my_field)
                if count_ships == 4 or count > 1000:
                    break
                
            count_ships = 0
            while True:
                row = random.randint(0, 9)
                cell = random.randint(0, 9)
                rotate = random.randint(0, 4)
                count += 1
                try: 

                    if m_data.my_field[row][cell] == 0: 
                        if m_data.my_field[row][cell+1] == 0 and rotate % 2 == 0 or m_data.my_field[row+1][cell] == 0 and rotate % 2 == 1: 
                            ship = Ship(x = 59, y = 115, cell = cell, row = row, name= "2", rotate = rotate * 90)
                            count_ships += 1
                            fill_field(m_data.my_field)
                except:
                    pass
                if count_ships == 3 or count > 1000:
                    break

            count_ships = 0
            while True:
                row = random.randint(0, 9)
                cell = random.randint(0, 9)
                rotate = random.randint(0, 4)
                count += 1
                try:
                    if m_data.my_field[row][cell] == 0:
                        if m_data.my_field[row][cell+1] == 0 and rotate % 2 == 0 or m_data.my_field[row+1][cell] == 0 and rotate % 2 == 1:
                            if m_data.my_field[row][cell+2] == 0 and rotate % 2 == 0 or m_data.my_field[row+2][cell] == 0 and rotate % 2 == 1:
                                ship = Ship(x = 59, y = 115, cell = cell, row = row, name= "3", rotate= rotate * 90)
                                count_ships += 1
                                fill_field(m_data.my_field)
                except:
                    pass
                if count_ships == 2 or count > 1000:
                    break
            
            count_ships = 0
            while True:
                row = random.randint(0, 9)
                cell = random.randint(0, 9)
                rotate = random.randint(0, 4)
                count += 1
                try:
                    if m_data.my_field[row][cell] ==  0:
                        if m_data.my_field[row][cell+1] == 0 and rotate % 2 == 0 or m_data.my_field[row+1][cell] == 0 and rotate % 2 == 1:
                            if m_data.my_field[row][cell+2] == 0 and rotate % 2 == 0 or m_data.my_field[row+2][cell] == 0 and rotate % 2 == 1:
                                if m_data.my_field[row][cell+3] == 0 and rotate % 2 == 0 or m_data.my_field[row+3][cell] == 0 and rotate % 2 == 1:
                                    ship = Ship(x = 59, y = 115, cell = cell, row = row, name= "4", rotate= rotate * 90)
                                    count_ships += 1
                                    fill_field(m_data.my_field)
                except:
                    pass
                if count_ships == 1 or count > 1000:
                    for row1 in m_data.my_field:
                        print(row1)

                    break
            if count > 1000:
                self.randomship(cor)


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
ip1 = ""
nick = getpass.getuser()
if m_data.read_data["nickname"] != "":
    nick = m_data.read_data["nickname"]
if "." in m_data.read_data["ip"]:
    ip1 = m_data.read_data["ip"]
button_start = Button(width = 402 , height = 120, x = 435, y = 370, name = "", text= "start")
m_data.list_blits["menu"].append(button_start)

input = Input(width = 496, height = 148, x = 387 , y = 568, name = "button_start", text = f"ip: {ip1}")
nickname = Input(x= 42, y= 43, width= 281, height= 84, name = "button_start", text = nick, list = "any")
ip = Button(x = 981, y = 59, width = 281, height = 84, name = "button_start", text = m_client.ip, size = 50)
for object in [nickname, ip]:
    size = object.FONT.size(object.TEXT)
    if object.width - size[0] - 10 < 0:
        width = -(object.width - size[0] - 10)
        object.x -= width
        object.width += width
        object.update_image()
text_ip = Button(x = ip.x, y = 10, width = ip.width, height = 45, text = "user ip", size = 50)
m_data.list_blits["menu"].append(text_ip)
auto = Auto(width= 179, height= 79, x= 794, y= 587)
rotate = Button(fun= 'ship',  width = 222, height = 68, x= 1000, y= 600, name = "", progression= "pre-game", text= "")
play = Button(x = 900, y = 720, name = "", fun= 'play', width = 200, height = 65, text = "")
revenge = Button(height = 90, width = 372, x = 28, y = 600, text = "", progression = "win", fun= "win_lose")
out = Button(height = 80, width = 518, x = 0, y = 712, progression = "win", text = "", fun = "check")
m_data.list_blits["pre-game"].extend([rotate,play])
# revenge = Button(height = 90, width = 372, x = 28, y = 600, text = "", progression = "lose", fun= "win_lose")
# out = Button(height = 80, width = 518, x = 0, y = 712, progression = "lose", text = "", fun = "check")
music =Button(width = 76,height = 72,x = nickname.width + 50, y = 45, text = "", fun = "music", name =  "music")
client = Button(width= 281, height= 100, name= "button_start", text= "client", x= 42, y= 600, fun= "c_s:client")  
shop = Button(width= 281, height= 90, name= "button_start", text= "shop", x= 387+60, y= 725, fun= "shop",progression="NONE")
shop_ = Button(width= 321, height= 145, name= "", text= "", x= 0, y= 0, fun= "shop",progression='shop', size = 40)
achievements = Button(width= 500, height= 90, name= "button_start", text= "achievements", x= 387, y= 725, fun= "achievements",progression="menu")
achievements_ = Button(width= 281, height= 90, name= "button_start", text= "back to menu", x= 960, y= 15, fun= "achievements",progression='achievements', size = 40)
server = Button(width= 281, height= 100, name= "button_start", text= "server", x= 981, y= 600, fun= "c_s:server")
wait = Button(width= 1280, x = 0, y = 712, height= 59, text = "wait", progression= "game")
enemy_nickname = Button(y = 10, x = 1000, width= 200, height= 40, size = 40)
your_nickname = Button(y = 10, x = 20, width= 200, height= 40, size = 40)
coins = Button(y = 30, x = 950, width= 300, height= 90, size = 40, progression= "shop", text = "0", name = "")
# coin = Button(y = 50, x = 970, width= 50, height= 50, size = 0, progression= "shop", text = "", name = "duplone")
description = Button(y = 175, x = 950, width= 300, height= 533, size = 20, progression= "shop", text = "select item")
description_ = Button(y = 150, x = 950, width= 300, height= 533, size = 20, progression= "achievements", text = "select achievement")
buy = Button(y = 696, x = 957, width= 321, height= 145, size = 40, progression= "shop", text = "", name = "",fun='buy')
# m_data.list_blits["shop"].append(description)
homing_rocket = Button(y = 235, x = 15, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/rockets/homing_rocket")
line_rocket= Button(y = 235, x = 167, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/rockets/line_rocket")
fire_rocket = Button(y = 235, x = 319, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/rockets/fire_rocket")
rocket_3x3 = Button(y = 235, x = 469, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/rockets/rocket_3x3")

Anti_fire = Button(y = 514, x = 15, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/buff/Anti_fire")
radar = Button(y = 514, x = 167, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/buff/radar")
Energetic = Button(y = 514, x = 319, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/buff/Energetic")
Air_Defence = Button(y = 514, x = 469, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/buff/Air_Defence")
list_weapons = [homing_rocket,rocket_3x3,line_rocket,fire_rocket,Energetic,radar,Air_Defence,Anti_fire]

m_data.list_blits['shop'] += list_weapons+[coins,buy,description]
if m_data.client_server == "server":
    server.COLOR =(40,2,255)
if m_data.client_server == "client":
    client.COLOR =(40,2,255)
your_turn = Button(width= 272, height= 66, x= 133, y= 712, text= "your step", progression= "", color=(0, 0, 255),size=50)
opponent_turn = Button(width= 350, height= 66, x= 800, y= 712, text= "enemy step", progression= "", color = (255, 0, 0),size=50)

m_data.list_blits["game"].append(your_nickname)
m_data.list_blits["game"].append(enemy_nickname)

m_data.list_blits["lose"].extend([revenge, out])
for achievement_code in m_data.achievements_data:
    m_data.list_achievements_view[achievement_code] = Button(fun=f"set_achievements/{achievement_code}",width=50,height=50,x=0,y=0,name=f"achievements/{achievement_code}",progression='NONE',text='')
# for achievement in m_data.list_achievements_view:
#     pass
 
# achievements