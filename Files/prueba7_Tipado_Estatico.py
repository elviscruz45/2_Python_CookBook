def is_palindrome(string:str) ->bool:
    string=string.replace(" ","").lower()
    string==string[::-1]
    return "casa"

def run():
    print(is_palindrome("hola"))
    
if __name__=="__main__":
    run()
    
    