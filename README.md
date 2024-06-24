# R-Vision
'''
1. OVAL файлы содержат секции (<definitions> <tests> <objects> <states>)
	Элементы red-def: rpminfo_object
	         red:def: rpmverifyfile_object

rpminfo_object имеют id, версии, названия (важно)
rpmverifyfile_object имеют id, версии, поведения, путь (важно) (остальные параметры сравнения, нужны для понимания условия проверки)

2.

rpminfo_object
Этот объект OVAL используется для собирания информации о RPM пакетах, установленных в системе. Он помогает проверять атрибуты пакетов, такие как имя, версия, релиз и архитектура, что важно для оценки состояния системы и соответствия установленного ПО требованиям безопасности.

rpmverifyfile_object используется для верификации свойств файлов в системе, в данном случае файла `/etc/redhat-release`

Type: rpminfo_object
ID: oval:com.redhat.rhba:obj:20191992001
Version: 635
Name: cloud-init

Type: rpmverifyfile_object
ID: oval:com.redhat.rhba:obj:20191992002
Version: 635
FilePath: /etc/redhat-release

3. Все перечисленные в <advisory> кроме <severity>

4. Id, Title, Discription, Criteria, Severity
'''
