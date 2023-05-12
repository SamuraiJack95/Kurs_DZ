--1.
--SELECT ID, Produce PROD, Material MAT, Color COL, Size SZ, Country CTR, ID_salespeople IDS, Price PR, Count CNT, REM
--FROM WARE
--WHERE IDS IS NULL

--2.
--SELECT PRODUCE, ID_salespeople, COUNTRY
--FROM WARE
--WHERE COUNTRY = "Украина"

--3.
--DELETE FROM WARE
--WHERE COUNTRY == "Германия"

--4.
--UPDATE WARE
--SET COUNTRY = "Россия"
--WHERE COUNTRY = "Польша"

--SELECT ID, PRODUCE, COUNTRY, REM
--FROM WARE

--5.
/*INSERT into WARE (ID, PRODUCE, MATERIAL, COLOR, SIZE, COUNTRY, ID_salespeople, PRICE, COUNT, REM)
VALUES (1026, "FKFFO4454", "полиэстер", "ч", "38x21x70", "Германия", 2014, 126, 0, "fjjjifjesif")*/

/*INSERT into WARE (ID, PRODUCE, MATERIAL, COLOR, SIZE, COUNTRY, ID_salespeople, PRICE, COUNT, REM)
VALUES (1254, "Ffferfe54", "кожзам", "ч", "40x30x8", "Германия", 2001, 325, 14, "vmdcbnresif")*/

/*INSERT into WARE (ID, PRODUCE, MATERIAL, COLOR, SIZE, COUNTRY, ID_salespeople, PRICE, COUNT, REM)
VALUES (1049, "FJTJFUGNR45", "нейлон", "ч", "38x29x7", "Германия", 2011, 110, 6, "fjjfjуdcrfsif")*/

/*INSERT into WARE (ID, PRODUCE, MATERIAL, COLOR, SIZE, COUNTRY, ID_salespeople, PRICE, COUNT, REM)
VALUES (1001, "Fffreswdg454", "кожзам", "ч", "41x30x8", "Германия", 2001, 143, 2, "ffuuyytiikesif")*/

/*INSERT into WARE (ID, PRODUCE, MATERIAL, COLOR, SIZE, COUNTRY, ID_salespeople, PRICE, COUNT, REM)
VALUES (1036, "EPKLDFJJ4454", "полиэстер", "ч", "39x30x5", "Германия", 2011, 435, 32, "fEQDWDArfresif")*/

/*INSERT into WARE (ID, PRODUCE, MATERIAL, COLOR, SIZE, COUNTRY, ID_salespeople, PRICE, COUNT, REM)
VALUES (1017, "KKLOKD4454", "полиэстер", "ч", "44x33x5", "Германия", 2015, 110, 29, "fjjDCSCSsskd")*/

--6.
--SELECT PRODUCE, PRICE, ID_salespeople
--FROM WARE
--WHERE COLOR != "ч"

--7.
/*INSERT into WARE (ID, PRODUCE, MATERIAL, COLOR, SIZE, COUNTRY, ID_salespeople, PRICE, COUNT, REM)
VALUES (1046, "NTC-117BK", "нейлон", "ч", "13x8x5", "Украина", 2016, 110, 29, "Micro Camera Case")*/

--8.
--INSERT into WARE (id, PRODUCE, MATERIAL, COLOR, SIZE, COUNTRY, ID_salespeople, PRICE, COUNT, REM)
--VALUES (1234, "POC-463BK", "полиэстер", "ч", "11x7x4", Null, Null, Null, Null, "Compact Camera Case")

--9.
--SELECT produce, country, ID_salespeople
--FROM WARE
--WHERE (ID_salespeople == 2065) AND COUNTRY == "Россия"

--10.
--SELECT PRODUCE, PRICE
--FROM WARE
--WHERE PRICE BETWEEN 200 AND 346

--11.
--SELECT PRODUCE, SIZE, MATERIAL
--FROM WARE
--WHERE MATERIAL == "кожа" AND SIZE < "4"

--12.
--SELECT REM, ID_salespeople
--FROM WARE
--WHERE COUNT*PRICE < 1200

--13.
--UPDATE WARE
--SET ID_salespeople = 2000
--WHERE PRICE * COUNT < 500

--14.
--SELECT REM
--FROM WARE
--WHERE (COUNT < 5) AND (COUNT * PRICE < 450)

--15.
--SELECT REM
--FROM WARE
--WHERE (MATERIAL == 'нейлон') AND (PRICE < 250)

--16.
--UPDATE WARE
--SET MATERIAL = 'брезент'
--WHERE MATERIAL == 'нейлон' AND (PRICE < 250)

--17.
--SELECT REM
--FROM WARE
--WHERE REM LIKE "%косметичка%"

--18.
--SELECT *
--FROM WARE
--WHERE (MATERIAL == "кожа") AND (COLOR == "ч") AND (COUNTRY == "Китай")

--19.
--SELECT REM
--FROM WARE
--WHERE SIZE > "15"

--20.
--SELECT ID_salespeople, COLOR
--FROM WARE
--GROUP BY ID_salespeople
--HAVING COLOR NOT IN ("ч")

--21.
--UPDATE WARE
--SET MATERIAL = "нейлон"
--WHERE COUNTRY == "Китай" AND MATERIAL == "полиэстер"

--22.
--UPDATE WARE
--SET MATERIAL = "полиэстер"
--WHERE (COUNTRY = "Китай") AND (ID in (1015, 1041,1032, 1010))