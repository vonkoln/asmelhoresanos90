import os

caminho = r"C:\dev\alea\files"
os.chdir(caminho)

for f in os.listdir():
   f_name, f_ext = os.path.splitext(f)


   f_name = f_name.replace(' ','')
   
   new_name = f_name

   os.rename(f, new_name)