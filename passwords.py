# passrords

password = 'Takotail'
a = 3

while a > 0 :
	a = a - 1
	word = ( input('請輸入密碼：') )
	if word == password :
		print('歡迎登入')
		break
	else :
		print ('輸入錯誤還有')
		if a > 0 :
			print ('還有', a, '次機會')
		else :
			print ('輸入多次錯誤，無法再次輸入')

