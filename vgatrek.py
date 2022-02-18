# Import modules
# Lib has the custom modules
from lib import art # Art lib that has screens
from lib import menus as menu # Game menus are here
# Connect MySQL
from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser

'''
def connect():
	""" Connect to MySQL database """
	conn = None
	try:
		conn = mysql.connector.connect(host='localhost',
										database='vgatrek',
										user='root',
										password='')
		if conn.is_connected():
			#print('Connected to MySQL database')
			pass
	except Error as e:
		print(e)

	finally:
		if conn is not None and conn.is_connected():
			conn.close()
#connect()
'''
def read_db_config(filename='dbconfig.ini', section='mysql'):
	""" Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db

def connect():
	""" Connect to MySQL database """

	db_config = read_db_config()
	conn = None
	try:
		#print('Connecting to MySQL database...')
		conn = MySQLConnection(**db_config)

		if conn.is_connected():
			#print('Connection established.')
			pass
		else:
			#print('Connection failed.')
			pass
	except Error as error:
		print(error)

	finally:
		if conn is not None and conn.is_connected():
			conn.close()
			#print('Connection closed.')
			pass

def query_with_fetchone():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM players")

        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


# Show random screen
art.mainscreen()

# Show main menu
menu.main()