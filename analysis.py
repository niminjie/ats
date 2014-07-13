# coding:gbk
from dataset import DataSet

class Analysis():
    def __init__(self, dataset):
        '''
        Construct function
        ---------------------------------
        Args:
            dataset:     Input dataset
        Returns:
            None
        '''
        self._comments = dataset.comments

    def get_onelevel_comment(self, key):
        '''
        {key1: {key2: value}}
        Get one level: {key2: value}
        ---------------------------------
        Args:
            key:          
        Returns:
            one_comment   Comment value
        '''
        one_comment = []
        for c in self._comments:
            one_comment.append(c[key.decode('gbk')])
        return one_comment

    def avg_rate(self, item):
        '''
        Calculate average rate score
        ---------------------------------
        Args:
            item:         Rate rank list
        Returns:
            score:        Average rank score
        '''
        rank = self._rank_list(item)
        return round(sum(rank) * 1.0 / len(item), 1)

    def _rank_list(self, comment):
        '''
        Get rank score list from level one and convert to float
        ---------------------------------
        Args:
            Comment:      Level one comment
        Returns:
            rank:         
        '''
        rank = []
        for c in comment:
            rank.append(float(c['rank']))
        return rank

    def _convert_to_float(self, l):
        return [float(i) for i in l]

    def stat_rank(self, fields):
        '''
        Statistic all avg rate in fields
        ---------------------------------
        Args:
            fields:       Field list: ['操控', '内饰', ...]
        Returns:
            None
        '''
        for f in fields:
            f_value = self.get_onelevel_comment(f)
            print f.decode('gbk'), '\t', self.avg_rate(f_value)

def test():
    ATS = DataSet('./dataset/ATS.txt')
    BMW = DataSet('./dataset/BMW.txt')
    Benz = DataSet('./dataset/Benz.txt')
    Audi = DataSet('./dataset/Audi.txt')
    # ATS.json_print()
    ana_ATS = Analysis(ATS)
    ana_BMW = Analysis(BMW)
    ana_Benz = Analysis(Benz)
    ana_Audi = Analysis(Audi)


    field = ['空间', '动力', '操控', '油耗', '舒适性', '外观', '内饰', '性价比']
    print 'ATS'
    ana_ATS.stat_rank(field)
    print '-' * 50
    print 'BMW'
    ana_BMW.stat_rank(field)
    print '-' * 50
    print 'Benz'
    ana_Benz.stat_rank(field)
    print '-' * 50
    print 'Audi'
    ana_Audi.stat_rank(field)

    # car = ana_Audi.get_onelevel_comment('购买车型')
    # for c in car:
    #     print c
    

    # space = ana_ATS.get_onelevel_comment('空间')
    # dynamic = ana_ATS.get_onelevel_comment('动力')
    # control = ana_ATS.get_onelevel_comment('操控')
    # fuel = ana_ATS.get_onelevel_comment('油耗')
    # comfort = ana_ATS.get_onelevel_comment('舒适性')
    # appearance = ana_ATS.get_onelevel_comment('外观')
    # trim = ana_ATS.get_onelevel_comment('内饰')
    # price = ana_ATS.get_onelevel_comment('性价比')

    # print ana_ATS.avg_rate(space)
    # print ana_ATS.avg_rate(dynamic)

def main():
    pass

if __name__ == '__main__':
    test()
