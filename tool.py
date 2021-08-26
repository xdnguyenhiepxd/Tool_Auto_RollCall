from selenium import webdriver
from tkinter import *
import  time
with open('data.txt','a') as fl:
    pass
with open('data.txt','r') as fl:
            tentk=fl.readline().rstrip("\n")
            matkhau=fl.readline().rstrip("\n")
cal=Tk()
cal.title("Tool web")
masv=Label(text='Mã sv')
masv.pack()
text_masv=StringVar()
txt_masv=Entry(cal,width=30,font=('arial',20,'bold'),textvariable=text_masv,bd=30,insertwidth=4,bg='aqua',justify='right')
txt_masv.pack()
mk=Label(text='Mật khẩu')
mk.pack()
text_mk=StringVar()
txt_mk=Entry(cal,width=30,font=('arial',20,'bold'),textvariable=text_mk,bd=30,insertwidth=4,bg='aqua',justify='right')
txt_mk.pack()
if tentk!='':
    text_masv.set(tentk)
    text_mk.set(matkhau)
def pri():
    tk = txt_masv.get()
    pw = txt_mk.get()
    if tentk=='':
        with open("data.txt",'w') as file:
            file.write(tk+"\n")
            file.write(pw+"\n")
    a = webdriver.Chrome('chromedriver.exe')
    a.get('http://sinhvien.epu.edu.vn/')
    a.find_element_by_name('ctl00$ucRight1$txtMaSV').send_keys(tk)
    a.find_element_by_name('ctl00$ucRight1$txtMatKhau').send_keys(pw)
    time.sleep(10)
    d = a.find_elements_by_tag_name('center')
    if len(d) > 0:
        for i in range(int(len(d) / 2)):
            a.execute_script("document.getElementById('tblPhieuKhaoSat').getElementsByTagName('tbody')[0].getElementsByTagName('tr')[1].getElementsByTagName('a')[0].click();\
            document.getElementById('chiTietPhieuKhaoSat').getElementsByTagName('input')[4].click();\
            document.getElementById('chiTietPhieuKhaoSat').getElementsByTagName('input')[6].click();\
            document.getElementById('chiTietPhieuKhaoSat').getElementsByTagName('input')[7].click();\
            LuuPhieuKhaoSat();")
            time.sleep(1)
button=Button(cal,text='Run',width=20,height=3,bg='#34A2FE',command=pri)
button.pack()
cal.mainloop()
