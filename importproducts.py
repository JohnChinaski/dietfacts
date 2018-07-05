# coding: utf-8
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
# print models

# partners = models.execute_kw(database, uid, password,
#                              'product.template',
#                              'search_read',[[]],
#                              {'fields': ['name', 'list_price', 'comment','calories']})


nome = raw_input("Digite o nome: ")

partners = models.execute_kw(database, uid, password,
                             'res.partner',
                             'search_read',[[['name','=',nome]]],
                             {'fields': ['name']})

partners_full = models.execute_kw(database, uid, password,
                                  'res.partner',
                                  'search_read', [[]],
                                  {'fields': ['name']})

if len(partners) < 1:
    choice = raw_input("Nome não cadastrado, deseja cadastrar? (S ou N): ")
    if choice.lower() == "s":
        phone = raw_input("Digite o telefone: ")
        id = models.execute_kw(database, uid, password, 'res.partner', 'create', [{
            'name': nome,
            'phone': phone
        }])

else:
    print("Nome ja cadastrado!")

print(partners_full)

# x = [pessoa['id'] for pessoa in partners_full if pessoa['name'] == 'Diogo Berti']
#
# for item in x[1:]:
#     print(item)
#     models.execute_kw(database, uid, password, 'res.partner', 'unlink', [[item]])


# print(x)
# seen = set()
# new_partners = []
# for d in partners_full:
#     t = tuple(d.items())
#     if t not in seen:
#         seen.add(t)
#         new_partners.append(d)
#
# print("opa", new_partners)

"""
criar variavel pra contador com valor de 
Para item na lista verificar se o nome é x


"""

# for item in partners:
#     print item.get('name')
#     print item['id']
#     # for k,v in item.iteritems():
#     #     print('%s\t%s' % (k,v))
#
# if len(partners) > 0:
#     print('Ja existe')
# else:
#     print('Nao tem')






# for item in partners:
#     for k,v in item.items():
#         print "%s\t%s" % (k,v)
#
# id = models.execute_kw(database, uid, password, 'res.partner', 'create', [{
#     'name': "Diogo Berti",
#     'phone':'666ll'
#             ''
# }])




# ids = models.execute_kw(database, uid, password,
#
#                         "product.product.template",
#                         "render_qweb_pdf", [[]],
#                         {'fields': ['name', 'list_price', 'comment','calories']})
