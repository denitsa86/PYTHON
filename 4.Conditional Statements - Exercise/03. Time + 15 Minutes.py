#чете час и минути от 24-часово денонощие, въведени от потребителя и изчислява
# колко ще е часът след 15 минути. Резултатът да се отпечата във формат
# часове:минути. Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59.
# Часовете се изписват с една или две цифри. Минутите се изписват винаги с по две
# цифри, с водеща нула, когато е необходимо.
hours = int(input())
minutes = int(input())
converted_time = hours * 60 + minutes +15
hours = int(converted_time / 60)
if hours > 23:
    hours = 0
minutes = int(converted_time % 60)
if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")