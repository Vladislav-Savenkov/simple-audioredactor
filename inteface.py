from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog

def CloseApp():
    root.destroy()
    print('На сегодня ты наредактировался, лох')

root = Tk()  # создаем корневой объект - окно
root.title("Аудиоредактор от Владоса Темщика и Вовки ХаХалка")  # устанавливаем заголовок окна
root.geometry("800x600+200+200")  # устанавливаем размеры окна
root.resizable(False, False)
root.iconbitmap(default='penis.ico')
root.protocol('WM_DELETE_WINDOW', CloseApp)

input_file_entry = Entry(width=50)
input_file_entry.place(x=15, y=15)
input_file_entry.insert(0, 'Путь к файлу')

def LoadAudioFile():
    #ВСТАВЬ СЮДА ХУЕТУ, ЧТОБЫ ФАЙЛ ГРУЗИЛО
    filepath = filedialog.askopenfilename()
    if filepath != "":
            text = filepath
            input_file_entry.delete("0", END)
            input_file_entry.insert("0", text)
    print('у тебя файл не грузит, дебила кусок')
    audio_image_panel.place(x=0, y = 40)

def VolumeChanged(new_volume):
    print('У тебя громкость не меняется, дебила запчасть')

def SpeedChanged(new_speed):
    print('У тебя скорость не меняется, ебала')

def ReplaceSelectedFragment():
    print('Еблан, у тебя фрагмент не удаляется!!!!ДЕБИЛОЙД')
def OpenReplaceWindow():
    replace_fragment_window = Tk()
    replace_fragment_window.title('Вырезка фрагмента')
    replace_fragment_window.geometry('300x200')

    text_lable = Label(replace_fragment_window, text='Выберите фрагмент')
    text_lable.place(x=90, y=15)

    from_entry = Entry(replace_fragment_window, width=10)
    from_entry.place(x=50, y=50)
    from_entry.insert(0, 'От')

    lable_from = Label(replace_fragment_window, text='->')
    lable_from.place(x=120, y=50)

    to_entry = Entry(replace_fragment_window, width=10)
    to_entry.place(x=150, y=50)
    to_entry.insert(0, 'До')

    confirm_button = Button(replace_fragment_window, text='Confirm', command=ReplaceSelectedFragment)
    confirm_button.place(x=120, y = 100)

def ReturnBackward():
    print('Долбоклюй, у тебя не возвращает изменения')

def ReturnForward():
    print('Совсем ящер? Еще и вперед не возвращает')

def FadeInFragment():
    print('У тебя не фейд инится')

def FadeOutFragment():
    print('У тебя не фейд аутится')

def ExportFile():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = input_file_entry.get(0, END)
        with open(filepath, "w") as file:
            file.write(text)
    print('У тебя не экспортируется, дятел')

load_input_file_btn = Button(text='Загрузить', command=LoadAudioFile)
load_input_file_btn.place(x=330, y=12)

export_file_button = Button(text='Экспортировать', command=ExportFile)
export_file_button.place(x=695, y=12)

audio_image = ImageTk.PhotoImage(Image.open('dorojka1.png').resize((800, 100), Image.BILINEAR))
audio_image_panel = Label(root, image = audio_image)


volume = StringVar(value="100")
volume_label = Label(text='Громкость')
volume_label.place(x=15, y = 130)
volume_entry = Entry(width=10, textvariable=volume)
volume_entry.place(x=15, y =150)

speed = StringVar(value='1')
speed_lable = Label(text='Скорость')
speed_lable.place(x=100, y=130)
speed_entry = Entry(width=10, textvariable=speed)
speed_entry.place(x=100, y=150)

replace_button = Button(text='Вырезать кусок', command=OpenReplaceWindow)
replace_button.place(x=40, y=180)

return_backward_button = Button(text='<=', command=ReturnBackward)
return_backward_button.place(x=420, y = 12)

return_forward_button = Button(text='=>', command=ReturnForward)
return_forward_button.place(x=460, y=12)

fragment_to_edit_lable = Label(text="Фрагмент:")
fragment_to_edit_lable.place(x=500, y = 15)

fragment_to_edit_from = StringVar(value='0')
fragment_to_edit_from_entry = Entry(width=7, textvariable=fragment_to_edit_from)
fragment_to_edit_from_entry.place(x = 565, y = 15)

fragment_to_edit_to_lable = Label(text="-->")
fragment_to_edit_to_lable.place(x=610, y = 15)

fragment_to_edit_to = StringVar(value='10^00')
fragment_to_edit_to_entry = Entry(width=7, textvariable=fragment_to_edit_to)
fragment_to_edit_to_entry.place(x = 640, y = 15)

fade_in_button = Button(text='fade in', command=FadeInFragment)
fade_in_button.place(x=200, y = 145)

fade_out_button = Button(text='fade out', command=FadeOutFragment)
fade_out_button.place(x=250, y = 145)

fade_in_out_value = IntVar(value='1.0')
fade_in_out_entry = Entry(width=10, textvariable=fade_in_out_value)
fade_in_out_entry.place(x=225, y = 180)

root.mainloop()
