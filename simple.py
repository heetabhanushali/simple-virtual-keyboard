import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)


detector = HandDetector(detectionCon= 0.8)
keys = [["1", "2" , "3", "4", "5", "6", "7", "8", "9", "0"],
        ["Q", "W" , "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S" , "D", "F", "G", "H", "J", "K", "L"],
        ["Z", "X" , "C", "V", "B", "N", "M" , "Delete"],
        ["Space" ]]



class Button():
    def __init__(self , pos , text, size = [85 , 85] , bcolor = (255,0,255)):
        self.pos = pos
        self.text = text
        self.size = size
        self.bcolor = bcolor
    
    def draw(self , img , bcolor = None , ptext = None):
        x , y = self.pos
        w , h = self.size
        colorr = bcolor if bcolor else self.bcolor
        text = ptext if ptext else self.text

        overlay = img.copy()
        alpha = 0.5
        cv2.rectangle(img , self.pos, (x + w , y + h) , colorr , cv2.FILLED)
        cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)
        cv2.putText(img, text , (x + 20 , y + 60 ) , cv2.FONT_HERSHEY_PLAIN , 4 , (255,255,255) , 3)

        return img

buttonlist = []
finaltext = ""
caps = False

for i in range(len(keys)):
    for j ,key in enumerate(keys[i]):
        if key == "Space":
            buttonlist.append(Button([100 * j + 50 , 100 * i + 50], key , size = [400 , 85]))
        elif key == "Delete":
            buttonlist.append(Button([100 * j + 50 , 100 * i + 50], key , size = [285 , 85]))
        # elif key == "Caps Lock":
        #     buttonlist.append(Button([100 * j + 600 , 100 * i + 50], key , size = [200 , 85]))
        else:
            buttonlist.append(Button([100 * j + 50 , 100 * i + 50], key))

placeholder = Button([50 , 600] , "" , [1000 , 100])

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img , draw =False )

    for button in buttonlist:
        button.draw(img)

    
    placeholder.draw(img , ptext = finaltext)
    
    if hands:
        for hand in hands:
            lmList = hand["lmList"]
            for button in buttonlist:
                x , y = button.pos
                w , h = button.size
                if x < lmList[8][0] < x+w and y < lmList[8][1] < y+h:
                    button.draw(img, (0,0,255))
                    l ,_ , _ = detector.findDistance( lmList[8][:2], lmList[4][:2], img)
                    if l < 40:
                        print("Clicked:" , button.text)
                        button.draw(img, (175, 0 ,175))
                        if button.text == "Delete":
                            finaltext = finaltext[:-1]
                        elif button.text == "Space":
                            finaltext += " "
                        else: 
                            finaltext += button.text
                        placeholder.draw(img , ptext = finaltext)
                        sleep(0.5)



    cv2.imshow("Virtual Keyboard" , img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
