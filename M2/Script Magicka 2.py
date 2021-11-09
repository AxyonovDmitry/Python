import pyautogui
import time
import keyboard

with open("settings_m2.txt") as file:
	mas = file.read().strip().split('\n')[1:]
ind = 0
for index,i in enumerate(mas):
	if i == "users_input:":
		ind = index
user_input =[i.split('=') for i in mas[ind+1:]]
settings = [i.split()[-1] for i in mas][:ind-1]

for i in range(len(user_input)):
	settings.append(user_input[i].pop(1)[1:])
tmp = []
for i in user_input:
	a = list(str(*i))
	a.pop(-1)
	a = ''.join(a)
	tmp.append(a)
user_input = tmp


print(settings)
print(user_input)
time.sleep(2)
shiled_combination = "eddqqrr"
fire_dead_line = "ssfff"
ice_attack = "dqqqqrrrr"
heal = "sssss"
teleport = list("ass") + ["space"]
resurect = list("wa") + ["space"]
guard = list("wwae") + ["space"]
ice_storm = list("qrqrdrr") + ["space"]
void = list("sde") + ["space"]
while True:
	time.sleep(0.1)
	if settings[0] != "None":
		if keyboard.is_pressed(settings[0]):
			for i in shiled_combination:
				pyautogui.press(i)
			pyautogui.middleClick()
	if settings[3] != "None":
		if keyboard.is_pressed(settings[3]):
			for i in heal:
				pyautogui.press(i)
			pyautogui.middleClick()
	if settings[1] != "None":
		if keyboard.is_pressed(settings[1]):
			for i in fire_dead_line:
				pyautogui.press(i)
	if settings[2] != "None":
		if keyboard.is_pressed(settings[2]):
			for i in ice_attack:
				pyautogui.press(i)
	if settings[4] != "None":
		if keyboard.is_pressed(settings[4]):
			for i in teleport:
				pyautogui.press(i)
	if settings[5] != "None":
		if keyboard.is_pressed(settings[5]):
			for i in resurect:
				pyautogui.press(i)
	if settings[6] != "None":
		if keyboard.is_pressed(settings[6]):
			for i in guard:
				pyautogui.press(i)
	if settings[7] != "None":
		if keyboard.is_pressed(settings[7]):
			for i in ice_storm:
				pyautogui.press(i)
	if settings[8] != "None":
		if keyboard.is_pressed(settings[8]):
			for i in void:
				pyautogui.press(i)
	if settings[-3] != "None":
		if keyboard.is_pressed(settings[-3]):
			for i in user_input[0]:
				pyautogui.press(i)
	if settings[-2] != "None":
		if keyboard.is_pressed(settings[-2]):
			for i in user_input[1]:
				pyautogui.press(i)
	if settings[-1] != "None":
		if keyboard.is_pressed(settings[-1]):
			for i in user_input[2]:
				pyautogui.press(i)		
	if keyboard.is_pressed('/'):
		quit()
