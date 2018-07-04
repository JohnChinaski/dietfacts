import xmlrpclib
import csv

host = 'http://localhost:8069'
database = 'dietfacts'
user = 'admin'
password = 'admin'

# info = xmlrpclib.ServerProxy(host).start()
# url, db, username, password = \
#     info['host'], info['database'], info['user'], info['password']

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(host))
uid = common.authenticate(database, user, password, {})

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(host))
print models

partners = models.execute_kw(database, uid, password,
                             'product.template',
                             'search_read',[[]],
                             {'fields': ['name', 'list_price', 'comment','calories']})

for item in partners:
    for k,v in item.items():
        print "%s\t%s" % (k,v)

id = models.execute_kw(database, uid, password, 'res.partner', 'create', [{
    'name': "Diogo Berti",
    'phone':'666ll'
            ''
}])