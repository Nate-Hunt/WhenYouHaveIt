"""Generates a wav file from """
import mysql.connector
mydb = mysql.connector.connect()
import speech_recognition as sr

def extract(inFile, result):
    mydb = mysql.connector.connect(
        host = inFile.HOST,
        user = inFile.USER,
        passwd = inFile.PASSWD,
        database = inFile.DATABASE,
        port = inFile.PORT
    )
    
    resultString = ""

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
        "1st Samuel": 8,
        "2nd Samuel": 9,
        "1st Kings": 10,
        "2nd Kings": 11,
        "1st Chronicles": 12,
        "2nd Chronicles": 13,
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
        "1st Corinthians": 45,
        "2nd Corinthians": 46,
        "Galatians": 47,
        "Ephesians": 48,
        "Philippians": 49,
        "Colossians": 50,
        "1st Thessalonians": 51,
        "2nd Thessalonians": 52,
        "1st Timothy": 53,
        "2nd Timothy": 54,
        "Titus": 55,
        "Philemon": 56,
        "Hebrews": 57,
        "James": 58,
        "1st Peter": 59,
        "2nd Peter": 60,
        "1st John": 61,
        "2nd John": 62,
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
        "1st Samuel": 31,
        "2nd Samuel": 24,
        "1st Kings": 22,
        "2nd Kings": 25,
        "1st Chronicles": 29,
        "2nd Chronicles": 36,
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
        "1st Corinthians": 16,
        "2nd Corinthians": 13,
        "Galatians": 6,
        "Ephesians": 6,
        "Philippians": 4,
        "Colossians": 4,
        "1st Thessalonians": 5,
        "2nd Thessalonians": 3,
        "1st Timothy": 6,
        "2nd Timothy": 4,
        "Titus": 3,
        "Philemon": 1,
        "Hebrews": 13,
        "James": 5,
        "1st Peter": 5,
        "2nd Peter": 3,
        "1st John": 5,
        "2nd John": 1,
        "3 John": 1,
        "Jude": 1,
        "Revelation": 22
    }


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
                # print(*n)
                column1 = n[0]
                resultString += f"Your verse: {column1}\n"

        else:
            resultString = ("\n " + input_chapter + " is not a valid chapter for " + input_book + "!")

    else:
        resultString = ("\nYou have not input a valid book.\n")
    
    print("Excuted")
    return resultString

    # extract(result)

#Result is only the text with the most confidence

#Use the result as data to query the SQL database for the text to pop up

#This is a test
