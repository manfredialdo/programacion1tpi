# el desafio de los gutierrez
# progrmaacion1 utn tup
# trabajo pracitco integrador version02
# datos avanzados, arboles de decision
# aldo manfredi // bruno pighin
"""
La familia gutierrez, como muchas en Argentina, enfrenta diariamente el desafío
de dudar sobre su alimentación en un contexto de alta inflación, y recursos
limitados. Cada mañana, se encuentran ante una serie de decisiones dificiles que
determinarán si podrán poner algo en la mesa ese día.
No hay un camino fácil, y cada elección tiene consecuencias directas en su bienestar.
Nos piden, una forma de simular estas complejas decisiones para entender las posibles
trayectorias y desenlaces, así como los factores que influyen en su situación.
Esto es solo una simulacion del dia a dia de la familia.
"""
import random

# Árbol binario
import random

# Árbol binario
manual_cesta_basica = [
    "¿Queda plata en la billetera?",
    [
        "¿Hay alguna oferta o descuento en el super de la esquina?",
        [
            "¿podre comprar algo esencial (pan y/o leche y/o arroz)?",
            [
                "¿Podemos al menos conseguir algun producto de segunda marca?",
                [
                    "¿hay espacio para guardar varios duas?",
                    [
                        "¿Podemos compartir con otro hogar cercano?",
                        "¡Solidaridad doble! Hoy comemos y ayudamos a otros.", # 'solidaridad'
                        "¡Aseguramos provisiones, pero solo para casa!"       # 'provisiones'
                    ],
                    "¡Compramos lo justo! No hay lugar para almacenar más." # 'compramos lo justo'
                ],
                "¡Sobrevivimos hoy, pero mañana será otro desafío."       # 'sobevivimos' (corregida la tilde, coincide)
            ],
            "El descuento no alcanza, ¡solo podemos comprar lo barato!" # No hay una clave directa, pero podemos ver si una palabra común sirve.
        ],
        [
            "¿Podemos pedir fiado en la verdulería?",
            [
                "¿El verdulero ya nos ha fiado esta semana?",
                "¡Al limite de la confianza, pero hoy se come, gracias al fiado!", # 'fiado'
                "¡Gracias a la confianza del barrio, salvamos el día con el fiado!" # 'fiado'
            ],
            "¡**GRAVE**: No hay ofertas, no alcanza ni fiado, ni piedad, ni opción para hoy." # 'grave'
        ]
    ],
    [
        "¿Queda algo de comida de anda saber cuando en esa heladera casi vacia?",
        [
            "¿Se puede repartir entre todos aunque sea poco?",
            [
                "¿Algun vecino puede aportar algo a la olla?",
                "¡Comunidad unida! Hoy comemos todos.", # 'comemos todos'
                "¡Comemos poco, pero comemos juntos!"  # 'comemos juntos'
            ],
            "¡**CRÍTICO**: No alcanza, algunos pasarán hambre hoy." # 'crítico'
        ],
        [
            "¿Hay comedor comunitario cerca?",
            [
                "¿Esta abierto hoy, hay lugar?",
                "¡Recibimos la ayuda vital del comedor, pero quedamos hambrientos!", # 'ayuda vital'
                "Ya no queda ni las migas.. El comedor esta saturado, preferimos dormir vacios intentaremos mañana." # 'saturado'
            ],
            "¡**DESASTRE TOTAL**: No hay comida, dinero ni ayuda visible." # 'desastre'
        ]
    ]
]

# Diccionario de "menus del día" (sin cambios, ya que ajustamos los textos del árbol)
menu_del_dia = {
    "solidaridad": "asado con amigos y mate compartido",
    "provisiones": "guiso de lentejas y pan casero",
    "compramos lo justo": "fideos con manteca",
    "sobevivimos": "te con leche tibia y galletitas de agua",
    "fiado": "sopa improvisada con una alita de pollo que sobro de hace dos dias",
    "grave": "café negro y sin azucar... hay que agradecer?",
    "crítico": "un vaso de agua y una mirada al cielo",
    "desastre": "nos miramos las caras y nos vamos a dormir... gracias",
    "comemos todos": "arroz con aceite y un cuarto de choripan para cada uno... gracias",
    "comemos juntos": "pan con manteca compartido, un fiasco!",
    "ayuda vital": "una bolsita chiquita tipo vianda comunitaria caliente",
    "saturado": "mate cocido frio con pan duro"
}
def obtener_menu(resultado_final):
    # busca palabras clave en el resultado final del arbol para sugerir un 
    # menu del dia.
    texto = resultado_final.lower()
    for clave, menu in menu_del_dia.items():
        if clave in texto:
            return menu
    return "lo que tengo no alcanza.. hoy: nada... por ahora."

def evaluar_arbol(arbol, decidir, historial=None):
    # recorre recursivamente el arbol de decisiones, tomando y registrando 
    # cada decisión.
    if historial is None:
        historial = []

    if isinstance(arbol, str):
        historial.append(("RESULTADO", arbol))
        return historial

#    if not isinstance(arbol, list) or len(arbol) != 3:
#        raise ValueError("Estructura del árbol inválida. Debe ser [pregunta, rama_si, rama_no].")

    pregunta, rama_si, rama_no = arbol
    decision = decidir(pregunta)
    historial.append((pregunta, "sí" if decision else "no"))

    siguiente_rama = rama_si if decision else rama_no
    return evaluar_arbol(siguiente_rama, decidir, historial)

def respuestas_aleatorias(pregunta):
    # simula un "sí" o "no" al azar para cada pregunta del arbol.
    respuesta = random.choice([True, False])
    print("\n" + pregunta)
    print("Respuesta aleatoria:", "sí" if respuesta else "no")
    return respuesta

def imprimir_historial(historial):
    # muestra la secuencia de decisiones tomadas y el menú final determinado.
    print("\n=== Decisiones tomadas ===")
    resultado_final = ""
    for paso in historial:
        if paso[0] == "RESULTADO":
            resultado_final = paso[1]
        else:
            print(f"{paso[0]} → {paso[1]}")

    print(f"\nResultado final: {resultado_final}")
    menu = obtener_menu(resultado_final)
    print(f"Menu del dia: hoy {menu}.")


def inicio():
    # Principal. Ejecutar simulación
    print("=== Simulacion aleatoria con menu del dia ===")
    historial = evaluar_arbol(manual_cesta_basica, respuestas_aleatorias)
    imprimir_historial(historial)


inicio()
