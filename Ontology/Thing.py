# coding=utf-8

class Thing (object):
    
    @staticmethod
    def getSubTopicOf(topic):
        
        if (topic == "Participación Política"):
            return "- Asociaciones \n - Propuestas \n - Grupos Sociales"
        
        elif (topic == "Culture"):
            return "- Arte \n - Ciencia \n - Deportes"
            
        elif ("Democracia"):
            return "- Vivienda \n - Igualdad \n - Servicios Sociales"
            
        elif ("Economía"):
            return "- Sector Primario \n - Sector Secundario \n - Sector Terciario \n - Sector Cuaternario"
            
        elif ("Gobierno"):
            return "- Gobierno local \n - Gobierno municipal \n - Gobierno nacional \n - Política \n - Partidos políticos"
            
        elif ("Sanidad"):
            return "- Sanidad pública \n - Atención primaria"
            
        elif ("Justicia"):
            return "- Derechos humanos \n - Leyes"
            
        elif ("Democracia"):
            None
            
        elif ("Ocio"):
            None
            
        elif ("Medio Ambiente"):
            None
            
        elif ("Personas"):
            return "- Ciudadanos \n - Funcionarios \n - Políticos"
            
        elif ("Seguridad"):
            return "- Ejército \n - Agentes medioambientales \n - Inteligencia \n - Policía"
            
        else:
            return None