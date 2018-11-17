# Script detailing web browesing mechanics
import webbrowser as wb

def search_Google(query):
	wb.open("http://google.com/?#q="+query,2)

def open_browser():
	wb.open("http://google.com/",2)