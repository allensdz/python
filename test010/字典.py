#简单数据库
#使用人名作为键的字典。每个人用另外一个字典来表示，其键“phone”和“add”分别代表电话和住址
people = {
	'Alice':{
		"phone":"2345"
		"add":"Foo drive 23"
	}
	"Beth":{
		"phone":"2442"
		"add":"Bar street 42"
	}
	"Cecil"{
		"phone":"2432"
		"add":"Baz avenue 90"
	}
}

#针对打电话号码和地址的描述性标签，会在打印输出时用到
labels = {
	"phone":"phone number"
	"add":"address"
}

name = raw_input("Name:")

#查找是电话号码还是地址，寻找正确的键

#使用正确的键
if request == "p": key = "phone"
if request == "a": key = "add"

#如果名字是字典中的有效值才打印信息：
if name in people: print"%s's %s is %s."%(name, labels[key],people[name][key])
