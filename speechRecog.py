import mysql.connector
mydb = mysql.connector.connect()

import cred.py

import speech_recognition as sr
r = sr.Recognizer()
file = sr.AudioFile('Audio Files/VoiceRecording2.wav')

with file as source:
    #r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    result = r.recognize_google(audio, language = 'en')


mydb = mysql.connector.connect(
    host = cred.host,
    user = cred.user,
    passwd = cred.passwd, 
    database = cred.database,
    port = cred.port
)

mycursor = mydb.cursor()

Books = {

    #Old Testament
    "Genesis": 0,
    "Exodus": 1,
    "Leviticus": 2,
    "Numbers": 3,
    "Deuteronomy": 4,
    "Joshua": 5,
    "Judges": 6,
    "Ruth": 7,
    "1 Samuel": 8,
    "2 Samuel": 9,
    "1 Kings": 10,
    "2 Kings": 11,
    "1 Chronicles": 12,
    "2 Chronicles": 13,
    "Ezra": 14,
    "Nehemiah": 15,
    "Esther": 16,
    "Job": 17,
    "Pslams": 18,
    "Proverbs": 19,
    "Ecclesiastes": 20,
    "Song of Solomon": 21,
    "Isaiah": 22,
    "Jeremiah": 23,
    "Lamentations": 24,
    "Ezekiel": 25,
    "Daniel": 26,
    "Hosea": 27,
    "Joel": 28,
    "Amos": 29,
    "Obadiah": 30,
    "Jonah": 31,
    "Micah": 32,
    "Nahum": 33,
    "Habakkuk": 34,
    "Zephaniah": 35,
    "Haggai": 36,
    "Zechariah": 37,
    "Malachi": 38,

    #New Testament
    "Matthew": 39,
    "Mark": 40,
    "Luke": 41,
    "John": 42,
    "Acts": 43,
    "Romans": 44,
    "1 Corinthians": 45,
    "2 Corinthians": 46,
    "Galatians": 47,
    "Ephesians": 48,
    "Philippians": 49,
    "Colossians": 50,
    "1 Thessalonians": 51,
    "2 Thessalonians": 52,
    "1 Timothy": 53,
    "2 Timothy": 54,
    "Titus": 55,
    "Philemon": 56,
    "Hebrews": 57,
    "James": 58,
    "1 Peter": 59,
    "2 Peter": 60,
    "1 John": 61,
    "2 John": 62,
    "3 John": 63,
    "Jude": 64,
    "Revelation": 65
    }

Chapters = {

    #Old Testament
    "Genesis": 50,
    "Exodus": 40,
    "Leviticus": 27,
    "Numbers": 36,
    "Deuteronomy": 34,
    "Joshua": 24,
    "Judges": 21,
    "Ruth": 4,
    "1 Samuel": 31,
    "2 Samuel": 24,
    "1 Kings": 22,
    "2 Kings": 25,
    "1 Chronicles": 29,
    "2 Chronicles": 36,
    "Ezra": 10,
    "Nehemiah": 13,
    "Esther": 10,
    "Job": 42,
    "Pslams": 150,
    "Proverbs": 31,
    "Ecclesiastes": 12,
    "Song of Solomon": 8,
    "Isaiah": 66,
    "Jeremiah": 52,
    "Lamentations": 5,
    "Ezekiel": 48,
    "Daniel": 12,
    "Hosea": 14,
    "Joel": 3,
    "Amos": 9,
    "Obadiah": 1,
    "Jonah": 4,
    "Micah": 7,
    "Nahum": 3,
    "Habakkuk": 3,
    "Zephaniah": 3,
    "Haggai": 2,
    "Zechariah": 14,
    "Malachi": 4,

    #New Testament
    "Matthew": 28,
    "Mark": 16,
    "Luke": 24,
    "John": 21,
    "Acts": 28,
    "Romans": 16,
    "1 Corinthians": 16,
    "2 Corinthians": 13,
    "Galatians": 6,
    "Ephesians": 6,
    "Philippians": 4,
    "Colossians": 4,
    "1 Thessalonians": 5,
    "2 Thessalonians": 3,
    "1 Timothy": 6,
    "2 Timothy": 4,
    "Titus": 3,
    "Philemon": 1,
    "Hebrews": 13,
    "James": 5,
    "1 Peter": 5,
    "2 Peter": 3,
    "1 John": 5,
    "2 John": 1,
    "3 John": 1,
    "Jude": 1,
    "Revelation": 22
    }


#import mysql.connector

#db = mysql.connector.connect()



#print(result)

#print(result[0: result.find(' ')])
#print(result[result.find(' ') + 1: result.find(':')])
#print(result[result.find(':') + 1])


input_book = result[0: result.find(' ')]
input_chapter = result[result.find(' ') + 1: result.find(':')]
input_verse = result[result.find(':') + 1]


if input_book in Books:
    # print(input_book + " is a valid book.")
    q_book = Books[input_book]

    if int(input_chapter) <= Chapters[input_book] and int(input_chapter) > 0:
        # print(input_chapter + " is a valid chapter for " + input_book + "!")

        #Commit SQL query with given information
        default_query_info = (Books[input_book], input_chapter, input_verse)
        default_query = "SELECT verse FROM bible WHERE Book = %s AND Chapter = %s AND Versecount = %s"
        mycursor.execute(default_query, default_query_info)


        for n in mycursor:
            print(*n)



    else:
        print("\n " + input_chapter + " is not a valid chapter for " + input_book + "!")


else:
    print("\nYou have not input a valid book.\n")


    

#Result is only the text with the most confidence

#Use the result as data to query the SQL database for the text to pop up

