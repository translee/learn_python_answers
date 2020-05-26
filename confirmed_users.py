#首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users=['alice','brian','candace']
confirmed_users=[]
while unconfirmed_users:
	current_user=unconfirmed_users.pop()
	print("Veryfying user: "+current_user.title())
	confirmed_users.append(current_user)
print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
