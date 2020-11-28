import mail
import csv
import random
import copy
import sys


class Person:
	def __init__(self, name, email, wishlist):
		self.__name = name
		self.__email = email
		self.__wishlist = wishlist

	def __str__(self):
		return self.__name+" has email: "+self.__email+" and wants: "+self.__wishlist

	def name(self):
		return self.__name

	def email(self):
		return self.__email

	def wishlist(self):
		return self.__wishlist


def enter_info(csv_list, domain):
	info = {}
	names = []
	f = open(csv_list, 'r')
	reader = csv.reader(f)
	next(reader, None)

	for row in reader:
		names.append(row[0])
		info[row[0]] = Person(row[0], convert_emails(row[1], domain), row[2])

	return info, names


def convert_emails(alias, domain):
	return alias+"@"+domain


def draw_names(names):
	my_list = names
	choose = copy.copy(my_list)
	selections = []
	for i in my_list:
		names = copy.copy(my_list)
		names.pop(names.index(i))
		chosen = random.choice(list(set(choose) & set(names)))
		selections.append((i, chosen))
		choose.pop(choose.index(chosen))
	return selections


def send_mails(info, selections):
	for pair in selections:
		sender = pair[0]
		receiver = pair[1]
		email = info[sender].email()
		wishlist = info[receiver].wishlist()
		mail.mail(sender, receiver, email, wishlist)


def main(argv):
	if not len(argv) == 2:
		raise TypeError('This takes 2 arguments ({} given)'.format(len(argv)))
	info, names = enter_info(argv[0], argv[1])
	selections = draw_names(names)
	send_mails(info, selections)


if __name__ == "__main__":
	main(sys.argv[1:])
