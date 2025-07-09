count=0
def joel():
    global count     # Allowing the function to use the Global variable
    count=count+1
    print("Hi Joel")
    print("This function has been called",{count}, "times")

joel()
joel()
joel()
joel()