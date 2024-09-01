import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter.ttk import Progressbar
from pkg_resources import resource_filename
import webbrowser
import random
import threading

icon_data = resource_filename(__name__, 'ColorRectForgecklogo.ico')

root = tk.Tk()
root.title("彩矩工坊")
root.iconbitmap(icon_data)
root.resizable(False, False)

def main():
    def generate_image():
        fw_R_start = int(slider_R_start.get())
        fw_R_end = int(slider_R_end.get())
        if fw_R_start > fw_R_end:
            messagebox.showwarning("警告", "R值错误")
            return 0
        
        fw_G_start = int(slider_G_start.get())
        fw_G_end = int(slider_G_end.get())
        if fw_G_start > fw_G_end:
            messagebox.showwarning("警告", "G值错误")
            return 0
        
        fw_B_start = int(slider_B_start.get())
        fw_B_end = int(slider_B_end.get())
        if fw_B_start > fw_B_end:
            messagebox.showwarning("警告", "B值错误")
            return 0
        
        fw_X_start = int(slider_X_start.get())
        fw_X_end = int(slider_X_end.get())
        if fw_X_start > fw_X_end:
            messagebox.showwarning("警告", "方块X值错误")
            return 0
        
        fw_Y_start = int(slider_Y_start.get())
        fw_Y_end = int(slider_Y_end.get())
        if fw_Y_start > fw_Y_end:
            messagebox.showwarning("警告", "方块Y值错误")
            return 0
        
        progress_window = tk.Toplevel(root)
        progress_window.iconbitmap(icon_data)
        progress_window.title("生成进度")
        progress_window.geometry("+{}+{}".format(
            root.winfo_rootx() + (root.winfo_width() // 2) - 150,
            root.winfo_rooty() + (root.winfo_height() // 2) - 50
        ))
        progress_window.transient(root)
        progress_window.grab_set()
        progress_window.protocol("WM_DELETE_WINDOW", lambda: None)  # 禁止关闭窗口
        progress_bar = Progressbar(progress_window, orient="horizontal", length=300, mode="determinate")
        progress_bar.pack(pady=10, padx=10)
        progress_window.update_idletasks()
        
        x = int(slider_QT_DX_X.get())
        y = int(slider_QT_DX_Y.get())
        bg = Image.new("RGB", (x+200, y+200), "#FFFFFF")

        def sjxs():
            hex_r = hex(random.randint(fw_R_start, fw_R_end))[2:].upper()
            hex_g = hex(random.randint(fw_G_start, fw_G_end))[2:].upper()
            hex_b = hex(random.randint(fw_B_start, fw_B_end))[2:].upper()
            hex_r0 = hex_r.zfill(2)
            hex_g0 = hex_g.zfill(2)
            hex_b0 = hex_b.zfill(2)
            return "#" + str(hex_r0) + str(hex_g0) + str(hex_b0)

        num_blocks = int(slider_SL.get())
        for i in range(num_blocks):
            tp = Image.new("RGB", (1, 1), sjxs())
            tp = tp.resize((random.randint(fw_X_start, fw_X_end), random.randint(fw_Y_start, fw_Y_end)))
            bg.paste(tp, (random.randint(0, x+200), random.randint(0, y+200)))
            progress_bar['value'] = (i + 1) * 100 / num_blocks
            progress_window.update_idletasks()

        cropped_bg = bg.crop((100, 100, x+100, y+100))

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            cropped_bg.save(file_path)
            messagebox.showinfo("完成", "图片生成完成！")
        else:
            messagebox.showwarning("警告", "保存操作被取消")

        progress_window.destroy()
        root.grab_release()

    root.grab_set()
    threading.Thread(target=generate_image).start()

def slider_changed(value, label):
    int_value = round(float(value))
    label.config(text=str(int_value))

label_frame_FK = ttk.LabelFrame(root, text="方块设置", labelanchor='n')
label_frame_FK.grid(row=0, column=0)

label_frame_RGB = ttk.LabelFrame(label_frame_FK, text="颜色取值范围", labelanchor='n')
label_frame_RGB.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_frame_R = ttk.LabelFrame(label_frame_RGB, text="R值范围", labelanchor='n')
label_frame_R.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_R_start = tk.Label(label_frame_R, text="开始：")
label_R_start.grid(row=0, column=0)
slider_R_start = ttk.Scale(label_frame_R, from_=0, to=255, orient=tk.HORIZONTAL, value=25, command=lambda v: slider_changed(v, label_value_R_start))
slider_R_start.grid(row=0, column=1)
label_value_R_start = tk.Label(label_frame_R, text="25")
label_value_R_start.grid(row=0, column=2)

label_R_end = tk.Label(label_frame_R, text="结束：")
label_R_end.grid(row=1, column=0)
slider_R_end = ttk.Scale(label_frame_R, from_=0, to=255, orient=tk.HORIZONTAL, value=175, command=lambda v: slider_changed(v, label_value_R_end))
slider_R_end.grid(row=1, column=1)
label_value_R_end = tk.Label(label_frame_R, text="175")
label_value_R_end.grid(row=1, column=2)

label_frame_G = ttk.LabelFrame(label_frame_RGB, text="G值范围", labelanchor='n')
label_frame_G.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_G_start = tk.Label(label_frame_G, text="开始：")
label_G_start.grid(row=0, column=0)
slider_G_start = ttk.Scale(label_frame_G, from_=0, to=255, orient=tk.HORIZONTAL, value=50, command=lambda v: slider_changed(v, label_value_G_start))
slider_G_start.grid(row=0, column=1)
label_value_G_start = tk.Label(label_frame_G, text="50")
label_value_G_start.grid(row=0, column=2)

label_G_end = tk.Label(label_frame_G, text="结束：")
label_G_end.grid(row=1, column=0)
slider_G_end = ttk.Scale(label_frame_G, from_=0, to=255, orient=tk.HORIZONTAL, value=200, command=lambda v: slider_changed(v, label_value_G_end))
slider_G_end.grid(row=1, column=1)
label_value_G_end = tk.Label(label_frame_G, text="200")
label_value_G_end.grid(row=1, column=2)

label_frame_B = ttk.LabelFrame(label_frame_RGB, text="B值范围", labelanchor='n')
label_frame_B.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_B_start = tk.Label(label_frame_B, text="开始：")
label_B_start.grid(row=0, column=0)
slider_B_start = ttk.Scale(label_frame_B, from_=0, to=255, orient=tk.HORIZONTAL, value=75, command=lambda v: slider_changed(v, label_value_B_start))
slider_B_start.grid(row=0, column=1)
label_value_B_start = tk.Label(label_frame_B, text="75")
label_value_B_start.grid(row=0, column=2)

label_B_end = tk.Label(label_frame_B, text="结束：")
label_B_end.grid(row=1, column=0)
slider_B_end = ttk.Scale(label_frame_B, from_=0, to=255, orient=tk.HORIZONTAL, value=225, command=lambda v: slider_changed(v, label_value_B_end))
slider_B_end.grid(row=1, column=1)
label_value_B_end = tk.Label(label_frame_B, text="225")
label_value_B_end.grid(row=1, column=2)

label_frame_CC = ttk.LabelFrame(label_frame_FK, text="尺寸取值范围", labelanchor='n')
label_frame_CC.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_frame_FK_X = ttk.LabelFrame(label_frame_CC, text="X值范围", labelanchor='n')
label_frame_FK_X.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_X_start = tk.Label(label_frame_FK_X, text="开始：")
label_X_start.grid(row=0, column=0)
slider_X_start = ttk.Scale(label_frame_FK_X, from_=10, to=999, orient=tk.HORIZONTAL, value=10, command=lambda v: slider_changed(v, label_value_X_start))
slider_X_start.grid(row=0, column=1)
label_value_X_start = tk.Label(label_frame_FK_X, text="10")
label_value_X_start.grid(row=0, column=2)

label_X_end = tk.Label(label_frame_FK_X, text="结束：")
label_X_end.grid(row=1, column=0)
slider_X_end = ttk.Scale(label_frame_FK_X, from_=10, to=999, orient=tk.HORIZONTAL, value=100, command=lambda v: slider_changed(v, label_value_X_end))
slider_X_end.grid(row=1, column=1)
label_value_X_end = tk.Label(label_frame_FK_X, text="100")
label_value_X_end.grid(row=1, column=2)

label_frame_FK_Y = ttk.LabelFrame(label_frame_CC, text="Y值范围", labelanchor='n')
label_frame_FK_Y.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_Y_start = tk.Label(label_frame_FK_Y, text="开始：")
label_Y_start.grid(row=0, column=0)
slider_Y_start = ttk.Scale(label_frame_FK_Y, from_=10, to=999, orient=tk.HORIZONTAL, value=10, command=lambda v: slider_changed(v, label_value_Y_start))
slider_Y_start.grid(row=0, column=1)
label_value_Y_start = tk.Label(label_frame_FK_Y, text="10")
label_value_Y_start.grid(row=0, column=2)

label_Y_end = tk.Label(label_frame_FK_Y, text="结束：")
label_Y_end.grid(row=1, column=0)
slider_Y_end = ttk.Scale(label_frame_FK_Y, from_=10, to=999, orient=tk.HORIZONTAL, value=100, command=lambda v: slider_changed(v, label_value_Y_end))
slider_Y_end.grid(row=1, column=1)
label_value_Y_end = tk.Label(label_frame_FK_Y, text="100")
label_value_Y_end.grid(row=1, column=2)

label_frame_QT = ttk.LabelFrame(root, text="其他设置", labelanchor='n')
label_frame_QT.grid(row=1, column=0)

label_frame_DX = ttk.LabelFrame(label_frame_QT, text="图片大小", labelanchor='n')
label_frame_DX.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_QT_DX_X = tk.Label(label_frame_DX, text="图片长：")
label_QT_DX_X.grid(row=0, column=0)
slider_QT_DX_X = ttk.Scale(label_frame_DX, from_=100, to=3840, orient=tk.HORIZONTAL, value=1920, command=lambda v: slider_changed(v, label_value_QT_DX_X))
slider_QT_DX_X.grid(row=0, column=1)
label_value_QT_DX_X = tk.Label(label_frame_DX, text="1920")
label_value_QT_DX_X.grid(row=0, column=2)

label_QT_DX_Y = tk.Label(label_frame_DX, text="图片宽：")
label_QT_DX_Y.grid(row=1, column=0)
slider_QT_DX_Y = ttk.Scale(label_frame_DX, from_=100, to=2160, orient=tk.HORIZONTAL, value=1080, command=lambda v: slider_changed(v, label_value_QT_DX_Y))
slider_QT_DX_Y.grid(row=1, column=1)
label_value_QT_DX_Y = tk.Label(label_frame_DX, text="1080")
label_value_QT_DX_Y.grid(row=1, column=2)

label_frame_SL = ttk.LabelFrame(label_frame_QT, text="方块", labelanchor='n')
label_frame_SL.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_SL = tk.Label(label_frame_SL, text="数量：")
label_SL.grid(row=0, column=0)
slider_SL = ttk.Scale(label_frame_SL, from_=100, to=999999, orient=tk.HORIZONTAL, value=37500, command=lambda v: slider_changed(v, label_value_SL))
slider_SL.grid(row=0, column=1)
label_value_SL = tk.Label(label_frame_SL, text="37500")
label_value_SL.grid(row=0, column=2)

button_QD = ttk.Button(root, text="确定", command=main)
button_QD.grid(row=2, column=0, sticky='nsew')

def create_copyright_window():
    # 创建版权信息窗口
    copyright_window = tk.Toplevel(root)
    # 设置窗口图标 (请确保icon_data包含有效的图标路径)
    copyright_window.iconbitmap(icon_data)
    copyright_window.title("关于")
    # 设置窗口居中
    copyright_window.geometry("+{}+{}".format(
        root.winfo_rootx() + (root.winfo_width() // 2) - 115,
        root.winfo_rooty() + (root.winfo_height() // 2) - 100
    ))
    copyright_window.transient(root)
    copyright_window.grab_set()

    # 创建一个框架来放置控件
    frame = ttk.Frame(copyright_window, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # 中文名字
    chinese_name = ttk.Label(frame, text="彩矩工坊普通版", font=("Arial", 18, "bold"), foreground="black")
    chinese_name.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # 英文名字
    english_name = ttk.Label(frame, text="ColorRectForge", font=("Arial", 14,), foreground="black")
    english_name.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # 创建超链接样式的标签
    style = ttk.Style()
    style.configure("TLabel", foreground="blue", cursor="hand2")

    # 官网链接
    website_label = ttk.Label(frame, text="ColorRectForge.080207.xyz", style="TLabel")
    website_label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    website_label.bind("<Button-1>", lambda e: webbrowser.open("https://ColorRectForge.080207.xyz"))

    # 个人博客链接
    blog_label = ttk.Label(frame, text="www.080207.xyz", style="TLabel")
    blog_label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    blog_label.bind("<Button-1>", lambda e: webbrowser.open("https://www.080207.xyz/"))

    # 帮助按钮
    help_button = ttk.Button(frame, text="帮助",)
    help_button.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    help_button.bind("<Button-1>", lambda e: webbrowser.open("https://ColorRectForge.080207.xyz/help"))
    
    # 帮助按钮
    help_button = ttk.Button(frame, text="联系作者",)
    help_button.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    help_button.bind("<Button-1>", lambda e: webbrowser.open("mailto:m240l@outlook.com"))

button_GY = ttk.Button(root, text="关于", command=create_copyright_window)
button_GY.grid(row=3, column=0, sticky='nsew')

root.mainloop()

# pyinstaller --onefile --noconsole --icon=logo.ico --add-data "ColorRectForgecklogo.ico;." ColorRectForge.py