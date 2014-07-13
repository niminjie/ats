import json

class DataSet:

    def __init__(self, path):
        '''
        Construct function
        ---------------------------------
        Args:
            path:      Input json file path
        Returns:
            None
        '''

        self._path = path
        self._json_file = open(path, 'r')
        self.comments = self._make()

    def __repr__(self):
        '''
        Dataset description
        ---------------------------------
        Args:
            None
        Returns:
            des:       Descript of datset
        '''

        des = '''Data from: %s \nAll %d lines ''' % (self.get_path(), len(self.comments))
        return des

    def get_path(self):
        '''
        Return path of dataset
        ---------------------------------
        Args:
            None
        Returns:
            self._path:     Dataset path
        '''
        return self._path

    def get_json_file(self):
        '''
        Return input file of json
        ---------------------------------
        Args:
            None
        Returns:
            _json_file:     Json file
        '''
        return self._json_file

    def _make(self):
        '''
        Convert json file to dict type
        ---------------------------------
        Args:
            None
        Returns:
            comments:       comments of the car
        '''
        comments = []
        for line in self._json_file:
            if line.strip():
               comments.append(json.loads(line))
        return comments

    def json_print(self):
        '''
        Pretty print dataset:
        {
            "field1": {"value1"},
            "field2": {"value2"},
            ...
        }
        ---------------------------------
        Args:
            None
        Returns:
            None
        '''
        for d in self.comments:
            print json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
