class Employee:
    def __init__(self, id, name, department, evaluations):
        self.id = id
        self.name = name
        self.department = department
        self.evaluations = evaluations

    def average_score(self):
        return sum(self.evaluations.values()) / len(self.evaluations)
    
    def performance_level(self):
        avg = self.average_score()

        if avg >= 4.5:
            return "Excellent"
        elif avg >= 3.5:
            return "Good"
        elif avg >= 2.5:
            return "Average"
        else:
            return "Needs Improvement"
        
    def get_suggestions(self):

        tips = {
            "Punctuality": "Improve time management",
            "Teamwork": "Collaborate better with pears",
            "Productivity": "Set clear goals and avoid distractions",
            "Communication": "Be clear and listen well",
            "Problem-Solving": "Break down problems step-by-step"
        }

        suggestions = []
        for k, v in self.evaluations.items():
            if v < 3:
                suggestion = f"{k}:{tips[k]}"
                suggestions.append(suggestion)
        return suggestions

    def display_summary(self):
        print(f"\nID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print("Evaluation Scores:")
        for k, v in self.evaluations.items():
            print(f"    - {k}: {v}/5")
        print(f"\nAverage Score: {self.average_score()}")
        print(f"Performace Level: {self.performance_level()}")
        print("Suggestions:")
        for suggestion in self.get_suggestions():
            print(f"    - {suggestion}")
        print()

    
employee_db = {
    "101": {
        "name": "Alice",
        "department": "HR",
        "evaluations": {
            "Punctuality": 4.5,
            "Teamwork": 4.0,
            "Productivity": 3.8,
            "Communication": 4.2,
            "Problem-Solving": 4.0
        }
    },
    "102": {
        "name": "Bob",
        "department": "IT",
        "evaluations": {
            "Punctuality": 2.0,
            "Teamwork": 2.5,
            "Productivity": 3.0,
            "Communication": 2.8,
            "Problem-Solving": 2.0
        }
    }
}

def evaluate_all():
    for emp_id, info in employee_db.items():
        emp = Employee(emp_id, info["name"], info["department"], info["evaluations"])
        emp.display_summary()

def evaluate_one():
    emp_id = input("Enter Employee ID: ")
    if emp_id in employee_db:
        info = employee_db[emp_id]
        emp = Employee(emp_id, info["name"], info["department"], info["evaluations"])
        emp.display_summary()
    else:
        print("Employee not found.")

def add_and_evaluate():
    emp_id = input("Enter new Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Employee Department: ")
    evaluations = {}
    eval = ["Punctuality", "Teamwork", "Productivity", "Communication", "Problem-Solving"]

    for e in eval:
        score = float(input(f"Enter score for {e} - (0-5): "))
        evaluations[e] = score
    
    emp = Employee(emp_id, name, department, evaluations)
    emp.display_summary()
    employee_db[emp_id] = {
        "name": name,
        "department": department,
        "evaluations": evaluations
    }


def main():
    while True:
        print("\n========Employee Evaluation Expert System========")
        print("1. Evaluate ALL employees.")
        print("2. Evaluate ONE employee by ID.")
        print("3. Add and Evaluate NEW employee.")
        print("4. Exit")

        choice = int(input("Choose an option(1-4): "))

        if choice == 1:
            evaluate_all()
        elif choice == 2:
            evaluate_one()
        elif choice == 3:
            add_and_evaluate()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid option!. Try again")

if __name__ == "__main__":
    main()
            
