import tkinter
from tkinter import filedialog
from PIL import Image



def get_img():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    orig_image = Image.open(file_path)
    watermark = Image.open("WATER MARK.png")

    width, height = orig_image.size
    watermark = watermark.resize(size=(width // 5, height // 5))

    position = (width - watermark.width, height - watermark.height)

    orig_image.paste(watermark, position, mask=watermark)

    orig_image.save("Watermarked.png")
    orig_image.show()



custom_font = ("Helvetica", 21, "bold")
custom_font_for_text = ("Helvetica", 14)

tk = tkinter.Tk()
tk.geometry("480x280")

container = tkinter.Canvas(tk, width=400, height=400)
container.grid(row=0, column=0, pady=40, padx=60)

name = tkinter.Label(container, text="WATER\nMARK  ", font=custom_font, anchor="e")
name.grid(row=0, column=0, sticky="w")

label = tkinter.Label(container, text="Choose image and get custom watermark", font=custom_font_for_text, pady=20)
label.grid(row=1, column=0, columnspan=2, sticky="w")

btn1 = tkinter.Button(container, text=" Choose image to open ", font=custom_font_for_text,
                      background="#1e1e1e", borderwidth=0, fg="white", command=get_img)
btn1.grid(row=3, column=0, columnspan=2, sticky="w")
tk.mainloop()
