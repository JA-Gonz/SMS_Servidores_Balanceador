import datetime
import jinja2
import os
import webapp2
import cgi
import re
from Estadisticas import Estadisticas

plantilla_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))

class PaginaGetEstadisticas(webapp2.RequestHandler):
    def get(self):
        plantilla = plantilla_env.get_template('plantilla/index.html')
        self.response.out.write(plantilla.render())

    def post(self):
        print "COJONES2!"
        if not(self.request.get('orden')):
            print "COJONES3!"
            plantilla = plantilla_env.get_template('plantilla/index.html')
            self.response.out.write(plantilla.render())

        else:

            string = "a"
            if(self.request.get('orden')) =="obtenerPorcentajeSuspensosProfesores":
                string = str(Estadisticas.obtenerPorcentajeSuspensosProfesores("SinFiltros"))


            templateVars = {"texto" : string}
            plantilla = plantilla_env.get_template('plantilla/index.html')
            self.response.out.write(plantilla.render(templateVars))


class PaginaConfigurarEstadisticas(webapp2.RequestHandler):

    def get(self):
        plantilla=plantilla_env.get_template('plantilla/configurar_estadisticas.html')
    	self.response.out.write(plantilla.render())

class PaginaExitoConfigurarEstadisticas(webapp2.RequestHandler):
    def get(self):
        plantilla=plantilla_env.get_template('plantilla/configurar_estadisticas_exito.html')
        self.response.out.write(plantilla.render())


aplicacion = webapp2.WSGIApplication([
                                      ('/configurar_estadisticas',PaginaConfigurarEstadisticas),
                                      ('/configurar_estadisticas_exito',PaginaExitoConfigurarEstadisticas),
                                      ('/',PaginaGetEstadisticas),
					], debug=True)




def main():
    from paste import httpserver
    httpserver.serve(aplicacion, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()