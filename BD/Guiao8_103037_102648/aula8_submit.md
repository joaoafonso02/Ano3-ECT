# BD: Guião 8


## ​8.1. Complete a seguinte tabela.
Complete the following table.


| #    | Query                                                                                                      | Rows  | Cost  | Pag. Reads | Time (ms) | Index used | Index Op.            | Discussion |
| :--- | :--------------------------------------------------------------------------------------------------------- | :---- | :---- | :--------- | :-------- | :--------- | :------------------- | :--------- |
| 1    | SELECT * from Production.WorkOrder                                                                         | 72591 | 0.484 | 531        | 1171      | …          | Clustered Index Scan |            |
| 2    | SELECT * from Production.WorkOrder where WorkOrderID=1234                                                  |     1 | 0.003 | 26         | 26        | 1          |                      |            |
| 3.1  | SELECT * FROM Production.WorkOrder WHERE WorkOrderID between 10000 and 10010                               |    11 | 0.003 | 26         | 56        | 11         |                      |            |
| 3.2  | SELECT * FROM Production.WorkOrder WHERE WorkOrderID between 1 and 72591                                   | 72591 | 0.475 | 556        | 471       | *          |                      |            |
| 4    | SELECT * FROM Production.WorkOrder WHERE StartDate = '2007-06-25'                                          |     0 | 0.473 | 556        | 29        | *          |                      |            |
| 5    | SELECT * FROM Production.WorkOrder WHERE ProductID = 757                                                   |     9 | 0.037 | 46         | 41        | 11         |                      |            |
| 6.1  | SELECT WorkOrderID, StartDate FROM Production.WorkOrder WHERE ProductID = 757                              |     9 | 0.037 | 46         | 58        | 11         |                      |            |
| 6.2  | SELECT WorkOrderID, StartDate FROM Production.WorkOrder WHERE ProductID = 945                              |  1105 | 0.470 | 556        | 40        | *          |                      |            |
| 6.3  | SELECT WorkOrderID FROM Production.WorkOrder WHERE ProductID = 945 AND StartDate = '2006-01-04'            |     0 |       |            |           |            |                      |            |
| 7    | SELECT WorkOrderID, StartDate FROM Production.WorkOrder WHERE ProductID = 945 AND StartDate = '2006-01-04' |     0 |       |            |           |            |                      |            |
| 8    | SELECT WorkOrderID, StartDate FROM Production.WorkOrder WHERE ProductID = 945 AND StartDate = '2006-01-04' |     0 |       |            |           |            |                      |            |

## ​8.2.

### a)

```` SQL
CREATE TABLE mytemp ( 
    rid BIGINT /*IDENTITY (1, 1)*/ NOT NULL, 
    at1 INT NULL, 
    at2 INT NULL, 
    at3 INT NULL, 
    lixo VARCHAR(100) NULL,
    PRIMARY KEY CLUSTERED (rid)
);
````

### b)

```
	
```

### c)


| FILLFACTOR | Time (ms) | PAD_INDEX |
|:----------:|:---------:|:--------:|
|     65     |   62427   |    ON    |
|     65     |   61020   |   OFF    |
|     80     |   60103   |    ON    |
|     80     |   61594   |   OFF    |
|     90     |   68460   |    ON    |
|     90     |   65793   |   OFF    |



### d)

```` SQL
CREATE TABLE mytemp ( 
    rid BIGINT IDENTITY (1, 1) NOT NULL, 
    at1 INT NULL, 
    at2 INT NULL, 
    at3 INT NULL, 
    lixo VARCHAR(100) NULL,
    PRIMARY KEY CLUSTERED (rid) WITH (FILLFACTOR=90, PAD_INDEX=OFF) /* could change if its 65,80/90. and if PAD_INDEX is ON/OFF
);
````

### e)

``` SQL
create NONCLUSTERED index at1 on mytemp(at1);
create NONCLUSTERED index at2 on mytemp(at2);
create NONCLUSTERED index at3 on mytemp(at3);
create NONCLUSTERED index lixo on mytemp(lixo);
```


## ​8.3.

### i)
``` SQL
CREATE UNIQUE CLUSTERED INDEX IndexxSsn ON EMPLOYEE(Ssn);
```

### ii)
``` SQL
CREATE COMPOSITE CLUSTERED INDEX IndexNames ON EMPLOYEE(Fname, Lname,);
```

### iii)
``` SQL
CREATE NONCLUSTERED INDEX IndexxDno ON Company.EMPLOYEE(Dno); /* Check, not sure
```

### iv)
``` SQL
CREATE COMPOSITE CLUSTERED INDEX IndexxSsnPno ON WORKS_ON(Essn,Pno,);  /* Confirm, not sure
```
