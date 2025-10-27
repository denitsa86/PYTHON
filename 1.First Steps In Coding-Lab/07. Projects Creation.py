#Напишете програма, която изчислява колко часа ще са необходими на един архитект,
# за да изготви проектите на няколко строителни обекта. Изготвянето на един проект
# отнема три часа. Вход:
#1.	Името на архитекта - текст
#2.	Брой на проектите, които трябва да изготви - цяло число в интервала [0 … 100]
#Output: •	"The architect {името на архитекта} will need {необходими часове}
# hours to complete {брой на проектите} project/s."
name = input()
projects_count = int(input())
hours_needed = projects_count * 3
print(f"The architect {name} will need {hours_needed} hours to complete {projects_count} project/s.")