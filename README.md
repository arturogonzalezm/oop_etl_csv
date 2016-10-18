# Overview:

This is just a *very basic* example to work around the different ways to
create an ETL tool in Python 3.5 and it's csv module.

In this example OOP has been implemented.

### Specs:

1. CSV file will contain user data and have three columns: name, surname, email

2. CSV file will have an arbitrary list of users

3. Name and surname field should be set to be capitalised e.g. from “john” to “John”

4. Emails need to be set to be lower case

5. Get rid of the whitespaces

6. The script should validate the email address to make sure that it is valid (valid means that it is a legal email format e.g. “xxxx@asdf@asdf is not a legal format). In the instance that an email is invalid an error message will be reported to STDOUT

7. Script will iterate through the CSV rows and insert each record into a dedicated MySQL database into the table “users”

8. The users database table will need to be created/rebuilt as part of the Python script. This will be de ned as a Command Line directive below.

9. In the instance that an email is invalid, no insert should be made to database and error message reported to STDOUT.


### Script Command Line Directives:

- -- le "csv_filename" – this is the name of the CSV to be parsed

- --create_table – this will cause the MySQL users table to be built (and no further action will be taken)

- --dry_run – this will be used with the -- le directive in the instance that we want to run the script but not insert into the DB. All other functions will be executed, but the database won't be altered.

- -u – MySQL username

- -p – MySQL password

- -h – MySQL host

- --help – which will output the above list of directives with details.

### Technical Notes:

For this example I have utilised ...

- Language: Python 3.5

- Operative System: macOS sierra, also it works for any Linux/Unix based
  distribution.

- Modules/Libraries: Please refer to the conf, requirements.txt and
  setup files.

- PyCharm IDE

### Workflow:

- TODO...

----

>Notes:

>A sample project that exists as an aid to the 'Python Packaging User
>Guide <https://packaging.python.org>'_'s 'Tutorial on Packaging and
>Distributing Projects
><https://packaging.python.org/en/latest/distributing.html>'_.

>This projects does not aim to cover best practices for Python project
>development as a whole. For example, it does not provide guidance or tool
>recommendations for version control, documentation, or testing.


>This is the README file for the project.

>The file should use UTF-8 encoding and be written using ReStructured Text. It
>will be used to generate the project webpage on PyPI and will be displayed as
>the project homepage on common code-hosting services, and should be written for
>that purpose.

>Typical contents for this file would include an overview of the project, basic
>usage examples, etc. Generally, including the project changelog in here is not
>a good idea, although a simple "What's New" section for the most recent version
>may be appropriate.
