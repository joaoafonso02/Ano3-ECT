# BD: Guião 9


## ​9.1
 
### *a)*

```` SQL
CREATE PROC delEmployee @issn AS char(9)
AS
    BEGIN

        DELETE FROM Works_on WHERE Essn = @issn;

        DELETE FROM Dependent WHERE Essn = @issn;

        UPDATE DEPARTMENT SET Mgr_ssn = NULL WHERE Mgr_ssn = @issn;

        UPDATE EMPLOYEE SET Super_ssn = NULL WHERE Super_ssn = @issn;

        DELETE FROM EMPLOYEE WHERE Ssn = @issn;

END
GO
````

### *b)* 

```` SQL
GO
CREATE PROC RecGest (@anosout CHAR(9) OUTPUT, @ssnout INT OUTPUT)
AS
	BEGIN
		SELECT * FROM (dbo.EMPLOYEE JOIN dbo.DEPARTMENT ON Ssn = Mgr_ssn);
            (SELECT TOP 1 @anosout = MAX(DATEDIFF(year,dbo.DEPARTMENT.Mgr_start_date,getDate())), @ssnout = dbo.DEPARTMENT.Mgr_ssn
                FROM dbo.EMPLOYEE JOIN dbo.DEPARTMENT ON Ssn = Mgr_ssn
                    GROUP BY dbo.DEPARTMENT.Mgr_start_date, dbo.DEPARTMENT.Mgr_Ssn)
END

````

### *c)* 

```` SQL
CREATE TRIGGER singleManager ON DEPARTMENT AFTER INSERT, UPDATE 
AS
BEGIN
    IF EXISTS(SELECT Mgr_ssn, COUNT(*) AS num FROM DEPARTMENT GROUP BY(Mgr_ssn) HAVING COUNT(*) > 1) 
        BEGIN
            RAISERROR('Employee só pode ser manager de um departamento!', 16, 1); 
            ROLLBACK TRAN;
        END

END
GO
````

### *d)* 

```` SQL
GO
CREATE TRIGGER dbo.checkMoney on dbo.EMPLOYEE
AFTER INSERT, UPDATE
AS
	BEGIN
		SET NOCOUNT ON;

		DECLARE @Msalario DECIMAL(6,2)
		DECLARE @Dno INT
		DECLARE @ssn CHAR(9)
		DECLARE @salario DECIMAL(6,2)
		SELECT @Dno=Dno, @salario=Salary, @ssn=Ssn FROM inserted;

		SELECT @Msalario=Salary
		FROM dbo.DEPARTMENT JOIN dbo.EMPLOYEE ON Mgr_ssn=Ssn
		WHERE Dnumber=@Dno

		IF (@salario > @MSalario)
		BEGIN
			UPDATE dbo.EMPLOYEE
			SET Salary=@MSalario - 1
			WHERE Ssn=@ssn
		END
	END
GO
````

### *e)* 

```` SQL
CREATE FUNCTION empProjects (@ssn char(9)) RETURNS TABLE
AS
    RETURN (SELECT em.Fname + ' ' + em.Minit + '. ' + em.Lname as Name, pr.Plocation 
        FROM Works_on wo 
            INNER JOIN EMPLOYEE em ON wo.Essn = em.Ssn 
                INNER JOIN PROJECT pr ON WO.Pno = pr.Pnumber 
                    WHERE wo.Essn = @ssn);

GO
--DROP TRIGGER dbo.checkMoney;
````

### *f)* 

```` SQL
CREATE FUNCTION dbo.Dnov (@dno INT)
RETURNS @table TABLE
(
  Fname VARCHAR,
  Lname VARCHAR,
  Ssn INT
)
AS
    BEGIN
        DECLARE @avgSalary DECIMAL(10,2)
        SET @avgSalary = SELECT(AVG(dbo.EMPLOYEE.Salary) FROM dbo.EMPLOYEE WHERE Dno=@dno)
        INSERT @table
        SELECT Fname, Lname, Ssn FROM dbo.EMPLOYEE WHERE Dno=@dno AND Salary > @avgSalary
        RETURN
    END;
GO

````

### *g)* 

```` SQL
CREATE FUNCTION employeeDeptHighAverage (@Dno INT) RETURNS @Pbudget TABLE (pname varchar(15), pnumber int primary key, plocation varchar(15), dnum int, budget numeric(10,2), totalbudget numeric(10,2)) AS
BEGIN

    DECLARE C CURSOR FOR SELECT Pname, Pnumber, Plocation, Dnum FROM PROJECT WHERE Dnum = @Dno;
    OPEN C;

    DECLARE @name AS varchar(15), @pnum AS INT, @location AS varchar(15), @dnum AS INT;
    FETCH C INTO @name, @pnum, @location, @dnum;
    
    DECLARE @prevBudget AS numeric(10,2);
    SET @prevBudget = 0;

    WHILE @@FETCH_STATUS = 0
        BEGIN

            DECLARE @cost AS numeric(10,2);
            SELECT @cost = SUM(wo.Hours * em.Salary / 40) FROM Works_on wo INNER JOIN EMPLOYEE em ON em.Ssn = wo.Essn WHERE wo.Pno = @pnum;
            
            SET @prevBudget += @cost;
        
            INSERT INTO @Pbudget VALUES (@name, @pnum, @location, @dnum, @cost, @prevBudget);
            
            FETCH C INTO @name, @pnum, @location, @dnum;

        END

    CLOSE C;
    DEALLOCATE C;

    RETURN;
END
````

### *h)* 
```` SQL
CREATE TRIGGER dbo.delDepInst ON dbo.DEPARTMENT
INSTEAD OF DELETE
AS
		BEGIN
			DECLARE @Dname VARCHAR(30);
			DECLARE @Dnumber int;
			DECLARE @Mgr_ssn int;
			DECLARE @Mgr_start_date date;

			SELECT @Dname = Dname FROM deleted;
			SELECT @Dnumber = Dnumber FROM deleted;
			SELECT @Mgr_ssn = Mgr_ssn FROM deleted;
			SELECT @Mgr_start_date = Mgr_start_date FROM deleted;

			IF (NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES
				WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = 'DEPARTMENT_DELETED'))
				    CREATE TABLE dbo.DEPARTMENT_DELETED (Dname VARCHAR(30), Dnumber int, Mgr_ssn int NULL, Mgr_start_date date NULL);
			INSERT INTO dbo.DEPARTMENT_DELETED VALUES (@Dname, @Dnumber, @Mgr_ssn, @Mgr_start_date);
			DELETE FROM dbo.DEPARTMENT WHERE Dnumber = @Dnumber; 
		END		

GO
````

### *i)* 

```` SQL
CREATE TRIGGER dbo.delDepInst ON dbo.DEPARTMENT
INSTEAD OF DELETE
AS
		BEGIN
			DECLARE @Dname VARCHAR(30);
			DECLARE @Dnumber int;
			DECLARE @Mgr_ssn int;
			DECLARE @Mgr_start_date date;

			SELECT @Dname = Dname FROM deleted;
			SELECT @Dnumber = Dnumber FROM deleted;
			SELECT @Mgr_ssn = Mgr_ssn FROM deleted;
			SELECT @Mgr_start_date = Mgr_start_date FROM deleted;

			IF (NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES
				WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = 'DEPARTMENT_DELETED'))
				    CREATE TABLE dbo.DEPARTMENT_DELETED (Dname VARCHAR(30), Dnumber int, Mgr_ssn int NULL, Mgr_start_date date NULL);
			INSERT INTO dbo.DEPARTMENT_DELETED VALUES (@Dname, @Dnumber, @Mgr_ssn, @Mgr_start_date);
			DELETE FROM dbo.DEPARTMENT WHERE Dnumber = @Dnumber; 
		END		

GO
````
