# coding=utf-8

class Thing (object):
    
    @staticmethod
    def getSubTopicOf(topic):
        
        topic = topic.lower()
        
        ret = ""
        
        if (topic == ("Participación Política").lower()):
            ret = ret + "\n" + "- Asociaciones \n- Propuestas \n- Grupos Sociales"
        
        elif (topic == ("Cultura").lower()):
            ret = ret + "\n" +  "- Arte \n- Ciencia \n- Deportes"
            
        elif (topic == ("Democracia").lower()):
            ret = ret + "\n" +  "- Vivienda \n- Igualdad \n- Servicios Sociales"
            
        elif (topic == ("Educación").lower()):
            ret = ret + "\n" +  "- Educación preescolar \n- Educación primaria \n- Educación secundaria \n- Universidad \n- Formación Profesional"
            
        elif ((topic == ("Discapacidad").lower()) | (topic == ("Trabajo").lower()) | (topic == ("Pensiones").lower())):
            ret = ret + "\n" +  "- Servicios Sociales"
            
        elif ((topic == ("Agricultura").lower()) | (topic == ("Pesca").lower()) | (topic == ("Minería").lower())):
            ret = ret + "\n" +  "- Sector primario"
            
        elif ((topic == ("Comunicación").lower()) | (topic == ("Electricidad").lower()) | (topic == ("Industria").lower())):
            ret = ret + "\n" +  "- Sector secundario"
            
        elif ((topic == ("Construcción").lower()) | (topic == ("Educación").lower()) | (topic == ("Finanzas").lower()) | (topic == ("Turismo").lower()) | (topic == ("Comercio").lower()) | (topic == ("Transporte").lower())):
            ret = ret + "\n" +  "- Sector terciario"
            
        elif ((topic == ("Investigación").lower()) | (topic == ("Tecnología").lower()) | (topic == ("Desarrollo").lower()) | (topic == ("Ciencia").lower())):
            ret = ret + "\n" +  "- Sector cuaternario"
            
        elif (topic == ("Economía").lower()):
            ret = ret + "\n" +  "- Sector Primario \n- Sector Secundario \n- Sector Terciario \n- Sector Cuaternario"
            
        elif (topic == ("Finanzas").lower()):
            ret = ret + "\n" +  "- Deuda \n- Banca pública \n- Educación secundaria \n- Universidad \n- Formación Profesional"
            
        elif (topic == ("Gobierno").lower()):
            ret = ret + "\n" +  "- Gobierno local \n- Gobierno municipal \n- Créditos"
            
        elif (topic == ("Política").lower()):
            ret = ret + "\n" +  "- Política Nacional \n- Política Exterior \n- Política Social \n- Partidos Políticos"
            
        elif (topic == ("Sanidad").lower()):
            ret = ret + "\n" +  "- Sanidad pública \n- Atención primaria"
            
        elif (topic == ("Justicia").lower()):
            ret = ret + "\n" +  "- Derechos humanos \n- Leyes"
            
        elif (topic == ("Ocio").lower()):
            None
            
        elif (topic == ("Medio Ambiente").lower()):
            None
            
        elif (topic == ("Personas").lower()):
            ret = ret + "\n" +  "- Ciudadanos \n- Funcionarios \n- Políticos"
            
        elif (topic == ("Seguridad").lower()):
            ret = ret + "\n" +  "- Ejército \n- Agentes medioambientales \n- Inteligencia \n- Policía"
            
        elif (topic == ("Embarazo").lower()):
            ret = ret + "\n" +  "- Derechos"
            
        else:
            return None
            
        return ret