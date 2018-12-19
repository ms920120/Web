from common.basepage import BasePage
class OperaData(BasePage):
    #此方法是将表格体中的二维列表[[],[]]转换成列表包含字典每一行数据存储在一个字典内缺点字典的key每一次都要自己写入代码复用性低
    def get_(self,data):
        mylist=[]
        for trdata in data:
            mydict={}
            for tddata in range(len(trdata)):
                mydict["学号"]=tddata[0]
                mydict["姓名"] = tddata[1]
                mydict["性别"] = tddata[2]
                mydict["院系"] = tddata[3]
                mydict["年级"] = tddata[4]
                mydict["专业"] = tddata[5]
                mydict["行政班"] = tddata[6]
                mydict["入学日期"] = tddata[7]
                mydict["毕业日期"] = tddata[8]
                mydict["培养层次"] = tddata[9]
                mydict["学生类别"] = tddata[10]
                mydict["学籍状态"] = tddata[11]
                mydict["详细信息"] = tddata[12]
            mylist.append(mydict)

