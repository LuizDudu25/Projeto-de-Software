from models import Employee
from menus import Menu

class Nurse(Employee):
    def __init__(self, nome, cpf, idade, genero, contato, salario, turno, especialidade):
        super().__init__(nome, cpf, idade, genero, contato, "Enfermeiro", salario, turno)
        self.especialidade = especialidade
        self.plantões = []

    def update_info(self):
        super().update_info()
        self.especialidade = input(f"Especialidade [{self.especialidade}]: ") or self.especialidade

    def print_info(self):
        super().print_info()
        print(f"Especialidade: {self.especialidade}")

def staff_area(hospital):
    choice1 = Menu.menu_staff()
    choice2 = Menu.menu_group()

    if choice1 != '0':
        if choice2 == 'Médico':
            group = hospital.doctors
        elif choice2 == 'Enfermeiro':
            group = hospital.nurses
        else:
            choice2 = input("\nDigite o cargo do funcionário: ")
            group = hospital.employees
    
    if choice1 == '1':
        if group:
            for employee in group:
                employee.print_info()
        else:
            print("\nNenhum funcionário registrado.")
    elif choice1 == '2':        
        hospital.register_employee(choice2, group)
    elif choice1 == '3':
        cpf = input("\nDigite o CPF do funcionário: ")
        employee = hospital.find_person(cpf, group)
        if employee:
            employee.print_info()
            choice = input("\nDeseja alterar as informações do funcionário? (S/N) ")
            if choice == 'S':
                employee.update_info()
    elif choice1 == '4':
        cpf = input("\nDigite o CPF do funcionário: ")
        employee = hospital.find_person(cpf, group)
        if employee:
            group.remove(employee)
            print("\nFuncionário removido.")
    elif choice1 == '0':
        return
    else:
        print("\nOpção inválida.")
    
    input("\nPressione ENTER para continuar ")