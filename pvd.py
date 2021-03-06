from PIL import Image
import math

host_image = Image.open('baboon512.bmp','r') #open image
secret_image = Image.open('boat256.bmp','r') #open image

pixel_value_hostimage = list(host_image.getdata()) #we have pixels in this list

pix_val_secret=list(secret_image.getdata())
#print(pix_val_secret[0:30])
def pixel_value(list_of_values): #RGB(R,G,B) in gray scale = RGB(X,X,X) so one of them is enough
    pixel_val=[]
    for i in list_of_values:
        pixel_val+=[i[0]]
    return pixel_val

def calculate_di(pixels_value):
    list_of_di=[]
    for i in range(0,len(pixels_value),2):
        list_of_di+=[abs(pixels_value[i]-pixels_value[i+1])]
    return list_of_di


def find_domain_in_quantity_table(list_of_di):
    uper_lower_bound=[]
    for i in list_of_di :
        if 0<=i<=7 :
            m = int(math.log2(7)) #int -> lower bound
            uper_lower_bound+=[[0,7,m]]
        elif 8<=i<=15 :
            m = int(math.log2(7)) 
            uper_lower_bound+=[[8,15,m]]
        elif 16<=i<=31 :
            m = int(math.log2(15)) 
            uper_lower_bound+=[[16,31,m]]
        elif 32 <= i <=63 :
            m = int(math.log2(31))
            uper_lower_bound+=[[32,63,m]]
        elif  64 <= i <=127 :
            m =int(math.log2(63)) 
            uper_lower_bound+=[[64,127,m]]
        elif 128 <= i <=255 :
             m = int(math.log2(127)) 
             uper_lower_bound+=[[128,255,m]]
    return uper_lower_bound

def list_of_secret_data(file):#all the scret data in the one string 
        with open("secretdata.txt", "r") as ins:
            array = []
            for line in ins:
                array.append(line.rstrip('\n'))
        my_lst_str = ''.join(map(str,array))
        return my_lst_str    

def spilit_k_secret_data(string_of_secret_data,lowerbound_and_k_slice):
    list_of_k_secret_data=[]
    for i in lowerbound_and_k_slice:
        if string_of_secret_data=='' or list_of_k_secret_data==[] :
            return list_of_k_secret_data
        else :
            temp= i[2] #how much we want to slice
            #print(temp)
            list_of_k_secret_data +=[string_of_secret_data[0:temp]]
            
            string_of_secret_data =string_of_secret_data[temp:]

    return list_of_k_secret_data
            
        
def convert_secret_data_to_decimal(secret_data_k_slice_k_slice):
    decimal_secret_data_k_slices=[]
    for i in secret_data_k_slice_k_slice :
        z=int(i,2)
        decimal_secret_data_k_slices += [z]
    return decimal_secret_data_k_slices


def calculate_new_di(find_domain_in_quantity_table_and_lowerbound,convert_secret_data_decimal,difrense_2pixels):
    new_di=[]
    for i in range(len(convert_secret_data_decimal)) :
       new_di+=[find_domain_in_quantity_table_and_lowerbound[i][0]+convert_secret_data_decimal[i]]
        #print(find_domain_in_quantity_table_and_lowerbound[i][0])
       if find_domain_in_quantity_table_and_lowerbound[i][0]<= new_di[i] <= find_domain_in_quantity_table_and_lowerbound[i][1] and find_domain_in_quantity_table_and_lowerbound[i][0]<= difrense_2pixels[i] <=find_domain_in_quantity_table_and_lowerbound[i][1]:
          continue
    return new_di
            

def cal_new_val_of_pixels(pixel_value,new_di,difrense_2pixels):
    new_pixels=[]
    j=0
    for i in range(len(new_di)): 
        if pixel_value[j] >= pixel_value[j+1] and new_di[i]>difrense_2pixels[i] :
            new_pixels += [(pixel_value[j]+(int(abs(new_di[i]-difrense_2pixels[i])/2)+1)) ,(pixel_value[j+1]-int(abs(new_di[i]-difrense_2pixels[i])/2))]
            j+=2
        elif pixel_value[j] < pixel_value[j+1] and new_di[i]>difrense_2pixels[i] :
            new_pixels += [(pixel_value[j]-(int(abs(new_di[i]-difrense_2pixels[i])/2))) ,(pixel_value[j+1]+int(abs(new_di[i]-difrense_2pixels[i])/2)+1)]        
            j+=2
        elif pixel_value[j] >= pixel_value[j+1] and new_di[i] <= difrense_2pixels[i] :
            new_pixels += [(pixel_value[j]-(int(abs(new_di[i]-difrense_2pixels[i])/2)+1)),(pixel_value[j+1]+int(abs(new_di[i]-difrense_2pixels[i])/2))]
            j+=2
        elif pixel_value[j] < pixel_value[j+1] and new_di[i] <= difrense_2pixels[i] :
            new_pixels += [(pixel_value[j]+(int(abs(new_di[i]-difrense_2pixels[i])/2)+1)) ,(pixel_value[j+1]-int(abs(new_di[i]-difrense_2pixels[i])/2))]
            j+=2
    for k in range(j,len(pixel_values),2):
        new_pixels+=[pixel_values[k],pixel_values[k+1]]
    
    return  new_pixels


def convert_pixelvalue_to_binary(pixel_val):
    binary_of_pixel_value=[]
    for i in pixel_val:
        binary_of_pixel_value+=['{0:08b}'.format(i)]

    return binary_of_pixel_value

def show_new_picture(pixels):
    img = Image.new('L', (512, 512))
    img.putdata(pixels)
    img.save("new_img.bmp")
    img.show()



pixel_values=pixel_value(pixel_value_hostimage)
#print(pixel_value)
difrense_2pixels =calculate_di(pixel_values)

find_domain_in_quantity_table_and_lowerbound=find_domain_in_quantity_table(difrense_2pixels)
#print(find_domain_in_quantity_table_and_lowerbound[0:30])

##3tayi bayad iki bashe
pixel_value2=pixel_value(pix_val_secret)
#print(pixel_value2[0:30])
binary_pixel_values_secret= convert_pixelvalue_to_binary(pixel_value2)

#print(binary_pixel_values_secret[0:30])
pixel_val =[]
f_sec_pix='' 
for i in range(len(binary_pixel_values_secret)) :
    f_sec_pix +=binary_pixel_values_secret[i]


string_of_secret_data=f_sec_pix
#print("len: ",string_of_secret_data)
#print(string_of_secret_data)
secret_data_k_slice_k_slice = spilit_k_secret_data(string_of_secret_data,find_domain_in_quantity_table_and_lowerbound)
print(secret_data_k_slice_k_slice[0:30])
convert_secret_data_decimal=convert_secret_data_to_decimal(secret_data_k_slice_k_slice)

new_di=calculate_new_di(find_domain_in_quantity_table_and_lowerbound,convert_secret_data_decimal,difrense_2pixels)

pvd_pixels=cal_new_val_of_pixels(pixel_value,new_di,difrense_2pixels)


show_new_picture(pvd_pixels)

