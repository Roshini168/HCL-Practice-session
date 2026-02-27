with open("sunshine.txt","w+") as f:
    f.seek(0)
    f.write("The sun was setting behind the hills when Arjun found an old wooden box near the river. It was covered in dust and tied with a faded red ribbon. Curious and excited, he slowly opened it.")
    d= f.read()
    count=d.count("the")
    print(count)

