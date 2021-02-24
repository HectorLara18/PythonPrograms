E_LN = input("Ingrese el apellido: ")
E_Puesto = f_puesto()
E_JOB = f_puesto_string(E_Puesto)
JOB_ID = f_jobid(E_Puesto)
NewEmployeer = {
    "UserID": E_EmpNum,
    "FName": E_FN,
    "LName": E_LN,
    "Job": E_JOB,
    "JobID":JOB_ID
}

CollUsers = DBIClient["Employers"]
MyDict_Input = CollUsers.insert_one(NewEmployeer)

print(NewEmployeer)