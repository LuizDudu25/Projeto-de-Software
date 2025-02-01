import datetime
import os

# Banco de dados simulado
hospital_data = {
    "patients": {},  # ID -> {dados do paciente}
    "appointments": [],
    "medical_records": {},  # ID -> {histórico do paciente}
    "billing": {},  # ID -> {faturas}
    "prescriptions": {},  # ID -> {receitas médicas}
    "lab_tests": {},  # ID -> {exames laboratoriais}
    "wards": {},  # Número do quarto -> {paciente alocado}
    "inventory": {},  # Item -> Quantidade
    "staff_schedule": {},  # Nome -> {horário de trabalho}
    "emergency_cases": []
}

#Registra um novo paciente.
def register_patient():
    os.system('clear')
    print("AREA DE REGISTRO DE PACIENTES\n")
    
    patient_id = max(hospital_data["patients"].keys(), default = 10000) + 1
    error = 0

    name = input("Nome do paciente: ")
    cpf = input("CPF: ")
    for patient in hospital_data["patients"]:
        if hospital_data["patients"][patient]["cpf"] == cpf:
            print(f"\nPaciente ja registrado com ID {patient}.")
            error = 1
            break;
    
    if error == 0:
        age = input("Idade: ")
        gender = input("Gênero: ")
        contact = input("Contato: ")

        hospital_data["patients"][patient_id] = {"name": name, "cpf": cpf, "age": age, "gender": gender, "contact": contact}

        print(f"\nPaciente registrado com ID {patient_id}.")
    
    input("\nPressione ENTER para prosseguir")

#Agendar consulta.
def schedule_appointment():
    os.system('clear')
    print("AREA DE AGENDAMENTO DE CONSULTA\n")
    
    patient_id = int(input("ID do paciente: "))

    if patient_id in hospital_data["patients"]:
        doctor = input("Nome do médico: ")
        date = input("Data da consulta (YYYY-MM-DD): ")
        hospital_data["appointments"].append({"patient_id": patient_id, "doctor": doctor, "date": date})
        print("Consulta agendada com sucesso.")
    else:
        print("\nID do paciente nao encontrado\n")
        print("Deseja criar um ID?")
        print("(1) Sim")
        print("(2) Nao\n")

        choice = input()

        if choice == "1":
            register_patient()
            return
    
    input("\nPressione ENTER para prosseguir")

#Gerencia os registros médicos.
def manage_medical_records():
    os.system('clear')
    print("AREA DE GERENCIAMENTO DOS REGISTROS MEDICOS\n")
    
    patient_id = int(input("ID do paciente: "))
    if patient_id in hospital_data["patients"]:
        if patient_id not in hospital_data["medical_records"]:
            hospital_data["medical_records"][patient_id] = []
        else:
            print("- ", end = "")
            print("\n- ".join(map(str, hospital_data["medical_records"][patient_id])))
        record = input("Registro médico: ")
        hospital_data["medical_records"][patient_id].append(record)

        print("Registro atualizado.")
    else:
        print("\nID do paciente nao encontrado\n")
        print("Deseja criar um ID?")
        print("(1) Sim")
        print("(2) Nao\n")

        choice = input()

        if choice == "1":
            register_patient()
            return
        
    input("\nPressione ENTER para prosseguir")

#Processa faturamento.
def process_billing():
    os.system('clear')
    print("AREA DE CONTROLE DE FATURAMENTO\n")
    
    patient_id = int(input("ID do paciente: "))
    if patient_id in hospital_data["patients"]:
        current = hospital_data["billing"].get(patient_id, 0)
        print(f"Valor atual: R$ {current}\n")
        amount = float(input("Valor da fatura: "))
        hospital_data["billing"][patient_id] = hospital_data["billing"].get(patient_id, 0) + amount

        print("Fatura registrada.")
    else:
        print("\nID do paciente nao encontrado\n")
        print("Deseja criar um ID?")
        print("(1) Sim")
        print("(2) Nao\n")

        choice = input()

        if choice == "1":
            register_patient()
            return

    input("\nPressione ENTER para prosseguir")

#Gerencia prescrições médicas.
def manage_prescriptions():
    os.system('clear')
    print("AREA DE GERENCIAMENTO DE PRESCRICOES MEDICAS\n")
    
    patient_id = int(input("ID do paciente: "))
    if patient_id in hospital_data["patients"]:
        if patient_id not in hospital_data["prescriptions"]:
            hospital_data["prescriptions"][patient_id] = []
        else:
            print("- ", end = "")
            print("\n- ".join(map(str, hospital_data["prescriptions"][patient_id])))
        prescription = input("Prescrição médica: ")
        hospital_data["prescriptions"][patient_id].append(prescription)
        print("Prescrição adicionada.")
    else:
        print("\nID do paciente nao encontrado\n")
        print("Deseja criar um ID?")
        print("(1) Sim")
        print("(2) Nao\n")

        choice = input()

        if choice == "1":
            register_patient()
            return

    input("\nPressione ENTER para prosseguir")

#Solicita exames laboratoriais.
def order_lab_test():
    os.system('clear')
    print("AREA DE GERENCIAMENTO DE PRESCRICOES MEDICAS\n")

    patient_id = int(input("ID do paciente: "))
    if patient_id in hospital_data["patients"]:
        test = input("Nome do exame: ")
        hospital_data["lab_tests"].setdefault(patient_id, []).append(test)
        print("Exame solicitado.")
    else:
        print("\nID do paciente nao encontrado\n")
        print("Deseja criar um ID?")
        print("(1) Sim")
        print("(2) Nao\n")

        choice = input()

        if choice == "1":
            register_patient()
            return

    input("\nPressione ENTER para prosseguir")

#Gerencia leitos hospitalares.
def manage_wards():
    os.system('clear')
    print("AREA DE GERENCIAMENTO DE LEITOS HOSPITALARES\n")

    ward = input("Número do quarto: ")
    if ward in hospital_data["wards"]:
        print(f"O quarto {ward} está OCUPADO por ID do paciente {hospital_data['wards'][ward]}.")
    else:
        print(f"O quarto {ward} está DISPONÍVEL.")
    
    patient_id = int(input("ID do paciente: "))
    if patient_id in hospital_data["patients"]:
        hospital_data["wards"][ward] = patient_id
        print(f"Paciente {patient_id} alocado no quarto {ward}.")
    else:
        print("\nID do paciente nao encontrado\n")
        print("Deseja criar um ID?")
        print("(1) Sim")
        print("(2) Nao\n")

        choice = input()

        if choice == "1":
            register_patient()
            return

    input("\nPressione ENTER para prosseguir")

#Gerencia o estoque de suprimentos médicos.
def manage_inventory():
    os.system('clear')
    print("AREA DE GERENCIAMENTO DE INVENTARIO\n")

    if not hospital_data["inventory"]:
        print("O inventário está vazio.")
    else:
        print("\n=== Inventário do Hospital ===")
        for item, quantity in hospital_data["inventory"].items():
            print(f"{item}: {quantity}")
        print("==============================")

    item = input("Nome do item: ")
    quantity = int(input("Quantidade: "))
    hospital_data["inventory"][item] = hospital_data["inventory"].get(item, 0) + quantity
    print("Estoque atualizado.")

    input("\nPressione ENTER para prosseguir")

#Agenda turnos para os funcionários.
def schedule_staff():
    os.system('clear')
    print("AREA DE GERENCIAMENTO DE TURNOS DE FUNCIONARIOS\n")

    staff_name = input("Nome do funcionário: ")
    shift = input("Horário de trabalho: ")
    hospital_data["staff_schedule"][staff_name] = shift
    print("Horário de trabalho registrado.")

    input("\nPressione ENTER para prosseguir")

#Adiciona um caso de emergência.
def emergency_case():
    os.system('clear')
    print("CASOS DE EMERGENCIA\n")
    
    patient_name = input("Nome do paciente: ")
    condition = input("Condição do paciente: ")
    priority = input("Prioridade (Alta/Média/Baixa): ")
    hospital_data["emergency_cases"].append({"name": patient_name, "condition": condition, "priority": priority})
    print("Emergência registrada.")

    input("\nPressione ENTER para prosseguir")

#Menu
def main():
    while True:
        os.system('clear')
        
        print("\nSistema Hospitalar")
        print("1. Registrar paciente")
        print("2. Agendar consulta")
        print("3. Gerenciar registros médicos")
        print("4. Processar faturamento")
        print("5. Gerenciar prescrições")
        print("6. Solicitar exames laboratoriais")
        print("7. Gerenciar leitos hospitalares")
        print("8. Gerenciar inventário")
        print("9. Agendar turnos de funcionários")
        print("10. Adicionar emergência")
        print("0. Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            register_patient()
        elif choice == "2":
            schedule_appointment()
        elif choice == "3":
            manage_medical_records()
        elif choice == "4":
            process_billing()
        elif choice == "5":
            manage_prescriptions()
        elif choice == "6":
            order_lab_test()
        elif choice == "7":
            manage_wards()
        elif choice == "8":
            manage_inventory()
        elif choice == "9":
            schedule_staff()
        elif choice == "10":
            emergency_case()
        elif choice == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()