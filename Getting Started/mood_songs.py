import webbrowser

mood = input("What kind of mood are you in(sad, happy, angry): ")

if mood == "sad":
    webbrowser.open("https://www.youtube.com/watch?v=Cwkej79U3ek")
elif mood == "happy":
    webbrowser.open("https://www.youtube.com/watch?v=fWNaR-rxAic")
elif mood == "angry":
    webbrowser.open("https://www.youtube.com/watch?v=seEjFQ0lNhY")