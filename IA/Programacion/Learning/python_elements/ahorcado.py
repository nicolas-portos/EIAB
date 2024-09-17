import random
import string

vidas_diccionario_visual = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }
lista_palabras = ["de","la","que","el","en","y","a","los","se","del","las","un","por","con","no","una","su","para","es","al","lo","como","más","o","pero","sus","le","ha","me","si","sin","sobre","este","ya","entre","cuando","todo","esta","ser","son","dos","también","fue","había","era","muy","años","hasta","desde","está","mi","porque","qué","sólo","han","yo","hay","vez","puede","todos","así","nos","ni","parte","tiene","él","uno","donde","bien","tiempo","mismo","ese","ahora","cada","e","vida","otro","después","te","otros","aunque","esa","eso","hace","otra","gobierno","tan","durante","siempre","día","tanto","ella","tres","sí","dijo","sido","gran","país","según","menos","mundo","año","antes","estado","contra","sino","forma","caso","nada","hacer","general","estaba","poco","estos","presidente","mayor","ante","unos","les","algo","hacia","casa","ellos","ayer","hecho","primera","mucho","mientras","además","quien","momento","millones","esto","españa","hombre","están","pues","hoy","lugar","madrid","nacional","trabajo","otras","mejor","nuevo","decir","algunos","entonces","todas","días","debe","política","cómo","casi","toda","tal","luego","pasado","primer","medio","va","estas","sea","tenía","nunca","poder","aquí","ver","veces","embargo","partido","personas","grupo","cuenta","pueden","tienen","misma","nueva","cual","fueron","mujer","frente","josé","tras","cosas","fin","ciudad","he","social","manera","tener","sistema","será","historia","muchos","juan","tipo","cuatro","dentro","nuestro","punto","dice","ello","cualquier","noche","aún","agua","parece","haber","situación","fuera","bajo","grandes","nuestra","ejemplo","acuerdo","habían","usted","estados","hizo","nadie","países","horas","posible","tarde","ley","importante","guerra","desarrollo","proceso","realidad","sentido","lado","mí","tu","cambio","allí","mano","eran","estar","san","número","sociedad","unas","centro","padre","gente","final","relación","cuerpo","obra","incluso","través","último","madre","mis","modo","problemas","cinco","carlos","hombres","información","ojos","muerte","nombre","algunas","público","mujeres","siglo","todavía","meses","mañana","esos","nosotros","hora","muchas","pueblo","alguna","dar","problema","don","da","tú","derecho","verdad","maría","unidos","podría","sería","junto","cabeza","aquel","luis","cuanto","tierra","equipo","segundo","director","dicho","cierto","casos","manos","nivel","podía","familia","largo","partir","falta","llegar","propio","ministro","cosa","primero","seguridad","hemos","mal","trata","algún","tuvo","respecto","semana","varios","real","sé","voz","paso","señor","mil","quienes","proyecto","mercado","mayoría","luz","claro","iba","éste","pesetas","orden","español","buena","quiere","aquella","programa","palabras","internacional","van","esas","segunda","empresa","puesto","ahí","propia","m","libro","igual","político","persona","últimos","ellas","total","creo","tengo","dios","c","española","condiciones","méxico","fuerza","solo","único","acción","amor","policía","puerta","pesar","zona","sabe","calle","interior","tampoco","música","ningún","vista","campo","buen","hubiera","saber","obras","razón","ex","niños","presencia","tema","dinero","comisión","antonio","servicio","hijo","última","ciento","estoy","hablar","dio","minutos","producción","camino","seis","quién","fondo","dirección","papel","demás","barcelona","idea","especial","diferentes","dado","base","capital","ambos","europa","libertad","relaciones","espacio","medios","ir","actual","población","empresas","estudio","salud","servicios","haya","principio","siendo","cultura","anterior","alto","media","mediante","primeros","arte","paz","sector","imagen","medida","deben","datos","consejo","personal","interés","julio","grupos","miembros","ninguna","existe","cara","edad","etc","movimiento","visto","llegó","puntos","actividad","bueno","uso","niño","difícil","joven","futuro","aquellos","mes","pronto","soy","hacía","nuevos","nuestros","estaban","posibilidad","sigue","cerca","resultados","educación","atención","gonzález","capacidad","efecto","necesario","valor","aire","investigación","siguiente","figura","central","comunidad","necesidad","serie","organización","nuevas","calidad","economía","carácter","jefe","estamos","prensa","control","sociales","universidad","militar","cabo","diez","fuerzas","congreso","ésta","hijos","justicia","mundial","dólares","juego","económica","políticos","duda","recursos","pública","crisis","próximo","tenemos","decisión","varias","popular","tenido","apenas","época","banco","presente","menor","quiero","pasar","resultado","televisión","encuentra","gracias","ministerio","conjunto","defensa","alguien","queda","hacen","pasa","resto","causa","seguir","allá","intento","voy","cuya","vamos","mar","estudios","derechos","importancia","cuales","contrario","manuel","garcía","fuerte","sol","jóvenes","apoyo","habría","civil","miguel","pedro","partidos","libre","fuentes","administración","común","dejar","cine","salir","comunicación","b","experiencia","demasiado","plan","respuesta","energía","izquierda","función","principal","superior","naturaleza","podemos","unión","especialmente","rey","domingo","favor","cantidad","elecciones","clase","productos","españoles","conocer","teatro","importantes","evitar","color","actividades","mesa","p","decía","cuyo","debido","alta","francisco","secretario","objeto","quizá","posición","parecía","natural","elementos","hubo","objetivo","formas","única","pueda","origen","blanco","mismos","lleva","económico","opinión","ayuda","oficial","silencio","buenos","pensar","república","dónde","sangre","encuentro","siquiera","autor","reunión","haciendo","suelo","muestra","viejo","encima","resulta","tomar","bastante","siete","lucha","pudo","amigos","línea","sur","pocos","medidas","norte","partes","iglesia","tratamiento","existencia","cargo","grande","américa","boca","plaza","pie","trabajadores","poner","existen","viene","permite","análisis","argentina","acto","hechos","tiempos","políticas","radio","puedo","crecimiento","francia","compañía","amigo","autoridades","realizar","acciones","padres","diario","ve","derecha","ambiente","i","habrá","precisamente","enfermedad","especie","ejército","santa","cambios","río","sabía","seguro","espera","momentos","viaje","quería","ocho","vivir","región","formación","escuela","cuarto","valores","quedó","participación","éxito","baja","artículo","principales","fernando","metros","marcha","régimen","consecuencia","conocimiento","corazón","campaña","estructura","efectos","finalmente","modelo","carta","construcción","médico","miedo","mayores","entrada","humanos","sean","actitud","deja","dejó","d","llevar","negro","texto","mitad","estuvo","alrededor","acerca","peso","humano","pequeño","fecha","serán","doctor","ideas","vino","materia","llega","carrera","cierta","sola","psoe","lejos","juez","características","riesgo","fácil","diferencia","cultural","libros","práctica","mayo","nuestras","programas","memoria","llegado","plazo","expresión","diciembre","mantener","enero","volver","cuadro","producto","produce","europea","conciencia","tenían","atrás","felipe","creación","chile","precio","película","puerto","fuego","cuestión","pasó","costa","supuesto","local","habla","aspectos","cuba","sala","cámara","vuelta","vía","mirada","mejores","informe","unidad","distintos","suerte","tales","mira","llamado","técnica","título","s","principios","octubre","volvió","período","g","encontrar","democracia","aumento","fútbol","prueba","consumo","pese","ocasiones","exterior","solución","u","hija","sueño","parís","capaz","ocasión","industria","adelante","salida","ciencia","asunto","asociación","puso","intereses","oro","podrá","pregunta","oposición","entrar","señora","señaló","santiago","dolor","zonas","comercio","operación","tribunal","instituciones","temas","militares","junio","marco","sectores","hacerlo","aspecto","razones","contenido","juicio","electoral","considera","tendrá","mucha","voluntad","dicen","recuerdo","socialista","área","aparece","vio","cama","aun","presenta","pp","revolución","busca","abril","rodríguez","fiscal","lópez","victoria","violencia","primeras","pequeña","armas","debía","ii","esfuerzo","humana","posibilidades","centros","profesional","asimismo","grado","has","toma","distintas","material","carne","llama","particular","jorge","trabajar","propuesta","muerto","precios","reforma","hermano","corte","comenzó","etapa","obstante","pone","diversos","visita","concepto","pacientes","semanas","tipos","solamente","deseo","sistemas","encuentran","siguientes","martín","suficiente","marzo","propios","jamás","dan","club","instituto","constitución","curso","lenguaje","estilo","rosa","imposible","pablo","buscar","peor","piel","arriba","generales","septiembre","blanca","r","aquellas","teoría","animales","hicieron","larga","perdido","imágenes","paciente","conseguir","máximo","noviembre","j","líder","hospital","diversas","rafael","vuelve","destino","torno","proyectos","flores","niveles","afirmó","explicó","n","somos","términos","premio","tercera"]
abecedario = set(string.ascii_lowercase)
jugar = True

def adivinar():
    while True:
        adivinar = input("Inserte el caracter para comprobar\n")
        if (len(adivinar) != 1):
            print("Inserte un solo caracter")
        elif (adivinar not in abecedario):
            print("Inserte un caracter")
        elif (adivinar in caracter_acertado):
            print("Ya ha acertado ese caracter")
        else:
            return adivinar.lower()

while(jugar):
    finalizar = False
    vidas = 7
    # Falta filtra lista_palabras
    palabra_ha_adivinar = random.choice(lista_palabras)
    palabra_vista = '_' * len(palabra_ha_adivinar) 
    caracter_erroneo = ''
    caracter_acertado = ''
    print(f"{palabra_ha_adivinar}")

    while not finalizar:
        print(f"{vidas_diccionario_visual[int(vidas)]}\n{' '.join(palabra_vista)}\nCaracteres acertados - {caracter_acertado}\nCaracteres erroneos - {caracter_erroneo}\nLe quedan {vidas} vidas")

        if(vidas == 0):
            print(f"Una pena, has perdido, la palabra era {palabra_ha_adivinar}")

        caracter_usuario = adivinar()
                
        if (caracter_usuario in palabra_ha_adivinar): 
            caracter_acertado += caracter_usuario
            palabra_vista = [letra if letra in caracter_acertado else '-' for letra in palabra_ha_adivinar]
        else:
            caracter_erroneo += caracter_usuario
            vidas -= 1

        if (''.join(palabra_vista) == palabra_ha_adivinar):
            print("FELICIDADES HAS GANADO")
            finalizar = True

    if (input("Desea seguir jugando? [si], no cualquier otra letra").lower() != 'si'):
        jugar = False