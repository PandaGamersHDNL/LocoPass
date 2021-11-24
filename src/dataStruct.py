class dataHandling:
    def __init__(self):
        print("boop")
    
    def createData(name, username, email, password, url, desciption):
        return{
            "name": name,
            "username": username, 
            "email": email,
            "password": password,
            "url": url,
            "description": desciption
        }
    
    def createEmpty():
        return {
            "entries": []
        }