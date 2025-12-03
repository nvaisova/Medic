import json
import os

DB_FILE = "medical_records.json"

# Load database
def load_db():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

# Save database
def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)

# Add new patient
def add_patient():
    db = load_db()

    patient_id = input("Enter patient ID: ")
    name = input("Enter full name: ")
    age = input("Enter age: ")
    symptoms = input("Enter symptoms: ")
    allergies = input("Enter allergies: ")
    notes = input("Doctor's notes: ")

    db[patient_id] = {
        "name": name,
        "age": age,
        "symptoms": symptoms,
        "allergies": allergies,
        "notes": notes
    }

    save_db(db)
    print("Patient added successfully!")

# View patient
def view_patient():
    db = load_db()

    patient_id = input("Enter patient ID: ")
    if patient_id in db:
        print("\n--- Patient Info ---")
        for key, value in db[patient_id].items():
            print(f"{key}: {value}")
    else:
        print("Patient not found.")

# Update patient record
def update_patient():
    db = load_db()

    patient_id = input("Enter patient ID: ")
    if patient_id not in db:
        print("Patient not found.")
        return

    print("Leave field empty to keep previous value.\n")

    name = input(f"Full name ({db[patient_id]['name']}): ") or db[patient_id]['name']
    age = input(f"Age ({db[patient_id]['age']}): ") or db[patient_id]['age']
    symptoms = input(f"Symptoms ({db[patient_id]['symptoms']}): ") or db[patient_id]['symptoms']
    allergies = input(f"Allergies ({db[patient_id]['allergies']}): ") or db[patient_id]['allergies']
    notes = input(f"Notes ({db[patient_id]['notes']}): ") or db[patient_id]['notes']

    db[patient_id] = {
        "name": name,
        "age": age,
        "symptoms": symptoms,
        "allergies": allergies,
        "notes": notes
    }

    save_db(db)
    print("Patient updated successfully!")

# Delete patient
def delete_patient():
    db = load_db()

    patient_id = input("Enter patient ID to delete: ")
    if patient_id in db:
        del db[patient_id]
        save_db(db)
        print("Record deleted.")
    else:
        print("Patient not found.")

# Menu
def main():
    while True:
        print("\n--- Medical Record Manager ---")
        print("1. Add Patient")
        print("2. View Patient")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patient()
        elif choice == "3":
            update_patient()
        elif choice == "4":
            delete_patient()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
