link_sistec = "https://portalvpnssl.claro.com.pe/proveedores"
user_sistec = "E8840100"
pass_sistec = "kwJyvzp4%$"
ruta = (r'\\10.120.15.33\Sistec')
delete_files = (r'del /S /Q \\10.120.15.33\Sistec\*')

print("abrir firefox")
sleep(2)
type("r",KeyModifier.WIN)
sleep(3)
paste("firefox")
sleep(2)
type(Key.ENTER)
sleep(15)

print("Ingresar pagina")
wait("1572464723460.png",120)
sleep(2)
click(Pattern("1572464723460.png").targetOffset(11,4),120)
sleep(3)
type("l",KEY_CTRL)
sleep(2)
paste(link_sistec)
sleep(2)
type(Key.ENTER)
sleep(2)

print("login sistec")
wait("1572465072616.png",120)
sleep(2)
paste(Pattern("1572465094429.png").targetOffset(-84,7),user_sistec)
sleep(2)
type(Key.TAB)
sleep(2)
paste(pass_sistec)
sleep(2)
type(Key.ENTER)
sleep(5)
try:
    
    print("ingreso sistec")
    wait("1572465273197.png",60)
    sleep(2)
    click(Pattern("1572465309109.png").targetOffset(-22,1))
    sleep(5)
    
    print("inicio exportar datos")
    wait("1572465350803.png")
    sleep(2)
    click(Pattern("1572465350803.png").targetOffset(-3,0))
    sleep(2)
    wait("1572465428190.png",10)
    sleep(2)
    click("1572465428190.png")
    sleep(2)
    click(Pattern("1572465481829.png").targetOffset(4,43))
    sleep(2)
    wait("1572465575957.png",10)
    sleep(2)
    
    print("exportar data")
    click(Pattern("1572465651565.png").targetOffset(4,14))
    sleep(2)
    type("w",KEY_CTRL)
    #click("1572465575957.png")
    #sleep(2)
    #wait("1572475542397.png")
    #sleep(2)
    #type("l",KEY_CTRL)
    #sleep(2)
    #paste(ruta)
    #sleep(2)
    #type(Key.ENTER)
    #sleep(2)
    #type(Key.ENTER)
    #sleep(10)
    click(Pattern("1579882479369.png").targetOffset(0,1))
    sleep(5)
    type("w",KEY_CTRL)

    
except:
    print("error")
    type("w",KEY_CTRL)
    sleep(2)
    type("w",KEY_CTRL)
    sleep(2)
    type("w",KEY_CTRL)
    sleep(2)
