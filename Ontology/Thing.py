# coding=utf-8

class Thing (object):
    
    @staticmethod
    def getSubTopicOf(topic):
        
        topic = topic.lower()
        
        if (topic == ("Participación Política").lower()):
            return "- Asociaciones \n- Propuestas \n- Grupos Sociales"
        
        elif (topic == ("Cultura").lower()):
            return "- Arte \n- Ciencia \n- Deportes"
            
        elif (topic == ("Democracia").lower()):
            return "- Vivienda \n- Igualdad \n- Servicios Sociales"
            
        elif (topic == ("Economía").lower()):
            return "- Sector Primario \n- Sector Secundario \n- Sector Terciario \n- Sector Cuaternario"
            
        elif (topic == ("Gobierno").lower()):
            return "- Gobierno local \n- Gobierno municipal \n- Gobierno nacional \n- Política \n- Partidos políticos"
            
        elif (topic == ("Sanidad").lower()):
            return "- Sanidad pública \n- Atención primaria"
            
        elif (topic == ("Justicia").lower()):
            return "- Derechos humanos \n- Leyes"
            
        elif (topic == ("Democracia").lower()):
            None
            
        elif (topic == ("Ocio").lower()):
            None
            
        elif (topic == ("Medio Ambiente").lower()):
            None
            
        elif (topic == ("Personas").lower()):
            return "- Ciudadanos \n- Funcionarios \n- Políticos"
            
        elif (topic == ("Seguridad").lower()):
            return "- Ejército \n- Agentes medioambientales \n- Inteligencia \n- Policía"
            
        else:
            return None