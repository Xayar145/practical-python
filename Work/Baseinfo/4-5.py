#import tableformat

class TableFormatter:
    def headings(self,header):
        '''
        输出表格标题
        '''
        raise NotImplementedError()
    
    def row(self,rowdata):
        '''
        输出单行表格数据
        '''
        raise NotImplementedError()
    

    def print_report(reportdata,formatter):
        '''
        根据包含 (名称, 股份数, 价格, 变动) 元组的列表，打印格式美观的表格。
        '''

        formatter.headings(['Name','Shapes','Price','Change'])
        for name,shares,price,change in reportdata:
            rowdata = [name,str(shares),f'{price:0.2f}',f'{change:0.2f}'] 
            formatter.row[rowdata]

    def portfolio_report(portfoliofile,pricefile):
        '''
        根据投资组合和价格数据文件，生成一份股票报告。
        '''

        #Read data file
        #portfolio = read_portfolio(portfoliofile)
        #price = read_prices(pricefile)

        #Creat the report data
        #report = make_report_data(portfolio,price)

        #Print it out
       # formatter = tableformat.TableGormatter()
        #print_report(report,formatter)


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def share(self):
        return self._shares
    #@share.setter