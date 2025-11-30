#company names and an employees' id until you receive the command "End" command. Add each employee to the
# given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
#SoftUni -> AA12345
company_data = {}
data = input().split(" -> ")
while not data[0] == "End":
    company_name = data[0]
    employee = data[1]
    if company_name not in company_data:
        company_data[company_name] = []
        if employee not in company_data[company_name]:
            company_data[company_name].append(employee)
    else:
        if employee not in company_data[company_name]:
            company_data[company_name].append(employee)

    data = input().split(" -> ")

for key, value in company_data.items():
    print(f"{key}")
    for item in value:
        print(f"-- {item}")
