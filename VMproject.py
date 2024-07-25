# -*- coding: utf-8 -*-
"""

@authors:
        - Aya Al Balushi (135131)
        - Khadija Al Bulushi (133556)
        - Quds Al Breiki (133343)
        - Maysoon Ambu Saidi (135352)
"""

'''
This program is to demonstrate the work of virtual memory
Key points:
    - The Pediatric_surgery represents the main memory.
    - The Pediatric represents the virtual memory.
    - The patient and his/her companions represent one process.
    - the beds in the pediatric_surgery represent the frames
    - The flow of the program start on a random moment in the past.
    - The Cumulative Transfer Latency represents the whole time taken by the patients to do the transfers.
'''
import time
import random 
class Patient:
    '''
       Constructor for the Patient class.
    
       Parameters:
       - id (int): The unique identifier for the patient.
       - name (str): The name of the patient.
       - status (str): The health status of the patient ('Critical', 'Serious', 'Stable', etc.).
       - companions (int): The number of companions accompanying the patient.
    '''
    def __init__(self, id, name, status, companions):
        self.id = id
        self.name = name
        self.status = status
        self.companions = companions
        
    ''' Returns a string representation of the Patient object.'''
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Status: {self.status}, Companions: {self.companions}"
    
    '''
        Calculates the number of beds needed based on the number of companions.
        Returns: int: The number of beds needed.
    '''
    def beds_needed(self):
        if self.companions == 1:
            return 2
        elif self.companions == 2:
            return 3
      


class Pediatric_surgery:
    
    '''
        Constructor for the pediatric_surgery class.
        Parameters:
        - max_beds (int): The maximum number of beds available in the pediatric_surgery.
    '''
    def __init__(self, max_beds):
        self.max_beds = max_beds
        self.patients = []
        self.transfer_latency = 0  

    
    '''Displays information about the occupied beds and patients in the Pediatric_surgery.'''
    def display(self):
       
        occupied_beds = sum(patient.beds_needed() for patient in self.patients)
        print(f"Occupied Beds in the Pediatric_surgery: {occupied_beds}/{self.max_beds}\n")
        # Print header
        print("{:<5} {:<20} {:<10} {:<12}".format("ID", "Name", "Status", "Companions"))
        print("-" * 48)

           # Print patient information in a table format
        for patient in self.patients:
           print("{:<5} {:<20} {:<10} {:<12}".format(patient.id, patient.name, patient.status, patient.companions))
    
    '''
       Transfers stable patients from the Pediatric_surgery to a pediatric.
       Parameters:
       - pediatric (pediatric): The pediatric to which stable patients are transferred.
    '''
    def transfer_patients_to_pediatric(self, pediatric):
        start_time = time.time()
        time.sleep(random.uniform(0.1, 0.3))  # To simulate transfer time
        transfer_operation_latency = time.time() - start_time
        self.transfer_latency += transfer_operation_latency
        stable_patients = [patient for patient in self.patients if patient.status == 'Stable']
        for patient in stable_patients:
            self.patients.remove(patient)
            pediatric.add_patient(patient)
    
    '''
        Transfers patients from a pediatric to a valid table based on their status.
        Parameters:
        - pediatric (pediatric): The pediatric from which patients are transferred.
        - valid_table (list): The list representing a valid table to which patients are transferred.
    '''
    def transfer_to_valid_table(self, pediatric, valid_table):
        start_time = time.time()
        time.sleep(random.uniform(0.1, 0.3))  # To simulate transfer time
        transfer_operation_latency = time.time() - start_time
        self.transfer_latency += transfer_operation_latency
        valid_patients = [patient for patient in pediatric.patients if patient.status in ['Critical', 'Serious']]
        valid_table.extend(valid_patients)
        pediatric.patients = [patient for patient in pediatric.patients if patient not in valid_patients]
    
    '''
        Transfers priority patients from a valid table to the Pediatric_surgery.
        Parameters:
        - valid_table (list): The list representing a valid table containing priority patients.
        - pediatric (pediatric): The pediatric where remaining patients from the valid table are returned.
    '''
    def transfer_priority_patients_to_pediatric_surgery(self, valid_table, pediatric):
        start_time = time.time()
        time.sleep(random.uniform(0.1, 0.3))  # To simulate transfer time
        transfer_operation_latency = time.time() - start_time
        self.transfer_latency += transfer_operation_latency
        empty_beds = self.max_beds - sum(patient.beds_needed() for patient in self.patients)
        priority_patients = [patient for patient in valid_table if patient.status == 'Critical'] + \
                            [patient for patient in valid_table if patient.status == 'Serious']
        for patient in priority_patients:
            if empty_beds >= patient.beds_needed():
                self.patients.append(patient)
                valid_table.remove(patient)
                empty_beds -= patient.beds_needed()
    
        pediatric.patients.extend(valid_table)
        valid_table.clear()
   
    '''
        Adds a patient to a pediatric.
        Parameters:
        - patient (Patient): The patient to be added to the pediatric.
        - pediatric (pediatric): The pediatric where the patient is added.
    '''
    def add_patient_to_pediatric(self, patient, pediatric):
        pediatric.add_patient(patient)

class Pediatric:
    '''
        Constructor for the Pediatric class.
        Parameters:
        - max_beds (int): The maximum number of beds available in the Pediatric.
    '''
    def __init__(self, max_beds):
        self.max_beds = max_beds
        self.patients = []

    '''
        Adds a patient to the Pediatric.
        Parameters:
        - patient (Patient): The patient to be added to the Pediatric.
    '''
    def add_patient(self, patient):
        self.patients.append(patient)

    '''
        Displays information about the occupied beds and patients in the Pediatric.
    '''
    def display(self):
        occupied_beds = sum(patient.beds_needed() for patient in self.patients)
        print(f"Occupied Beds in Pediatric: {occupied_beds}/{self.max_beds}\n")
        # Print header
        print("{:<5} {:<20} {:<10} {:<12}".format("ID", "Name", "Status", "Companions"))
        print("-" * 48)

           # Print patient information in a table format
        for patient in self.patients:
           print("{:<5} {:<20} {:<10} {:<12}".format(patient.id, patient.name, patient.status, patient.companions))
           
           
'''
    Initialize patient data for the Pediatric_surgery and Pediatric from text files.
    Parameters:
    - Pediatric_surgery (Pediatric_surgery): The Pediatric_surgery object.
    - Pediatric (Pediatric): The Pediatric object.
    - pediatric_surgery_file (str): Path to the text file containing Pediatric_surgery patient data.
    - shelter_file (str): Path to the text file containing shelter patient data.
'''          
def initialize_data(Pediatric_surgery, Pediatric, pediatric_surgery_file, pediatric_file):
    with open(pediatric_surgery_file, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            patient = Patient(int(data[0]), data[1], data[2], int(data[3]))
            Pediatric_surgery.patients.append(patient)

    with open(pediatric_file, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            patient = Patient(int(data[0]), data[1], data[2], int(data[3]))
            Pediatric.patients.append(patient)
            
            
            
'''
    Change the status of a patient in the pediatric_surgery_or_pediatric.
    Parameters:
    - pediatric_surgery_or_pediatric: The pediatric surgery or pediatric object.
    - patient_id (int): The ID of the patient.
    - new_status (str): The new status for the patient.
'''
def change_patient_status(pediatric_surgery_or_pediatric, patient_id, new_status):
    patients = pediatric_surgery_or_pediatric.patients
    for patient in patients:
        if patient.id == patient_id:
            if new_status.capitalize().lower() == 'hale':
                patients.remove(patient)
            else:
                try:
                    # Validate new status
                    valid_statuses = ['stable', 'critical', 'serious', 'hale']
                    if new_status.lower() not in valid_statuses:
                        raise ValueError("Invalid status. Please enter 'Stable', 'Critical', 'Serious', or 'Hale'.")
                        
                    perv_status = patient.status
                    patient.status = new_status.capitalize()
                    print(f"Patient with ID {patient_id} status is successfully changed from {perv_status} to {new_status.capitalize()}.\n")
                except ValueError as e:
                    print(f"Error: {e}")
            
            return
    else:
        print(f"Patient with ID {patient_id} not found.")
        
        
'''
    Add a new patient to the Pediatric.
    Parameters:
    - Pediatric (Pediatric): The Pediatric object.  
'''
def add_new_patient_to_pediatric(Pediatric):
    try:
        id = int(input("Enter patient ID: "))
        name = input("Enter patient name: ")
        status = input("Enter patient status: ").lower()

        # Validate status
        valid_statuses = ['stable', 'critical', 'serious']
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Please enter one of: {', '.join(valid_statuses)}")

        companions = int(input("Enter number of companions(1/2): "))

        # Validate companions
        if companions < 0:
            raise ValueError("Number of companions cannot be negative.")
        elif companions > 2:
            raise ValueError("Number of companions cannot be more than 2.")
            
        new_patient = Patient(id, name, status, companions)
        Pediatric.add_patient(new_patient)
        print(f"Patient {name} (id: {id}, status: {status}) is initially added to pediatric.\n")
    except ValueError as e:
        print(f"Error: {e}")


'''
    Remove a patient from the Pediatric_surgery or Pediatric.
    Parameters:
    - Pediatric_surgery (Pediatric_surgery): The Pediatric_surgery object.
    - Pediatric (Pediatric): The Pediatric object.
    - patient_id (int): The ID of the patient to be removed.
'''  
def remove_patient(Pediatric_surgery, Pediatric, patient_id):
    ps_patients = Pediatric_surgery.patients
    p_patients = Pediatric.patients
    
    flag = False
    for patient in ps_patients:
        if patient.id == patient_id:
            ps_patients.remove(patient)
            flag = True
            break  # Break out of the loop after removal

    for patient in p_patients:
        if patient.id == patient_id:
            p_patients.remove(patient)
            flag = True
            break  # Break out of the loop after removal

    if flag:
        print(f"Patient with ID {patient_id} is successfully removed from the system.\n")
        
    else:
        print(f"Patient with ID {patient_id} doesn't exist in the system.\n")   
    return flag   
    
    
def main():
    max_beds_pediatric_surgery = 40
    max_beds_pediatric = 50

    pediatric_surgery_instance = Pediatric_surgery(max_beds_pediatric_surgery)
    pediatric_instance = Pediatric(max_beds_pediatric)
    valid_table = []

    initialize_data(pediatric_surgery_instance, pediatric_instance, 'pediatric_surgery.txt', 'pediatric.txt')
    # Display initial data
    print("\n================= Initial Data ===================")
    print("\n        Initial Pediatric_surgery Data")
    pediatric_surgery_instance.display()
    print("\n        Initial Pediatric Data")
    pediatric_instance.display()
    
    
    while True:
        # Perform transferring actions
        print("\n================= Transferring Actions ===================")
        pediatric_surgery_instance.transfer_patients_to_pediatric(pediatric_instance)
        pediatric_surgery_instance.transfer_to_valid_table(pediatric_instance, valid_table)
        pediatric_surgery_instance.transfer_priority_patients_to_pediatric_surgery(valid_table, pediatric_instance)

        # Display resulting data after transferring
        print("\n================= Resulting Data ===================")
        print("\n        Current Pediatric_surgery Data")
        pediatric_surgery_instance.display()
        print("\n        Current Pediatric Data")
        pediatric_instance.display()
        
        # Display the cumulative transfer latency
        print(f"Transfer Latency: {int(pediatric_surgery_instance.transfer_latency*100)} minutes")


        try:
            print("\n================= Pediatric Surgery Management System ===================")
            print("1. Change Patient Status")
            print("2. Add New Patient(s)")
            print("3. Remove Patient(s)")
            print("0. Exit")
        
            choice = input("Enter your choice (0-3): ")
               
            if choice == '1':
                while(True):
                    location = input("Enter patient location (pediatric_surgery/pediatric): ")
                    while not(location.lower() == 'pediatric_surgery' or location.lower() == 'pediatric'):
                        print("Invalid location. Please enter either 'pediatric_surgery' or 'pediatric'.\n")
                        location = input("Enter patient location (pediatric_surgery/pediatric): ")
                    
                    patient_id = int(input("Enter patient ID: "))
                    new_status = input("Enter new status (Critical/Serious/Stable/Hale): ")
                    if location.lower() == 'pediatric_surgery':
                        change_patient_status(pediatric_surgery_instance, patient_id, new_status)
                        

                    else:
                        change_patient_status(pediatric_instance, patient_id, new_status)
                    
                    
                    answer = input("Do you want to change another patient's status? (y/n):")
                    while (not(answer.lower().strip() == 'n' or answer.lower().strip() == 'y')):
                        print("Invalid input. Please enter either 'y' or 'n'.\n")
                        answer = input("Do you want to remove another patient? (y/n):")
                    if answer.lower().strip() == 'n':
                        break
                    elif answer.lower().strip() == 'y':
                        continue
    
                        
            elif choice == '2':                    
                while True:
                    print("\n--- Adding New Patient ---")
                    add_new_patient_to_pediatric(pediatric_instance)
                    answer = input("Do you want to add another patient? (y/n):")
                    while (not(answer.lower().strip() == 'n' or answer.lower().strip() == 'y')):
                        print("Invalid input. Please enter either 'y' or 'n'.\n")
                        answer = input("Do you want to remove another patient? (y/n):")
                    if answer.lower().strip() == 'n':
                        break
                    elif answer.lower().strip() == 'y':
                        continue
    
            elif choice == '3':
                while True:
                    print("\n--- Removing A Patient ---")
                    patient_id = int(input("Enter patient ID: "))
                    flag = remove_patient(pediatric_surgery_instance, pediatric_instance, patient_id)
                    while not flag:
                        patient_id = int(input("Enter patient ID: "))
                        flag = remove_patient(pediatric_surgery_instance, pediatric_instance, patient_id)
                        
                    answer = input("Do you want to remove another patient? (y/n):")
                    while (not(answer.lower().strip() == 'n' or answer.lower().strip() == 'y')):
                        print("Invalid input. Please enter either 'y' or 'n'.\n")
                        answer = input("Do you want to remove another patient? (y/n):")
                    if answer.lower().strip() == 'n':
                        break
                    elif answer.lower().strip() == 'y':
                        continue
    
      
    
            elif choice == '0':
                print("Exiting the program. Goodbye!")
                break
    
            else:
                print("Invalid choice. Please enter a number between 0 and 3.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
