# Secret Santa Name Draw
This is a Python code to help with drawing names for the Secret Santa event and then sending out the emails. Feel free to share and use it.

Each participant receives an email of who he/she picked, what their email is, and what they want (in form of wish list link or written request).

***Running the code:***

```sh
python main.py [--domain DOMAIN] [filename]
```

or

```sh
./main [--domain DOMAIN] [filename]
```

Arguments:

- filename (required): List of participants, their emails and what they want, in CSV format. Please see "example.csv" for an example.
- --domain, -D (optional): Domain name, if all the participants have the same email domains (i.e. gmail.com). In this case, your CSV file must have email usernames without the appending "@" and the domain name. See "example-domain.csv" for details.

***Files Required***

- CSV file: a list of participants, their emails and wish list
- config.py: configuration file that contains the host email (email from which all the notifications will be sent). See config-examples.py for details. If password is not provided, then the program will prompt for it.