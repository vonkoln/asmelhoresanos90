import os

caminho = r"C:\dev\alea\files"
os.chdir(caminho)

for f in os.listdir():
   f_name, f_ext = os.path.splitext(f)

#    f_erro, f_num, f_nome, f_autor = f_name.split('-')
   f_name = f_name.replace(' ','')
   
   new_name = f_name

   os.rename(f, new_name)



    # f'{f_nome}-{f_autor}{f_ext}'
    #   teste = os.path.splitext(f).replace(' ','')