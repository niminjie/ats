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

    def get_onelevel_comment(self, key, comments):
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
        for c in comments:
            one_comment.append(c[key.decode('gbk')])
        return one_comment

    def filter_comment_list(self, constrain = None):
        '''
        constrain: {'crawlURL':'', 'pubtime': '', '�㳵�����':'', '����ص�':'','����ʱ��':'','������':'','����ϵ':'','����Ŀ��':'','����������':'' }
        '''
        if constrain == None:
            return self._comments
        rank = []
        for c in self._comments:
            match_constrain = True
            for key, value in constrain.items():
                if value != c[key]:
                    match_constrain = False
            if match_constrain:
                rank.append(c)
        return rank

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

    def stat_rank(self, fields, comment):
        '''
        Statistic all avg rate in fields
        ---------------------------------
        Args:
            fields:       Field list: ['�ٿ�', '����', ...]
        Returns:
            None
        '''
        for f in fields:
            f_value = self.get_onelevel_comment(f, comment)
            print f.decode('gbk'), '\t', self.avg_rate(f_value)


def ana_gen_score():
    field = ['�ռ�', '����', '�ٿ�', '�ͺ�', '������', '���', '����', '�Լ۱�']
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


def print_car_type(ana, versus = True):
    car = ana.get_onelevel_comment('������', ana.filter_comment_list())
    # for c in set(car):
    #     print c
    return set(car)

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

    all_car_type = print_car_type(ana_Audi)
    # print all_car_type

    field = ['�ռ�', '����', '�ٿ�', '�ͺ�', '������', '���', '����', '�Լ۱�']

    for t in all_car_type:
        dic = {}
        # dic['������'.decode('gbk')] = '2012�� 325i ������'.decode('gbk')
        dic['������'.decode('gbk')] = t
        print t
        ats_28t = ana_Audi.filter_comment_list(constrain=dic)
        if ats_28t:
            ana_Audi.stat_rank(field, ats_28t)

def main():
    pass

if __name__ == '__main__':
    test()
