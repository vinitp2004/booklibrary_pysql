###############################################################################
# Authors: Vinit Patel
#
# Revision: 0.0.1
#
# TABLE: users
# userid       INTEGER  (unique ID in the table)
# userfname    TEXT     (First name of the user)
# userlname    TEXT     (Last name of the user)
# useraddress  TEXT     (Address of the user)
# useremail    TEXT     (Email ID of the user)
# userphone    TEXT     (Phone number of the user)
# usertype     INTEGER  (Type of user: 1 = friend, 2 = relative)
# useramount   INTEGER  (Fine Amount to be paid by the user)
# usermaxloan  INTEGER  (Max number of items that can be loaned = 5)
# useritemid1  INTEGER  (ItemID of item # 1 loaned to the user)
# useritemid2  INTEGER  (ItemID of item # 2 loaned to the user)
# useritemid3  INTEGER  (ItemID of item # 3 loaned to the user)
# useritemid4  INTEGER  (ItemID of item # 4 loaned to the user)
# useritemid5  INTEGER  (ItemID of item # 5 loaned to the user)
# userloan     INTEGER  (Number of items loaned to this user <=5)
# useractive   INTEGER  (Status of the user: 1 = active, 0 = inactive, 2 = banned)
#
# TABLE: items
# itemid       INTEGER  (unique ID in the table)
# itemname     TEXT     (name of the item)
# itemtype     INTEGER  (Item Type, 1 = Paperback Book, 2 = Hardcover Book, 3 = Magazine, 4 = CD, etc.)
# itemauthor   TEXT     (Author(s) of the book)
# itempublisherTEXT     (Publisher of the book)
# itemISBN     INTEGER  (ISBN of the item)
# itemartist   TEXT     (Artist(s) of the album)
# itemproducer TEXT     (Producer of the album)
# itempubyear  INTEGER  (Publishing/releasing year of the item)
# itemadddate  INTEGER  (Date when the item was added to the database)
# itemgenre    INTEGER  (Item Genre, 1 = Comedy, 2 = Adult, 4 = Children, 8 = Novel, etc.) (Should be 2^)
# itemlanguage INTEGER  (Item Language, 1 = English, 2 = Gujarati, 3 = Hindi, etc.)
# itemstatus   INTEGER  (Item Status in database, 1 = available, 2 = loaned, 3 = lost/stolen, 4 = in process of adding)
# itemloandate TEXT     (Date when the item was loaned)
# itemretdate  TEXT     (Due date/return date of the item)
# itemuserid   INTEGER  (ID of the user who has the item on loan)
#FUTURE COLUMNS
# itempages    INTEGER  (Number of pages in case item is a book)
# itemlength   INTEGER  (Number of minutes of length in case item is an album)
# itemfine     REAL     (Fine if any)
# finestatus   INTEGER  (Fine paid or not, 0 = paid, 1 = not paid, 2 = forgiven)
# itemtotalfineREAL     (Total fine collected on this item)
# itemtotalou-
#    tstanding REAL     (Total fine yet to be paid on this item)
#
# TABLE: for types of users
# TABLE: for status of users
# TABLE: for types of items
# TABLE: for genres of items
# TABLE: for languages of items
# TABLE: for status of items
# TABLE: for status of fine
#
###############################################################################
# When        Who           What
#------------------------------------------------------------------------------
# 11/10/2015  Vinit Patel   First draft of the library code
###############################################################################

# CREATE TABLE users ()
# INSERT INTO users VALUES ()
# UPDATE users SET userfname = 'newname' WHERE userid = 2
# ALTER TABLE users ADD COLUMN usercity text
# DELETE from users WHERE usercity IS NULL
# SELECT * FROM users
## SELECT DISTINCT usertype FROM users
## SELECT * FROM users WHERE userid < 3
## SELECT * FROM users WHERE userfname LIKE 'Jose_hine'
## SELECT * FROM users WHERE userlname LIKE 'S%'
## SELECT * FROM users WHERE userfname LIKE '%n%'
## SELECT * FROM users WHERE userfname BETWEEN 'A' AND 'J'
## SELECT * FROM users WHERE userid BETWEEN 2 AND 5
## SELECT * FROM users WHERE userid BETWEEN 2 AND 5 AND usertype = 'friend'
## SELECT * FROM users WHERE userid BETWEEN 2 AND 5 OR usertype = 'friend'
## SELECT * FROM users ORDER BY userid ASC/DESC
## SELECT * FROM users ORDER BY userid ASC/DESC LIMIT 2
## SELECT * FROM users WHERE userfname LIKE 'Jose_hine' AND userlname LIKE ='S_river' ORDER BY userid ASC;
## SELECT COUNT(*) FROM users
## SELECT COUNT(*) FROM users WHERE userfname LIKE 'Jose_hine'
## SELECT usertype, COUNT(*) FROM users GROUP BY usertype
## SELECT usertype, COUNT(*) FROM users WHERE useramount > 10.0 GROUP BY usertype
## SELECT SUM(loans) FROM users
## SELECT usertype, SUM(loans) FROM users GROUP BY usertype
## SELECT MAX(loans) FROM users
## SELECT userfname, usertype, MAX(loans) FROM users GROUP BY usertype
## SELECT MIN(loans) FROM users
## SELECT userfname, usertype, MIN(loans) FROM users GROUP BY usertype
## SELECT AVG(loans) FROM users
## SELECT usertype, AVG(loans) FROM users GROUP BY usertype
## SELECT usertype, ROUND(AVG(loans), 2) FROM users GROUP BY usertype
## SELECT usertype, ROUND(AVG(loans)) FROM users GROUP BY usertype

## SELECT * FROM users JOIN books ON users.albums.userbookid1 = books.id
## SELECT * FROM users LEFT JOIN books ON users.albums.userbookid1 = books.id ## when no book is loaned
## SELECT users.userid AS 'USERID', users.userfname, books.id AS 'BOOKID' FROM users JOIN books ON users.albums.userbookid1 = books.id WHERE books.id > 100

###############################################################################
#Various Imports
###############################################################################
import sqlite3
import getpass

###############################################################################
#Various subroutines
###############################################################################
###############################################################################
#Helper functions
###############################################################################
def getnumberinput():
   getinput = raw_input()
   try:
      getinput = int(getinput)
   except ValueError:
      print "That is not a valid number. Exiting"
      getinput = 0
   return getinput
def convertsqloutput(c):
   (sqloutput) = c.fetchone()
   sqloutput = int(sqloutput[0])
   return sqloutput
###############################################################################
#Library functionality functions
###############################################################################
###############################################################################
#For deleting the table
###############################################################################
def deletetable(tableID):
   conn=sqlite3.connect('example.db')
   c = conn.cursor()
   if (tableID == 1): # deletes table of users
      c.execute('DROP TABLE IF EXISTS users')
   elif (tableID == 2): # deletes table of items
      c.execute('DROP TABLE IF EXISTS items')
   else:
      print "Incorrect tableID set"
   conn.commit()
   conn.close()
###############################################################################
#For creating the table for first time
###############################################################################
def createtable(tableID):
   conn=sqlite3.connect('example.db')
   c = conn.cursor()
   if (tableID == 1): # creates table of users
      c.execute('''CREATE TABLE users
            (userid BIGINT, userfname VARCHAR(20), userlname VARCHAR(20), useraddress VARCHAR(50), useremail VARCHAR(25), userphone VARCHAR(20), usertype SMALLINT, userfine DECIMAL(2,2), usermaxloan SMALLINT, useritemid1 BIGINT, useritemid2 BIGINT, useritemid3 BIGINT, useritemid4 BIGINT, useritemid5 BIGINT, userloan SMALLINT, userstatus SMALLINT)''')
   elif (tableID == 2): # creates table of items
      c.execute('''CREATE TABLE items
            (itemid BIGINT, itemname VARCHAR(50), itemtype SMALLINT, itemauthor VARCHAR(40), itempublisher VARCHAR(40), itemISBN_10 VARCHAR(20), itemartist VARCHAR(40), itemproducer VARCHAR(40), itempubyear INTEGER, itemadddate DATE, itemgenre SMALLINT, itemlanguage SMALLINT, itemstatus SMALLINT, itemloandate DATE, itemretdate DATE, itemuserid BIGINT)''')
   else:
      print "Incorrect tableID set"
   conn.close()
###############################################################################
#For printing entire table without any conditions
###############################################################################
def printtable(tableID):
   conn=sqlite3.connect('example.db')
   c = conn.cursor()
   if (tableID == 1): # prints table of users
      for row in c.execute('SELECT * FROM users'):
         print row
   elif (tableID == 2): # prints table of items
      for row in c.execute('SELECT * FROM items'):
         print row
   elif (tableID == 3): # prints table of items issued
      for row in c.execute('SELECT * FROM issueditems'):
         print row
   conn.close()
###############################################################################
#For entering new user or new item
###############################################################################
def insertrow(tableID):
   conn=sqlite3.connect('example.db')
   c = conn.cursor()
   if (tableID == 1): # inserts new user in users table
      print "You want to enter a new user (y/n)?"
      rawinput = raw_input()
      if rawinput == 'y':
         # Gather user's inputs
         print "Enter user's first name:"
         userfname = raw_input()
         print "Enter user's last name:"
         userlname = raw_input()
         print "Enter user's address (in single line) (eg, 123, ABC Road, DEF City, CA-12345):"
         useraddress = raw_input()
         print "Enter user's Email ID:"
         useremail = raw_input()
         print "Enter user's phone (in xxx-xxx-xxxx format):"
         userphone = raw_input()
         
         # Open the database and insert new user details
         conn=sqlite3.connect('example.db')
         c = conn.cursor()
         userID = c.execute('SELECT MAX(userid) FROM users')
         c.execute('INSERT INTO users VALUES (' + str(userID+1) + ', userfname, userlname, useraddress, useremail, userphone, ''friend'', 0.00, 5, 0, 0, 0, 0, 0, 0, 1, 0)')
   elif (tableID == 2): # inserts new item in items table
      print "You want to enter a new item (y/n)?"
      rawinput = raw_input()
      if rawinput == 'y':
         # Gather user's inputs
         print "Enter item name:"
         itemname = raw_input()
         print "Enter item type (1 = Paperback Book, 2 = Hardcover Book, 3 = Magazine, 4 = CD, 5 = Audio tape, 6 = Video Tape, 7 = DVD, 8 = BlueRay):"
         itemtype = getnumberinput()
         if (itemtype == 1 or itemtype == 2):
            print "Enter book author:"
            itemauthor = raw_input()
            print "Enter book publisher:"
            itempublisher = raw_input()
            print "Enter item ISBN:"
            itemISBN = raw_input()
            itemartist = 0
            itemproducer = 0
         elif (itemtype == 3):
            itemauthor = 0
            print "Enter magazine publisher:"
            itempublisher = raw_input()
            itemISBN = 0
            itemartist = 0
            itemproducer = 0
         elif (itemtype == 4 or itemtype == 5 or itemtype == 6 or itemtype == 7 or itemtype == 8):
            itemauthor = 0
            itempublisher = 0
            itemISBN = 0
            print "Enter album artist:"
            itemartist = raw_input()
            print "Enter album producer:"
            itemproducer = raw_input()
         else:
            print "Incorrect type entered. Start Again"
            return
         print "Enter item publishing year:"
         itempubyear = getnumberinput()
         print "Enter item add date:"
         itemadddate = raw_input()
         print "Enter item genre:"
         itemgenre = getnumberinput()
         print "Enter item language:"
         itemlanguage = getnumberinput()
         
         # Open the database and insert new user details
         conn=sqlite3.connect('example.db')
         c = conn.cursor()
         c.execute('SELECT MAX(itemid) FROM items')
         itemID = convertsqloutput(c)
         c.execute('INSERT INTO items VALUES (' + str(itemID+1) + ', itemname, itemtype, itemauthor, itempublisher, itemISBN, itemartist, itemproducer, itempubyear, itemadddate, itemgenre, itemlanguage, 1, 0, 0)')
   else: 
      print "Incorrect table ID specified"
   conn.commit()
   conn.close()
###############################################################################
#For loaning an item from database
###############################################################################
def loanitem(itemID, userID):
   conn=sqlite3.connect('example.db')
   c = conn.cursor()
   itemloaned = 0 # flag to indicate if loan process was successful
   c.execute('SELECT itemstatus FROM items WHERE itemid=' + str(itemID))
   itemstat = convertsqloutput(c)
   if (itemstat == 1): 
   # item status = 1 means available to loan
      # query how many items are loaned to this user
      c.execute('SELECT userloan FROM users WHERE userid=' + str(userID))
      userloans = convertsqloutput(c)
      # query the max number of items that can be loaned to this user
      c.execute('SELECT usermaxloan FROM users WHERE userid=' + str(userID))
      usermaxloans = convertsqloutput(c)
      # if items loaned is less than max_can_be_loaned, then proceed to loan
      if (userloans < usermaxloans):
         for i in range (0, usermaxloans):
            # query the first useritemid field which is set to 0
            c.execute('SELECT useritemid' + str(i+1) + ' FROM users WHERE userid=' + str(userID))
            newitemid = convertsqloutput(c)
            if (newitemid == 0):
            # when empty field found, associate the new item to that field
               # set item status = 2 means loaned
               c.execute('UPDATE items SET itemstatus=2 WHERE itemid=' + str(itemID))
               # set user's item field with the new item's ID
               c.execute('UPDATE users SET useritemid' + str(i+1) + '=' + str(itemID) + ' WHERE userid=' + str(userID))
               # increase the count of items loaned to this user
               c.execute('UPDATE users SET userloan=' + str(userloans+1) + ' WHERE userid=' + str(userID))
               # set item's user field with the new user ID
               c.execute('UPDATE items SET itemuserid=' + str(userID) + ' WHERE itemid=' + str(itemID))
               itemloaned = 1
               break
      else:
         print "User reached max loan number. Please return one or more items to loan new items."
   else:
      print "Item not available to loan"
   
   if (itemloaned == 1):
      print "Item issued"
      print "User has now total items: ", userloans+1
   else:
      print "Item not issued"
   conn.commit()
   conn.close()
###############################################################################
#For returning the item back to database
###############################################################################
def returnitem(itemID):
   conn=sqlite3.connect('example.db')
   c = conn.cursor()
   itemreturned = 0 # flag to indicate if return process was successful
   # query the userID of the user who loaned this item
   c.execute('SELECT itemuserid FROM items WHERE itemid=' + str(itemID))
   userID = convertsqloutput(c)
   # query how many items are loaned to this user
   c.execute('SELECT userloan FROM users WHERE userid=' + str(userID))
   userloans = convertsqloutput(c)
   # query the max number of items that can be loaned to this user
   c.execute('SELECT usermaxloan FROM users WHERE userid=' + str(userID))
   usermaxloans = convertsqloutput(c)
   # go through each itemid associated with this user
   for i in range (0, usermaxloans):
      # get the itemid from each field one by one
      c.execute('SELECT useritemid' + str(i+1) + ' FROM users WHERE userid=' + str(userID))
      curritemid = convertsqloutput(c)
      # start the return process once the itemid of the returning item matches the one in user's itemid field
      if (curritemid == itemID):
         # update user's itemid field to 0 as the item is no longer loaned to the user
         c.execute('UPDATE users SET useritemid' + str(i+1) + '=0 WHERE userid=' + str(userID))
         # update user's number of loaned items to current loaned items - 1
         c.execute('UPDATE users SET userloan=' + str(userloans - 1) + ' WHERE userid=' + str(userID))
         # update the items's status to 1 (available to loan)
         c.execute('UPDATE items SET itemstatus=1 WHERE itemid=' + str(itemID))
         itemreturned = 1
         break
   if (itemreturned == 1):
      print "User returned item successfully"
      print "User has now total items: ", userloans - 1
   else:
      print "Item not returned successfully"
   conn.commit()
   conn.close()
###############################################################################
#For querying all the loaned items
###############################################################################
def queryallloaneditems():
   conn=sqlite3.connect('example.db')
   c = conn.cursor()
   loanstatus = 2 #loanstatus 2 means item is loaned
   for row in c.execute('SELECT itemid, itemname, itemloandate, itemretdate, itemuserid FROM items WHERE itemstatus=' + str(loanstatus)):
      print row
   conn.close()
###############################################################################
#For querying total outstanding fine
###############################################################################
###############################################################################
#For querying items loaned to a particular user
###############################################################################
def queryallloaneditemsbyuser(userID):
   totloan = 0
   conn=sqlite3.connect('example.db')
   c = conn.cursor()
   c.execute('SELECT userloan FROM users WHERE userID=' + str(userID))
   userloan = convertsqloutput(c)
   c.execute('SELECT usermaxloan FROM users WHERE userid=' + str(userID))
   usermaxloans = convertsqloutput(c)
   for i in range (0, usermaxloans):
      c.execute('SELECT useritemid' + str(i+1) + ' FROM users WHERE userid=' + str(userID))
      curritemID = convertsqloutput(c)
      if (curritemID != 0):
         totloan = totloan + 1
         print totloan, ": ", curritemID[0]
   if (totloan != userloan):
      print "Error: Totloans not matching userloans"
   conn.close()
###############################################################################
#For querying outstanding fine from a particular user
###############################################################################
###############################################################################
#For querying return date of an loaned items
###############################################################################
def queryreturndateloaneditems():
   conn=sqlite3.connect('example.db')
   c = conn.cursor()
   loanstatus = 2 #loanstatus 2 means item is loaned
   for row in c.execute('SELECT itemid, itemname, itemretdate, itemuserid FROM items WHERE itemstatus=' + str(loanstatus) + ' ORDER BY itemretdate DESC'):
      print row
   conn.close()
###############################################################################
#For querying items by name
###############################################################################
def queryitemsbyname(itemNAME):
   conn=sqlite3.connect('example.db')
   c = conn.cursor()
   for row in c.execute('SELECT itemid, itemname, itemauthor, itemartist FROM items WHERE itemname LIKE "%' + itemNAME + '%"' + ' ORDER BY itemname ASC'):
      print row
   conn.close()
###############################################################################
#For querying items by author/artist
###############################################################################
def queryitemsbyauthor(itemAUTHOR):
   conn=sqlite3.connect('example.db')
   c = conn.cursor()
   for row in c.execute('SELECT itemid, itemname, itemauthor, itemartist FROM items WHERE itemauthor LIKE "%' + itemAUTHOR + '%"' + ' OR itemartist LIKE "%' + itemAUTHOR + '%"' + ' ORDER BY itemname ASC'):
      print row
   conn.close()
###############################################################################
#For querying items by name and author
###############################################################################
def queryitemsbynameauthor(itemNAME, itemAUTHOR):
   conn=sqlite3.connect('example.db')
   c = conn.cursor()
   for row in c.execute('SELECT itemid, itemname, itemauthor, itemartist FROM items WHERE itemname LIKE "%' + itemNAME + '%"' + ' AND (itemauthor LIKE "%' + itemAUTHOR + '%"' + ' OR itemartist LIKE "%' + itemAUTHOR + '%")' + ' ORDER BY itemname ASC'):
      print row
   conn.close()
###############################################################################
#For querying items by name and author
###############################################################################
def queryall(tableID):
   conn=sqlite3.connect('example.db')
   c = conn.cursor()
   if (tableID == 1): # queries basic fields of all users from users table
      for row in c.execute('SELECT userid, userfname, userlname, userphone, useremail FROM users ORDER BY userid ASC'):
         print row
   elif (tableID == 2): # queries basic fields of all items from items table
      for row in c.execute('SELECT itemid, itemname, itemauthor, itemartist FROM items ORDER BY itemname ASC'):
         print row
   elif (tableID == 3): # queries all the fields of all users from the users table
      for row in c.execute('SELECT * FROM users ORDER BY userid ASC'):
         print row
   elif (tableID == 4): # queries all the fields of all items from the items table
      for row in c.execute('SELECT * FROM items ORDER BY itemname ASC'):
         print row
   conn.close()
###############################################################################
#Fill up test data in the table
###############################################################################
def filluptestdata():
   conn=sqlite3.connect('example.db')
   c = conn.cursor()
   c.execute("INSERT INTO users VALUES (1,   'Josephine',   'Skriver',     '123, ABC Road, San Ramon, CA-12345, USA',  'Josephine@hotmail.com',    '111-111-1111',   'friend',   0.00, 5, 0, 0, 0, 0, 0, 0, 1)")
   c.execute("INSERT INTO users VALUES (2,   'Adriana',     'Lima',        '456, def Road, San Ramon, CA-12345, USA',  'Adriana@yahoo.com',        '222-222-2222',   'friend',   0.00, 3, 0, 0, 0, 0, 0, 0, 1)")
   c.execute("INSERT INTO users VALUES (3,   'Candice',     'Swanepoel',   '789, ghi drive, San Ramon, CA-12345, USA', 'Candice@yahoo.com',        '333-333-3333',   'friend',   0.00, 5, 0, 0, 0, 0, 0, 0, 1)")
   c.execute("INSERT INTO users VALUES (4,   'Alessandra',  'Ambrosio',    '134, kkj drive, San Ramon, CA-12345, USA', 'Alessandra@gmail.com',     '194-444-4444',   'friend',   0.00, 5, 0, 0, 0, 0, 0, 0, 1)")
   c.execute("INSERT INTO users VALUES (5,   'Behati',      'Prinsloo',    '498, kjs drive, San Ramon, CA-12345, USA', 'Behati@yahoo.com',         '498-982-3456',   'friend',   0.00, 5, 0, 0, 0, 0, 0, 0, 1)")
   c.execute("INSERT INTO users VALUES (6,   'Lily',        'Aldrige',     '390, klo drive, San Ramon, CA-12345, USA', 'Lily@gmail.com',           '982-982-4444',   'friend',   0.00, 4, 0, 0, 0, 0, 0, 0, 1)")
   c.execute("INSERT INTO users VALUES (7,   'Elsa',        'Hosk',        '982, ade drive, San Ramon, CA-12345, USA', 'Elsa@yahoo.com',           '498-444-3457',   'friend',   0.00, 3, 0, 0, 0, 0, 0, 0, 1)")
   c.execute("INSERT INTO users VALUES (8,   'Jac',         'Jagaciak',    '194, azv drive, San Ramon, CA-12345, USA', 'Jac@hotmail.com',          '903-498-4444',   'friend',   0.00, 0, 0, 0, 0, 0, 0, 0, 1)")
   c.execute("INSERT INTO users VALUES (9,   'Kate',        'Grigorieva',  '903, ekx drive, San Ramon, CA-12345, USA', 'Kate@gmail.com',           '194-903-7894',   'friend',   0.00, 1, 0, 0, 0, 0, 0, 0, 1)")
   c.execute("INSERT INTO users VALUES (10,  'Taylor',      'Hill',        '237, ilz drive, San Ramon, CA-12345, USA', 'Taylor@hotmail.com',       '982-498-4321',   'friend',   0.00, 4, 0, 0, 0, 0, 0, 0, 1)")

   c.execute("INSERT INTO items VALUES (1, \
      'Diary of Wimpy Kid 10 Old School',   \
      2, \
      'Jeff Kinney',     \
      'Amulet Books', \
      'B00V8JK8A4',\
      '',  \
      '',  \
      2015,   \
      '11/11/2015',   \
      5, \
      1, \
      1, \
      '', \
      '', \
      0)")
   c.execute("INSERT INTO items VALUES (2, \
      'Harry Potter Coloring Book',   \
      2, \
      'Scholastic',     \
      'Scholastic Inc.', \
      '1338029991',\
      '',  \
      '',  \
      2015,   \
      '11/11/2015',   \
      4, \
      1, \
      1, \
      '', \
      '', \
      0)")
   c.execute("INSERT INTO items VALUES (3, \
      'Fallout 4 Vault Dweller''s Survival Guide Collector''s Edition: Prima Official Game Guide (Prima Official Game Guides)',   \
      2, \
      'David Hodgson, Nick von Esmarch',     \
      'Prima Games', \
      '0744016312',\
      '',  \
      '',  \
      2015,   \
      '11/11/2015',   \
      2, \
      1, \
      1, \
      '', \
      '', \
      0)")
   c.execute("INSERT INTO items VALUES (4, \
      'Troublemaker: Surviving Hollywood and Scientology',   \
      2, \
      'Leah Remini, Rebecca Paley',     \
      'Ballantine Books', \
      'B015BCX0JY',\
      '',  \
      '',  \
      2015,   \
      '11/11/2015',   \
      2, \
      1, \
      1, \
      '', \
      '', \
      0)")
   c.execute("INSERT INTO items VALUES (5, \
      'The Life-Changing Magic of Tidying Up: The Japanese Art of Decluttering and Organizing',   \
      2, \
      'Marie Kondo',     \
      'Ten Speed Press', \
      'B00KK0PICK',\
      '',  \
      '',  \
      2014,   \
      '11/11/2015',   \
      2, \
      1, \
      1, \
      '', \
      '', \
      0)")
   c.execute("INSERT INTO items VALUES (6, \
      'The Pioneer Woman Cooks: Dinnertime: Comfort Classics, Freezer Food, 16-Minute Meals, and Other Delicious Ways to Solve Supper!',   \
      2, \
      'Ree Drummond',     \
      'William Morrow Cookbooks', \
      'B00SRUZRNU',\
      '',  \
      '',  \
      2015,   \
      '11/11/2015',   \
      2, \
      1, \
      1, \
      '', \
      '', \
      0)")
   c.execute("INSERT INTO items VALUES (7, \
      'Sweet Home Alabama',   \
      5, \
      '',     \
      '', \
      '0788842978',\
      'Reese Witherspoon',  \
      'BUENA VISTA HOME VIDEO',  \
      2004,   \
      '11/11/2015',   \
      2, \
      1, \
      1, \
      '', \
      '', \
      0)")
   conn.commit()
   conn.close()

###############################################################################
#Options available for regular user
###############################################################################
def regularuseroptions():
   while(1):
      print "\n\nEnter options 1-4. 0 to exit"
      print "1 - To query items loaned to a user"
      print "2 - To query items by name"
      print "3 - To query items by author"
      print "4 - To query items by name and author"
      userinput = getnumberinput()
      if (userinput == 1):
         print "Query items loaned to a user"
         print "Enter userID"
         userID = getnumberinput()
         queryallloaneditemsbyuser(userID)
      elif (userinput == 2):
         print "Query items by name"
         print "Enter item name"
         itemNAME = raw_input()
         queryitemsbyname(itemNAME)
      elif (userinput == 3):
         print "Query items by author or artist"
         print "Enter author/artist name"
         itemAUTHOR = raw_input()
         queryitemsbyauthor(itemAUTHOR)
      elif (userinput == 4):
         print "Query items by name and author"
         print "Enter item name"
         itemNAME = raw_input()
         print "Enter author/artist name"
         itemAUTHOR = raw_input()
         queryitemsbynameauthor(itemNAME, itemAUTHOR)
      else:
         print "Exiting"
         break
###############################################################################
#Options available for admin user
###############################################################################
def adminuseroptions():
   while(1):
      print "\n\nEnter options 1-11. 0 to exit"
      print "1 - To add a new user"
      print "2 - To insert a new item to the database"
      print "3 - To loan an item"
      print "4 - To return an item"
      print "5 - To query items loaned from library"
      print "6 - To query items loaned to a user"
      print "7 - To query items by name"
      print "8 - To query items by author"
      print "9 - To query items by name and author"
      print "10 - To query all users basic info"
      print "11 - To query all items basic info"
      print "12 - To query all users all info"
      print "13 - To query all items all info"
      userinput = getnumberinput()
      if(userinput == 1):
         print "Insert a new user"
         insertrow(userinput)
      elif (userinput == 2):
         print "Insert a new item to the database"
         insertrow(userinput)
      elif (userinput == 3):
         print "Check out an item to a user"
         print "Enter item ID to be checked out"
         itemID = getnumberinput()
         print "Enter user ID of the user who is checking out"
         userID = getnumberinput()
         loanitem(itemID, userID)
      elif (userinput == 4):
         print "Return an item from the user"
         print "Enter item ID to be returned"
         itemID = getnumberinput()
         returnitem(itemID)
      elif (userinput == 5):
         print "Query all loaned items from the database"
         queryallloaneditems()
      elif (userinput == 6):
         print "Query all loaned items by a user"
         print "Enter userID"
         userID = getnumberinput()
         queryallloaneditemsbyuser(userID)
      elif (userinput == 7):
         print "Query all items by name"
         print "Enter item name"
         itemNAME = raw_input()
         queryitemsbyname(itemNAME)
      elif (userinput == 8):
         print "Query all items by author or artist"
         print "Enter author/artist name"
         itemAUTHOR = raw_input()
         queryitemsbyauthor(itemAUTHOR)
      elif (userinput == 9):
         print "Query all items by name and author"
         print "Enter item name"
         itemNAME = raw_input()
         print "Enter author/artist name"
         itemAUTHOR = raw_input()
         queryitemsbynameauthor(itemNAME, itemAUTHOR)
      elif (userinput == 10):
         print "Query all users basic info"
         tableID = 1
         queryall(tableID)
      elif (userinput == 11):
         print "Query all items basic info"
         tableID = 2
         queryall(tableID)
      elif (userinput == 12):
         print "Query all users all info"
         tableID = 3
         queryall(tableID)
      elif (userinput == 13):
         print "Query all items all info"
         tableID = 4
         queryall(tableID)
      else:
         print "Exiting"
         break

###############################################################################
#Main routine
###############################################################################
tablecreated = 0
tablefilled = 0
print "Let's Start"
# deletetable(1)
# deletetable(2)
# createtable(1)
# print "table 1 created"
# createtable(2)
# print "table 2 created"
# printtable(1)
# print "table 1 printed"
# printtable(2)
# print "table 2 printed"
# filluptestdata()
# print "test data filled"
# printtable(1)
# print "table 1 printed"
# printtable(2)
# print "table 2 printed"
while (1):
   if (tablecreated == 1):
      print "Table is already created"
      if (tablefilled == 1):
         print "Table is already filled with test data"
      else:
         print "Fill table first"
   else:
      print "Create table first"
   print "\n\nWho are you (Enter 1-regular user, 2-admin user, 3-create table, 4-fill test data, 0 to exit):"
   usermodeinput = getnumberinput()
   if (usermodeinput == 1):
      regularuseroptions()
   elif (usermodeinput == 2):
      print "Enter Admin Password:"
      pw = getpass.getpass()
      if (pw == 'MyPa$$w0rd'):
         adminuseroptions()
      else:
         print "Don't fake to be an admin"
         print "Exiting"
   elif (usermodeinput == 3):
      deletetable(1)
      deletetable(2)
      createtable(1)
      createtable(2)
      tablecreated = 1
   elif (usermodeinput == 4):
      filluptestdata()
      tablefilled = 1
   elif (usermodeinput == 0):
      print "Exiting"
      break
   else:
      print "Start Again"

print "******Happy Programming******"
