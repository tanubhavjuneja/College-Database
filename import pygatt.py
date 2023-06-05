import customtkinter
import webbrowser
import pyperclip
from PIL import Image
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
label_list = (
    ["B.Sc. (Honours) Computer Science",
     ["Tanubhav Juneja","2022CSC1008","+91 7827139401","tanubhavjuneja"],
     ["Gurleve Singh","2022CSC1046","+91 9315687808","__khalsa_ji"]],
    ["B.Sc. (Honours) Chemistry","BSCC101"],
    ["B.Sc. (Honours) Botany","BSCB101"],
    ["B.Sc. (Honours) Electronic Science","BSES101"],
    ["B.Sc. (Honours) Life Science","BSLS101"],
    ["B.Sc. (Honours) Mathematics","BSMA101"],
    ["B.Sc. (Honours) Physical Science","BSPS101"],
    ["B.Sc. (Honours) Physics","BSPH101"],
    ["B.Sc. (Honours) Zoology","BSZL101"],
    ["B.Com. Programme","BCOM101"],
    ["B.Com. (Honours)","BCOH101"],
    ["B.A. (Honours) Business Economics","BABE101"],
    ["B.A. (Honours) Economics","BAEC101"],
    ["B.A. (Honours) English","BAEN101"],
    ["B.A. (Honours) Hindi","BAHI101"],
    ["B.A. (Honours) Punjabi","BAPU101"],
    ["B.A. (Honours) Political Science","BAPS101"],
    ["B.A. (Honours) Humanities and Social Sciences","BAHS101"],
    ["B.A. (Honours) History","BAHI101"]
)
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range=RANGE_NAME).execute()
values = result.get('values', [])
def create_new_window(sub_list):
    global app,i,j,label_list
    app.destroy()
    i=label_list.index(sub_list)
    app = customtkinter.CTk()
    app.geometry("1500x800+210+100")
    frame = customtkinter.CTkScrollableFrame(app,width=1400,height=790)
    frame.pack(fill="both")
    for j in range(1,len(sub_list)):
        label = customtkinter.CTkLabel(frame, text=sub_list[j][0],bg_color="gray17",width=225,height=110,fg_color="gray10", corner_radius=30)
        label.grid(row=(j-1)//6, column=(j-1)%6, padx=10, pady=10)
        label.bind("<Button-1>", lambda event, sub_list1=sub_list[j]: create_new_window1(sub_list1))
    app.mainloop()
def create_new_window1(sub_list1):
    global app,i,j
    app.destroy()
    app = customtkinter.CTk()
    app.geometry("500x240+710+300")
    frame = customtkinter.CTkFrame(app)
    frame.pack(fill="both")
    img = Image.open("C:/Users/Tanubhav Juneja/Desktop/projects/icons/instagram.png")
    img1 = Image.open("C:/Users/Tanubhav Juneja/Desktop/projects/icons/Whatsapp.png")
    ctk_img = customtkinter.CTkImage(img, size=(20, 20))
    ctk_img1 = customtkinter.CTkImage(img1, size=(20, 20))
    name_label = customtkinter.CTkLabel(frame,text=sub_list1[0],bg_color="gray17",width=230,height=100,fg_color="gray10", corner_radius=30)
    name_label.grid(row=(0)//2, column=(0)%2, padx=10, pady=10)
    name_label.bind("<Button-1>", lambda event, function=2,info=sub_list1[1]: do_function(function,info))
    roll_label = customtkinter.CTkLabel(frame,text=sub_list1[1],bg_color="gray17",width=230,height=100,fg_color="gray10", corner_radius=30)
    roll_label.grid(row=(1)//2, column=(1)%2, padx=10, pady=10)
    whatsapp_label = customtkinter.CTkLabel(frame, image=ctk_img1,text="   "+sub_list1[2],bg_color="gray17",width=230,height=100,fg_color="gray10", corner_radius=30,compound="left")
    whatsapp_label.grid(row=(2)//2, column=(2)%2, padx=10, pady=10)
    whatsapp_label.bind("<Button-1>", lambda event, function=0,info=sub_list1[2]: do_function(function,info))
    instagram_label = customtkinter.CTkLabel(frame, image=ctk_img,text="   "+sub_list1[3],bg_color="gray17",width=230,height=100,fg_color="gray10", corner_radius=30,compound="left")
    instagram_label.grid(row=(3)//2, column=(3)%2, padx=10, pady=10)
    instagram_label.bind("<Button-1>", lambda event, function=1,info=sub_list1[3]: do_function(function,info))
    app.mainloop()
def do_function(function,info):
    global label_list,i,j
    if function == 1:
        pyperclip.copy(info)
        profile_url="https://www.instagram.com/"+info+"/"
        webbrowser.open(profile_url)
    elif function == 0:
        pyperclip.copy(info)
        text = "Hello"
        url = f"whatsapp://send?phone={info}"
        webbrowser.open(url)
    elif function == 2:
        sub_list=label_list[i]
        create_new_window(sub_list)
def start():
    global app,label_list,i,j
    app = customtkinter.CTk()
    app.geometry("1500x800+210+100")
    frame = customtkinter.CTkFrame(app)
    frame.pack(fill="both")
    for i in range(len(label_list)):
        label = customtkinter.CTkLabel(frame, text=label_list[i][0],bg_color="gray17",width=480,height=94,fg_color="gray10", corner_radius=30)
        label.grid(row=i//3, column=i%3, padx=10, pady=10)
        label.bind("<Button-1>", lambda event, sub_list=label_list[i]: create_new_window(sub_list))
    app.mainloop()
start()