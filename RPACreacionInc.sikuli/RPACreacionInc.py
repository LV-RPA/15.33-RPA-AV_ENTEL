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

print("abrir iexplorer")
App.open("C:\\Program Files\\internet explorer\\iexplore.exe")
sleep(10)
if exists("1576879424332-1.png",5):
    sleep(2)
    click(Pattern("1576879424332-1.png").targetOffset(-4,-17))
    sleep(5) 
    
print("Ingresar Portal")
wait("1568303506821-1.png",120)
sleep(3)
paste(Pattern("1568303696409-1.png").targetOffset(65,-12), user_portal)
sleep(2)
type(Key.TAB)
sleep(2)
paste(pass_portal)
sleep(2)
type(Key.ENTER)
sleep(10)
if exists ("1568322894042-1.png",10):
    click(Pattern("1568323065585-1.png").targetOffset(0,1))
    sleep(2)
    click(Pattern("1568323106628-1.png").targetOffset(-56,2))
    sleep(10)
    
click(Pattern("1576283268126.png").targetOffset(-14,12))
sleep(10)
click("1576872194943-1.png")
sleep(3)
type('w',Key.CTRL)
sleep(10)

print("ingresar al portal")
type(Key.TAB, KEY_CTRL)
sleep(3)
type(Key.UP, KeyModifier.WIN)
sleep(5)
paste(Pattern("1568321503727-1.png").targetOffset(40,-11), user_entel)
sleep(2)
type(Key.TAB)
sleep(2)
paste(pass_entel)
sleep(2)
type(Key.ENTER)
sleep(5)
if exists ("1568324732583-1.png",120):
    sleep(2)
    click(Pattern("1568324773276-1.png").targetOffset(-55,1))
    sleep(2)

try:
    conn = zxJDBC.connect(d, u, p, v)
    cursor = conn.cursor()
    cursor.execute("use AnovoASR exec sp_obtenerpreincidente_nuevo")
    sleep(5)
        
    for ost,cia,ano,gs,tlf,ncto,tcto,obs,iori in cursor.fetchall():
        print("abrir modulo")
        sleep(5)
        type(Key.ENTER)
        sleep(5)
        wait("1568323949843.png",120)
        sleep(2)
        click(Pattern("1568323985698.png").targetOffset(23,1))
        sleep(2)
        click(Pattern("1568324133635.png").targetOffset(68,2))
        sleep(10)
        
        print("Ingreso de datos")
        paste(Pattern("1568760487864.png").similar(0.80).targetOffset(-48,9),tlf)
        sleep(3)
        type(Key.ENTER)
        sleep(10)
        if exists("1568761138131.png",10):
            click(Pattern("1568761138131.png").targetOffset(109,-1))
            sleep(2)
    
        print("ingresar datos contacto")
        click(Pattern("1568761510523.png").targetOffset(214,13))
        sleep(3)
        click(Pattern("1568761607782.png").targetOffset(-56,-3))
        sleep(3)
        
        if exists("1568761138131.png",15):
            click(Pattern("1568761138131.png").targetOffset(109,-1))
            sleep(2)   

        sleep(3)
        paste(Pattern("1568764411275.png").targetOffset(102,2), ncto)
        sleep(2)
        type(Key.TAB)
        sleep(2)
        paste(ncto)
        sleep(3)
        paste(Pattern("1568764563603.png").targetOffset(101,0), tcto)
        sleep(3)
    
        print("ingresar descripcion")
        paste(Pattern("1568764827739.png").targetOffset(95,-12), obs)
        sleep(2)
        click(Pattern("1568821737641-1.png").targetOffset(-1,28))
        sleep(2)
        type(Key.END)
        sleep(5)
        click(Pattern("1568821971430.png").targetOffset(2,0))
        sleep(15)

        print("crear incidente")
        click(Pattern("1573230252336.png").targetOffset(82,15))
        sleep(3)
        click(Pattern("1568823329808-1.png").targetOffset(0,8))
        sleep(3)
        type(Key.TAB)
        sleep(3)
        click(Pattern("1569014535329-1.png").targetOffset(140,6))
        sleep(3)
        click(Pattern("1568823592994-1.png").targetOffset(-58,26))
        sleep(2)
        type(Key.TAB)
        sleep(3)
        click("1569014627556.png")
        sleep(3)
        click(Pattern("1568823890121-1.png").targetOffset(-17,20))
        sleep(3)
        type(Key.TAB)
        sleep(3)
        click(Pattern("1569020990460.png").targetOffset(104,7))
        sleep(3)
        click(Pattern("1568824106526.png").targetOffset(-20,14))
        sleep(3)
        type(Key.TAB)
        sleep(3)
        type(Key.TAB)
        sleep(4)
        click(Pattern("1569021872330.png").targetOffset(90,7))
        sleep(3)
        click(Pattern("1568824333339.png").targetOffset(-13,13))
        sleep(3)
        click(Pattern("1569021984006.png").targetOffset(80,2))
        sleep(3)
        click(Pattern("1568824440751.png").targetOffset(-45,17))
        sleep(2)
        click(Pattern("1568825162977.png").targetOffset(0,-10))
        sleep(2)
        click(Pattern("1568824514249.png").targetOffset(73,8))
        sleep(3)
        click(Pattern("1568825470455.png").targetOffset(-26,30))
        sleep(3)
    
        print("grabar incidente")
        paste(Pattern("1568825633671.png").similar(0.80).targetOffset(165,12), ncto)
        sleep(3)
        paste(Pattern("1568825719627.png").targetOffset(162,-10), tcto)
        sleep(3)
        
        print("lapicito")
        click(Pattern("1569533949500.png").targetOffset(-64,64))
        sleep(15)
        paste(Pattern("1569539538068.png").targetOffset(78,13), tlf)
        sleep(3)
        type(Key.TAB)
        sleep(20)
        if exists("1570750600130.png",10):
            sleep(2)
            click("1570750600130.png")
            sleep(2)
            click(Pattern("1570750692717.png").targetOffset(-1,-3))
        else:
            paste(Pattern("1569541011218.png").targetOffset(73,2), obs)
            sleep(3)        
            click(Pattern("1569538559738.png").targetOffset(-26,-2))
            sleep(5)        
            click(Pattern("1569538559738.png").targetOffset(34,-2))        
            sleep(5)
            
        print("grabar")
        sleep(3)
        click(Pattern("1583022321850.png").targetOffset(-36,-9))
        sleep(2)
        type(Key.DOWN)
        sleep(2)
        click(Pattern("1568825760289.png").targetOffset(3,1))
        sleep(10)
        type(Key.ENTER)
        sleep(10)
    
        print("registrar id incidente")
        doubleClick(Pattern("1568826020877.png").targetOffset(-10,26))
        sleep(2)
        type("c", KEY_CTRL)
        sleep(2)
        increg = Env.getClipboard().strip()
        print(increg)
        sleep(3)

        sql = "use AnovoASR exec sp_registrarnumeroincidente_nuevo ?,?,?,?,?,?,?"
        val = (cia,ano,ost,increg,obs,iori,"EN ESPERA") 
        cursor.execute(sql,val)   
        conn.commit()
        print(cursor.rowcount, "record(s) affected")
        
        print("agregar fecha entrega tienda")
        sql = """use AnovoASR exec sp_ProcesoLogistico_actualizarOrdenGuiaDespacho ?,?,?,'USER_RPA','',?,'','2','2'"""
        val = (gs,cia,ost,ano)
        cursor.execute(sql,val)
        conn.commit()
        
        sql = """use AnovoASR exec sp_ProcesoLogistico_actualizarGuiaDespacho ?,?,'USER_RPA','',?,'2'"""
        val = (gs,cia,ano)
        cursor.execute(sql,val)
        conn.commit()
        print("actualizado")

        click(Pattern("1576192682939-1.png").targetOffset(-17,-10))
        sleep(10)

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

finally:
    conn.close()
    print("conexion cerrada")
 