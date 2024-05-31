#earn mon
import qrcode, os,tempfile
import tkinter as tk
from PIL import Image, ImageTk

text = "TUYFGwExAe1TcbwkbMiXXmRZWkvUPGQBri"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(text)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
file_path = os.path.join(os.environ['USERPROFILE'],"qrcode.png")
if not os.path.isfile(file_path):
    img.save(file_path)
root = tk.Tk()
root.title("Deposit! TRC-20 (150$)")
image = Image.open(file_path)
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.pack()
root.mainloop()
