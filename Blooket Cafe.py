import time, keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from threading import Thread

_DEBUG = False

Driver = webdriver.Chrome('C:\\Users\\theme\\Documents\\chromedriver.exe')
Driver.get('https://blooket.com/login')

AllowedGames = {
	'https://www.blooket.com/cafe': 'cafe',
	'https://www.blooket.com/cafe/shop': 'cafe'
}
def gamefunctionCAFE():
	Threads = []

	def GetPlates():
		Plates = {}

		for I in range(1, 10):
			Plate = Driver.find_element_by_id('plate' + str(I))
			Divs = Plate.find_elements_by_css_selector('div')
			if len(Divs) > 0 and Divs[0]:
				try:
					Food = Divs[0]
					Icon = Food.find_element_by_css_selector('img')
					if Icon:
						NameOfFood = Icon.get_attribute('alt')
						Plates[NameOfFood] = Plate
				except:
					try:
						if len(Divs) > 1 and Divs[1]:
							Food = Divs[1]
							try:
								Icon = Food.find_element_by_css_selector('img')
							except Exception as e:
								Icon = None
								print('[2]Failed to get food image of plate: ', e)

							if Icon:
								NameOfFood = Icon.get_attribute('alt')
								Plates[NameOfFood] = Plate
					except Exception as e:
						if _DEBUG:
							print('[3]Failed to get NameOFFood of plate: ', e)

		return Plates

	def GetFoodItems():
		FoodItems = {}

		Plates = GetPlates()

		for NameOfFood in Plates:
			Plate = Plates.get(NameOfFood)
			if Plate:
				Divs = Plate.find_elements_by_css_selector('div')
				if Divs[1]:
					FoodCount = None
					Text = Divs[1].get_attribute('textContent')
					if Text and len(Text) > 0:
						FoodCount = int(float(Divs[1].get_attribute('textContent')))
					if FoodCount:
						FoodItems[NameOfFood] = FoodCount

		return FoodItems

	def ClickFirstAnswer():
		Driver.find_element_by_css_selector('body').send_keys(Keys.SPACE)
		time.sleep(.4)
		
		try:
			AnswersHolders = Driver.find_elements_by_class_name('styles__answersHolder___1tefk-camelCase')
		except Exception as e:
			AnswersHolders = None
			if _DEBUG:
				print('Failed to get answersholders: ', e)
		if AnswersHolders and AnswersHolders[0]:
			try:
				Answers = AnswersHolders[0].find_elements_by_css_selector('*')
			except Exception as e: 
				Answers = None
				if _DEBUG:
					print('Failed to get answers: ', e)
			if Answers:
				try:
					Answers[2].click()
					Driver.find_element_by_css_selector('body').send_keys(Keys.SPACE)
				except Exception as e:
					if _DEBUG:
						print('Failed to click / send space key: ', e)

	def ServerCustomers():
		try:
			Customers = Driver.find_elements_by_class_name('styles__container___2Z1Kp-camelCase')
		except Exception as e:
			Customers = None
			if _DEBUG:
				print('Failed getting customers: ', e)

		RealCustomers = []
		CustomerFood = {}

		if Customers:
			for Customer in Customers:
				try:
					if Customer and Customer.get_attribute('id') == 'customer':
						RealCustomers.append(Customer)
				except Exception as e:
					if _DEBUG:
						print('Failed to add customer to realcustomers list: ', e)

		for Customer in RealCustomers:
			try:
				Bubble = Customer.find_elements_by_class_name('styles__speechBubble___HEFTN-camelCase')[0]
			except Exception as e:
				Bubble = None
				if _DEBUG:
					print('Failed to get Customers speech bubble: ', e)
			if Bubble:
				try:
					FoodRows = Bubble.find_elements_by_class_name('styles__foodRow___2mF8X-camelCase')
				except Exception as e:
					FoodRows = None
					if _DEBUG:
						print('Failed to get FoodRows of Customers speechbubble: ', e)
				if FoodRows:
					for Row in FoodRows:
						try:
							Divs = Row.find_elements_by_css_selector('div')
						except Exception as e:
							Divs = None
							if _DEBUG:
								print('Failed to find divs of Customers speechbubbles FoodRows: ', e)
						if Divs:
							if Divs[0] and Divs[1]:
								Food = Divs[0]

								try:
									Amount = int(float(Divs[1].get_attribute('textContent')))
								except Exception as e:
									Amount = None
									if _DEBUG:
										print('Failed to get food amount of Customer: ', e)
								if Amount:
									try:
										Icon = Food.find_element_by_css_selector('img')
									except Exception as e:
										Icon = None
										if _DEBUG:
											print('Failed to get Customers food amount: ', e)
									if Icon:
										NameOfFood = Icon.get_attribute('alt')
										if NameOfFood:
											#FoodItems = GetFoodItems()
											#while True:
											#	if FoodItems.get(NameOfFood):
											#		if FoodItems.get(NameOfFood) < Amount:
											#			ClickFirstAnswer()
											#			FoodItems = GetFoodItems()

											Plates = GetPlates()
											if Plates and Plates.get(NameOfFood):
												try:
													Plates.get(NameOfFood).click()
													time.sleep(.05)
													Customer.click()
												except Exception as e:
													if _DEBUG:
														print('Failed to server customer: ', e)

	def ZKeyPressLoop():
		while True:
			keyboard.wait('z')
			ServerCustomers()
	def XKeyPressLoop():
		while True:
			keyboard.wait('x')
			ClickFirstAnswer()

	Thread1 = Thread(target = ZKeyPressLoop)
	Thread2 = Thread(target = XKeyPressLoop)

	Thread1.start()
	Thread2.start()

	Thread1.join()
	Thread2.join()

GameFunctions = {
	'cafe': gamefunctionCAFE
}
GameMessages = {
	'cafe': 'Controls: \n\tz: server customers\n\tx: click first answer'
}
SelectedGame = ''

while True:
	if Driver.current_url == 'https://www.blooket.com/login':
		break
print('Loaded! Please login.')

while True:
	if Driver.current_url == 'https://www.blooket.com/stats' or Driver.current_url == 'https://www.blooket.com/dashboard':
		break
print('Logged in! Please navigate to a SOLO game.')

while True:
	if len(Driver.window_handles) > 1:
		break
Driver.switch_to.window(Driver.window_handles[1])

while True:
	if 'https://www.blooket.com/solo' in Driver.current_url:
		break
print('Alright, now select a gamemode.')

while True:
	if Driver.current_url in AllowedGames:
		SelectedGame = AllowedGames[Driver.current_url]
		break

print(f'Great! You selected {SelectedGame}.\nHave fun!')
print(f'[{SelectedGame}] {GameMessages[SelectedGame]}')

GameFunctions[SelectedGame]()
