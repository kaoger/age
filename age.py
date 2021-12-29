driving = input('你有沒有開過車: ')
if driving != '有' or driving != '沒有':
	print('你是看不懂中文是不是?輸入有/沒有')
	raise SystemExit

age = input('請問你的年齡: ')
age = int(age)
if driving == '有':
	if age >= 18: 
		print('你是合法的!')
	else:
		print('你犯法了!')
elif driving == '沒有':
	if age >= 18:
		print('幹嘛不去考?')
	else:
		print('快去吃飯長大')
