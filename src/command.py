import xlrd
import os

class command():
    def __init__(self):
        super().__init__()
        self.fileList=[]
        self.sendStrList=[]   #指令存储在这个二维数组内
    def getCommand(self):
        self.XLS='.xls'
        # 返回一个列表，其中包含在目录条目的名称
        self.Path = r'zhilingji'
        self.files = os.listdir(self.Path)
        for f in self.files:
            if(self.XLS in f):
                # 添加文件
                f.encode('GBK')
                self.fileList.append(f)
        for i in self.fileList:
            list_i=list(i)
            list_i.insert(0,'zhilingji\\')
            i=''.join(list_i)
            self.readbook = xlrd.open_workbook(i)
            self.sheet=self.readbook.sheet_by_index(0)
            self.sendStrList.append(self.sheet.col_values(0))
        return self.sendStrList