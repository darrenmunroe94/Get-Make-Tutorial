#used to obtian the makefile tutorial form gnu.org

from urllib import urlopen
import time
import sys

make_URI = ("http://www.gnu.org/software/make/manual/make.html")
make_Tut = open("C:\\C\\htmlMake_tutorial.html", 'r+')

def main(web_url, save_file): #connect to site, open file, save file
    
    try:        
        get_info = urlopen(web_url).read()
        
        save_file.truncate()
        save_file.write(str(get_info))
        
        print "Data succesfully obtained."
        
        time.sleep(5)
        
        sys.exit() #Weird Traceback error, closes fine though. 

    except Exception, e: #An error occured
        print("[-]Error %s has occured.[-]") % e
        
        time.sleep(5)
        
        sys.exit(0)

if __name__ == "__main__":
    main(make_URI, make_Tut)
