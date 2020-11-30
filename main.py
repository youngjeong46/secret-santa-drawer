#!/usr/bin/env python3

import mail
import csv
import random
import copy
import sys
import argparse
import time


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
		email = row[1]
		if domain:
			email = convert_emails(email, domain)
		info[row[0]] = Person(row[0], email, row[2])

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
		time.sleep(2)


def main(argv):
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('file')
	parser.add_argument('--domain', '-D', dest="domain", action='store',
						help='domain for participant emails '\
							 '(use this if you are running a '\
							 'company secret santa, for example).')
	args = parser.parse_args()
	info, names = enter_info(args.file, args.domain)
	selections = draw_names(names)
	send_mails(info, selections)


if __name__ == "__main__":
	main(sys.argv[1:])
