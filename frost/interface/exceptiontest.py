input=raw_input()


try:
	if input=="bob":
		raise Exception("not bob")
	if not abs(int(input))==1:
		raise ValueError()
except ValueError:
		print "invalid number"
except Exception as inst:
	print inst
