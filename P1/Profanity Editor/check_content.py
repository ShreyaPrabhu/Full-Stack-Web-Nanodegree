import urllib
def read_text():
    quotes = open(r"C:\Python27\Full-Stack-Web-Nanodegree\P1\Profanity Editor\textChecking.txt") #Replace with your file path
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert")
    elif "false" in output:
        print("There are no curse words in your file")
    else:
        print("Could not scan the content of the file")

read_text()
