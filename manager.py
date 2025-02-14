import connection as conn
from datetime import datetime

class function_show():
    def __init__(self):
        self.connection = conn.get_connection()
        self.cursor = self.connection.cursor()

    @staticmethod
    def get_departments():
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            sql = "SELECT * FROM DEPARTAMENT"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Erro ao buscar departamentos: {e}")
            return None

    def get_employee():
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            sql = "SELECT ID, NAME_EMPL, EMAIL, ROLE_EMP, SALARY, ADMISSION_DATE FROM EMPLOYEE"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error ao buscar funcionarios: {e}")
            return None
    def get_view():
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            sql = "SELECT * FROM VW_FUNCIONARIOS_DEPARTAMENTOS"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

        except Exception as e:
            print(f"Error ao buscar cadastro: {e}")
class FunctionInsert:
    def __init__(self):
        self.connection = conn.get_connection()
        self.cursor = self.connection.cursor()

    def insert_employee(self, name, email, role, salary, admission, name_dept):
        try:
            sql = """INSERT INTO EMPLOYEE (NAME_EMPL, EMAIL, ROLE_EMP, SALARY, ADMISSION_DATE, DEPARTAMENT_ID)
                     VALUES (%s, %s, %s, %s, %s,%s)"""
            self.cursor.execute(sql, (name, email, role, salary, admission, name_dept))
            self.connection.commit()
            return function_show.get_employee()
        except Exception as e:
            print(f"Erro ao inserir funcionário: {e}")
        finally:
            self.cursor.close()
            self.connection.close()

    def insert_dept(self, dept):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()

            sql = "INSERT INTO DEPARTAMENT (NAME_DEPT) VALUES (%s)"
            cursor.execute(sql, (dept,))

            connection.commit()
        except Exception as e:
            print(f"Erro ao inserir departamento: {e}")
        finally:
            self.cursor.close()
            self.connection.close()


class ChoseInsert:
    @staticmethod
    def cinsert_employee():
        name = input("Nome do funcionário: ")
        email = input("Email do funcionário: ")
        role = input("Função do funcionário: ")
        salary = float(input("Salário do funcionário (Exemplo 2000.00): "))
        admission = input("Data de Admissão do funcionário (AAAA-MM-DD): ")
        admission = datetime.strptime(admission, "%Y-%m-%d").date()

        print(function_show.get_departments())
        name_dept = int(input("Selecionar o número do departamento: "))

        inserter = FunctionInsert()
        employees = inserter.insert_employee(name, email, role, salary, admission, name_dept)
        return employees

    @staticmethod
    def cinsert_dept():
        dept = input("Insira o nome do novo departamento: ")
        inserter = FunctionInsert()
        deptr = inserter.insert_dept(dept)
        return deptr

class DeleteRegister():

    def delete_employee():
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            view = function_show.get_view()
            for view in view:
                print(view)
            id = int(input("Qual o id do funcionario?"))
            delete = "DELETE FROM EMPLOYEE WHERE ID = %s"
            cursor.execute(delete, (id, ))
            connection.commit()
        except Exception as e:
            print(f"erro ao deletar {e}")
        finally:
            cursor.close()
            connection.close()

    def delete_derpatmente():
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            function_show.get_departments()
            id = int(input("Selecione o id de um departamento:"))
            delete = "DELETE FROM DEPARTAMENT WHERE ID = %s"
            cursor.execute(delete, (id, ))
            connection.commit()
        except Exception as e:
            print(f"erro ao deletar {e}")
        finally:
            cursor.close()
            connection.close()

print("escolha a função")
print("-----------------------------------")
print("1 - Mostrar")
print("-----------------------------------")
print("2 - Inserir")
print("-----------------------------------")
print("3 - Deletar")
print("-----------------------------------")
print("qualquer tecla - Procurar por email")
print("-----------------------------------")


sel1 = input("Escolha uma opção:")

if sel1 == "1":
    print('----Mostrar-----')
    print("--Qual tabela?--")
    print("1 - Funcionarios")
    print("----------------")
    print("2 - Departamento")
    print("----------------")
    print("3 - Funci/depart")
    print("----------------")
    sel2 = input("Numero: ")
    if sel2 == "1":
        employee = function_show.get_employee()
        if employee:
            for employee in employee:
                print(employee)
    elif sel2 == "2":
        departamentos = function_show.get_departments()
        if departamentos:
            for departamento in departamentos:
                print(departamento)
    elif sel2 == "3":
        view = function_show.get_view()
        for view in view:
            print(view)
    else:
        print("Opção invalida")
elif sel1 == "2":
    print('----Inserir-----')
    print("--Qual tabela?--")
    print("1 - Funcionarios")
    print("----------------")
    print("2 - Departamento")
    print("----------------")
    print("3 - Funci/depart")
    print("----------------")
    sel2 = input("Numero: ")
    if sel2 == "1":
        ChoseInsert.cinsert_employee()
    elif sel2 == "2":
        ChoseInsert.cinsert_dept()
    else:
        print("Opção invalida")
elif sel1 == "3":
    print('----Deletar-----')
    print("--Qual tabela?--")
    print("1 - Funcionarios")
    print("----------------")
    print("2 - Departamento")
    print("----------------")
    sel2 = input("Numero: ")
    if sel2 == "1":
        DeleteRegister.delete_employee()
    elif sel2 == "2":
        DeleteRegister.delete_derpatmente()
else:
    email = input("Digite o Email/Nome: ")

    try:
        connection = conn.get_connection()  # Conectar ao banco
        cursor = connection.cursor()

        sql = "SELECT * FROM VW_FUNCIONARIOS_DEPARTAMENTOS WHERE EMAIL LIKE %s OR NOME LIKE %s"
        cursor.execute(sql, ('%' + email + '%', '%' + email + '%'))  # Correção na passagem do parâmetro

        result = cursor.fetchall()  # Pega os resultados

        if result:
            for row in result:
                print(row)  # Exibe os funcionários encontrados
        else:
            print("Nenhum funcionário encontrado.")

    except Exception as e:
        print(f"Erro ao buscar cadastro: {e}")
    finally:
        cursor.close()  # Fechar cursor
        connection.close()  # Fechar conexão
