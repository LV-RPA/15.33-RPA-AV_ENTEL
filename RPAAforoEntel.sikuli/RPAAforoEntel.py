load("mssql-jdbc-7.0.0.jre8.jar")
from com.ziclix.python.sql import zxJDBC
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding( "latin-1" )

user_portal = "externo.mesanchezm"
pass_portal = "Entel2025"
user_entel = "989868374"
pass_entel = "102030"

conn = None
d, u, p, v = "jdbc:sqlserver://10.120.25.80", "ENVIRONMENT_PRD", "@env-PRD-2015$#", "com.microsoft.sqlserver.jdbc.SQLServerDriver"

print("abrir iexplorer")
type("r",KeyModifier.WIN)
sleep(3)
paste("iexplore")
sleep(2)
type(Key.ENTER)
sleep(10)
if exists("1576879424332.png"):
    sleep(2)
    click(Pattern("1576879424332.png").targetOffset(-4,-17))
    sleep(5) 
    
print("Ingresar Portal")
wait("1568303506821.png",120)
sleep(3)
paste(Pattern("1568303696409.png").targetOffset(65,-12), user_portal)
sleep(2)
type(Key.TAB)
sleep(2)
paste(pass_portal)
sleep(2)
type(Key.ENTER)
sleep(10)
if exists ("1568322894042.png",10):
    click(Pattern("1568323065585.png").targetOffset(0,1))
    sleep(2)
    click(Pattern("1568323106628.png").targetOffset(-56,2))
    sleep(10)
    
click(Pattern("1576283268126.png").targetOffset(-14,12))
sleep(10)
click("1576872194943.png")
sleep(3)
type('w',Key.CTRL)
sleep(10)

print("ingresar al portal")
type(Key.TAB, KEY_CTRL)
sleep(3)
type(Key.UP, KeyModifier.WIN)
sleep(5)
paste(Pattern("1568321503727.png").targetOffset(40,-11), user_entel)
sleep(2)
type(Key.TAB)
sleep(2)
paste(pass_entel)
sleep(2)
type(Key.ENTER)
sleep(5)
if exists ("1568324732583.png",120):
    sleep(2)
    click(Pattern("1568324773276.png").targetOffset(-55,1))
    sleep(2)

try:
    conn = zxJDBC.connect(d, u, p, v)
    cursor = conn.cursor()
    cursor.execute("use AnovoASR exec usp_ObtenerOrdenesAforoEntel")
        
    for incidente,telefono,razon,entel in cursor.fetchall():
        print("abrir modulo")
        sleep(5)
        type(Key.ENTER)
        sleep(5)
        wait("1568323949843.png",120)
        sleep(2)
        click(Pattern("1577473957575.png").targetOffset(44,1))
        sleep(2)
        click(Pattern("1577473986005.png").targetOffset(88,1))
        sleep(2)
        click(Pattern("1577474019427.png").targetOffset(11,-1))
        sleep(10)
        wait("1577474070634.png",120)
        sleep(3)

        print("buscar incidente")
        paste(Pattern("1577474091534.png").targetOffset(-37,9), telefono)
        sleep(3)
        type(Key.ENTER)
        sleep(10)
        if exists("1577474389606.png"):
            sleep(2)
            print("no se encontro datos")
            sleep(2)
            
            sql = "update AnovoASR.dbo.INCIDENCIA2 set CreadoEntel =? where incidencia =? and telefono=?"
            val = ("0",incidente,telefono) 
        
            cursor.execute(sql,val)   
            conn.commit()
            print(cursor.rowcount, "record(s) affected")
            
            sql = "update AnovoASR.dbo.INCIDENCIA2 set CrearManual =? where incidencia =? and telefono=?"
            val = ("1",incidente,telefono) 
        
            cursor.execute(sql,val)   
            conn.commit()
            print(cursor.rowcount, "record(s) affected")

        elif exists("1577474672297.png"):
            sleep(2)
            print("IMEI robado")
            sleep(2)
            
            sql = "update AnovoASR.dbo.INCIDENCIA2 set CreadoEntel =? where incidencia =? and telefono=?"
            val = ("0",incidente,telefono) 
        
            cursor.execute(sql,val)   
            conn.commit()
            print(cursor.rowcount, "record(s) affected")
            
            sql = "update AnovoASR.dbo.INCIDENCIA2 set CrearManual =? where incidencia =? and telefono=?"
            val = ("1",incidente,telefono) 
        
            cursor.execute(sql,val)   
            conn.commit()
            print(cursor.rowcount, "record(s) affected")

        else:
            print("proceder")
            sleep(2)
            paste(Pattern("1577475115442.png").targetOffset(21,2), razon)
            sleep(2)
            paste(Pattern("1577475183825.png").targetOffset(-10,2),incidente)
            sleep(2)
            paste("//")
            sleep(2)
            doubleClick(Pattern("1577475392848.png").targetOffset(-3,18))
            sleep(2)
            type("c", KEY_CTRL)
            sleep(2)
            click(Pattern("1577475530226.png").targetOffset(-75,-74))
            sleep(2)
            type("v", KEY_CTRL)
            sleep(2)

            print("ingresar falla")
            paste(Pattern("1577475628546.png").targetOffset(52,1), telefono)
            sleep(2)
            paste(Pattern("1577475685593.png").targetOffset(104,-15), entel)
            sleep(3)

            print("lapicito")
            click(Pattern("1577475868858.png").targetOffset(1,-1))
            sleep(10)
            click("1577476533477.png")
            sleep(2)
            click(Pattern("1577476565926.png").targetOffset(82,-1))
            sleep(2)
            click(Pattern("1577476619063.png").targetOffset(-11,6))
            sleep(2)
            paste(Pattern("1577476680982.png").targetOffset(53,-16), entel)
            sleep(2)
            click(Pattern("1577476811359.png").targetOffset(45,0))
            sleep(10)
            #click(Pattern("1577476762593.png").targetOffset(-75,-1))
            #sleep(5)
            #type(Key.ENTER)
            sleep(5)
            print("fin del proceso")
            click(Pattern("1576192682939.png").targetOffset(-17,-10))
            sleep(2)
            
            sql = "update AnovoASR.dbo.INCIDENCIA2 set CrearManual =? where incidencia =? and telefono=?"
            val = ("1",incidente,telefono)  
        
            cursor.execute(sql,val)   
            conn.commit()
            print(cursor.rowcount, "record(s) affected")
            
            sql = "update AnovoASR.dbo.INCIDENCIA2 set CrearManual =? where incidencia =? and telefono=?"
            val = ("0",incidente,telefono)  
        
            cursor.execute(sql,val)   
            conn.commit()
            print(cursor.rowcount, "record(s) affected")

            
    else:
        print("No hay pendientes")
        conn.close()
        sleep(2)
        type("w",KEY_CTRL)
        sleep(2)
        print("FIN RPA")

except:
    exc_type, exc_val, exc_tb = sys.exc_info()

    ErrorText = "***** ERROR IN SCRIPTNAME = " + sys.argv[0] + " *****\n"
    ErrorText += "Date/Time : " + str(datetime.now()) + "\n"
    ErrorText += "Line Number: " + str(exc_tb.tb_lineno) + "\n"
    ErrorText += "Error Type : " + exc_type.__name__ + "\n"
    ErrorText += "Error Value: " + exc_val.message + "\n"
    ErrorText += "***************************************************************\n\r"
    print ErrorText