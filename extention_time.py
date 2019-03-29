import os

def get_txt_mdate():
    for file in os.listdir('C:\\Users\\wunde\\OneDrive\\Desktop\\Bootcamp Projects\\Python Projects\\The-Tech-Academy-Basic-Python-Projects\\A'): #searches files in dir
        if file.endswith('.txt'): #makes sure they are .txt files
            txtList = os.path.join('C:\\Users\\wunde\\OneDrive\\Desktop\\Bootcamp Projects\\Python Projects\\The-Tech-Academy-Basic-Python-Projects\\A', file) #concatenates for absolute path
            txtTime = os.path.getctime('C:\\Users\\wunde\\OneDrive\\Desktop\\Bootcamp Projects\\Python Projects\\The-Tech-Academy-Basic-Python-Projects\\A') #gets mdate for txt files
            print("\n{} | {}".format(txtList,txtTime)) #prints only txt files w/ absolute path and mdate


            
if __name__ == '__main__':
    get_txt_mdate()







