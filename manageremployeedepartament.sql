CREATE DATABASE IF NOT EXISTS COMPANYDB;

USE COMPANYDB;

CREATE TABLE IF NOT EXISTS DEPARTAMENT(
ID INT AUTO_INCREMENT PRIMARY KEY,
NAME_DEPT VARCHAR(200) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS EMPLOYEE (
ID INT AUTO_INCREMENT PRIMARY KEY,
NAME_EMPL VARCHAR(255) NOT NULL,
EMAIL VARCHAR(100) NOT NULL,
ROLE_EMP VARCHAR(100) NOT NULL,
SALARY DECIMAL(10,2) NOT NULL,
ADMISSION_DATE DATE NOT NULL,
DEPARTAMENT_ID INT,
FOREIGN KEY (DEPARTAMENT_ID) REFERENCES DEPARTAMENT(ID)
);

INSERT INTO DEPARTAMENT(NAME_DEPT) VALUES 
('TI'),
('RH'),
('Vendas'),
('Marketing'),
('Financeiro'),
('Desenvolvimento de Produto'),
('Atendimento ao Cliente'),
('Recursos Humanos'),
('TI e Infraestrutura'),
('Vendas Diretas'),
('Qualidade'),
('Logística'),
('Pesquisa e Desenvolvimento');

INSERT INTO EMPLOYEE(NAME_EMPL, EMAIL, ROLE_EMP, SALARY, ADMISSION_DATE, DEPARTAMENT_ID) VALUES
('Ana Costa', 'ana.costa@example.com', 'Desenvolvedora', 5000.00, '2022-01-15', 1),
('Carlos Mendes', 'carlos.mendes@example.com', 'Gerente', 7000.00, '2021-03-10', 2),
('Fernanda Lima', 'fernanda.lima@example.com', 'Vendedora', 4000.00, '2022-06-20', 3),
('Luiz Ferreira', 'luiz.ferreira@example.com', 'Analista Financeiro', 5500.00, '2021-08-05', 2),
('Mariana Sousa', 'mariana.sousa@example.com', 'Coordenadora de Marketing', 6000.00, '2020-10-12', 1),
('Pedro Alves', 'pedro.alves@example.com', 'Assistente de TI', 3500.00, '2022-02-28', 6),
('Carla Pinto', 'carla.pinto@example.com', 'Especialista em Logística', 4800.00, '2021-07-15', 9),
('Ricardo Ramos', 'ricardo.ramos@example.com', 'Gerente de Vendas', 7500.00, '2019-04-01', 7),
('Julia Oliveira', 'julia.oliveira@example.com', 'Analista de Qualidade', 4700.00, '2022-05-30', 8),
('Renato Silva', 'renato.silva@example.com', 'Pesquisador', 6200.00, '2023-01-10', 10);

CREATE INDEX IDX_EMAIL ON EMPLOYEE(EMAIL);

CREATE VIEW VW_FUNCIONARIOS_DEPARTAMENTOS AS
SELECT
    E.ID AS CODIGO,
	E.NAME_EMPL AS NOME,
	E.EMAIL,
    E.ROLE_EMP AS CARGO,
    E.SALARY AS SALARIO,
    E.ADMISSION_DATE AS 'DATA DE ADMISSÃO',
    D.NAME_DEPT AS DEPARTAMENTO
FROM EMPLOYEE E
JOIN DEPARTAMENT D ON E.DEPARTAMENT_ID = D.ID;

SELECT * FROM VW_FUNCIONARIOS_DEPARTAMENTOS;

DELIMITER //
CREATE PROCEDURE SP_UPDATE_SALARY(IN EMPLOYEE_ID INT, IN NEW_SALARY DECIMAL(10, 2))
BEGIN
    UPDATE EMPLOYEE SET SALARY = NEW_SALARY WHERE ID = EMPLOYEE_ID;
END //
DELIMITER ;

CALL SP_UPDATE_SALARY(1, 5500.00);

SELECT * FROM VW_FUNCIONARIOS_DEPARTAMENTOS;

SELECT * FROM VW_FUNCIONARIOS_DEPARTAMENTOS WHERE EMAIL LIKE '%na%';

