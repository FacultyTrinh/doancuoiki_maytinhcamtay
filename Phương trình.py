import math as m
from tkinter import messagebox
from tkinter import *
import tkinter as tk

btn_paremeters = {
   'padx': 2,
   'pady': 2,
   'bd': 4,
   'fg': 'white',
   'bg': 'grey',
   'font': ('arial', 15),
   'width': 5,
   'height': 1
}
# 9 nút số
btn_paremeters_2 = {
   'padx': 2,
   'pady': 2,
   'bd': 4,
   'fg': 'black',
   'bg': 'powder blue',
   'font': ('arial', 15),
   'width': 5,
   'height': 1
}
btn_paremeters_3 = {
   'padx': 2,
   'pady': 2,
   'bd': 4,
   'fg': 'black',
   'bg': 'pink',
   'font': ('arial', 15),
   'width': 5,
   'height': 1
}
π = m.pi
e=m.exp(1)

def sin(x):
   return m.sin(m.radians(x))

def cos(x):
   return m.cos(m.radians(x))

def tan(x):
   return m.tan(m.radians(x))

def giai_thua(x):
   return m.factorial(x)

def so_e():
   return m.exp(1)

def so_pi():
   return m.pi

def log(x):
   return m.log10(x)

def ln(x):
   return m.log(x)

#Khai báo thuộc tính của đối tượng
class Sci_Calculator:
   def __init__(self, master):
       self.master = master
       master.title('Scientific Calculator')
       self.expression = ""    #chuỗi lưu trữ biểu thức toán học
       self.result = ""    #chuỗi lưu trữ kết lỗi
       self.input_txt = tk.StringVar()


       # khung giao diện
       MainFrame = tk.Frame(self.master, bg='light gray')
       MainFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


       # viền thanh hiện dữ liệu
       top_frame = tk.Frame(MainFrame, height=100, width=100, bg='black', bd=2)
       top_frame.pack(side=tk.TOP)


       # khung cho nút
       bottom_frame = tk.Frame(MainFrame, height=100, width=100, bg='light grey')
       bottom_frame.pack(side=tk.TOP)


       # phần trong thanh hiện dữ liệu
       self.screen = tk.Entry(top_frame, width=80, background="black", foreground="white", textvariable=self.input_txt,
                              bd=6, justify='right')
       self.screen.pack()


       # Hàng 1
       self.binh_phuong = tk.Button(bottom_frame, **btn_paremeters, text='x²', command=self.binh_phuong_btn)
       self.binh_phuong.grid(row=3, column=0)


       self.lap_phuong = tk.Button(bottom_frame, text='x³', **btn_paremeters, command=self.lap_phuong_btn)
       self.lap_phuong.grid(row=3, column=1)


       self.x_mu_n = tk.Button(bottom_frame, **btn_paremeters, text='xⁿ', command=self.x_mu_n_btn)
       self.x_mu_n.grid(row=3, column=2)


       self.luy_thua_cua_10 = tk.Button(bottom_frame, text='10ˣ', **btn_paremeters, command=self.luy_thua_cua_10_btn)
       self.luy_thua_cua_10.grid(row=3, column=3)


       self.e_mu_x = tk.Button(bottom_frame, text='eˣ', **btn_paremeters, command=self.e_mu_x_btn)
       self.e_mu_x.grid(row=3, column=4)


       #Hàng 2
       self.can_bac_2 = tk.Button(bottom_frame, **btn_paremeters, text='√', command=self.can_bac_2_btn)
       self.can_bac_2.grid(row=4, column=0)


       self.can_bac_3 = tk.Button(bottom_frame, text='∛', **btn_paremeters, command=self.can_bac_3_btn)
       self.can_bac_3.grid(row=4, column=1)


       self.can_bac_n = tk.Button(bottom_frame, text='ⁿ√', **btn_paremeters, command=self.can_bac_n_btn)
       self.can_bac_n.grid(row=4, column=2)


       self.log = tk.Button(bottom_frame, **btn_paremeters, text='log', command=self.log_btn)
       self.log.grid(row=4, column=3)


       self.ln = tk.Button(bottom_frame, **btn_paremeters, text='ln', command=self.ln_btn)
       self.ln.grid(row=4, column=4)


       #Hàng3
       self.giai_thua = tk.Button(bottom_frame, text='n!', **btn_paremeters, command=self.giai_thua_btn)
       self.giai_thua.grid(row=5, column=0)


       self.chia_lay_du = tk.Button(bottom_frame, **btn_paremeters, text='mod', command=self.chia_lay_du_btn)
       self.chia_lay_du.grid(row=5, column=1)


       self.chia_lay_nguyen = tk.Button(bottom_frame, **btn_paremeters, text='div', command=self.chia_lay_nguyen_btn)
       self.chia_lay_nguyen.grid(row=5, column=2)


       self.ngoac_trai = tk.Button(bottom_frame, **btn_paremeters, text='(', command=self.ngoac_trai_btn)
       self.ngoac_trai.grid(row=5, column=3)


       self.ngoac_phai = tk.Button(bottom_frame, **btn_paremeters, text=')', command=self.ngoac_phai_btn)
       self.ngoac_phai.grid(row=5, column=4)


       #Hàng4
       #đổi dấu số
       self.doi_dau = tk.Button(bottom_frame, **btn_paremeters, text='( - )',
                                           command=self.doi_dau_btn)
       self.doi_dau.grid(row=6, column=0)
       #giá trị sin
       self.sin = tk.Button(bottom_frame, **btn_paremeters, text='Sin', command=self.sin_btn)
       self.sin.grid(row=6, column=1)
       # giá trị cos
       self.cos = tk.Button(bottom_frame, **btn_paremeters, text='Cos', command=self.cos_btn)
       self.cos.grid(row=6, column=2)
       # giá trị tan
       self.tan = tk.Button(bottom_frame, **btn_paremeters, text='Tan', command=self.tan_btn)
       self.tan.grid(row=6, column=3)
       # số pi
       self.so_pi = tk.Button(bottom_frame, **btn_paremeters, text='π', command=self.so_pi_btn)
       self.so_pi.grid(row=6, column=4)


       # Hàng 5
       # số 7
       self.so_7 = tk.Button(bottom_frame, **btn_paremeters_2, text='7', command=self.so_7_btn)
       self.so_7.grid(row=7, column=0)


       # số 8
       self.so_8 = tk.Button(bottom_frame, **btn_paremeters_2, text='8', command=self.so_8_btn)
       self.so_8.grid(row=7, column=1)


       # số 9
       self.so_9 = tk.Button(bottom_frame, **btn_paremeters_2, text='9', command=self.so_9_btn)
       self.so_9.grid(row=7, column=2)


       # xóa 1 ký tự
       self.xoa_1_ky_tu = tk.Button(bottom_frame, **btn_paremeters, text='DEL', command=self.xoa_1_ky_tu_btn)
       self.xoa_1_ky_tu.grid(row=7, column=3)


       # xóa hết
       self.xoa_ky_tu = tk.Button(bottom_frame, **btn_paremeters, text='AC', command=self.xoa_ky_tu_btn)
       self.xoa_ky_tu.grid(row=7, column=4)


       # Hàng 6


       # số 4
       self.so_4 = tk.Button(bottom_frame, **btn_paremeters_2, text='4', command=self.so_4_btn)
       self.so_4.grid(row=8, column=0)


       # số 5
       self.so_5 = tk.Button(bottom_frame, **btn_paremeters_2, text='5', command=self.so_5_btn)
       self.so_5.grid(row=8, column=1)


       # số 6
       self.so_6 = tk.Button(bottom_frame, **btn_paremeters_2, text='6', command=self.so_6_btn)
       self.so_6.grid(row=8, column=2)


       # dấu nhân
       self.dau_nhan = tk.Button(bottom_frame, **btn_paremeters, text='x', command=self.nhan_btn)
       self.dau_nhan.grid(row=8, column=3)


       # dấu chia
       self.dau_chia = tk.Button(bottom_frame, **btn_paremeters, text='/', command=self.chia_btn)
       self.dau_chia.grid(row=8, column=4)




       # Dòng 7
       # số 1
       self.so_1 = tk.Button(bottom_frame, **btn_paremeters_2, text='1', command=self.so_1_btn)
       self.so_1.grid(row=12, column=0)


       # số 2
       self.so_2 = tk.Button(bottom_frame, **btn_paremeters_2, text='2', command=self.so_2_btn)
       self.so_2.grid(row=12, column=1)


       # số 3
       self.so_3 = tk.Button(bottom_frame, **btn_paremeters_2, text='3', command=self.so_3_btn)
       self.so_3.grid(row=12, column=2)


       # dấu +
       self.dau_cong = tk.Button(bottom_frame, **btn_paremeters, text='+', command=self.cong_btn)
       self.dau_cong.grid(row=12, column=3)


       # dấu trừ
       self.dau_tru = tk.Button(bottom_frame, **btn_paremeters, text='-', command=self.tru_btn)
       self.dau_tru.grid(row=12, column=4)




       # dòng 8
       # số 0
       self.so_0 = tk.Button(bottom_frame, **btn_paremeters, text='0', command=self.so_0_btn)
       self.so_0.grid(row=15, column=0)


       # dấu chấm
       self.dau_cham = tk.Button(bottom_frame, **btn_paremeters, text='.', command=self.dau_cham_btn)
       self.dau_cham.grid(row=15, column=1)


       #số pi
       self.so_e = tk.Button(bottom_frame, **btn_paremeters, text='e', command=self.so_e_btn)
       self.so_e.grid(row=15, column=2)


       # dấu bằng
       self.dau_bang = tk.Button(bottom_frame, **btn_paremeters, text='=', command=self.dau_bang_btn, )
       self.dau_bang.grid(row=15, columnspan=2, column=3, sticky="nsew")
       # Phương trình bậc nhất
       self.bac_nhat = tk.Button(bottom_frame, **btn_paremeters_2, text=' bậc 1', command=self.bac_nhat_btn)
       self.bac_nhat.grid(row=6, column=5,sticky="nsew")
       self.text_a = tk.Entry(bottom_frame, font=('arial', 10, 'bold'), bd=3, insertwidth=1, bg='white', justify='right')
       self.text_a.grid(row=3, column=5, sticky="nsew")
       self.text_b = tk.Entry(bottom_frame, font=('arial', 10, 'bold'), bd=3, insertwidth=1, bg='white', justify='right')
       self.text_b.grid(row=4, column=5, sticky="nsew")
       self.text_c = tk.Entry(bottom_frame, font=('arial', 10, 'bold'), bd=3, insertwidth=1, bg='white', justify='right')
       self.text_c.grid(row=5, column=5, sticky="nsew")
       # Phương trình bậc 2
       self.bac_hai = tk.Button(bottom_frame, **btn_paremeters_2, text=' bậc 2', command=self.bac_hai_btn)
       self.bac_hai.grid(row=7, column=5, sticky="nsew")


   def giai_thua_btn(self):
       self.btn_click('m.factorial(')

   def can_bac_3_btn(self):
       self.btn_click('**(1/3)')

   def lap_phuong_btn(self):
       self.btn_click('**3')

   def luy_thua_cua_10_btn(self):
       self.btn_click('10**')

   def can_bac_2_btn(self):
       self.btn_click('**(1/2)')

   def binh_phuong_btn(self):
       self.btn_click('**2')

   def x_mu_n_btn(self):
       self.btn_click('**')

   def log_btn(self):
       self.btn_click('log(')

   def ln_btn(self):
       self.btn_click('ln(')

   def doi_dau_btn(self):
       self.btn_click('(-')

   def e_mu_x_btn (self):
       self.btn_click('e**')

   def sin_btn (self):
       self.btn_click('sin(')

   def cos_btn (self):
       self.btn_click('cos(')

   def tan_btn (self):
       self.btn_click('tan(')

   def so_e_btn (self):
       self.btn_click('e')

   def so_pi_btn (self):
       self.btn_click('π')

   def ngoac_trai_btn (self):
       self.btn_click('(')

   def ngoac_phai_btn (self):
       self.btn_click(')')

   def so_1_btn(self):
       self.btn_click('1')

   def so_2_btn(self):
       self.btn_click('2')

   def so_3_btn(self):
       self.btn_click('3')

   def so_4_btn(self):
       self.btn_click('4')

   def so_5_btn(self):
       self.btn_click('5')

   def so_6_btn(self):
       self.btn_click('6')

   def so_7_btn(self):
       self.btn_click('7')

   def so_8_btn(self):
       self.btn_click('8')

   def so_9_btn(self):
       self.btn_click('9')

   def so_0_btn(self):
       self.btn_click('0')

   def nhan_btn (self):
       self.btn_click('*')

   def chia_btn(self):
       self.btn_click('/')

   def cong_btn(self):
       self.btn_click('+')

   def tru_btn(self):
       self.btn_click('-')

   def dau_cham_btn(self):
       self.btn_click('.')

   def can_bac_n_btn(self):
       self.btn_click('**(1/')

   def chia_lay_du_btn(self):
       self.btn_click('%')

   def chia_lay_nguyen_btn(self):
       self.btn_click('//')

   def btn_click(self, x):
           self.expression = self.expression + str(x)
           self.input_txt.set(self.expression)

   def xoa_1_ky_tu_btn(self):
       self.expression = self.expression[:-1]
       self.input_txt.set(self.expression)

   def dau_bang_btn(self):
       self.result = str(eval(self.expression))
       self.expression = self.result
       self.input_txt.set(self.expression)

   def xoa_ky_tu_btn(self):
       self.expression = ""
       self.input_txt.set(self.expression)
   def bac_nhat_btn(self):
       a = float(self.text_a.get())
       b = float(self.text_b.get())
       if a == 0:
           if b == 0:
               self.result = "Vô số nghiệm"
           else:
               self.result = "Vô nghiệm"
       else:
           x = -b / a
           self.result = f"X = {x}"
       self.input_txt.set(self.result)

   # Phương trình bậc 2
   def bac_hai_btn(self):
       a = float(self.text_a.get())
       b = float(self.text_b.get())
       c = float(self.text_c.get())
       delta = b ** 2 - 4 * a * c
       if delta < 0:
           self.result = "Vô nghiệm"
       elif delta == 0:
           x = -b / (2 * a)
           self.result = f"X = {x}"
       else:
           x1 = (-b + m.sqrt(delta)) / (2 * a)
           x2 = (-b - m.sqrt(delta)) / (2 * a)
           self.result = f"X1 = {x1} , X2 = {x2}"
       self.input_txt.set(self.result)
# Hàm xử lý sự kiện khi người dùng click vào một mục trong thanh menubar
def open_new_window():
  global matrix1_entries, matrix2_entries
  def add_matrices():
      matrix1 = get_matrix_from_entry(matrix1_entries)
      matrix2 = get_matrix_from_entry(matrix2_entries)
      result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
      show_result(result)

  # Hàm tính hiệu hai ma trận
  def subtract_matrices():
      matrix1 = get_matrix_from_entry(matrix1_entries)
      matrix2 = get_matrix_from_entry(matrix2_entries)
      result = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
      show_result(result)

  # Hàm tính tích hai ma trận
  def multiply_matrices():
      matrix1 = get_matrix_from_entry(matrix1_entries)
      matrix2 = get_matrix_from_entry(matrix2_entries)
      result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for
                i in range(len(matrix1))]
      show_result(result)

  # Hàm tính định thức của ma trận
  def calculate_determinant():
      matrix = get_matrix_from_entry(matrix1_entries)
      if len(matrix) == len(matrix[0]):
          determinant = calculate_determinant_recursion(matrix)
          messagebox.showinfo("Kết quả", f"Định thức của ma trận là: {determinant}")
      else:
          messagebox.showerror("Lỗi", "Ma trận không phải là ma trận vuông")

  # Hàm tính định thức của ma trận bằng đệ quy
  def calculate_determinant_recursion(matrix):
      if len(matrix) == 1:
          return matrix[0][0]
      if len(matrix) == 2:
          return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
      determinant = 0
      for j in range(len(matrix[0])):
          submatrix = [[matrix[i][k] for k in range(len(matrix[0])) if k != j] for i in range(1, len(matrix))]
          determinant += matrix[0][j] * ((-1) ** j) * calculate_determinant_recursion(submatrix)
      return determinant

  # Hàm lấy giá trị từ các ô nhập liệu và chuyển đổi sang dạng ma trận
  def get_matrix_from_entry(entries):
      matrix = []
      for entry_row in entries:
          row = []
          for entry in entry_row:
              try:
                  row.append(float(entry.get()))
              except ValueError:
                  messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")
                  return None
          matrix.append(row)
      return matrix

  # Hàm hiển thị kết quả lên giao diện
  def show_result(result):
      result_window = tk.Toplevel(root)
      result_window.title("Kết quả")
      result_window.geometry("300x200")
      result_label = tk.Label(result_window, text="Kết quả:", font=("Helvetica", 14))
      result_label.pack(pady=10)
      result_text = tk.Text(result_window, font=("Helvetica", 12), height=8, width=30)
      for row in result:
          result_text.insert(tk.END, " ".join(str(element) for element in row) + "\n")
      result_text.pack()

  # Hàm xóa nội dung trong các ô nhập liệu
  def clear_entries(entries):
      for entry_row in entries:
          for entry in entry_row:
              entry.delete(0, tk.END)

  import tkinter as tk

  # Hàm xóa nội dung trong các ô nhập liệu
  def clear_entries(entries):
      for entry_row in entries:
          for entry in entry_row:
              entry.delete(0, tk.END)

  # Hàm xử lý sự kiện nút "Xóa"
  def clear_button_click():
      clear_entries(matrix1_entries)
      clear_entries(matrix2_entries)

  # Tạo cửa sổ giao diện chính
  root = tk.Tk()
  root.title("Xử lý ma trận")
  root.geometry("515x170")

  range_entry = tk.Entry(root, width=10)
  range_entry.grid(row=6, column=0, padx=5, pady=5)
  # Khởi tạo các ô nhập liệu cho ma trận 1
  matrix1_entries = []
  for i in range(3):
      row = []
      for j in range(3):
          entry = tk.Entry(root, width=10)
          entry.grid(row=i, column=j, padx=5, pady=5)
          row.append(entry)
      matrix1_entries.append(row)

  # Khởi tạo các ô nhập liệu cho ma trận 2
  matrix2_entries = []
  for i in range(3):
      row = []
      for j in range(3):
          entry = tk.Entry(root, width=10)
          entry.grid(row=i, column=j + 4, padx=5, pady=5)
          row.append(entry)
      matrix2_entries.append(row)

  def set_range():
      global matrix1_entries, matrix2_entries
      range_value = int(range_entry.get())
      # Xóa các ô nhập liệu hiện tại
      for row in matrix1_entries:
          for entry in row:
              entry.destroy()
      for row in matrix2_entries:
          for entry in row:
              entry.destroy()
      # Tính toán lại số lượng cột và dòng dựa trên giá trị range mới
      num_rows = range_value
      num_cols = range_value
      # Khởi tạo lại các ô nhập liệu dựa trên giá trị range mới
      matrix1_entries = []
      for i in range(num_rows):
          row = []
          for j in range(num_cols):
              entry = tk.Entry(root, width=10)
              entry.grid(row=i, column=j, padx=5, pady=5)
              row.append(entry)
          matrix1_entries.append(row)
      matrix2_entries = []
      for i in range(num_rows):
          row = []
          for j in range(num_cols):
              entry = tk.Entry(root, width=10)
              entry.grid(row=i, column=j + num_cols + 1, padx=5, pady=5)
              row.append(entry)
          matrix2_entries.append(row)

  range_button = tk.Button(root, text="Nhập", command=set_range)
  range_button.grid(row=6, column=1, padx=5, pady=5)

  # Tạo nút và gán sự kiện cho các phép toán
  add_button = tk.Button(root, text="Cộng", command=add_matrices)
  add_button.grid(row=4, column=1, padx=5, pady=5)

  subtract_button = tk.Button(root, text="Trừ", command=subtract_matrices)
  subtract_button.grid(row=4, column=2, padx=5, pady=5)

  multiply_button = tk.Button(root, text="Nhân", command=multiply_matrices)
  multiply_button.grid(row=4, column=3, padx=5, pady=5)

  determinant_button = tk.Button(root, text="Định thức", command=calculate_determinant)
  determinant_button.grid(row=4, column=5, padx=5, pady=5)

  clear_button = tk.Button(root, text="Xóa", command=clear_button_click)
  clear_button.grid(row=4, column=6, padx=5, pady=5)

root = tk.Tk()
# Tạo thanh menubar
menu_bar = Menu(root)
root.config(menu=menu_bar)
# Tạo một mục trong thanh menubar
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Matrix", menu=file_menu)
file_menu.add_command(label="Mở giao diện ma trận",
                    command=open_new_window)  # Thêm một mục con cho mục "File" và gắn với hàm xử lý sự kiện open_new_window()
calc = Sci_Calculator(root)
root.mainloop()