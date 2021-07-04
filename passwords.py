# passrords

password = 'a123456'
a = 0

word = ( input('請輸入密碼：') )

while a <= 3 :
	a =  a + 1
	if word != 'a123456':
		if a == 1 :
			print ('輸入錯誤還有兩次機會')
			word = ( input('請輸入密碼：') )
		elif a == 2 :
			print ('輸入錯誤還有一次機會')
			word = ( input('請輸入密碼：') )
		elif a == 3 :
			print ('輸入多次錯誤，無法再次輸入')

	elif word == password :
		print('歡迎登入')
		break