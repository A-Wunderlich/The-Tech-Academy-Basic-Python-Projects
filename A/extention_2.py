import os


def get_txt_mdate():
    cwd = str(os.getcwd())#sets cwd to cwd and saves it as a string
    for file in os.listdir(cwd): #searches files in dir
        if file.endswith('.txt'): #makes sure they are .txt files
            txtList = os.path.join(cwd, file) #concatenates for absolute path
            txtTime = os.path.getctime(cwd) #gets mdate for txt files
            print("\n{} | {}".format(txtList,txtTime)) #prints only txt files w/ absolute path and mdate


            
if __name__ == '__main__':
    get_txt_mdate()
