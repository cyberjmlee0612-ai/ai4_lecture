# 포함관계(in, not in)
role = 'admin'

# if role == 'admin' or role =='manger or role == 'staffe'

# allowed_roles = ['dsmin','manager','staff']

if role in ['dsmin','manager','staff']:
    print('접근 허용')
else:
    print('접근 불가')
