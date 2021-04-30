from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

try:
    #acceso a Orbi
    driver = webdriver.Edge(executable_path="C:\\Users\\Admin\\Downloads\\edgedriver_win64\\msedgedriver")
    driver.maximize_window()
    driver.get('https://orbi.edu.do/orbi/evaluacion/recolecciond/registrar/177-0')
    time.sleep(5)

    #hacer login
    user = driver.find_element_by_id("txtNombreUsuario").send_keys("shaquillerodriguez4@gmail.com")
    password = driver.find_element_by_id("txtContrasena").send_keys("Shaquille21")
    login_button = driver.find_element_by_id("btnSesion").click()
    time.sleep(4)
    
    #selecciona opciones
    driver.get('https://orbi.edu.do/orbi/evaluacion/recolecciond/registrar/176-37111')
    time.sleep(2)
    driver.execute_script(
        '''
        var realesElementos = document.querySelectorAll("table tbody tr td")

        Array.from(realesElementos).forEach((elemento) => {
        if(elemento.textContent.trim() == "1" ) elemento.children[0].checked = true
        })
        '''
        )
    driver.find_element_by_class_name('espacio-d20')
except Exception as A:
    print ("hay un bobito: ", A)

    


#check = driver.find_element_by_xpath("//input[@value='49611']").is_selected()
#print (check)

