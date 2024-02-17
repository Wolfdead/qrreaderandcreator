import tkinter
import segno
import os
import cv2
from pyzbar.pyzbar import decode
Window = tkinter.Tk()
Window.minsize(width=300, height=300)
Window.title("QR Code Reader and Creator")
Window.configure(bg="black")

#başlık
my_label = tkinter.Label(text="QR Code Reader and Creator" , font = ("normal" , 24 ,"bold"))
my_label.config(bg="black" ,
                fg="red")
my_label.pack()



def QrCodeCreator_button():
    global Window
    Window_QrCodeCreator1 = tkinter.Tk()
    Window_QrCodeCreator1.title("Qr Code Creator")
    Window_QrCodeCreator1.geometry("300x200")
    Window_QrCodeCreator1.configure(background="black")
    qrcreator_entry = tkinter.Entry(Window_QrCodeCreator1 , width= 100)
    qrcreator_entry.pack()
    qrcreator_button1 = tkinter.Button(Window_QrCodeCreator1 , text="Micro Qr Code Creator" , command=lambda :QrCodeCreatorMicro(qrcreator_entry.get()), bg="black" , fg="red")
    qrcreator_button2 = tkinter.Button(Window_QrCodeCreator1 , text="Normal Qr Code" , command=lambda :QrCodeCreatorNormal(qrcreator_entry.get()) , bg="black" , fg="red")
    qrcreator_button1.place(x = 0, y = 80 ,width = 150, height = 50 )
    qrcreator_button2.place(x=150, y = 80 ,width = 150, height = 50 )
    Window.destroy()

def QrCodeReader_button():
    Window_QrCodeReader1 = tkinter.Tk()
    Window_QrCodeReader1.title("Qr Code Creator")
    Window_QrCodeReader1.geometry("800x600")
    qrreader_button = tkinter.Button(Window_QrCodeReader1 , text="Qr Code Reader" , command=QrCodeReader)
    qrreader_button.pack()



def QrCodeCreatorMicro(content):
    qrcode_micro = segno.make_micro(content)
    qrcode_micro.save("qrcode_micro.png")
    os.startfile("qrcode_micro.png")

def QrCodeCreatorNormal(content):
    qrcode_normal = segno.make( content , micro=False )
    qrcode_normal.save("qrcode_normal.png")
    os.startfile("qrcode_normal.png")


def QrCodeReader():
    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        decoded_objects = decode(frame)

        for obj in decoded_objects:
            print(f'Tür: {obj.type}, Veri: {obj.data.decode("utf-8")}')

            points = obj.polygon
            if len(points) == 4:
                cv2.polylines(frame, [points], isClosed=True, color=(0, 255, 0), thickness=2)

        cv2.imshow("QR Kod Okuyucu", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

#ilk button
firs_button = tkinter.Button(text = "Qr Code Reader" , command =QrCodeReader )
firs_button.place(x = 0, y = 150 , width = 97*2, height =52)
firs_button.config(bg="black" , fg="red")




#ikinci button
second_button = tkinter.Button(text = "Qr Code Creator" , command = QrCodeCreator_button)
second_button.place(x = 253 , y= 150 , width = 97*2, height =52 )
second_button.config(bg="black" , fg="red")




Window.mainloop()



