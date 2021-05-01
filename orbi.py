from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from tkinter import *
import time

class Orbi():
    def __init__(self):
        self.mail = input("ingrese su correo: ")
        self.password = input(("ingrese su password: "))
        self.link = input(("link del formulario: "))
    
    def filler(self):
        try:
            #acceso a Orbi
            driver = webdriver.Edge(executable_path="C:\\Users\\Admin\\Downloads\\edgedriver_win64\\msedgedriver")
            driver.maximize_window()
            driver.get('https://orbi.edu.do/orbi/evaluacion/recolecciond/registrar/177-0')
            time.sleep(5)

            #hacer login
            driver.find_element_by_id("txtNombreUsuario").send_keys(self.mail)
            driver.find_element_by_id("txtContrasena").send_keys(self.password)
            driver.find_element_by_id("btnSesion").click()
            time.sleep(4)
            
            #selecciona opciones
            driver.get(self.link)
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

    



