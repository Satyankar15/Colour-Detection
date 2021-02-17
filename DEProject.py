
import pandas as pd
import cv2 

inp=input("Enter image location ")
img_path = inp
img = cv2.imread(img_path)

clicked = False
r = g = b = xpos = ypos = 0

df=pd.read_csv('wikipedia_color_names.csv')
csv=df[['Name','Hex','R','G','B']]

def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"Name"]
    return cname

def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
       
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)
img=cv2.resize(img,(960,540))
prev="Text"
count=1

while(1):
    
    cv2.imshow("image",img)
    if (clicked):
   
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        col=getColorName(r,g,b)
        if(col!=prev):
            print(str(count)+" "+col)
            count=count+1
            prev=col
        
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False
 
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()
