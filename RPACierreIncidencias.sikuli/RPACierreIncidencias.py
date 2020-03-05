load("mssql-jdbc-7.0.0.jre8.jar")
from com.ziclix.python.sql import zxJDBC
from datetime import datetime
import os 
import glob
import sys

user_portal = "anv_cquispea"
pass_portal = "PaSsWk2020"
user_entel = "EXTCQUISPEA"
pass_entel = "140120"

conn = None
d, u, p, v = "jdbc:sqlserver://10.120.25.80", "ENVIRONMENT_PRD", "@env-PRD-2015$#", "com.microsoft.sqlserver.jdbc.SQLServerDriver"

print("cerrar procesos")
os.system('taskkill /f /im firefox.exe')
os.system('taskkill /f /im iexplore.exe')

try:
    print("abrir iexplorer")
    App.open("C:\\Program Files\\internet explorer\\iexplore.exe")
    sleep(15)
    if exists("1576879424332.png",10):
        sleep(2)
        click(Pattern("1576879424332.png").targetOffset(-4,-17))
        sleep(5) 
        
    sleep(3)    
    print("Ingresar Portal")
    wait("1568303506821.png",120)
    sleep(3)
    paste(Pattern("1568303696409.png").targetOffset(65,-12),user_portal)
    sleep(2)
    type(Key.TAB)
    sleep(2)
    paste(pass_portal)
    sleep(2)
    type(Key.ENTER)
    sleep(15)
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

    print("inicio de conexion, bucle")
    conn = zxJDBC.connect(d, u, p, v)
    cursor = conn.cursor()
    cursor.execute("use AnovoASR exec usp_ObtenerIncidenciasCierreEntel")
        
    for incidente,entel in cursor.fetchall():
        print("abrir modulo")
        sleep(5)
        type(Key.ENTER)
        sleep(5)
        wait("1568323949843.png",120)
        sleep(2)
        click(Pattern("1576191309881.png").targetOffset(-18,2))
        sleep(2)
        click(Pattern("1576191361590.png").targetOffset(84,1))
        sleep(10)
        wait("1576191457837.png",120)
        sleep(3)

        print("buscar incidente")
        paste(Pattern("1576191525973.png").targetOffset(129,1), incidente)
        sleep(3)
        click(Pattern("1576191457837.png").targetOffset(-15,12))
        sleep(20)
        if exists(Pattern("1576191694728.png").targetOffset(0,16)):
            sleep(3)
            click(Pattern("1576191694728.png").targetOffset(0,16))
            sleep(10)
            
        elif exists("1578442497348.png"):
            sleep(3)
            click(Pattern("1578442497348.png").targetOffset(-2,2))
            sleep(10)
            
        type(Key.ENTER)
        sleep(8)
        wait("1576191793092.png",120)
        sleep(3)
        type(Key.DOWN*20)
        sleep(2)

        print("cambiar estado")
        if exists(Pattern("1576279285354.png").similar(0.80).targetOffset(79,6)):
            print("abierto 1")
            click(Pattern("1576279285354.png").similar(0.80).targetOffset(79,6))
            sleep(2)
            click(Pattern("1576192185485.png").targetOffset(-57,20))
            sleep(2)
            click(Pattern("1576192245705.png").targetOffset(-84,2))
            sleep(2)
    
            print("pegar comentario")
            paste(Pattern("1576192842718.png").targetOffset(-27,6), entel)
            sleep(5)
            click(Pattern("1576279596812.png").targetOffset(-55,-9))
            sleep(3)
            type(Key.DOWN*5)
            sleep(3)
            
            print("grabar")
            click("1576279651584.png")
            sleep(10)
            type(Key.ENTER)
            sleep(10)
            type(Key.ENTER)
            sleep(10)
            type(Key.UP*10)
            sleep(5)
    
            print("fin del proceso")
            click(Pattern("1576192682939.png").targetOffset(-17,-10))
            sleep(10)
            
            sql = "update AnovoASR.dbo.INCIDENCIA2 set IncidenteCerrado =? where incidencia =?"
            val = ("1",incidente) 
        
            cursor.execute(sql,val)   
            conn.commit()    
            print(cursor.rowcount, "record(s) affected")

            print("cambiar estado")
        elif exists(Pattern("1576541273834.png").similar(0.80).targetOffset(79,5)):
            print("abierto 1")
            click(Pattern("1576541273834.png").similar(0.80).targetOffset(79,5))
            sleep(2)
            click(Pattern("1576192185485.png").targetOffset(-57,20))
            sleep(2)
            click(Pattern("1576192245705.png").targetOffset(-84,2))
            sleep(2)
    
            print("pegar comentario")
            paste(Pattern("1576192842718.png").targetOffset(-27,6), entel)
            sleep(5)
            click(Pattern("1576279596812.png").targetOffset(-55,-9))
            sleep(3)
            type(Key.DOWN*5)
            sleep(3)
            
            print("grabar")
            click("1576279651584.png")
            sleep(10)
            type(Key.ENTER)
            sleep(10)
            type(Key.ENTER)
            sleep(10)
            type(Key.UP*10)
            sleep(2)
    
            print("fin del proceso")
            click(Pattern("1576192682939.png").targetOffset(-17,-10))
            sleep(10)
            
            sql = "update AnovoASR.dbo.INCIDENCIA2 set IncidenteCerrado =? where incidencia =?"
            val = ("1",incidente) 
        
            cursor.execute(sql,val)   
            conn.commit()    
            print(cursor.rowcount, "record(s) affected")
            
        elif exists(Pattern("1578613063566.png").similar(0.80)):
            print("cerrado")
            sleep(5)
            type(Key.UP*15)
            sleep(2)
            print("fin del proceso")
            click(Pattern("1576192682939.png").targetOffset(-17,-10))
            sleep(10)
            
            sql = "update AnovoASR.dbo.INCIDENCIA2 set IncidenteCerrado =? where incidencia =?"
            val = ("1",incidente) 
        
            cursor.execute(sql,val)   
            conn.commit()    
            print(cursor.rowcount, "record(s) affected")

        elif exists("1578527129072.png"):
            print("cerrado")
            sleep(5)
            type(Key.UP*15)
            sleep(2)
            print("fin del proceso")
            click(Pattern("1576192682939.png").targetOffset(-17,-10))
            sleep(10)
            
            sql = "update AnovoASR.dbo.INCIDENCIA2 set IncidenteCerrado =? where incidencia =?"
            val = ("1",incidente) 
        
            cursor.execute(sql,val)   
            conn.commit()    
            print(cursor.rowcount, "record(s) affected")

    else:
        print("No hay pendientes")
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
    App.open("C:\\WINDOWS\\system32\\notepad.exe")
    sleep(5)
    paste(ErrorText)
    sleep(5)
    App.open("C:\\Users\\Administrador\\Documents\\App\\SSmail\\SSmail.exe")
    sleep(5)
    
finally:
    conn.close()
    print("conexion cerrada")