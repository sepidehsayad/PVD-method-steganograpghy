from PIL import Image
import math
host_image = Image.open('new_img.bmp','r') #open image 

pixel_value_hostimage = list(host_image.getdata())


def calculate_di(pixels_value):
    list_of_di=[]
    for i in range(0,len(pixels_value),2):
        list_of_di+=[abs(pixels_value[i]-pixels_value[i+1])]
    return list_of_di



def find_domain_in_quantity_table(list_of_di):
    uper_lower_bound=[]
    for i in list_of_di :

        if 0<=i<=7 :

            uper_lower_bound+=[0]

        elif 8<=i<=15 :
        
            uper_lower_bound+=[8]

        elif 16<=i<=31 :
             
            uper_lower_bound+=[16]
            
        elif 32 <= i <=63 :
           
            uper_lower_bound+=[32]
        elif  64 <= i <=127 :
            
            uper_lower_bound+=[64]
        elif 128 <= i <=255 :
              
             uper_lower_bound+=[128]
    return uper_lower_bound


def calculate(list_of_di,lower_bound):
    b=[]
    for i in range(len(list_of_di)):
        b+=[list_of_di[i]-lower_bound[i]]
        
    return b


def convert_dec_to_bin(b):
    bine=[]
    for i in b :
        bine+=[bin(i)[2:]]
    return bine
        

def show_new_picture(pixels):
    img = Image.new('L', (400,400))
    img.putdata(pixels)
    img.save("new__img.bmp")
    img.show()
    

di=calculate_di(pixel_value_hostimage)
#print(pixel_value_hostimage[-2])
lower_bound=find_domain_in_quantity_table(di)

z=calculate(di,lower_bound)

show_new_picture(z)
#print(z[0:40])
#q=convert_dec_to_bin(z)
#print(q[0:40])
