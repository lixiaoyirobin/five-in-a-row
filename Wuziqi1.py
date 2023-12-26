import turtle   # 导入库
import yaml
class Qipan():   # 创建棋盘类
    global abc
    def __init__(self,x,line):   # 定义棋盘数据
        self.x = x / 2
        self.y = self.x
        self.line = line
        self.a = 2 * self.x
        self.qipan_list = [[0] * (self.line + 1) for _ in range(self.line + 1)]
    def Huaqipan(self):   # 创建画棋盘方法
        turtle.penup()   # 移动位置
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.fillcolor('goldenrod')   # 定义填充颜色
        turtle.begin_fill()
        for i in range(4):   # 画边缘并涂色
            turtle.right(90)
            for i in range(self.line):
                turtle.pensize(3)
                turtle.dot()
                turtle.pensize(2)
                turtle.forward(1 / self.line * self.a)
        turtle.end_fill()
        turtle.right(180)   # 调整角度
        turtle.pensize(1)
        for i in range(self.line):   # 画横线
            turtle.penup()
            turtle.goto(self.x,self.y)
            turtle.pendown()
            for i in range(self.line):
                turtle.pensize(3)
                turtle.dot()
                turtle.pensize(1)
                turtle.forward(1 / self.line * self.a)
            self.y -= self.a / self.line
        turtle.right(90)   # 调整角度
        for i in range(self.line + 1):   # 画竖线
            turtle.penup()
            turtle.goto(self.x,self.y)
            turtle.pendown()
            turtle.forward(self.a)
            self.x -= self.a / self.line
        self.x = qipan_x / 2
        self.y = qipan_x / 2
    def Check_win(self,x):   # 创建检查胜利方法
        jishuqi1 = 0   # 定义变量
        jishuqi2 = 0
        abc = 0
        for i in range(len(self.qipan_list)):   # 检测横行
            for j in range(len(self.qipan_list[0])):
                if self.qipan_list[i][j] == x:   # 判断
                    jishuqi1 += 1
                    if jishuqi1 >= 5 and x == 1:
                        abc = 1
                    if abc == 1:
                        if jishuqi1 == 0:
                            abc = 0
                            return True
                        else:
                            abc = 0
                            qizi.jinshou()
                            return False
                else:   # 清零
                    jishuqi1 = 0
        for i in range(len(self.qipan_list[0])):   # 检测竖行
            for j in range(len(self.qipan_list)):
                if self.qipan_list[j][i] == x:   # 判断
                    jishuqi2 += 1
                    if jishuqi2 >= 5 and x == 1:
                        abc = 1
                    if abc == 1:
                        if jishuqi2 == 0:
                            abc = 0
                            return True
                        else:
                            abc = 0
                            qizi.jinshou()
                            return False
                else:   # 清零
                    jishuqi2 = 0
        for i in range(len(self.qipan_list) - 4):   # 检测左上到右下方向
            for j in range(len(self.qipan_list[0]) - 4):
                if self.qipan_list[i][j] == self.qipan_list[i+1][j+1] == self.qipan_list[i+2][j+2] == self.qipan_list[i+3][j+3] == self.qipan_list[i+4][j+4] == x:   # 判断
                    if i + 5 <= len(self.qipan_list) and j + 5 <= len(self.qipan_list[0]) and x == 1:
                        if self.qipan_list[i+5][j+5] == 1:
                            qizi.jinshou()
                            qizi.e = 1
                            return False
                    if i - 1 >= 0 and j - 1 >= 0 and x == 1:
                        if self.qipan_list[i-1][j-1] == 1:
                            qizi.jinshou()
                            qizi.e = 1
                            return False
                    return True
        for i in range(4, len(self.qipan_list)):   # 检测左下到右上方向
            for j in range(len(self.qipan_list[0]) - 4):
                if self.qipan_list[i][j] == self.qipan_list[i-1][j+1] == self.qipan_list[i-2][j+2] == self.qipan_list[i-3][j+3] == self.qipan_list[i-4][j+4] == x:   # 判断
                    return True
        return False
class Qizi():   # 创建棋子类
    def __init__(self,a,line):   # 定义棋子数据
        self.r = int(a / line / 3)
        self.d = 2 * self.r
        self.z = 1
        self.e = 0
    def Black(self,x,y):   # 创建黑子方法
        turtle.fillcolor('black')   # 设置填充颜色
        qizi.Huaqizi(x,y)   # 调用画棋子方法
    def White(self,x,y):   # 创建白子方法
        turtle.fillcolor('white')   # 设置填充颜色
        qizi.Huaqizi(x,y)   # 调用画棋子方法
    def Huaqizi(self,x,y):   # 创建画棋子方法
        turtle.penup()   # 移动到指定位置
        turtle.goto(x,y)
        turtle.right(90)
        turtle.forward(self.r)
        turtle.left(90)
        turtle.pendown()
        turtle.begin_fill()   # 画棋子
        turtle.circle(self.r,360,100)
        turtle.end_fill()
    def Xiaqi(self,x,y,a,b,Yi,Er):   # 创建下棋方法
        for i in range(len(qipan.qipan_list)):   # 遍历qipan.qipan_list
            for j in range(len(qipan.qipan_list[0])):
                if qipan.qipan_list[i][j] == 1:   # 记录黑子数量
                    Yi += 1
                elif qipan.qipan_list[i][j] == 2:   # 记录白子数量
                    Er += 1
        if qipan.qipan_list[a][b] == 0:   # 检测当前位置是否有棋
            if Yi == Er:   # 判断黑先还是白先
                qizi.Black(x,y)   # 调用黑子方法
                qipan.qipan_list[a][b] = 1   # 记录黑子
            elif Yi > Er:
                qizi.White(x,y)   # 调用白子方法
                qipan.qipan_list[a][b] = 2   # 记录白子
    def win(self,x):   # 创建胜利方法
        if x == 1:   # 判断
            turtle.color('blue')   # 设置颜色为蓝
            turtle.title('黑棋666')   # 修改名称
            turtle.penup()   # 移动到指定位置
            turtle.goto(-200,-50)
            turtle.pendown()
            turtle.write('黑棋获胜',font=('Arial', 100, 'normal'))   # 显示'黑棋获胜'
        elif x == 2:
            turtle.color('red')   # 设置颜色为红
            turtle.title('白棋666')   # 修改名称
            turtle.penup()   # 移动到指定位置
            turtle.goto(-200,-50)
            turtle.pendown()
            turtle.write('白棋获胜',font=('Arial', 100, 'normal'))   # 显示'白棋获胜'
    def jinshou(self):
        turtle.color('pink')   # 设置颜色为粉
        turtle.penup()   # 移动到指定位置
        turtle.goto(-200,50)
        turtle.pendown()
        turtle.write('黑棋禁手',font=('Arial', 100, 'normal'))   # 显示'黑棋禁手'
        turtle.penup()   # 移动到指定位置
        turtle.goto(-200,-50)
        turtle.pendown()
        turtle.write('白棋获胜',font=('Arial', 100, 'normal'))   # 显示'白棋获胜'
def get_click_coordinate(x,y):   # 获取坐标
    Yi = Er = f = 0   # 定义变量
    c = (x - ( - qipan.x)) / (qipan.a / qipan.line)
    d = (y - ( - qipan.x)) / (qipan.a / qipan.line)
    a = int(c)
    b = int(d)
    e = qizi.e
    if x <= qipan.x and x >= -qipan.x and y <= qipan.x and y >= -qipan.x:   # 判断棋子是否在棋盘内
        if c - a >= 0.7:   # 判断棋子离那一个X轴近
            a += 1
            x = a * (qipan.a / qipan.line) - qipan.x
        elif c - a <= 0.3:   # 判断棋子离那一个X轴近
            x = a * (qipan.a / qipan.line) - qipan.x
        else:   # 判断棋子是否在误差范围外
            e += 1
        if d - b >= 0.7:   # 判断棋子离那一个Y轴近 
            b += 1
            y = b * (qipan.a / qipan.line) - qipan.x
        elif d - b <= 0.3:   # 判断棋子离那一个Y轴近
            y = b * (qipan.a / qipan.line) - qipan.x
        else:   # 判断棋子是否在误差范围外
            e += 1
        if e == 0:   # 判断棋子是否在误差范围外
            qizi.Xiaqi(x,y,a,b,Yi,Er)   # 调用方法下棋
            if qipan.Check_win(1):
                qizi.win(1)   # 调用胜利方法
                qizi.e = 1
            elif qipan.Check_win(2):
                qizi.win(2)   # 调用胜利方法
                qizi.e = 1
            for i in range(len(qipan.qipan_list)):   # 遍历
                for j in range(len(qipan.qipan_list[0])):
                    if 0 != qipan.qipan_list[i][j]: f += 1   # 判断是否结束
            if f == (qipan.line + 1) ** 2:
                turtle.color('green')   # 设置颜色为绿
                turtle.penup()   # 移动到指定位置
                turtle.goto(-100,-50)
                turtle.pendown()
                turtle.write('平局',font=('Arial', 100, 'normal'))   # 显示'平局'
                qizi.e = 1
turtle.tracer(False)   # 瞬间完成画图
with open('/Users/lixiaoyi/Desktop/py_wuziqi.yaml','r') as f:   # 打开yaml文件
    text = f.read()   # 读取yaml文件
peizhi = yaml.safe_load(text)   # 转化为字典类型
qipan_x = peizhi['qipan_x']   # 定义变量
qipan_line = peizhi['qipan_line']
f.close()   # 关闭文件
abc = 0
if qipan_x > 900:   # 判断是否过大
    print('输入的棋盘长度太大了,自动调整为600')
    qipan_x = 600
    abc += 1
elif qipan_x < 50:   # 判断是否过小600
    print('输入的棋盘长度太小了,自动调整为600')
    qipan_x = 600
    abc += 1
if qipan_line > 30:   # 判断是否过大
    print('输入的行数太大了,自动调整为10')
    qipan_line = 10
    abc += 1
elif qipan_line < 4:   # 判断是否过小
    print('输入的行数太小了,自动调整为10')
    qipan_line = 10
    abc += 1
if qipan_x / qipan_line - int(qipan_x / qipan_line) != 0:   # 判断是否合适
    print('输入的棋盘长度和行数不和适,自动调整为600和10')
    qipan_x = 600
    qipan_line = 10
    abc += 1
if abc != 0:
    print('请等待五秒')    # 等待五秒
    time.sleep(5)
abc = 0
turtle.hideturtle()   # 隐藏海龟
qipan = Qipan(qipan_x,qipan_line)   # 创建五子棋对象
qizi = Qizi(qipan.a,qipan.line)   # 创建棋子对象
turtle.setup(1000,1000)   # 创建窗口
qipan.Huaqipan()   # 动用画棋盘方法
turtle.onscreenclick(get_click_coordinate)   # 获取坐标
turtle.title('五子棋')   # 修改名称
turtle.done()   # 结束