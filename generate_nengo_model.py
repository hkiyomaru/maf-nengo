import sqlite3

DATABASE = 'nengo.db'

class NengoModel:
    def __init__(self, database):
        self.database = self.get_db(database)

    def get_db(self, database):
        db = sqlite3.connect(database)
        db.row_factory = self.make_dicts
        return db

    def close_connection(self, exception):
        if self.database is not None:
            self.database.close()

    def make_dicts(self, cursor, row):
        return dict((cursor.description[idx][0], value)
            for idx, value in enumerate(row))

    def query_db(self, query, args=(), one=False):
        cur = self.database.execute(query ,args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

class GeneratePythonCode:
    def __init__(self, nengoDB):
        self.nengoDB = nengoDB
        # mojule data
        self.mojules = self.nengoDB.query_db('select * from mojules')
        # connection data
        self.connections = self.nengoDB.query_db('select * from connections')
        # cortex data
        self.cortexes = self.nengoDB.query_db('select * from cortexes')

    def execute(self):
        self.f = open('maf.py', 'w')
        self.write_header()
        self.write_mojule()
        self.write_connection()

    def write_header(self):
        header = 'import nengo'
        self.f.write(header)
        self.line_break()

        header = 'model = nengo.Network()'
        self.f.write(header)
        self.line_break()

        header = 'def f():'
        self.f.write(header)
        self.line_break()

        header = '\treturn None'
        self.f.write(header)
        self.line_break()

        header = 'with model:'
        self.f.write(header)
        self.line_break()

    def write_mojule(self):
        # Write mojules
        for mojule in self.mojules:
            if mojule['region'] == 'Isocortex' or mojule['region'] == 'Olfactory Areas':
                self.f.write('\twith nengo.Network(label="' + self.escape(mojule['name']) + '"):')
                self.line_break()
                for i in range(0, 7):
                    laminal = str(i)
                    if i == 2:
                        laminal = '2_3'
                    elif i== 3:
                        continue
                    self.f.write('\t\t' + self.escape(mojule['name']) + '_' + laminal + ' = nengo.Node(output=f, size_in=100, size_out=100)')
                    self.line_break()
            else:
                self.f.write('\t' + self.escape(mojule['name']) + ' = nengo.Node(output=f, size_in=100, size_out=100)')
                self.line_break()

    def write_connection(self):
        # Write connections
        for connection in self.connections:
            # Get region
            sourceRegion = self.nengoDB.query_db('select region from mojules where name="%s"' %connection['sourceName'])[0]['region']
            destinationRegion = self.nengoDB.query_db('select region from mojules where name="%s"' %connection['destinationName'])[0]['region']
            if connection['type'] != 'unk':
                cortex_link = self.nengoDB.query_db('select sourceCortex,destinationCortex from cortexes where sourceRegion="%s" and destinationRegion="%s" and type="%s"' %(sourceRegion, destinationRegion, connection['type']))[0]
            else:
                cortex_link = {'sourceCortex': 'C0', 'destinationCortex': 'C0'}
            if sourceRegion == 'Isocortex' or sourceRegion == 'Olfactory Areas':
                cortex_link['sourceCortex'] = cortex_link['sourceCortex'][1:]
                self.f.write('\tnengo.Connection(' + self.escape(connection['sourceName']) + '_' + cortex_link['sourceCortex'] + ',')
            else:
                self.f.write('\tnengo.Connection(' + self.escape(connection['sourceName']) + ',')
            if destinationRegion == 'Isocortex' or destinationRegion == 'Olfactory Areas':
                cortex_link['destinationCortex'] = cortex_link['destinationCortex'][1:]
                self.f.write(self.escape(connection['destinationName']) + '_' + cortex_link['destinationCortex'] + ')')
            else:
                self.f.write(self.escape(connection['destinationName']) + ')')
            self.line_break()

    def line_break(self):
        self.f.write('\n')

    def escape(self, string):
        string = string.replace('-', '_')
        return string

    def write_network():
        pass

if __name__ == '__main__':
    database = NengoModel(DATABASE)
    code = GeneratePythonCode(database)
    code.execute()
    print 'success!'
