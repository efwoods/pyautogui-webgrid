import pyautogui
import os

def loadImages():
    cwd = os.getcwd()
    target_image = cwd + '/images/blue-button.png'
    start_game_img = cwd + '/images/start-game.png'
    your_peak_score_img = cwd + '/images/your-peak-score.png'
    return target_image, start_game_img, your_peak_score_img

def startWebgrid(start_game_img):
    start_game_location = pyautogui.locateCenterOnScreen(start_game_img, confidence=0.9)
    
    # pyautogui.locateCenterOnScreen returns a location that is twice the size of the display;
    # The following is a fix
    start_game_mouse_coordinate_x = start_game_location[0]/2
    start_game_mouse_coordinate_y = start_game_location[1]/2
    
    pyautogui.click(start_game_mouse_coordinate_x, start_game_mouse_coordinate_y)
    pyautogui.click()

def clickWebGridTarget(target_image, your_peak_score_img):

    continue_searching = True
    count = 0
    while(continue_searching):
        count += 1
        print('attempt #: {}'.format(count))
        try:
            target = pyautogui.locateCenterOnScreen(target_image, confidence=0.9)
            # pyautogui.locateCenterOnScreen returns a location that is twice the size of the display;
            target_X = target[0]/2
            target_Y = target[1]/2
            pyautogui.click(target_X, target_Y)
            print('targetfound & clicked')
            # pyautogui.click()
        except pyautogui.ImageNotFoundException:
            print('target not found')
            try:
                # If the text 'Your peak score' is found, then the game is over.
                your_peak_score_img_location = pyautogui.locateCenterOnScreen(your_peak_score_img)
                continue_searching = False
                print('game over')
            except pyautogui.ImageNotFoundException:
                print('game over not found')
                # If the text 'Your peak score' is not found, then continue searching 
                pass

def playWebgrid():
    target_image, start_game_img, your_peak_score_img = loadImages()
    startWebgrid(start_game_img)
    clickWebGridTarget(target_image, your_peak_score_img)
    
def main():
    playWebgrid()
    
if __name__ == '__main__':
    playWebgrid()