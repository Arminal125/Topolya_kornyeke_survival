
import pygame





class caracter:

    def_caracter_WIDTH = 40
    def_caracter_HEIGHT = 60
    def_caracter_VEL = 5

    def __init__(self, x, y):

		self.caracter_x = x
		self.caracter_y = y

        self.caracter_WIDTH = def_caracter_WIDTH
        self.caracter_HEIGHT = def_caracter_HEIGHT
        self.caracter_VEL = def_caracter_VEL

        self.character_move_left = None
        self.character_move_right = None
        # self.caracter_WIDTH = caracter_WIDTH if caracter_WIDTH is not None else self.def_caracter_WIDTH
        # self.caracter_HEIGHT = caracter_HEIGHT if caracter_HEIGHT is not None else self.def_caracter_HEIGHT
        # self.caracter_VEL = caracter_VEL if caracter_VEL is not None else self.def_caracter_VEL


    # wisszaalitani a carakter meretet az alap beallitasra
    def return_default_size(self):
        self.caracter_WIDTH = self.def_caracter_WIDTH
        self.caracter_HEIGHT = self.def_caracter_HEIGHT

    def setup_player(self, player_img):
        #  player pictures
        for playe_image in player_img:
            img_right = pygame.image.load(playe_image)
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)

            self.character_move_left.append(img_right)
            self.character_move_right.append(img_left)


class Player():
	def __init__(self, x, y):
		self.reset(x, y)

	def update(self, game_over):
		dx = 0
		dy = 0
		walk_cooldown = 5
		col_thresh = 20

		if game_over == 0:
			#get keypresses
			key = pygame.key.get_pressed()
			if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
				self.vel_y = -15
				self.jumped = True
			if key[pygame.K_SPACE] == False:
				self.jumped = False
			if key[pygame.K_LEFT]:
				dx -= 5
				self.counter += 1
				self.direction = -1
			if key[pygame.K_RIGHT]:
				dx += 5
				self.counter += 1
				self.direction = 1
			if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
				self.counter = 0
				self.index = 0
				if self.direction == 1:
					self.image = self.images_right[self.index]
				if self.direction == -1:
					self.image = self.images_left[self.index]


			#handle animation
			if self.counter > walk_cooldown:
				self.counter = 0
				self.index += 1
				if self.index >= len(self.images_right):
					self.index = 0
				if self.direction == 1:
					self.image = self.images_right[self.index]
				if self.direction == -1:
					self.image = self.images_left[self.index]


			#add gravity
			self.vel_y += 1
			if self.vel_y > 10:
				self.vel_y = 10
			dy += self.vel_y

			#check for collision
			'''
			self.in_air = True
			for tile in world.tile_list:
				#check for collision in x direction
				if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
					dx = 0
				#check for collision in y direction
				if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
					#check if below the ground i.e. jumping
					if self.vel_y < 0:
						dy = tile[1].bottom - self.rect.top
						self.vel_y = 0
					#check if above the ground i.e. falling
					elif self.vel_y >= 0:
						dy = tile[1].top - self.rect.bottom
						self.vel_y = 0
						self.in_air = False
			'''




			'''
			#check for collision with enemies
			if pygame.sprite.spritecollide(self, blob_group, False):
				game_over = -1
				game_over_fx.play()

			#check for collision with lava
			if pygame.sprite.spritecollide(self, lava_group, False):
				game_over = -1
				game_over_fx.play()

			#check for collision with exit
			if pygame.sprite.spritecollide(self, exit_group, False):
				game_over = 1
			'''

			'''
			#check for collision with platforms
			for platform in platform_group:
				#collision in the x direction
				if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
					dx = 0
				#collision in the y direction
				if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
					#check if below platform
					if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
						self.vel_y = 0
						dy = platform.rect.bottom - self.rect.top
					#check if above platform
					elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
						self.rect.bottom = platform.rect.top - 1
						self.in_air = False
						dy = 0
					#move sideways with the platform
					if platform.move_x != 0:
						self.rect.x += platform.move_direction
			'''

			#update player coordinates
			self.rect.x += dx
			self.rect.y += dy

		'''
		elif game_over == -1:
			self.image = self.dead_image
			draw_text('GAME OVER!', font, blue, (screen_width // 2) - 200, screen_height // 2)
			if self.rect.y > 200:
				self.rect.y -= 5
		
		'''
		#draw player onto screen
		screen.blit(self.image, self.rect)

		return game_over


	def reset(self, x, y):
		self.images_right = []
		self.images_left = []
		self.index = 0
		self.counter = 0
		for num in range(1, 5):
			img_right = pygame.image.load(f'object_character/guy{num}.png')
			img_right = pygame.transform.scale(img_right, (40, 80))
			img_left = pygame.transform.flip(img_right, True, False)
			self.images_right.append(img_right)
			self.images_left.append(img_left)
		# image that show that the caracter has passed on and is dead
		self.dead_image = pygame.image.load('img/ghost.png')

		self.image = self.images_right[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False
		self.direction = 0
		self.in_air = True


HOPEHELY_IMG = pygame.transform.scale(pygame.image.load("object_hopehely/hopehely.png"), (HOPEHELY_WIDTH, HOPEHELY_HEIGHT))
GHOST_IMG = pygame.transform.scale(pygame.image.load("object_ghost/szellem.png"), (GHOST_WIDTH, GHOST_HEIGHT))
CARACTER_IMG = pygame.transform.scale(pygame.image.load("themes/caracter.png"), (caracter_WIDTH, caracter_HEIGHT))
HOEMBER_IMG = pygame.transform.scale(pygame.image.load("object_hoember/hoember.png"), (HOEMBER_WIDTH, HOEMBER_HEIGHT))
SANTA_IMG = pygame.transform.scale(pygame.image.load("object_santa/Santa.png"), (SANTA_WIDTH, SANTA_HEIGHT))

class ghost:

	GHOST_WIDTH = 50
	GHOST_HEIGHT = 80
	GHOST_VEL = 4
    def __init__(self, x, y):



class hopehely():

    def __init__(self, x, y):
		self.HOPEHELY_WIDTH = 40
		self.HOPEHELY_HEIGHT = 60
		self.HOPEHELY_VEL = 4

		self.reset(x, y)


	def update(self, game_over):
		dy = 0

		if game_over == 0:

			# rotate the star
			if self.hopehey_rotate_index >= 360:
				self.hopehey_rotate_index = 0
			else:
				self.hopehey_rotate_index = self.hopehey_rotate_index + 1


			# update position of the hopehely
			self.rect.y += dy

			# draw player onto screen
			screen.blit(pygame.transform.rotate(self.image, self.hopehey_rotate_index), (self.x, self.y))
			screen.blit(self.image, self.rect)


			return game_over

	def reset(self, x, y):
		self.index = 0
		self.counter = 0
		self.hopehely_img = pygame.image.load(f'object_hopehely/hopehely.png')

		# do this only if you have animation
		# for num in range(1, 5):
			# img_right = pygame.image.load(f'object_hopehely/hopehely{num}.png')
			# img_right = pygame.transform.scale(img_right, (40, 80))
			# img_left = pygame.transform.flip(img_right, True, False)
			# self.images_right.append(img_right)
			# self.images_left.append(img_left)
		# image that show that the caracter has passed on and is dead

		self.image = self.hopehely_img
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		# self.width = self.image.get_width()
		# self.height = self.image.get_height()
		self.width = self.HOPEHELY_WIDTH
		self.height = self.HOPEHELY_HEIGHT
		self.vel_y = self.HOPEHELY_VEL
		self.direction = 0




class hoember:
	HOEMBER_WIDTH = 50
	HOEMBER_HEIGHT = 70
	HOEMBER_VEL = 3

    def __init__(self, x, y):




class santa:
	SANTA_WIDTH = 50
	SANTA_HEIGHT = 70
	SANTA_VEL = 3
    def __init__(self, x, y):



class star:
	star_WIDTH = 10
	star_HEIGHT = 20
	star_VEL = 3

    def __init__(self, x, y):
        self.rotate_index = 0


    def draw_star(self, win, rotate):

        if self.rotate_index >= 360:
            self.rotate_index = 0
        else:
            self.rotate_index = self.rotate_index + 1








