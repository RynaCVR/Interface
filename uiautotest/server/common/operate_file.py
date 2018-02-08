# coding = utf-8

import os


class OperateFile:
    """
    method(r,w,a)
    """
    def __init__(self, file, method='w+'):
        self.file = file
        self.method = method
        self.fileHandle = None

    def write_txt(self, line):
        """
        文本写入数据line
        :param line: 要写入文件的数据
        :return:
        """
        self.check_file()
        self.fileHandle = open(self.file, self.method)
        self.fileHandle.write(line + "\n")
        self.fileHandle.close()

    def read_txt_row(self):
        """
        从文件中读取一行数据
        :return: 返回读取的数据
        """
        result = ""
        if self.check_file():
            self.fileHandle = open(self.file, self.method)
            result = self.fileHandle.readline()
            self.fileHandle.close()
        return result

    def read_txt_rows(self):
        """
        从文件中读取多行数据
        :return: 返回读取的数据
        """
        if self.check_file():
            self.fileHandle = open(self.file, self.method)
            file_list = self.fileHandle.readlines()
            for i in file_list:
                print(i.strip("\n"))
            self.fileHandle.close()

    def check_file(self):
        """
        判断文件路径是否存在
        :return: 返回结果 
        """
        if not os.path.isfile(self.file):
            # print('文件不存在' + self.file)
            # sys.exit()
            return False
        else:
            return True
        # print("文件存在！")

    def mkdir_file(self):
        """
        如果文件不存在，则创建
        :return:
        """
        if not os.path.isfile(self.file):
            f = open(self.file, self.method)
            f.close()
            print("创建文件成功")
        else:
            print("文件已经存在")

    def remove_file(self):
        """
        删除某个文件
        :return:
        """
        if os.path.isfile(self.file):
            os.remove(self.file)
            print("删除文件成功")
        else:
            print("文件不存在")

# if __name__ == '__main__':
#     bf = OperateFile("text.xml")
#     if bf.check_file() == False:
#         bf.mkdir_file()
#     bf.write_txt("111")
