#Напишете програма, която чете текст от конзолата(стринг) и го принтира, докато не
# получи командата "Stop".
word = ""
while word != "Stop":
    word = input()
    if word == "Stop":
        break
    print(word)
