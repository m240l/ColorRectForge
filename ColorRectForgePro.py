import re
import random
import pyperclip
import threading
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Progressbar
from pkg_resources import resource_filename
from PIL import Image, ImageTk, ImageSequence, ImageDraw, ImageFont

icon_data = resource_filename(__name__, 'ColorRectForgecklogo.ico')
image_TP = None

root = tk.Tk()
root.title("彩矩工坊专业版")
root.iconbitmap(icon_data)
root.resizable(False, False) 

def main():
    global image_TP
    # 获取当前选中的标签页的索引
    current_tab_index_RGB = tabControl_RGB.index(tabControl_RGB.select())
    print(current_tab_index_RGB)
    current_tab_index_CC = tabControl_CC.index(tabControl_CC.select())  #尺寸范围
    def generate_image():
        if int(current_tab_index_RGB) == 0 or int(current_tab_index_RGB) == 1:
            x = int(slider_QT_DX_X.get())
            y = int(slider_QT_DX_Y.get())
        elif int(current_tab_index_RGB) == 2:
            source_pixels = image_TP.load()
            x, y = image_TP.size
            
        bg = Image.new("RGB", (x+200, y+200), "#FFFFFF")

        num_blocks = int(slider_SL.get())
        def sjxs():
            if int(current_tab_index_RGB) == 0: # 普通
                hex_r = hex(random.randint(fw_R_start, fw_R_end))[2:].upper()
                hex_g = hex(random.randint(fw_G_start, fw_G_end))[2:].upper()
                hex_b = hex(random.randint(fw_B_start, fw_B_end))[2:].upper()
            elif int(current_tab_index_RGB) == 1: # 高级
                if current_tab_index_RGB_GJ == 0: # R为基准
                    random_R = random.randint(fw_R_start, fw_R_end)
                    hex_r = hex(random_R)[2:].upper()
                    if current_tab_index_RGB_GJ_R_G == 0: # G比例
                        hex_g = hex(int(float(random_R * BL_R_G)))[2:].upper()
                        if current_tab_index_RGB_GJ_R_B == 0: # B比例
                            hex_b = hex(int(float(random_R * BL_R_B)))[2:].upper()
                        elif current_tab_index_RGB_GJ_R_B == 1: # B增加
                            hex_b = hex(int(random_R + fw_R_B_ZJ))[2:].upper()
                        else:# B减少
                            hex_b = hex(int(random_R - fw_R_B_JS))[2:].upper()
                    elif current_tab_index_RGB_GJ_R_G == 1: # G增加
                        hex_g = hex(int(random_R + fw_R_G_ZJ))[2:].upper()
                        if current_tab_index_RGB_GJ_R_B == 0: # B比例
                            hex_b = hex(int(float(random_R * BL_R_B)))[2:].upper()
                        elif current_tab_index_RGB_GJ_R_B == 1: # B增加
                            hex_b = hex(int(random_R + fw_R_B_ZJ))[2:].upper()
                        else:# B减少
                            hex_b = hex(int(random_R - fw_R_B_JS))[2:].upper()
                    else:
                        hex_g = hex(int(random_R - fw_R_G_JS))[2:].upper()
                        if current_tab_index_RGB_GJ_R_B == 0: # B比例
                            hex_b = hex(int(float(random_R * BL_R_B)))[2:].upper()
                        elif current_tab_index_RGB_GJ_R_B == 1: # B增加
                            hex_b = hex(int(random_R + fw_R_B_ZJ))[2:].upper()
                        else:# B减少
                            hex_b = hex(int(random_R - fw_R_B_JS))[2:].upper()
                elif current_tab_index_RGB_GJ == 1: # G为基准
                    random_G = random.randint(fw_G_start, fw_G_end)
                    hex_g = hex(random_G)[2:].upper()
                    if current_tab_index_RGB_GJ_G_R == 0: # R比例
                        hex_r = hex(int(float(random_G * BL_G_R)))[2:].upper()
                        if current_tab_index_RGB_GJ_G_B == 0: # B比例
                            hex_b = hex(int(float(random_G * BL_G_B)))[2:].upper()
                        elif current_tab_index_RGB_GJ_G_B == 1: # B增加
                            hex_b = hex(int(random_G + fw_G_B_ZJ))[2:].upper()
                        else:# B减少
                            hex_b = hex(int(random_G - fw_G_B_JS))[2:].upper()
                    elif current_tab_index_RGB_GJ_G_R == 1: # R增加
                        hex_r = hex(int(random_G + fw_G_R_ZJ))[2:].upper()
                        if current_tab_index_RGB_GJ_G_B == 0: # B比例
                            hex_b = hex(int(float(random_G * BL_G_B)))[2:].upper()
                        elif current_tab_index_RGB_GJ_G_B == 1: # B增加
                            hex_b = hex(int(random_G + fw_G_B_ZJ))[2:].upper()
                        else:# B减少
                            hex_b = hex(int(random_G - fw_G_B_JS))[2:].upper()
                    else: #R减少
                        hex_r = hex(int(random_G - fw_G_R_JS))[2:].upper()
                        if current_tab_index_RGB_GJ_G_B == 0: # B比例
                            hex_b = hex(int(float(random_G * BL_G_B)))[2:].upper()
                        elif current_tab_index_RGB_GJ_G_B == 1: # B增加
                            hex_b = hex(int(random_G + fw_G_B_ZJ))[2:].upper()
                        else:# B减少
                            hex_b = hex(int(random_G - fw_G_R_JS))[2:].upper()
                else:# B为基准
                    random_B = random.randint(fw_B_start, fw_B_end)
                    hex_b = hex(random_B)[2:].upper()
                    if current_tab_index_RGB_GJ_B_R == 0: # R比例
                        hex_r = hex(int(float(random_B * BL_B_R)))[2:].upper()
                        if current_tab_index_RGB_GJ_B_G == 0: # G比例
                            hex_g = hex(int(float(random_B * BL_B_R)))[2:].upper()
                        elif current_tab_index_RGB_GJ_B_G == 1: # G增加
                            hex_g = hex(int(random_B + fw_B_G_ZJ))[2:].upper()
                        else:# B减少
                            hex_g = hex(int(random_B - fw_B_G_JS))[2:].upper()
                    elif current_tab_index_RGB_GJ_B_R == 1: # R增加
                        hex_r = hex(int(random_B + fw_B_R_ZJ))[2:].upper()
                        if current_tab_index_RGB_GJ_B_G == 0: # G比例
                            hex_g = hex(int(float(random_B * BL_B_G)))[2:].upper()
                        elif current_tab_index_RGB_GJ_B_G == 1: # G增加
                            hex_g = hex(int(random_B + fw_B_G_ZJ))[2:].upper()
                        else:# B减少
                            hex_g = hex(int(random_B - fw_B_G_JS))[2:].upper()
                    else:
                        hex_r = hex(int(random_B - fw_B_R_JS))[2:].upper()
                        if current_tab_index_RGB_GJ_B_G == 0: # G比例
                            hex_g = hex(int(float(random_B * BL_B_G)))[2:].upper()
                        elif current_tab_index_RGB_GJ_B_G == 1: # G增加
                            hex_g = hex(int(random_B + fw_B_G_ZJ))[2:].upper()
                        else:# B减少
                            hex_g = hex(int(random_B - fw_B_G_JS))[2:].upper()
            hex_r0 = hex_r.zfill(2)
            hex_g0 = hex_g.zfill(2)
            hex_b0 = hex_b.zfill(2)
            return "#" + str(hex_r0) + str(hex_g0) + str(hex_b0)
        def sjxs_TP(TP_WZ_X,TP_WZ_Y):
            # 获取像素颜色
            pixel_data = source_pixels[TP_WZ_X - 1, TP_WZ_Y - 1]
            hex_color = "#{:02X}{:02X}{:02X}".format(pixel_data[0], pixel_data[1], pixel_data[2])
            return hex_color
            
        # 颜色取值范围
        if int(current_tab_index_RGB) == 0: #普通
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
        elif int(current_tab_index_RGB) == 1:
            #高级
            current_tab_index_RGB_GJ = tabControl_RGB_GJ.index(tabControl_RGB_GJ.select())
            print(current_tab_index_RGB_GJ)
            if current_tab_index_RGB_GJ == 0:#R为基准
                fw_R_start = int(slider_R_start_GJ.get())
                fw_R_end = int(slider_R_end_GJ.get())
                if fw_R_start > fw_R_end:
                    messagebox.showwarning("警告", "R值错误")
                    return 0
                # R为基准G值
                current_tab_index_RGB_GJ_R_G = tabControl_RGB_GJ_R_G.index(tabControl_RGB_GJ_R_G.select())
                if current_tab_index_RGB_GJ_R_G == 0:#比例
                    BL_R_G = float(bookChosen_BL_R_G.get())
                    if int(float(BL_R_G * fw_R_end)) > 255:
                        messagebox.showwarning("警告", "G值错误,G值范围超过255")
                        return 0
                elif current_tab_index_RGB_GJ_R_G == 1:#增加
                    fw_R_G_ZJ = int(slider_R_ZJ_GJ_G.get())
                    if fw_R_G_ZJ + fw_R_end > 255:
                        messagebox.showwarning("警告", "G值错误,G值范围超过255")
                        return 0
                else:
                    fw_R_G_JS = int(slider_R_JS_GJ_G.get())
                    if fw_R_start - fw_R_G_JS < 0:
                        messagebox.showwarning("警告", "G值错误,G值范围小于0")
                        return 0
                
                # R为基准B值
                current_tab_index_RGB_GJ_R_B = tabControl_RGB_GJ_R_B.index(tabControl_RGB_GJ_R_B.select())
                if current_tab_index_RGB_GJ_R_B == 0:#比例
                    BL_R_B = float(bookChosen_BL_R_B.get())
                    if int(float(BL_R_B * fw_R_end)) > 255:
                        messagebox.showwarning("警告", "B值错误,B值范围超过255")
                        return 0
                elif current_tab_index_RGB_GJ_R_B == 1:#增加
                    fw_R_B_ZJ = int(slider_R_ZJ_GJ_B.get())
                    if fw_R_B_ZJ + fw_R_end > 255:
                        messagebox.showwarning("警告", "B值错误,B值范围超过255")
                        return 0
                else:
                    fw_R_B_JS = int(slider_R_JS_GJ_B.get())
                    if fw_R_start - fw_R_B_JS < 0:
                        messagebox.showwarning("警告", "B值错误,B值范围小于0")
                        return 0
            elif current_tab_index_RGB_GJ == 1:#G为基准
                fw_G_start = int(slider_G_start_GJ.get())
                fw_G_end = int(slider_G_end_GJ.get())
                if fw_G_start > fw_G_end:
                    messagebox.showwarning("警告", "G值错误")
                    return 0
                #G为基准R值
                current_tab_index_RGB_GJ_G_R = tabControl_RGB_GJ_G_R.index(tabControl_RGB_GJ_G_R.select())
                if current_tab_index_RGB_GJ_G_R == 0:#比例
                    BL_G_R = float(bookChosen_BL_G_R.get())
                    if int(float(BL_G_R * fw_G_end)) > 255:
                        messagebox.showwarning("警告", "R值错误,R值范围超过255")
                        return 0
                elif current_tab_index_RGB_GJ_G_R == 1:#增加
                    fw_G_R_ZJ = int(slider_G_ZJ_GJ_R.get())
                    if fw_G_R_ZJ + fw_G_end > 255:
                        messagebox.showwarning("警告", "R值错误,R值范围超过255")
                        return 0
                else:
                    fw_G_R_JS = int(slider_G_JS_GJ_R.get())
                    if fw_G_start - fw_G_R_JS < 0:
                        messagebox.showwarning("警告", "R值错误,R值范围小于0")
                        return 0
                #G为基准B值
                current_tab_index_RGB_GJ_G_B = tabControl_RGB_GJ_G_B.index(tabControl_RGB_GJ_G_B.select())
                if current_tab_index_RGB_GJ_G_B == 0:#比例
                    BL_G_B = float(bookChosen_BL_G_B.get())
                    if int(float(BL_G_B * fw_G_end)) > 255:
                        messagebox.showwarning("警告", "B值错误,B值范围超过255")
                        return 0
                elif current_tab_index_RGB_GJ_G_B == 1:#增加
                    fw_G_B_ZJ = int(slider_G_ZJ_GJ_B.get())
                    if fw_G_B_ZJ + fw_G_end > 255:
                        messagebox.showwarning("警告", "B值错误,B值范围超过255")
                        return 0
                else:
                    fw_G_B_JS = int(slider_G_JS_GJ_B.get())
                    if fw_G_start - fw_G_B_JS < 0:
                        messagebox.showwarning("警告", "B值错误,B值范围小于0")
                        return 0
            else:#B为基准
                fw_B_start = int(slider_B_start_GJ.get())
                fw_B_end = int(slider_B_end_GJ.get())
                if fw_B_start > fw_B_end:
                    messagebox.showwarning("警告", "B值错误")
                    return 0
                #B为基准R值
                current_tab_index_RGB_GJ_B_R = tabControl_RGB_GJ_B_R.index(tabControl_RGB_GJ_B_R.select())
                if current_tab_index_RGB_GJ_B_R == 0:#比例
                    BL_B_R = float(bookChosen_BL_B_R.get())
                    if int(float(BL_B_R * fw_B_end)) > 255:
                        messagebox.showwarning("警告", "R值错误,R值范围超过255")
                        return 0
                elif current_tab_index_RGB_GJ_B_R == 1:#增加
                    fw_B_R_ZJ = int(slider_B_ZJ_GJ_R.get())
                    if fw_B_R_ZJ + fw_B_end > 255:
                        messagebox.showwarning("警告", "R值错误,R值范围超过255")
                        return 0
                else:
                    fw_B_R_JS = int(slider_B_JS_GJ_R.get())
                    if fw_B_start - fw_B_R_JS < 0:
                        messagebox.showwarning("警告", "R值错误,R值范围小于0")
                        return 0
                # B为基准G值
                current_tab_index_RGB_GJ_B_G = tabControl_RGB_GJ_B_G.index(tabControl_RGB_GJ_B_G.select())
                if current_tab_index_RGB_GJ_B_G == 0:#比例
                    BL_B_G = float(bookChosen_BL_B_G.get())
                    if int(float(BL_B_G * fw_B_end)) > 255:
                        messagebox.showwarning("警告", "G值错误,G值范围超过255")
                        return 0
                elif current_tab_index_RGB_GJ_B_G == 1:#增加
                    fw_B_G_ZJ = int(slider_B_ZJ_GJ_G.get())
                    if fw_B_G_ZJ + fw_B_end > 255:
                        messagebox.showwarning("警告", "G值错误,G值范围超过255")
                        return 0
                else:
                    fw_B_G_JS = int(slider_B_JS_GJ_G.get())
                    if fw_B_start - fw_B_G_JS < 0:
                        messagebox.showwarning("警告", "G值错误,G值范围小于0")
                        return 0
                
        # 尺寸取值范围
        if current_tab_index_CC == 0: # 普通
            fw_X_PT_start = int(slider_X_start_PT.get())
            fw_X_PT_end = int(slider_X_end_PT.get())
            if fw_X_PT_start > fw_X_PT_end:
                messagebox.showwarning("警告", "方块X值错误")
                return 0
            
            fw_Y_PT_start = int(slider_Y_start_PT.get())
            fw_Y_PT_end = int(slider_Y_end_PT.get())
            if fw_Y_PT_start > fw_Y_PT_end:
                messagebox.showwarning("警告", "方块Y值错误")
                return 0
        elif current_tab_index_CC == 1:
            fw_JZ_BL_start = int(slider_JZ_start_BL.get())
            fw_JZ_BL_end = int(slider_JZ_end_BL.get())
            if fw_JZ_BL_start > fw_JZ_BL_end:
                messagebox.showwarning("警告", "基准值错误")
                return 0
        else:
            fw_JZ_ZJ_start = int(slider_JZ_start_GD.get())
            fw_JZ_ZJ_end = int(slider_JZ_end_GD.get())
            if fw_JZ_ZJ_start > fw_JZ_ZJ_end:
                messagebox.showwarning("警告", "基准值错误")
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
        print(current_tab_index_CC)
        if int(current_tab_index_RGB) == 0 or int(current_tab_index_RGB) == 1:
            if current_tab_index_CC == 0:
                for i in range(num_blocks):
                    tp = Image.new("RGB", (1, 1), sjxs())
                    tp = tp.resize((random.randint(fw_X_PT_start, fw_X_PT_end), random.randint(fw_Y_PT_start, fw_Y_PT_end)))
                    bg.paste(tp, (random.randint(0, x+200), random.randint(0, y+200)))
                    progress_bar['value'] = (i + 1) * 100 / num_blocks
                    progress_window.update_idletasks()
            elif current_tab_index_CC == 1:
                bl = float(bookChosen_BL.get())
                if int(radio_value_JZ_BL.get()) == 1:
                    for i in range(num_blocks):
                        tp = Image.new("RGB", (1, 1), sjxs())
                        x_0 = random.randint(fw_JZ_BL_start, fw_JZ_BL_end)
                        tp = tp.resize((x_0, int(float(x_0*bl))))
                        bg.paste(tp, (random.randint(0, x+200), random.randint(0, y+200)))
                        progress_bar['value'] = (i + 1) * 100 / num_blocks
                        progress_window.update_idletasks()
                else:
                    for i in range(num_blocks):
                        tp = Image.new("RGB", (1, 1), sjxs())
                        y_0 = random.randint(fw_JZ_BL_start, fw_JZ_BL_end)
                        tp = tp.resize((int(float(y_0*bl)),y_0 ))
                        bg.paste(tp, (random.randint(0, x+200), random.randint(0, y+200)))
                        progress_bar['value'] = (i + 1) * 100 / num_blocks
                        progress_window.update_idletasks()
                    
            else:
                zj = int(slider_ZJ_start_GD.get())
                if int(radio_value_JZ_GD.get()) == 1:
                    for i in range(num_blocks):
                        tp = Image.new("RGB", (1, 1), sjxs())
                        x_1 = random.randint(fw_JZ_ZJ_start, fw_JZ_ZJ_end)
                        tp = tp.resize((x_1, x_1+zj))
                        bg.paste(tp, (random.randint(0, x+200), random.randint(0, y+200)))
                        progress_bar['value'] = (i + 1) * 100 / num_blocks
                        progress_window.update_idletasks()
                else:
                    for i in range(num_blocks):
                        tp = Image.new("RGB", (1, 1), sjxs())
                        y_1 = random.randint(fw_JZ_ZJ_start, fw_JZ_ZJ_end)
                        tp = tp.resize((y_1+zj, y_1))
                        bg.paste(tp, (random.randint(0, x+200), random.randint(0, y+200)))
                        progress_bar['value'] = (i + 1) * 100 / num_blocks
                        progress_window.update_idletasks()
        
        elif int(current_tab_index_RGB) == 2:
            if current_tab_index_CC == 0:
                for i in range(num_blocks):
                    # 位置
                    random_X = random.randint(0, x)
                    random_Y = random.randint(0, y)
                    # 大小
                    random_width = random.randint(fw_X_PT_start, fw_X_PT_end)
                    random_height = random.randint(fw_Y_PT_start, fw_Y_PT_end)
                    # 新位置
                    random_new_X = int(float(random_X - random_width/2 + 100))
                    random_new_Y = int(float(random_Y - random_height/2 + 100))
                    tp = Image.new("RGB", (1, 1), sjxs_TP(random_X,random_Y))
                    tp = tp.resize((random_width, random_height))
                    bg.paste(tp, (random_new_X,random_new_Y))
                    progress_bar['value'] = (i + 1) * 100 / num_blocks
                    progress_window.update_idletasks()
                    
            elif current_tab_index_CC == 1:
                bl = float(bookChosen_BL.get())
                if int(radio_value_JZ_BL.get()) == 1:
                    for i in range(num_blocks):
                        # 位置
                        random_X = random.randint(0, x)
                        random_Y = random.randint(0, y)
                        # 大小
                        random_width = random.randint(fw_JZ_BL_start, fw_JZ_BL_end)
                        random_height = int(float(random_width*bl))
                        # 新位置
                        random_new_X = int(float(random_X - random_width/2 + 100))
                        random_new_Y = int(float(random_Y - random_height/2 + 100))
                        
                        tp = Image.new("RGB", (1, 1), sjxs_TP(random_X,random_Y))
                        tp = tp.resize((random_width, random_height))
                        bg.paste(tp, (random_new_X, random_new_Y))
                        progress_bar['value'] = (i + 1) * 100 / num_blocks
                        progress_window.update_idletasks()
                else:
                    for i in range(num_blocks):
                        # 位置
                        random_X = random.randint(0, x)
                        random_Y = random.randint(0, y)
                        # 大小
                        random_height = random.randint(fw_JZ_BL_start, fw_JZ_BL_end)
                        random_width = int(float(random_height*bl))
                        # 新位置
                        random_new_X = int(float(random_X - random_width/2 + 100))
                        random_new_Y = int(float(random_Y - random_height/2 + 100))
                        
                        tp = Image.new("RGB", (1, 1), sjxs_TP(random_X,random_Y))
                        tp = tp.resize((random_width,random_height ))
                        bg.paste(tp, (random_new_X,random_new_Y))
                        progress_bar['value'] = (i + 1) * 100 / num_blocks
                        progress_window.update_idletasks()
                    
            else:
                zj = int(slider_ZJ_start_GD.get())
                if int(radio_value_JZ_GD.get()) == 1:
                    for i in range(num_blocks):
                        # 位置
                        random_X = random.randint(0, x)
                        random_Y = random.randint(0, y)
                        # 大小
                        random_width = random.randint(fw_JZ_ZJ_start, fw_JZ_ZJ_end)
                        random_height = random_width+zj
                        # 新位置
                        random_new_X = int(float(random_X - random_width/2 + 100))
                        random_new_Y = int(float(random_Y - random_height/2 + 100))
                        
                        tp = Image.new("RGB", (1, 1), sjxs_TP(random_X,random_Y))
                        tp = tp.resize((random_width, random_height))
                        bg.paste(tp, (random_new_X,random_new_Y))
                        progress_bar['value'] = (i + 1) * 100 / num_blocks
                        progress_window.update_idletasks()
                else:
                    for i in range(num_blocks):
                        # 位置
                        random_X = random.randint(0, x)
                        random_Y = random.randint(0, y)
                        # 大小
                        random_height = random.randint(fw_JZ_ZJ_start, fw_JZ_ZJ_end)
                        random_width = random_height+zj
                        # 新位置
                        random_new_X = int(float(random_X - random_width/2 + 100))
                        random_new_Y = int(float(random_Y - random_height/2 + 100))
                        
                        tp = Image.new("RGB", (1, 1), sjxs_TP(random_X,random_Y))
                        tp = tp.resize((random_width, random_height))
                        bg.paste(tp, (random_new_X,random_new_Y))
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
    
#图片标签对图片尺寸的选定函数群
def on_tab_changed(event):
    # 获取当前选中的标签页
    current_tab = tabControl_RGB.index("current")
    
    # 检查当前选中的标签页
    if current_tab == 2:  # '图片'标签页
        # 锁住 label_frame_DX
        lock_frame(label_frame_DX)
        # 绑定点击事件以弹出警告
        label_frame_DX.bind("<Button-1>", show_warning)
    else:
        # 解锁 label_frame_DX
        unlock_frame(label_frame_DX)
        # 解除绑定点击事件
        label_frame_DX.unbind("<Button-1>")

def lock_frame(frame):
    # 锁住 frame 的所有控件
    for widget in frame.winfo_children():
        widget.config(state='disabled')

def unlock_frame(frame):
    # 解锁 frame 的所有控件
    for widget in frame.winfo_children():
        widget.config(state='normal')

def show_warning(event):
    messagebox.showwarning("警告", "标签页“图片”已被选中，无法操作此区域！")

#函数群结束

label_frame_FK = ttk.LabelFrame(root, text="方块设置", labelanchor='n')
label_frame_FK.grid(row=0, column=0)

label_frame_RGB = ttk.LabelFrame(label_frame_FK, text="颜色取值范围", labelanchor='n')
label_frame_RGB.pack(padx=5, pady=0, fill=tk.BOTH, expand=True)

tabControl_RGB = ttk.Notebook(label_frame_RGB)
tab1_RGB_1 = ttk.Frame(tabControl_RGB)
tabControl_RGB.add(tab1_RGB_1, text='普通')
tab1_RGB_2 = ttk.Frame(tabControl_RGB)
tabControl_RGB.add(tab1_RGB_2, text='高级')
tab1_RGB_3 = ttk.Frame(tabControl_RGB)
tabControl_RGB.add(tab1_RGB_3, text='图片')
tabControl_RGB.bind("<<NotebookTabChanged>>", on_tab_changed)
tabControl_RGB.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

#普通
label_frame_R = ttk.LabelFrame(tab1_RGB_1, text="R值范围", labelanchor='n')
label_frame_R.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

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

label_frame_G = ttk.LabelFrame(tab1_RGB_1, text="G值范围", labelanchor='n')
label_frame_G.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

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

label_frame_B = ttk.LabelFrame(tab1_RGB_1, text="B值范围", labelanchor='n')
label_frame_B.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

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

#高级
tabControl_RGB_GJ = ttk.Notebook(tab1_RGB_2)
tab1_RGB_R = ttk.Frame(tabControl_RGB_GJ)
tabControl_RGB_GJ.add(tab1_RGB_R, text='R为基准')
tab1_RGB_G = ttk.Frame(tabControl_RGB_GJ)
tabControl_RGB_GJ.add(tab1_RGB_G, text='G为基准')
tab1_RGB_B = ttk.Frame(tabControl_RGB_GJ)
tabControl_RGB_GJ.add(tab1_RGB_B, text='B为基准')
tabControl_RGB_GJ.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
label_frame_R_GJ = ttk.LabelFrame(tab1_RGB_R, text="R值范围", labelanchor='n')
label_frame_R_GJ.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

label_R_start_GJ = tk.Label(label_frame_R_GJ, text="开始：")
label_R_start_GJ.grid(row=0, column=0)
slider_R_start_GJ = ttk.Scale(label_frame_R_GJ, from_=0, to=255, orient=tk.HORIZONTAL, value=25, command=lambda v: slider_changed(v, label_value_R_start_GJ))
slider_R_start_GJ.grid(row=0, column=1)
label_value_R_start_GJ = tk.Label(label_frame_R_GJ, text="25")
label_value_R_start_GJ.grid(row=0, column=2)

label_R_end_GJ = tk.Label(label_frame_R_GJ, text="结束：")
label_R_end_GJ.grid(row=1, column=0)
slider_R_end_GJ = ttk.Scale(label_frame_R_GJ, from_=0, to=255, orient=tk.HORIZONTAL, value=175, command=lambda v: slider_changed(v, label_value_R_end_GJ))
slider_R_end_GJ.grid(row=1, column=1)
label_value_R_end_GJ = tk.Label(label_frame_R_GJ, text="175")
label_value_R_end_GJ.grid(row=1, column=2)

label_frame_R_G = ttk.LabelFrame(tab1_RGB_R, text="G值", labelanchor='n')
label_frame_R_G.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

tabControl_RGB_GJ_R_G = ttk.Notebook(label_frame_R_G)
tab1_RGB_R_G_BL = ttk.Frame(tabControl_RGB_GJ_R_G)
tabControl_RGB_GJ_R_G.add(tab1_RGB_R_G_BL, text='比例')
tab1_RGB_R_G_ZJ = ttk.Frame(tabControl_RGB_GJ_R_G)
tabControl_RGB_GJ_R_G.add(tab1_RGB_R_G_ZJ, text='增加')
tab1_RGB_R_G_JS = ttk.Frame(tabControl_RGB_GJ_R_G)
tabControl_RGB_GJ_R_G.add(tab1_RGB_R_G_JS, text='减少')
tabControl_RGB_GJ_R_G.pack(padx=10, pady=0, fill=tk.BOTH, expand=True)

book_BL_R_G = tk.StringVar()
bookChosen_BL_R_G = ttk.Combobox(tab1_RGB_R_G_BL, textvariable=book_BL_R_G)
bookChosen_BL_R_G['values'] = (0.1,0.2,0.25,0.5,0.75,0.8,1.0,1.2,1.25,1.3,1.5,1.75,2.0,2.25,2.5,2.75,3.0)
bookChosen_BL_R_G.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
bookChosen_BL_R_G.current(6)  #设置初始显示值，值为元组['values']的下标
bookChosen_BL_R_G.config(state='readonly')  #设为只读模式

label_R_ZJ_GJ_G = tk.Label(tab1_RGB_R_G_ZJ, text="值：")
label_R_ZJ_GJ_G.grid(row=0, column=0)
slider_R_ZJ_GJ_G = ttk.Scale(tab1_RGB_R_G_ZJ, from_=0, to=255, orient=tk.HORIZONTAL, value=25, command=lambda v: slider_changed(v, label_value_R_ZJ_GJ_G))
slider_R_ZJ_GJ_G.grid(row=0, column=1)
label_value_R_ZJ_GJ_G = tk.Label(tab1_RGB_R_G_ZJ, text="25")
label_value_R_ZJ_GJ_G.grid(row=0, column=2)

label_R_JS_GJ_G = tk.Label(tab1_RGB_R_G_JS, text="值：")
label_R_JS_GJ_G.grid(row=0, column=0)
slider_R_JS_GJ_G = ttk.Scale(tab1_RGB_R_G_JS, from_=0, to=255, orient=tk.HORIZONTAL, value=25, command=lambda v: slider_changed(v, label_value_R_JS_GJ_G))
slider_R_JS_GJ_G.grid(row=0, column=1)
label_value_R_JS_GJ_G = tk.Label(tab1_RGB_R_G_JS, text="25")
label_value_R_JS_GJ_G.grid(row=0, column=2)

label_frame_R_B = ttk.LabelFrame(tab1_RGB_R, text="B值", labelanchor='n')
label_frame_R_B.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

tabControl_RGB_GJ_R_B = ttk.Notebook(label_frame_R_B)
tab1_RGB_R_B_BL = ttk.Frame(tabControl_RGB_GJ_R_B)
tabControl_RGB_GJ_R_B.add(tab1_RGB_R_B_BL, text='比例')
tab1_RGB_R_B_ZJ = ttk.Frame(tabControl_RGB_GJ_R_B)
tabControl_RGB_GJ_R_B.add(tab1_RGB_R_B_ZJ, text='增加')
tab1_RGB_R_B_JS = ttk.Frame(tabControl_RGB_GJ_R_B)
tabControl_RGB_GJ_R_B.add(tab1_RGB_R_B_JS, text='减少')
tabControl_RGB_GJ_R_B.pack(padx=10, pady=0, fill=tk.BOTH, expand=True)

book_BL_R_B = tk.StringVar()
bookChosen_BL_R_B = ttk.Combobox(tab1_RGB_R_B_BL, textvariable=book_BL_R_B)
bookChosen_BL_R_B['values'] = (0.1,0.2,0.25,0.5,0.75,0.8,1.0,1.2,1.25,1.3,1.5,1.75,2.0,2.25,2.5,2.75,3.0)
bookChosen_BL_R_B.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
bookChosen_BL_R_B.current(6)  #设置初始显示值，值为元组['values']的下标
bookChosen_BL_R_B.config(state='readonly')  #设为只读模式

label_R_ZJ_GJ_B = tk.Label(tab1_RGB_R_B_ZJ, text="值：")
label_R_ZJ_GJ_B.grid(row=0, column=0)
slider_R_ZJ_GJ_B = ttk.Scale(tab1_RGB_R_B_ZJ, from_=0, to=255, orient=tk.HORIZONTAL, value=25, command=lambda v: slider_changed(v, label_value_R_ZJ_GJ_B))
slider_R_ZJ_GJ_B.grid(row=0, column=1)
label_value_R_ZJ_GJ_B = tk.Label(tab1_RGB_R_B_ZJ, text="25")
label_value_R_ZJ_GJ_B.grid(row=0, column=2)

label_R_JS_GJ_B = tk.Label(tab1_RGB_R_B_JS, text="值：")
label_R_JS_GJ_B.grid(row=0, column=0)
slider_R_JS_GJ_B = ttk.Scale(tab1_RGB_R_B_JS, from_=0, to=255, orient=tk.HORIZONTAL, value=25, command=lambda v: slider_changed(v, label_value_R_JS_GJ_B))
slider_R_JS_GJ_B.grid(row=0, column=1)
label_value_R_JS_GJ_B = tk.Label(tab1_RGB_R_B_JS, text="25")
label_value_R_JS_GJ_B.grid(row=0, column=2)

#GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
label_frame_G_R = ttk.LabelFrame(tab1_RGB_G, text="R值", labelanchor='n')
label_frame_G_R.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

tabControl_RGB_GJ_G_R = ttk.Notebook(label_frame_G_R)
tab1_RGB_G_R_RL = ttk.Frame(tabControl_RGB_GJ_G_R)
tabControl_RGB_GJ_G_R.add(tab1_RGB_G_R_RL, text='比例')
tab1_RGB_G_R_ZJ = ttk.Frame(tabControl_RGB_GJ_G_R)
tabControl_RGB_GJ_G_R.add(tab1_RGB_G_R_ZJ, text='增加')
tab1_RGB_G_R_JS = ttk.Frame(tabControl_RGB_GJ_G_R)
tabControl_RGB_GJ_G_R.add(tab1_RGB_G_R_JS, text='减少')
tabControl_RGB_GJ_G_R.pack(padx=10, pady=0, fill=tk.BOTH, expand=True)

book_RL_G_R = tk.StringVar()
bookChosen_BL_G_R = ttk.Combobox(tab1_RGB_G_R_RL, textvariable=book_RL_G_R)
bookChosen_BL_G_R['values'] = (0.1,0.2,0.25,0.5,0.75,0.8,1.0,1.2,1.25,1.3,1.5,1.75,2.0,2.25,2.5,2.75,3.0)
bookChosen_BL_G_R.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
bookChosen_BL_G_R.current(6)  #设置初始显示值，值为元组['values']的下标
bookChosen_BL_G_R.config(state='readonly')  #设为只读模式

label_G_ZJ_GJ_R = tk.Label(tab1_RGB_G_R_ZJ, text="值：")
label_G_ZJ_GJ_R.grid(row=0, column=0)
slider_G_ZJ_GJ_R = ttk.Scale(tab1_RGB_G_R_ZJ, from_=0, to=255, orient=tk.HORIZONTAL, value=25, command=lambda v: slider_changed(v, label_value_G_ZJ_GJ_R))
slider_G_ZJ_GJ_R.grid(row=0, column=1)
label_value_G_ZJ_GJ_R = tk.Label(tab1_RGB_G_R_ZJ, text="25")
label_value_G_ZJ_GJ_R.grid(row=0, column=2)

label_G_JS_GJ_R = tk.Label(tab1_RGB_G_R_JS, text="值：")
label_G_JS_GJ_R.grid(row=0, column=0)
slider_G_JS_GJ_R = ttk.Scale(tab1_RGB_G_R_JS, from_=0, to=255, orient=tk.HORIZONTAL, value=25, command=lambda v: slider_changed(v, label_value_G_JS_GJ_R))
slider_G_JS_GJ_R.grid(row=0, column=1)
label_value_G_JS_GJ_R = tk.Label(tab1_RGB_G_R_JS, text="25")
label_value_G_JS_GJ_R.grid(row=0, column=2)

label_frame_G_GJ = ttk.LabelFrame(tab1_RGB_G, text="G值范围", labelanchor='n')
label_frame_G_GJ.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

label_G_start_GJ = tk.Label(label_frame_G_GJ, text="开始：")
label_G_start_GJ.grid(row=0, column=0)
slider_G_start_GJ = ttk.Scale(label_frame_G_GJ, from_=0, to=255, orient=tk.HORIZONTAL, value=25, command=lambda v: slider_changed(v, label_value_G_start_GJ))
slider_G_start_GJ.grid(row=0, column=1)
label_value_G_start_GJ = tk.Label(label_frame_G_GJ, text="25")
label_value_G_start_GJ.grid(row=0, column=2)

label_G_end_GJ = tk.Label(label_frame_G_GJ, text="结束：")
label_G_end_GJ.grid(row=1, column=0)
slider_G_end_GJ = ttk.Scale(label_frame_G_GJ, from_=0, to=255, orient=tk.HORIZONTAL, value=175, command=lambda v: slider_changed(v, label_value_G_end_GJ))
slider_G_end_GJ.grid(row=1, column=1)
label_value_G_end_GJ = tk.Label(label_frame_G_GJ, text="175")
label_value_G_end_GJ.grid(row=1, column=2)

label_frame_G_B = ttk.LabelFrame(tab1_RGB_G, text="B值", labelanchor='n')
label_frame_G_B.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

tabControl_RGB_GJ_G_B = ttk.Notebook(label_frame_G_B)
tab1_RGB_G_B_BL = ttk.Frame(tabControl_RGB_GJ_G_B)
tabControl_RGB_GJ_G_B.add(tab1_RGB_G_B_BL, text='比例')
tab1_RGB_G_B_ZJ = ttk.Frame(tabControl_RGB_GJ_G_B)
tabControl_RGB_GJ_G_B.add(tab1_RGB_G_B_ZJ, text='增加')
tab1_RGB_G_B_JS = ttk.Frame(tabControl_RGB_GJ_G_B)
tabControl_RGB_GJ_G_B.add(tab1_RGB_G_B_JS, text='减少')
tabControl_RGB_GJ_G_B.pack(padx=10, pady=0, fill=tk.BOTH, expand=True)

book_BL_G_B = tk.StringVar()
bookChosen_BL_G_B = ttk.Combobox(tab1_RGB_G_B_BL, textvariable=book_BL_G_B)
bookChosen_BL_G_B['values'] = (0.1,0.2,0.25,0.5,0.75,0.8,1.0,1.2,1.25,1.3,1.5,1.75,2.0,2.25,2.5,2.75,3.0)
bookChosen_BL_G_B.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
bookChosen_BL_G_B.current(6)  #设置初始显示值，值为元组['values']的下标
bookChosen_BL_G_B.config(state='readonly')  #设为只读模式

label_G_ZJ_GJ_B = tk.Label(tab1_RGB_G_B_ZJ, text="值：")
label_G_ZJ_GJ_B.grid(row=0, column=0)
slider_G_ZJ_GJ_B = ttk.Scale(tab1_RGB_G_B_ZJ, from_=0, to=255, orient=tk.HORIZONTAL, value=25, command=lambda v: slider_changed(v, label_value_G_ZJ_GJ_B))
slider_G_ZJ_GJ_B.grid(row=0, column=1)
label_value_G_ZJ_GJ_B = tk.Label(tab1_RGB_G_B_ZJ, text="25")
label_value_G_ZJ_GJ_B.grid(row=0, column=2)

label_G_JS_GJ_B = tk.Label(tab1_RGB_G_B_JS, text="值：")
label_G_JS_GJ_B.grid(row=0, column=0)
slider_G_JS_GJ_B = ttk.Scale(tab1_RGB_G_B_JS, from_=0, to=255, orient=tk.HORIZONTAL, value=25, command=lambda v: slider_changed(v, label_value_G_JS_GJ_B))
slider_G_JS_GJ_B.grid(row=0, column=1)
label_value_G_JS_GJ_B = tk.Label(tab1_RGB_G_B_JS, text="25")
label_value_G_JS_GJ_B.grid(row=0, column=2)

#BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
label_frame_B_R = ttk.LabelFrame(tab1_RGB_B, text="R值", labelanchor='n')
label_frame_B_R.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

tabControl_RGB_GJ_B_R = ttk.Notebook(label_frame_B_R)
tab1_RGB_B_R_BL = ttk.Frame(tabControl_RGB_GJ_B_R)
tabControl_RGB_GJ_B_R.add(tab1_RGB_B_R_BL, text='比例')
tab1_RGB_B_R_ZJ = ttk.Frame(tabControl_RGB_GJ_B_R)
tabControl_RGB_GJ_B_R.add(tab1_RGB_B_R_ZJ, text='增加')
tab1_RGB_B_R_JS = ttk.Frame(tabControl_RGB_GJ_B_R)
tabControl_RGB_GJ_B_R.add(tab1_RGB_B_R_JS, text='减少')
tabControl_RGB_GJ_B_R.pack(padx=10, pady=0, fill=tk.BOTH, expand=True)

book_BL_B_R = tk.StringVar()
bookChosen_BL_B_R = ttk.Combobox(tab1_RGB_B_R_BL, textvariable=book_BL_B_R)
bookChosen_BL_B_R['values'] = (0.1,0.2,0.25,0.5,0.75,0.8,1.0,1.2,1.25,1.3,1.5,1.75,2.0,2.25,2.5,2.75,3.0)
bookChosen_BL_B_R.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
bookChosen_BL_B_R.current(6)  #设置初始显示值，值为元组['values']的下标
bookChosen_BL_B_R.config(state='readonly')  #设为只读模式

label_B_ZJ_GJ_R = tk.Label(tab1_RGB_B_R_ZJ, text="值：")
label_B_ZJ_GJ_R.grid(row=0, column=0)
slider_B_ZJ_GJ_R = ttk.Scale(tab1_RGB_B_R_ZJ, from_=0, to=255, orient=tk.HORIZONTAL, value=25, command=lambda v: slider_changed(v, label_value_B_ZJ_GJ_R))
slider_B_ZJ_GJ_R.grid(row=0, column=1)
label_value_B_ZJ_GJ_R = tk.Label(tab1_RGB_B_R_ZJ, text="25")
label_value_B_ZJ_GJ_R.grid(row=0, column=2)

label_B_JS_GJ_R = tk.Label(tab1_RGB_B_R_JS, text="值：")
label_B_JS_GJ_R.grid(row=0, column=0)
slider_B_JS_GJ_R = ttk.Scale(tab1_RGB_B_R_JS, from_=0, to=255, orient=tk.HORIZONTAL, value=25, command=lambda v: slider_changed(v, label_value_B_JS_GJ_R))
slider_B_JS_GJ_R.grid(row=0, column=1)
label_value_B_JS_GJ_R = tk.Label(tab1_RGB_B_R_JS, text="25")
label_value_B_JS_GJ_R.grid(row=0, column=2)

label_frame_B_G = ttk.LabelFrame(tab1_RGB_B, text="G值", labelanchor='n')
label_frame_B_G.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

tabControl_RGB_GJ_B_G = ttk.Notebook(label_frame_B_G)
tab1_RGB_B_G_BL = ttk.Frame(tabControl_RGB_GJ_B_G)
tabControl_RGB_GJ_B_G.add(tab1_RGB_B_G_BL, text='比例')
tab1_RGB_B_G_ZJ = ttk.Frame(tabControl_RGB_GJ_B_G)
tabControl_RGB_GJ_B_G.add(tab1_RGB_B_G_ZJ, text='增加')
tab1_RGB_B_G_JS = ttk.Frame(tabControl_RGB_GJ_B_G)
tabControl_RGB_GJ_B_G.add(tab1_RGB_B_G_JS, text='减少')
tabControl_RGB_GJ_B_G.pack(padx=10, pady=0, fill=tk.BOTH, expand=True)

book_BL_B_G = tk.StringVar()
bookChosen_BL_B_G = ttk.Combobox(tab1_RGB_B_G_BL, textvariable=book_BL_B_G)
bookChosen_BL_B_G['values'] = (0.1,0.2,0.25,0.5,0.75,0.8,1.0,1.2,1.25,1.3,1.5,1.75,2.0,2.25,2.5,2.75,3.0)
bookChosen_BL_B_G.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
bookChosen_BL_B_G.current(6)  #设置初始显示值，值为元组['values']的下标
bookChosen_BL_B_G.config(state='readonly')  #设为只读模式

label_B_ZJ_GJ_G = tk.Label(tab1_RGB_B_G_ZJ, text="值：")
label_B_ZJ_GJ_G.grid(row=0, column=0)
slider_B_ZJ_GJ_G = ttk.Scale(tab1_RGB_B_G_ZJ, from_=0, to=255, orient=tk.HORIZONTAL, value=25, command=lambda v: slider_changed(v, label_value_B_ZJ_GJ_G))
slider_B_ZJ_GJ_G.grid(row=0, column=1)
label_value_B_ZJ_GJ_G = tk.Label(tab1_RGB_B_G_ZJ, text="25")
label_value_B_ZJ_GJ_G.grid(row=0, column=2)

label_B_JS_GJ_G = tk.Label(tab1_RGB_B_G_JS, text="值：")
label_B_JS_GJ_G.grid(row=0, column=0)
slider_B_JS_GJ_G = ttk.Scale(tab1_RGB_B_G_JS, from_=0, to=255, orient=tk.HORIZONTAL, value=25, command=lambda v: slider_changed(v, label_value_B_JS_GJ_G))
slider_B_JS_GJ_G.grid(row=0, column=1)
label_value_B_JS_GJ_G = tk.Label(tab1_RGB_B_G_JS, text="25")
label_value_B_JS_GJ_G.grid(row=0, column=2)

label_frame_B_GJ = ttk.LabelFrame(tab1_RGB_B, text="B值范围", labelanchor='n')
label_frame_B_GJ.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

label_B_start_GJ = tk.Label(label_frame_B_GJ, text="开始：")
label_B_start_GJ.grid(row=0, column=0)
slider_B_start_GJ = ttk.Scale(label_frame_B_GJ, from_=0, to=255, orient=tk.HORIZONTAL, value=25, command=lambda v: slider_changed(v, label_value_B_start_GJ))
slider_B_start_GJ.grid(row=0, column=1)
label_value_B_start_GJ = tk.Label(label_frame_B_GJ, text="25")
label_value_B_start_GJ.grid(row=0, column=2)

label_B_end_GJ = tk.Label(label_frame_B_GJ, text="结束：")
label_B_end_GJ.grid(row=1, column=0)
slider_B_end_GJ = ttk.Scale(label_frame_B_GJ, from_=0, to=255, orient=tk.HORIZONTAL, value=175, command=lambda v: slider_changed(v, label_value_B_end_GJ))
slider_B_end_GJ.grid(row=1, column=1)
label_value_B_end_GJ = tk.Label(label_frame_B_GJ, text="175")
label_value_B_end_GJ.grid(row=1, column=2)

book_TP_BL_SZ = 1.0
#图片
def select_image_file():
    global image_TP,book_TP_BL_SZ
    file_path = filedialog.askopenfilename(
        title="选择图片文件",
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")]
    )
    if file_path:
        file_name = file_path.split("/")[-1]
        if len(file_name) > 10:  # 如果文件名超过15个字符
            display_name = file_name[:5] + "..." + file_name[-5:]
        else:
            display_name = file_name
        label_value_TP_WJ_name.config(text=display_name)
        image_TP = Image.open(file_path).convert('RGBA')
        width, height = image_TP.size
        BL_TP = float(book_TP_BL.get())
        new_width = int(float(width*BL_TP))
        new_height = int(float(height*BL_TP))
        if new_width > 3840 or new_height > 2160:
            # 弹出对话框询问用户是否继续
            result = messagebox.askyesno(
                "图片尺寸警告",
                "选择的图片缩放后尺寸超过 3840x2160 像素，是否自动缩放后继续导入？"
            )
            if not result:
                image_TP = None
                label_value_TP_WJ_name.config(text="无文件")
                return
            
            if width*3 < 3841 and height*3 < 2161 :
                book_TP_BL_SZ = 3
                book_TP_BL.set(3.0)
            elif int(float(width*2.5)) < 3841 and int(float(height*2.5)) < 2161 :
                book_TP_BL_SZ = 2.5
                book_TP_BL.set(2.5)
            elif width*2 <= 3841 and height*2 < 2161 :
                book_TP_BL_SZ = 2
                book_TP_BL.set(2.0)
            elif int(float(width*1.75)) < 3841 and int(float(height*1.75)) < 2161 :
                book_TP_BL.set(1.75)
                book_TP_BL_SZ = 1.75
            elif int(float(width*1.5)) < 3841 and int(float(height*1.5)) < 2161 :
                book_TP_BL.set(1.5)
                book_TP_BL_SZ = 1.5
            elif int(float(width*1.25)) < 3841 and int(float(height*1.25)) < 2161 :
                book_TP_BL.set(1.25)
                book_TP_BL_SZ = 1.25
            elif width*1 <= 3841 and height*1 < 2161 :
                book_TP_BL.set(1.0)
                book_TP_BL_SZ = 1
            elif int(float(width*0.75)) < 3841 and int(float(height*0.75)) < 2161 :
                book_TP_BL.set(0.75)
                book_TP_BL_SZ = 0.75
            elif int(float(width*0.5)) < 3841 and int(float(height*0.5)) < 2161 :
                book_TP_BL.set(0.5)
                book_TP_BL_SZ = 0.5
            elif int(float(width*0.25)) < 3841 and int(float(height*0.25)) < 2161 :
                book_TP_BL.set(0.25)
                book_TP_BL_SZ = 0.25
            else:
                result = messagebox.askyesno(
                    "图片尺寸警告",
                    "自动缩放失败，请使用其他的工具进行缩放"
                )
                image_TP = None
                label_value_TP_WJ_name.config(text="无文件")
                return
                
            BL_TP = float(book_TP_BL.get())
            
        new_width = int(float(width*BL_TP))
        new_height = int(float(height*BL_TP))
        slider_QT_DX_X.set(new_width)
        print(f"Image dimensions: {new_width}x{new_height}")
        image_TP = image_TP.resize((new_width,new_height), Image.Resampling.LANCZOS)
        label_TP_ZW_3.config(text=f"当前图片尺寸: {new_width}x{new_height}")
        
        return file_path
#选择图片函数
def update_combobox(event):
    global image_TP,book_TP_BL_SZ
    # Get the selected value
    selected_value = bookChosen_TP_BL.get()
    # Print the selected value
    print(selected_value)
    if image_TP:
        # 进行图像处理，例如获取图像尺寸
        width, height = image_TP.size
        print(f"Image dimensions: {width}x{height}")
        BL_TP = float(book_TP_BL.get())
        new_width = int(float(width*BL_TP))
        new_height = int(float(height*BL_TP))
        if new_width > 3840 or new_height > 2160:
            messagebox.showwarning("图片尺寸警告", "缩放失败，尺寸过大")
            book_TP_BL.set(book_TP_BL_SZ)
            return
        image_TP = image_TP.resize((int(float(width*BL_TP)), int(float(height*BL_TP))), Image.Resampling.LANCZOS)
        book_TP_BL_SZ = BL_TP
        width, height = image_TP.size
        label_TP_ZW_3.config(text=f"当前图片尺寸: {width}x{height}")
        print(f"Image dimensions: {width}x{height}")
#缩放图片比例函数
label_frame_TP_XZ = ttk.LabelFrame(tab1_RGB_3, text="图片选择", labelanchor='n')
label_frame_TP_XZ.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

label_value_TP_WJ_name = tk.Label(label_frame_TP_XZ, text="无文件")
label_value_TP_WJ_name.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

btn_select_file = ttk.Button(label_frame_TP_XZ, text="选择文件", command=select_image_file)
btn_select_file.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

label_frame_TP_FD = ttk.LabelFrame(tab1_RGB_3, text="图片缩放", labelanchor='n')
label_frame_TP_FD.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Create a StringVar for the combobox
book_TP_BL = tk.StringVar()
# Create the combobox
bookChosen_TP_BL = ttk.Combobox(label_frame_TP_FD, width=12, textvariable=book_TP_BL)
bookChosen_TP_BL['values'] = (0.25,0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0)
bookChosen_TP_BL.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
bookChosen_TP_BL.current(3)  # Set the initial display value
# Bind the combobox selection change event
bookChosen_TP_BL.bind("<<ComboboxSelected>>", update_combobox)
# Set the combobox to readonly mode
bookChosen_TP_BL.config(state='readonly')

#展位
frame_TP_ZW = ttk.Frame(tab1_RGB_3)
frame_TP_ZW.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

label_TP_ZW_1 = tk.Label(frame_TP_ZW, text="缩放基于当前图片尺寸")
label_TP_ZW_1.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_TP_ZW_2 = tk.Label(frame_TP_ZW, text="缩放后的图片不能超过3840x2160",fg = "red")
label_TP_ZW_2.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_TP_ZW_3 = tk.Label(frame_TP_ZW, text="")
label_TP_ZW_3.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_TP_ZW_4 = tk.Label(frame_TP_ZW, text="")
label_TP_ZW_4.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_frame_CC = ttk.LabelFrame(label_frame_FK, text="尺寸取值范围", labelanchor='n')
label_frame_CC.pack(padx=5, pady=10, fill=tk.BOTH, expand=True)

tabControl_CC = ttk.Notebook(label_frame_CC)
tab1_CC_1 = ttk.Frame(tabControl_CC)
tabControl_CC.add(tab1_CC_1, text='普通')
tab1_CC_2 = ttk.Frame(tabControl_CC)
tabControl_CC.add(tab1_CC_2, text='比例')
tab1_CC_3 = ttk.Frame(tabControl_CC)
tabControl_CC.add(tab1_CC_3, text='固定')
tabControl_CC.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

#普通
label_frame_FK_X_PT = ttk.LabelFrame(tab1_CC_1, text="X值范围", labelanchor='n')
label_frame_FK_X_PT.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_X_start_PT = tk.Label(label_frame_FK_X_PT, text="开始：")
label_X_start_PT.grid(row=0, column=0)
slider_X_start_PT = ttk.Scale(label_frame_FK_X_PT, from_=10, to=999, orient=tk.HORIZONTAL, value=10, command=lambda v: slider_changed(v, label_value_X_start_PT))
slider_X_start_PT.grid(row=0, column=1)
label_value_X_start_PT = tk.Label(label_frame_FK_X_PT, text="10")
label_value_X_start_PT.grid(row=0, column=2)

label_X_end_PT = tk.Label(label_frame_FK_X_PT, text="结束：")
label_X_end_PT.grid(row=1, column=0)
slider_X_end_PT = ttk.Scale(label_frame_FK_X_PT, from_=10, to=999, orient=tk.HORIZONTAL, value=100, command=lambda v: slider_changed(v, label_value_X_end_PT))
slider_X_end_PT.grid(row=1, column=1)
label_value_X_end_PT = tk.Label(label_frame_FK_X_PT, text="100")
label_value_X_end_PT.grid(row=1, column=2)

label_frame_FK_Y_PT = ttk.LabelFrame(tab1_CC_1, text="Y值范围", labelanchor='n')
label_frame_FK_Y_PT.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_Y_start_PT = tk.Label(label_frame_FK_Y_PT, text="开始：")
label_Y_start_PT.grid(row=0, column=0)
slider_Y_start_PT = ttk.Scale(label_frame_FK_Y_PT, from_=10, to=999, orient=tk.HORIZONTAL, value=10, command=lambda v: slider_changed(v, label_value_Y_start_PT))
slider_Y_start_PT.grid(row=0, column=1)
label_value_Y_start_PT = tk.Label(label_frame_FK_Y_PT, text="10")
label_value_Y_start_PT.grid(row=0, column=2)

label_Y_end_PT = tk.Label(label_frame_FK_Y_PT, text="结束：")
label_Y_end_PT.grid(row=1, column=0)
slider_Y_end_PT = ttk.Scale(label_frame_FK_Y_PT, from_=10, to=999, orient=tk.HORIZONTAL, value=100, command=lambda v: slider_changed(v, label_value_Y_end_PT))
slider_Y_end_PT.grid(row=1, column=1)
label_value_Y_end_PT = tk.Label(label_frame_FK_Y_PT, text="100")
label_value_Y_end_PT.grid(row=1, column=2)

#比例
label_frame_JZ_BL = ttk.LabelFrame(tab1_CC_2, text="基准值", labelanchor='n')
label_frame_JZ_BL.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

radio_value_JZ_BL = tk.StringVar()
radio_JZ_BL_X = ttk.Radiobutton(label_frame_JZ_BL, text="X", variable=radio_value_JZ_BL, value="1")
radio_JZ_BL_X.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

radio_JZ_BL_Y = ttk.Radiobutton(label_frame_JZ_BL, text="Y", variable=radio_value_JZ_BL, value="2")
radio_JZ_BL_Y.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

radio_value_JZ_BL.set(1)

label_frame_FK_JZ_BL = ttk.LabelFrame(tab1_CC_2, text="基准值范围", labelanchor='n')
label_frame_FK_JZ_BL.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_JZ_start_BL = tk.Label(label_frame_FK_JZ_BL, text="开始：")
label_JZ_start_BL.grid(row=0, column=0)
slider_JZ_start_BL = ttk.Scale(label_frame_FK_JZ_BL, from_=10, to=999, orient=tk.HORIZONTAL, value=10, command=lambda v: slider_changed(v, label_value_JZ_start_BL))
slider_JZ_start_BL.grid(row=0, column=1)
label_value_JZ_start_BL = tk.Label(label_frame_FK_JZ_BL, text="10")
label_value_JZ_start_BL.grid(row=0, column=2)

label_JZ_end_BL = tk.Label(label_frame_FK_JZ_BL, text="结束：")
label_JZ_end_BL.grid(row=1, column=0)
slider_JZ_end_BL = ttk.Scale(label_frame_FK_JZ_BL, from_=10, to=999, orient=tk.HORIZONTAL, value=100, command=lambda v: slider_changed(v, label_value_JZ_end_BL))
slider_JZ_end_BL.grid(row=1, column=1)
label_value_JZ_end_BL = tk.Label(label_frame_FK_JZ_BL, text="100")
label_value_JZ_end_BL.grid(row=1, column=2)

label_frame_BL = ttk.LabelFrame(tab1_CC_2, text="比例", labelanchor='n')
label_frame_BL.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

book_BL = tk.StringVar()
bookChosen_BL = ttk.Combobox(label_frame_BL, width=12, textvariable=book_BL)
bookChosen_BL['values'] = (0.1,0.2,0.25,0.5,0.75,0.8,1.0,1.2,1.25,1.3,1.5,1.75,2.0,2.25,2.5,2.75,3.0)
bookChosen_BL.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
bookChosen_BL.current(6)  #设置初始显示值，值为元组['values']的下标
bookChosen_BL.config(state='readonly')  #设为只读模式

#固定
label_frame_JZ_GD = ttk.LabelFrame(tab1_CC_3, text="基准值", labelanchor='n')
label_frame_JZ_GD.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

radio_value_JZ_GD = tk.StringVar()
radio_JZ_GD_X = ttk.Radiobutton(label_frame_JZ_GD, text="X", variable=radio_value_JZ_GD, value="1")
radio_JZ_GD_X.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

radio_JZ_GD_Y = ttk.Radiobutton(label_frame_JZ_GD, text="Y", variable=radio_value_JZ_GD, value="2")
radio_JZ_GD_Y.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

radio_value_JZ_GD.set(1)

label_frame_FK_JZ_GD = ttk.LabelFrame(tab1_CC_3, text="基准值范围", labelanchor='n')
label_frame_FK_JZ_GD.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_JZ_start_GD = tk.Label(label_frame_FK_JZ_GD, text="开始：")
label_JZ_start_GD.grid(row=0, column=0)
slider_JZ_start_GD = ttk.Scale(label_frame_FK_JZ_GD, from_=10, to=999, orient=tk.HORIZONTAL, value=10, command=lambda v: slider_changed(v, label_value_JZ_start_GD))
slider_JZ_start_GD.grid(row=0, column=1)
label_value_JZ_start_GD = tk.Label(label_frame_FK_JZ_GD, text="10")
label_value_JZ_start_GD.grid(row=0, column=2)

label_JZ_end_GD = tk.Label(label_frame_FK_JZ_GD, text="结束：")
label_JZ_end_GD.grid(row=1, column=0)
slider_JZ_end_GD = ttk.Scale(label_frame_FK_JZ_GD, from_=10, to=999, orient=tk.HORIZONTAL, value=100, command=lambda v: slider_changed(v, label_value_JZ_end_GD))
slider_JZ_end_GD.grid(row=1, column=1)
label_value_JZ_end_GD = tk.Label(label_frame_FK_JZ_GD, text="100")
label_value_JZ_end_GD.grid(row=1, column=2)

label_frame_FK_ZJ_GD = ttk.LabelFrame(tab1_CC_3, text="增加设置", labelanchor='n')
label_frame_FK_ZJ_GD.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_ZJ_start_GD = tk.Label(label_frame_FK_ZJ_GD, text="增加：")
label_ZJ_start_GD.grid(row=0, column=0)
slider_ZJ_start_GD = ttk.Scale(label_frame_FK_ZJ_GD, from_=1, to=999, orient=tk.HORIZONTAL, value=100, command=lambda v: slider_changed(v, label_value_ZJ_start_GD))
slider_ZJ_start_GD.grid(row=0, column=1)
label_value_ZJ_start_GD = tk.Label(label_frame_FK_ZJ_GD, text="100")
label_value_ZJ_start_GD.grid(row=0, column=2)

label_frame_QT = ttk.LabelFrame(root, text="其他设置", labelanchor='n')
label_frame_QT.grid(row=1, column=0)

label_frame_DX = tk.LabelFrame(label_frame_QT, text="图片大小", labelanchor='n')
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

def BL_panduan(sz):
    if sz == "010":
        return 0.1
    elif sz == "020":
        return 0.2
    elif sz == "025":
        return 0.25
    elif sz == "050":
        return 0.5
    elif sz == "075":
        return 0.75
    elif sz == "080":
        return 0.8
    elif sz == "100":
        return 1.0
    elif sz == "120":
        return 1.2
    elif sz == "125":
        return 1.25
    elif sz == "130":
        return 1.3
    elif sz == "150":
        return 1.5
    elif sz == "175":
        return 1.75
    elif sz == "200":
        return 2.0
    elif sz == "225":
        return 2.25
    elif sz == "250":
        return 2.5
    elif sz == "275":
        return 2.75
    elif sz == "300":
        return 3.0
    else:
        return -1

def FX_ZT():
    clipboard_content = pyperclip.paste()
    print(clipboard_content)
    if len(clipboard_content) == 14:
        print("判断字符长度通过")
        if bool(re.match(r'[0-9a-fA-F]+$', clipboard_content)):
            print("判断字符内容通过")
            if int(clipboard_content[0]) == 0:
                print("普通")
                tabControl_RGB.select(0)
                slider_R_start.set(int(clipboard_content[1:3], 16))
                slider_R_end.set(int(clipboard_content[3:5], 16))
                slider_G_start.set(int(clipboard_content[5:7], 16))
                slider_G_end.set(int(clipboard_content[7:9], 16))
                slider_B_start.set(int(clipboard_content[9:11], 16))
                slider_B_end.set(int(clipboard_content[11:13], 16))
            elif int(clipboard_content[0]) == 1:
                print("高级")
                tabControl_RGB.select(1)
                if int(clipboard_content[1]) == 0:
                    print("R为基准")
                    tabControl_RGB_GJ.select(0)
                    slider_R_start_GJ.set(int(clipboard_content[2:4], 16))
                    slider_R_end_GJ.set(int(clipboard_content[4:6], 16))
                    if int(clipboard_content[6]) == 0:
                        tabControl_RGB_GJ_R_G.select(0)
                        print("比例")
                        print(BL_panduan(clipboard_content[7:10]))
                        if BL_panduan(clipboard_content[7:10]) == -1:
                            messagebox.showwarning("警告", "读取失败！")
                            return 0
                        bookChosen_BL_R_G.set(BL_panduan(clipboard_content[7:10]))
                    elif int(clipboard_content[6]) == 1:
                        tabControl_RGB_GJ_R_G.select(1)
                        if int(clipboard_content[7]) == 0:
                            slider_R_ZJ_GJ_G.set(clipboard_content[8:10])
                        else:
                            slider_R_ZJ_GJ_G.set(clipboard_content[7:10])
                    elif int(clipboard_content[6]) == 2:
                        tabControl_RGB_GJ_R_G.select(2)
                        if int(clipboard_content[7]) == 0:
                            slider_R_JS_GJ_G.set(clipboard_content[8:10])
                        else:
                            slider_R_JS_GJ_G.set(clipboard_content[7:10])
                    else:
                        print("读取失败")
                        messagebox.showwarning("警告", "读取失败！")
                        return 0
                    if int(clipboard_content[10]) == 0:
                        tabControl_RGB_GJ_R_B.select(0)
                        print("比例")
                        if BL_panduan(clipboard_content[11:14]) == -1:
                            messagebox.showwarning("警告", "读取失败！")
                            return 0
                        bookChosen_BL_R_B.set(BL_panduan(clipboard_content[11:14]))
                    elif int(clipboard_content[10]) == 1:
                        tabControl_RGB_GJ_R_B.select(1)
                        if int(clipboard_content[11]) == 0:
                            slider_R_ZJ_GJ_B.set(clipboard_content[12:14])
                        else:
                            slider_R_ZJ_GJ_B.set(clipboard_content[11:14])
                    elif int(clipboard_content[10]) == 2:
                        tabControl_RGB_GJ_R_B.select(2)
                        if int(clipboard_content[11]) == 0:
                            slider_R_JS_GJ_B.set(clipboard_content[12:14])
                        else:
                            slider_R_JS_GJ_B.set(clipboard_content[11:14])
                    else:
                        print("读取失败")
                        messagebox.showwarning("警告", "读取失败！")
                        return 0
                elif int(clipboard_content[1]) == 1:
                    print("G为基准")
                    tabControl_RGB_GJ.select(1)
                    if int(clipboard_content[2]) == 0:
                        tabControl_RGB_GJ_G_R.select(0)
                        print("比例")
                        print(BL_panduan(clipboard_content[3:6]))
                        if BL_panduan(clipboard_content[3:6]) == -1:
                            messagebox.showwarning("警告", "读取失败！")
                            return 0
                        bookChosen_BL_G_R.set(BL_panduan(clipboard_content[3:6]))
                    elif int(clipboard_content[2]) == 1:
                        tabControl_RGB_GJ_G_R.select(1)
                        if int(clipboard_content[3]) == 0:
                            slider_G_ZJ_GJ_R.set(clipboard_content[4:6])
                        else:
                            slider_G_ZJ_GJ_R.set(clipboard_content[3:6])
                    elif int(clipboard_content[2]) == 2:
                        tabControl_RGB_GJ_G_R.select(2)
                        if int(clipboard_content[3]) == 0:
                            slider_G_JS_GJ_R.set(clipboard_content[4:6])
                        else:
                            slider_G_JS_GJ_R.set(clipboard_content[3:6])
                    else:
                        messagebox.showwarning("警告", "读取失败！")
                        return 0
                    slider_G_start_GJ.set(int(clipboard_content[6:8], 16))
                    slider_G_end_GJ.set(int(clipboard_content[8:10], 16))
                    if int(clipboard_content[10]) == 0:
                        tabControl_RGB_GJ_G_B.select(0)
                        print("比例")
                        if BL_panduan(clipboard_content[11:14]) == -1:
                            messagebox.showwarning("警告", "读取失败！")
                            return 0
                        bookChosen_BL_G_B.set(BL_panduan(clipboard_content[11:14]))
                    elif int(clipboard_content[10]) == 1:
                        tabControl_RGB_GJ_G_B.select(1)
                        if int(clipboard_content[11]) == 0:
                            slider_G_ZJ_GJ_B.set(clipboard_content[12:14])
                        else:
                            slider_G_ZJ_GJ_B.set(clipboard_content[11:14])
                    elif int(clipboard_content[10]) == 2:
                        tabControl_RGB_GJ_G_B.select(2)
                        if int(clipboard_content[11]) == 0:
                            slider_G_JS_GJ_B.set(clipboard_content[12:14])
                        else:
                            slider_G_JS_GJ_B.set(clipboard_content[11:14])
                    else:
                        print("读取失败")
                        messagebox.showwarning("警告", "读取失败！")
                        return 0
                    
                elif int(clipboard_content[1]) == 2:
                    print("B为基准")
                    tabControl_RGB_GJ.select(2)
                    if int(clipboard_content[2]) == 0:
                        tabControl_RGB_GJ_B_R.select(0)
                        print("比例")
                        print(BL_panduan(clipboard_content[3:6]))
                        if BL_panduan(clipboard_content[3:6]) == -1:
                            messagebox.showwarning("警告", "读取失败！")
                            return 0
                        bookChosen_BL_B_R.set(BL_panduan(clipboard_content[3:6]))
                    elif int(clipboard_content[2]) == 1:
                        tabControl_RGB_GJ_B_R.select(1)
                        if int(clipboard_content[3]) == 0:
                            slider_B_ZJ_GJ_R.set(clipboard_content[4:6])
                        else:
                            slider_B_ZJ_GJ_R.set(clipboard_content[3:6])
                    elif int(clipboard_content[2]) == 2:
                        tabControl_RGB_GJ_B_R.select(2)
                        if int(clipboard_content[3]) == 0:
                            slider_B_JS_GJ_R.set(clipboard_content[4:6])
                        else:
                            slider_B_JS_GJ_R.set(clipboard_content[3:6])
                    else:
                        messagebox.showwarning("警告", "读取失败！")
                        return 0
                    if int(clipboard_content[6]) == 0:
                        tabControl_RGB_GJ_B_G.select(0)
                        print("比例")
                        print(BL_panduan(clipboard_content[7:10]))
                        if BL_panduan(clipboard_content[7:10]) == -1:
                            messagebox.showwarning("警告", "读取失败！")
                            return 0
                        bookChosen_BL_B_G.set(BL_panduan(clipboard_content[7:10]))
                    elif int(clipboard_content[6]) == 1:
                        tabControl_RGB_GJ_B_G.select(1)
                        if int(clipboard_content[7]) == 0:
                            slider_B_ZJ_GJ_G.set(clipboard_content[8:10])
                        else:
                            slider_B_ZJ_GJ_G.set(clipboard_content[7:10])
                    elif int(clipboard_content[6]) == 2:
                        tabControl_RGB_GJ_B_G.select(2)
                        if int(clipboard_content[7]) == 0:
                            slider_B_JS_GJ_G.set(clipboard_content[8:10])
                        else:
                            slider_B_JS_GJ_G.set(clipboard_content[7:10])
                    else:
                        print("读取失败")
                        messagebox.showwarning("警告", "读取失败！")
                        return 0
                    slider_B_start_GJ.set(int(clipboard_content[10:12], 16))
                    slider_B_end_GJ.set(int(clipboard_content[12:14], 16))
                else:
                    print("读取失败")
                    messagebox.showwarning("警告", "读取失败！")
                    return 0
            else:
                print("读取失败")
                messagebox.showwarning("警告", "读取失败！")
                return 0
        else:
            messagebox.showwarning("警告", "判断不通过！")
            return 0
    else:
        messagebox.showwarning("警告", "判断不通过！")
        return 0

def FX_FZ():
    # 获取当前选中的标签页的索引
    current_tab_index_RGB = tabControl_RGB.index(tabControl_RGB.select())
    if current_tab_index_RGB == 0:
        pyperclip.copy(str(current_tab_index_RGB)+
                       str(hex(round(slider_R_start.get()))[2:].upper())+
                       str(hex(round(slider_R_end.get()))[2:].upper())+
                       str(hex(round(slider_G_start.get()))[2:].upper())+
                       str(hex(round(slider_G_end.get()))[2:].upper())+
                       str(hex(round(slider_B_start.get()))[2:].upper())+
                       str(hex(round(slider_B_end.get()))[2:].upper())+"0")#补齐14位
        return 0
    elif current_tab_index_RGB == 1:
        FZNT = str(current_tab_index_RGB)
        current_tab_index_RGB_GJ = tabControl_RGB_GJ.index(tabControl_RGB_GJ.select())
        FZNT = FZNT + str(current_tab_index_RGB_GJ)
        if current_tab_index_RGB_GJ == 0:
            FZNT = FZNT + str(hex(round(slider_R_start_GJ.get()))[2:].upper()) + str(hex(round(slider_R_end_GJ.get()))[2:].upper())
            current_tab_index_RGB_GJ_R_G = tabControl_RGB_GJ_R_G.index(tabControl_RGB_GJ_R_G.select())
            FZNT = FZNT + str(current_tab_index_RGB_GJ_R_G)
            if current_tab_index_RGB_GJ_R_G == 0:
                FZNT = FZNT + str(int(float(bookChosen_BL_R_G.get())*100))
            elif current_tab_index_RGB_GJ_R_G == 1:
                if round(slider_R_ZJ_GJ_G.get()) <100:
                    FZNT = FZNT + "0"
                FZNT = FZNT + str(round(slider_R_ZJ_GJ_G.get()))
            else:
                if round(slider_R_JS_GJ_G.get()) <100:
                    FZNT = FZNT + "0"
                FZNT = FZNT + str(round(slider_R_JS_GJ_G.get()))
            current_tab_index_RGB_GJ_R_B = tabControl_RGB_GJ_R_B.index(tabControl_RGB_GJ_R_B.select())
            FZNT = FZNT + str(current_tab_index_RGB_GJ_R_B)
            if current_tab_index_RGB_GJ_R_B == 0:
                FZNT = FZNT + str(int(float(bookChosen_BL_R_B.get())*100))
            elif current_tab_index_RGB_GJ_R_B == 1:
                if round(slider_R_ZJ_GJ_B.get()) <100:
                    FZNT = FZNT + "0"
                FZNT = FZNT + str(round(slider_R_ZJ_GJ_B.get()))
            else:
                if round(slider_R_JS_GJ_B.get()) <100:
                    FZNT = FZNT + "0"
                FZNT = FZNT + str(round(slider_R_JS_GJ_B.get()))
            pyperclip.copy(FZNT)
            return 0
        elif current_tab_index_RGB_GJ == 1:
            current_tab_index_RGB_GJ_G_R = tabControl_RGB_GJ_G_R.index(tabControl_RGB_GJ_G_R.select())
            FZNT = FZNT + str(current_tab_index_RGB_GJ_G_R)
            if current_tab_index_RGB_GJ_G_R == 0:
                FZNT = FZNT + str(int(float(bookChosen_BL_G_R.get())*100))
            elif current_tab_index_RGB_GJ_G_R == 1:
                if round(slider_G_ZJ_GJ_R.get()) <100:
                    FZNT = FZNT + "0"
                FZNT = FZNT + str(round(slider_G_ZJ_GJ_R.get()))
            else:
                if round(slider_G_JS_GJ_R.get()) <100:
                    FZNT = FZNT + "0"
                FZNT = FZNT + str(round(slider_G_JS_GJ_R.get()))
            FZNT = FZNT + str(hex(round(slider_G_start_GJ.get()))[2:].upper()) + str(hex(round(slider_G_end_GJ.get()))[2:].upper())
            current_tab_index_RGB_GJ_G_B = tabControl_RGB_GJ_G_B.index(tabControl_RGB_GJ_G_B.select())
            FZNT = FZNT + str(current_tab_index_RGB_GJ_G_B)
            if current_tab_index_RGB_GJ_G_B == 0:
                FZNT = FZNT + str(int(float(bookChosen_BL_G_B.get())*100))
            elif current_tab_index_RGB_GJ_G_B == 1:
                if round(slider_G_ZJ_GJ_B.get()) <100:
                    FZNT = FZNT + "0"
                FZNT = FZNT + str(round(slider_G_ZJ_GJ_B.get()))
            else:
                if round(slider_G_JS_GJ_B.get()) <100:
                    FZNT = FZNT + "0"
                FZNT = FZNT + str(round(slider_G_JS_GJ_B.get()))
            pyperclip.copy(FZNT)
            return 0
        else:
            current_tab_index_RGB_GJ_B_R = tabControl_RGB_GJ_B_R.index(tabControl_RGB_GJ_B_R.select())
            FZNT = FZNT + str(current_tab_index_RGB_GJ_B_R)
            if current_tab_index_RGB_GJ_B_R == 0:
                FZNT = FZNT + str(int(float(bookChosen_BL_B_R.get())*100))
            elif current_tab_index_RGB_GJ_B_R == 1:
                if round(slider_B_ZJ_GJ_R.get()) <100:
                    FZNT = FZNT + "0"
                FZNT = FZNT + str(round(slider_B_ZJ_GJ_R.get()))
            else:
                if round(slider_B_JS_GJ_R.get()) <100:
                    FZNT = FZNT + "0"
                FZNT = FZNT + str(round(slider_B_JS_GJ_R.get()))
            current_tab_index_RGB_GJ_B_G = tabControl_RGB_GJ_B_G.index(tabControl_RGB_GJ_B_G.select())
            FZNT = FZNT + str(current_tab_index_RGB_GJ_B_G)
            if current_tab_index_RGB_GJ_B_G == 0:
                FZNT = FZNT + str(int(float(bookChosen_BL_B_G.get())*100))
            elif current_tab_index_RGB_GJ_B_G == 1:
                if round(slider_B_ZJ_GJ_G.get()) <100:
                    FZNT = FZNT + "0"
                FZNT = FZNT + str(round(slider_B_ZJ_GJ_G.get()))
            else:
                if round(slider_B_JS_GJ_G.get()) <100:
                    FZNT = FZNT + "0"
                FZNT = FZNT + str(round(slider_B_JS_GJ_G.get()))
            FZNT = FZNT + str(hex(round(slider_B_start_GJ.get()))[2:].upper()) + str(hex(round(slider_B_end_GJ.get()))[2:].upper())
            pyperclip.copy(FZNT)
            return 0
    messagebox.showwarning("警告", "图片模式不能分享")
    return 0


label_frame_FX = ttk.LabelFrame(root, text="分享", labelanchor='n')
label_frame_FX.grid(row=2, column=0, stick="EW")

button_FX_FZ = ttk.Button(label_frame_FX, text="复制", command=FX_FZ)
button_FX_FZ.pack(padx=3, pady=3, fill=tk.BOTH, expand=True,side='left')

button_FX_ZT = ttk.Button(label_frame_FX, text="粘贴", command=FX_ZT)
button_FX_ZT.pack(padx=3, pady=3, fill=tk.BOTH, expand=True,side='right')

button_QD = ttk.Button(root, text="确定", command=main)
button_QD.grid(row=3, column=0, sticky='nsew')

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
    chinese_name = ttk.Label(frame, text="彩矩工坊专业版", font=("Arial", 18, "bold"), foreground="black")
    chinese_name.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # 英文名字
    english_name = ttk.Label(frame, text="ColorRectForge Pro", font=("Arial", 14,), foreground="black")
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
button_GY.grid(row=4, column=0, sticky='nsew')

root.mainloop()

# pyinstaller --onefile --noconsole --icon=logopro.ico --add-data "ColorRectForgecklogo.ico;." ColorRectForgePro.py