# import required classes
import main 
from PIL import Image, ImageDraw, ImageFont
 

# importing the dict from main
# print(main.dict1)






# create Image object with the input image
 
image = Image.open('joiker.jpg')
draw = ImageDraw.Draw(image)
font1 = ImageFont.truetype("arial.ttf",35)


points1 =350,220
string1 = ""
# string1 = "222"

points2 =180,860
string2 = ""
# string2 = "555"


points3 =180,350
string3 = ""
# string3 = "333"

points4 =350,600
string4 = ""
# string4 = "444"


points5 =350,1010
string5 = ""
# string5 = "666"


points6 =600,350
string6 = ""
# string6 = "001"


points7 =600,860
string7 = ""
# string7 = "777"


points8 =840,220
string8 = ""
# string8 = "122"


points9 = 840,600
string9 = ""
# string9 = "100"


points10 =840,1010
string10= ""
# string10= "888"


points11 =1010,350
string11 = ""
# string11 = "111"


points12 =1010,860
string12 = ""
# string12 = "999"


# using for in a loop
for x in main.dict1:
  if(main.dict1.get(x) == "12th House"):
      string12+=x+'\n'
  elif(main.dict1.get(x) == "11th House"):
      string11+=x + '\n' 
  elif(main.dict1.get(x) == "10th House"):
      string10+= x+ '\n'
  elif(main.dict1.get(x) == "9th House"):
      string9+= x+ '\n'
  elif(main.dict1.get(x) == "8th House"):
      string8+= x+ '\n'
  elif(main.dict1.get(x) == "7th House"):
      string7+= x+ '\n'
  elif(main.dict1.get(x) == "6th House"):
      string6+= x+ '\n'
  elif(main.dict1.get(x) == "5th House"):
      string5+= x+ '\n'
  elif(main.dict1.get(x) == "4th House"):
      string4+= x+ '\n'
  elif(main.dict1.get(x) == "3rd House"):
      string3+= x+ '\n'
  elif(main.dict1.get(x) == "2nd House"):
      string2+= x+ '\n'
  elif(main.dict1.get(x) == "1st House"):
      string1+= x+ '\n'
      
  print(x+" "+main.dict1.get(x))
  


 
draw.text(points1,string1,"red",font=font1)


# draw.text(points2,string2,"red")
draw.text(points2,string2,"red",font=font1)


# draw.text(points3,string3,"red")
draw.text(points3,string3,"red",font=font1)

# draw.text(points4,string4,"red")
draw.text(points4,string4,"red",font=font1)

# draw.text(points5,string5,"red")
draw.text(points5,string5,"red",font=font1)

# draw.text(points6,string6,"red")
draw.text(points6,string6,"red",font=font1)

# draw.text(points7,string7,"red")
draw.text(points7,string7,"red",font=font1)

# draw.text(points8,string8,"red")
draw.text(points8,string8,"red",font=font1)

# draw.text(points9,string9,"red")
draw.text(points9,string9,"red",font=font1)

# draw.text(points10,string10,"red")
draw.text(points10,string10,"red",font=font1)

# draw.text(points11,string11,"red")
draw.text(points11,string11,"red",font=font1)

# draw.text(points12,string12,"red")
draw.text(points12,string12,"red",font=font1)





image.show()
# draw = ImageDraw.Draw(image)
