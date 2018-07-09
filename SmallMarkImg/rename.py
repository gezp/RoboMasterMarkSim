#coding:utf8
import os;

def rename(path):
        i=0
        filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
        for files in filelist:#遍历所有文件
            
            Olddir=os.path.join(path,files);#原来的文件路径                
            if os.path.isdir(Olddir):#如果是文件夹则跳过
                    continue;
            filename=os.path.splitext(files)[0];#文件名
            filetype=os.path.splitext(files)[1];#文件扩展名
            Newdir=os.path.join(path,str(i)+filetype);#新的文件路径
            os.rename(Olddir,Newdir)#重命名
            i=i+1
rename("./2_")
rename("./3_")
rename("./4_")
rename("./5_")
rename("./6_")
rename("./7_")
rename("./8_")
rename("./9_")



