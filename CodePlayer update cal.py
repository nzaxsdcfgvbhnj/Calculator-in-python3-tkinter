from tkinter import *
from tkinter import ttk, messagebox

# تحسين الواجهة باستخدام ThemedTk لجعل التصميم أكثر حداثة واحترافية
me = Tk()
me.geometry("400x500")
me.title("Calculator")
me.resizable(False, False)  # منع تغيير حجم النافذة

# إعداد ألوان
BACKGROUND_COLOR = "#1e1e1e"  # لون خلفية النافذة
LABEL_COLOR = "#2196f3"        # لون خلفية العنوان
TEXT_COLOR = "#ffffff"         # لون النص في مربع الإدخال
BUTTON_COLOR = "#1976d2"       # لون أزرار العمليات
BUTTON_HOVER_COLOR = "#1565c0" # لون الأزرار عند التحويم
ENTRY_BACKGROUND = "#333333"   # لون خلفية مربع الإدخال

# إضافة شريط القوائم
menubar = Menu(me)
me.config(menu=menubar)

# إضافة قائمة Help
def show_help():
    messagebox.showinfo("Help", "This is a simple calculator.\n\n"
                                  "1. Use the number buttons to input numbers.\n"
                                  "2. Use the operation buttons (X, /, +, -) to perform calculations.\n"
                                  "3. Press '=' to see the result.\n"
                                  "4. Use 'CE' to clear the input.\n"
                                  "5. You can keep this window always on top using the 'Always on Top' option.")

help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="Help", command=show_help)
menubar.add_cascade(label="Options", menu=help_menu)

# إضافة خيار Always on Top
def toggle_always_on_top():
    if me.attributes('-topmost'):
        me.attributes('-topmost', False)
    else:
        me.attributes('-topmost', True)

# إضافة الخيار إلى القائمة
help_menu.add_separator()
help_menu.add_command(label="Always on Top", command=toggle_always_on_top)

# عنوان الحاسبة
melabel = Label(me, text="CALCULATOR", bg=LABEL_COLOR, fg=TEXT_COLOR, font=("Arial", 30, 'bold'))
melabel.grid(row=0, column=0, columnspan=4, pady=20)

# صندوق الإدخال
textin = StringVar()
operator = ""

def clickbut(number):
    global operator
    operator = operator + str(number)
    textin.set(operator)

def equlbut():
    global operator
    try:
        result = str(eval(operator.replace('X', '*')))  # التعامل مع 'X' كرمز للضرب
        textin.set(result)
        operator = ""
    except:
        textin.set("Error")
        operator = ""

def clrbut():
    global operator
    operator = ""
    textin.set("")

# تصميم مربع النص باستخدام grid بدلاً من pack
metext = Entry(me, font=("Arial", 24), textvar=textin, width=25, bd=10, bg=ENTRY_BACKGROUND, fg=TEXT_COLOR, justify='right', relief=SUNKEN)
metext.grid(row=1, column=0, columnspan=4, pady=10)

# إعداد خصائص الأزرار
button_config = {
    "padx": 20,
    "pady": 20,
    "bd": 5,
    "bg": BUTTON_COLOR,
    "fg": TEXT_COLOR,
    "font": ("Arial", 22),  # تكبير حجم الخط الخاص بالأزرار
}

def on_enter(e):
    e.widget['bg'] = BUTTON_HOVER_COLOR  # تغيير لون الزر عند التحويم

def on_leave(e):
    e.widget['bg'] = BUTTON_COLOR  # إعادة لون الزر عند الابتعاد عنه

# تنظيم الأزرار في شكل شبكة
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('X', 3, 3),  # استخدام "X" بدلًا من "*"
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        Button(me, text=text, command=equlbut, **button_config).grid(row=row, column=col, sticky="nsew")
    elif text == 'X':  # التعامل مع "X" كرمز الضرب
        Button(me, text=text, command=lambda: clickbut('X'), **button_config).grid(row=row, column=col, sticky="nsew")
    else:
        btn = Button(me, text=text, command=lambda t=text: clickbut(t), **button_config)
        btn.grid(row=row, column=col, sticky="nsew")
        btn.bind("<Enter>", on_enter)  # إضافة حدث التحويم
        btn.bind("<Leave>", on_leave)  # إضافة حدث الابتعاد

# زر المسح
Button(me, text="CE", command=clrbut, **button_config).grid(row=2, column=3, sticky="nsew")

# إعداد الشبكة لجعل الأزرار تتوسع بشكل متساوٍ عند تغيير حجم النافذة (اختياري)
for i in range(6):
    me.grid_rowconfigure(i, weight=1)
for i in range(4):
    me.grid_columnconfigure(i, weight=1)

me.config(bg=BACKGROUND_COLOR)  # تعيين لون خلفية النافذة
me.mainloop()
