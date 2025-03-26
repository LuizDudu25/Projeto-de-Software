from models import Employee
from menus import Menu

class Doctor(Employee):
    def __init__(self, nome, cpf, idade, genero, contato, especializacao, salario, turno):
        super().__init__(nome, cpf, idade, genero, contato, "Médico", salario, turno)
        self.especializacao = especializacao
        self.appointments = []
    
    def update_info(self):
        super().update_info()
        self.especializacao = input(f"Especialização [{self.especialização}]: ") or self.especializacao
    
    def print_info(self):
        super().print_info()
        print(f"Especialiação: {self.especializacao}")
    
    def is_available(self, date, time):
        for appointment in self.scheduled_appointments:
            if appointment.date == date and appointment.time == time:
                return False
        return True
    
    def book_appointment(self, patient):
        from appointments import Appointment
        date = input("\nDigite a data da consulta: ")
        time = input("Digite o horário da consulta: ")
        if not self.is_available(date, time):
            print("\nErro: O médico já tem uma consulta nesse horário!")
            return
        
        healthcare_plan = Menu.menu_plan()
        appointment = Appointment(patient, self, date, time, healthcare_plan)
        self.appointments.append(appointment)
        patient.add_appointment(appointment)

        print("\nConsulta agendada com sucesso.")
    
    def cancel_appointment(self, hospital):
        cpf_patient = input("\nDigite o CPF do paciente: ")
        patient = hospital.find_person(cpf_patient, hospital.patients)
        if not patient:
            print("\nPaciente não encontrado.")
            input("Pressione ENTER para voltar ao menu.")
            return
        
        date = input("\nDigite a data da consulta: ")
        time = input("Digite o horário da consulta: ")
        
        for appointment in self.appointments:
            if appointment.patient == patient and appointment.date == date and appointment.time == time:
                self.appointments.remove(appointment)
                patient.appointments.remove(appointment)
                print("\nConsulta cancelada com sucesso.")
                return patient
        print("\nConsulta não encontrada.")

