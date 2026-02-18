"""
Aplicación de Entrenamiento de Voleibol - Versión Standalone
Aplicación independiente que NO requiere navegador web externo
"""

import webview
import threading
from flask import Flask, render_template, jsonify, request
from datetime import datetime
import sys
import os

# Configuración para PyInstaller
if getattr(sys, 'frozen', False):
    # Si está ejecutándose como .exe
    bundle_dir = sys._MEIPASS
else:
    # Si está ejecutándose como .py
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

# Crear aplicación Flask
app = Flask(__name__, 
            template_folder=os.path.join(bundle_dir, 'templates'),
            static_folder=os.path.join(bundle_dir, 'static'))

# Base de datos de ejercicios
EJERCICIOS_DB = {
    'Preparación General': {
        'calentamiento': [
            'Trote suave alrededor de la cancha (5 min)',
            'Movilidad articular: círculos de brazos, rodillas, tobillos',
            'Estiramientos dinámicos',
            'Juego de atrapar (parejas)'
        ],
        'tecnica_basica': [
            'Posición básica y desplazamientos',
            'Golpe de antebrazos contra la pared',
            'Golpe de dedos en parejas',
            'Saques de abajo',
            'Recepción básica en parejas'
        ],
        'juegos_grupos': [
            'Pase 10: mantener el balón sin que caiga (grupos de 3-4)',
            'Carrera de relevos con balón',
            'Círculo de pases (grupos de 5-6)',
            'Mini voleibol (toda la cancha, equipos flexibles)'
        ],
        'acondicionamiento': [
            'Sentadillas (3 series de 10)',
            'Planchas (3 series de 15-20 seg)',
            'Saltos en el lugar (3 series de 10)',
            'Abdominales (3 series de 12)'
        ]
    },
    'Preparación Específica': {
        'calentamiento': [
            'Trote con cambios de dirección (5 min)',
            'Desplazamientos laterales y defensivos',
            'Pases en movimiento (parejas)',
            'Saltos de calentamiento'
        ],
        'tecnica_avanzada': [
            'Remate desde zona 4 (con lanzamiento)',
            'Bloqueo individual y en parejas',
            'Saques de arriba',
            'Recepción en formación W',
            'Colocación desde zona 3',
            'Defensa de campo con desplazamientos'
        ],
        'trabajo_grupal': [
            'Rotaciones y posiciones (equipos de 6)',
            'Cadena: recepción-colocación-remate (grupos de 4-5)',
            'Bloqueo-defensa-contraataque (grupos de 6)',
            'Juego dirigido 4 vs 4 o 6 vs 6'
        ],
        'acondicionamiento': [
            'Saltos al cajón (3 series de 8)',
            'Burpees (3 series de 10)',
            'Desplazamientos defensivos (30 seg x 3)',
            'Core: planchas laterales (30 seg cada lado)'
        ]
    },
    'Precompetitiva': {
        'calentamiento': [
            'Activación cardiovascular intensa (7 min)',
            'Desplazamientos específicos de voleibol',
            'Pases en triángulo con movimiento',
            'Saltos y bloqueos de activación'
        ],
        'tactica_equipo': [
            'Sistemas de recepción 3-1-2 / 3-2-1',
            'Sistemas ofensivos 4-2 / 5-1',
            'Jugadas ensayadas de remate',
            'Cobertura de bloqueo y ataque',
            'Transiciones defensa-ataque',
            'Situaciones de juego específicas'
        ],
        'simulacion': [
            'Set completo de práctica 6 vs 6',
            'Situaciones de presión (punto de oro)',
            'Práctica de rotaciones en juego real',
            'Estrategias contra diferentes formaciones'
        ],
        'acondicionamiento': [
            'Intervalos de alta intensidad (10 min)',
            'Circuito de potencia (4 estaciones)',
            'Saltos explosivos (4 series de 6)',
            'Recuperación activa'
        ]
    },
    'Competitiva': {
        'calentamiento': [
            'Rutina de precompetencia (10 min)',
            'Activación neuromuscular',
            'Práctica de remate y saque',
            'Mentalización y concentración'
        ],
        'mantenimiento': [
            'Repaso de jugadas clave del equipo',
            'Ajustes tácticos según rival',
            'Práctica de situaciones críticas',
            'Trabajo específico por posición',
            'Set de práctica corto (15 puntos)'
        ],
        'estrategia': [
            'Análisis del rival y ajustes',
            'Comunicación en cancha',
            'Rotaciones optimizadas',
            'Gestión de tiempo y sustituciones'
        ],
        'recuperacion': [
            'Estiramientos prolongados (15 min)',
            'Trabajo de movilidad',
            'Ejercicios de descarga',
            'Hidratación y nutrición'
        ]
    },
    'Transición': {
        'calentamiento': [
            'Actividad recreativa con balón (10 min)',
            'Juegos lúdicos grupales',
            'Movilidad general relajada'
        ],
        'recreativo': [
            'Vóley playa o en pasto',
            'Juegos modificados de voleibol',
            'Actividades multideportivas',
            'Competencias por equipos divertidas',
            'Circuitos recreativos con balón'
        ],
        'recuperacion_activa': [
            'Yoga para atletas (20 min)',
            'Natación o actividad acuática',
            'Caminata o trote suave',
            'Estiramientos y flexibilidad',
            'Juegos de coordinación'
        ],
        'evaluacion': [
            'Reflexión sobre la temporada',
            'Evaluación individual de progreso',
            'Establecimiento de metas personales',
            'Feedback grupal'
        ]
    }
}

# Ejercicios por fundamento
EJERCICIOS_FUNDAMENTOS = {
    'saque': [
        'Saques de abajo (principiantes)',
        'Saques de arriba tipo tenis',
        'Saques flotadores',
        'Saques en salto (avanzado)',
        'Práctica de precisión en zonas',
        'Saques bajo presión con cronómetro'
    ],
    'recepcion': [
        'Recepción de saque en parejas',
        'Formación en W',
        'Formación 3-2-1',
        'Recepción con desplazamiento',
        'Pase a zona de colocación',
        'Recepción en situación de juego'
    ],
    'armado': [
        'Golpe de dedos contra pared',
        'Colocación en parejas',
        'Colocaciones desde zona 3 a todas las zonas',
        'Colocación en movimiento',
        'Levantada de segunda intención',
        'Colocación bajo presión'
    ],
    'ataque': [
        'Aproximación y salto sin balón',
        'Remate con balón lanzado',
        'Remate desde zona 4',
        'Remate desde zona 2',
        'Remate con colocación',
        'Ataque en situación de juego'
    ],
    'bloqueo': [
        'Bloqueo individual',
        'Bloqueo en parejas',
        'Bloqueo triple',
        'Desplazamiento y bloqueo',
        'Lectura del rematador',
        'Bloqueo en situación de juego'
    ],
    'defensa': [
        'Posición defensiva básica',
        'Defensa de remates bajos',
        'Defensa con desplazamiento',
        'Cobertura de ataque',
        'Defensa en sistema 2-1-3',
        'Transición defensa-ataque'
    ]
}

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/manifest.json')
def manifest():
    """Servir el manifest de la PWA"""
    return app.send_static_file('manifest.json')

@app.route('/api/generar-plan', methods=['POST'])
def generar_plan():
    """Genera un plan de entrenamiento personalizado"""
    data = request.json
    
    edad = data.get('edad')
    cantidad = int(data.get('cantidad', 0))
    etapa = data.get('etapa')
    fundamento = data.get('fundamento')
    tiempo = int(data.get('tiempo', 90))
    
    plan = {
        'fecha': datetime.now().strftime('%d/%m/%Y %H:%M'),
        'parametros': {
            'edad': edad,
            'cantidad': cantidad,
            'etapa': etapa,
            'fundamento': fundamento,
            'tiempo': tiempo
        },
        'secciones': []
    }
    
    # Obtener ejercicios de la etapa
    ejercicios_etapa = EJERCICIOS_DB.get(etapa, {})
    
    # Si se seleccionó un fundamento específico
    if fundamento and fundamento != 'todos':
        ejercicios_fundamento = EJERCICIOS_FUNDAMENTOS.get(fundamento, [])
        if ejercicios_fundamento:
            plan['secciones'].append({
                'nombre': f'Fundamento: {fundamento.title()}',
                'duracion': '20-30 min',
                'ejercicios': ejercicios_fundamento
            })
    
    # Agregar secciones de la etapa
    for categoria, ejercicios in ejercicios_etapa.items():
        # Seleccionar ejercicios según cantidad de jugadoras
        if cantidad <= 6 and 'grupal' in categoria.lower():
            ejercicios_adaptados = [f"{ej} (adaptar a grupo pequeño)" for ej in ejercicios[:3]]
        elif cantidad > 15 and 'parejas' in categoria.lower():
            ejercicios_adaptados = [f"{ej} (múltiples parejas simultáneas)" for ej in ejercicios[:3]]
        else:
            ejercicios_adaptados = ejercicios
        
        # Calcular duración estimada
        if 'calentamiento' in categoria.lower():
            duracion = '10-15 min'
        elif 'acondicionamiento' in categoria.lower():
            duracion = '15-20 min'
        else:
            duracion = '25-30 min'
        
        plan['secciones'].append({
            'nombre': categoria.replace('_', ' ').title(),
            'duracion': duracion,
            'ejercicios': ejercicios_adaptados
        })
    
    # Agregar recomendaciones
    plan['recomendaciones'] = generar_recomendaciones(edad, cantidad, etapa)
    
    return jsonify(plan)

@app.route('/api/ejercicios/<etapa>')
def obtener_ejercicios(etapa):
    """Obtiene todos los ejercicios de una etapa"""
    ejercicios = EJERCICIOS_DB.get(etapa, {})
    return jsonify(ejercicios)

@app.route('/api/fundamentos')
def obtener_fundamentos():
    """Obtiene la lista de fundamentos disponibles"""
    return jsonify(list(EJERCICIOS_FUNDAMENTOS.keys()))

def generar_recomendaciones(edad, cantidad, etapa):
    """Genera recomendaciones basadas en los parámetros"""
    recomendaciones = []
    
    if cantidad > 15:
        recomendaciones.append('⚠️ Considere tener un asistente para manejar grupos grandes')
        recomendaciones.append('💡 Organice por estaciones para mejor aprovechamiento')
    
    if cantidad < 6:
        recomendaciones.append('💡 Aproveche el grupo pequeño para trabajo técnico detallado')
    
    if edad == '8-10':
        recomendaciones.append('🎮 Mantenga ejercicios divertidos y variados para esta edad')
        recomendaciones.append('⏱️ Sesiones más cortas, alta rotación de actividades')
    
    if edad == '14-16' or edad == '17+':
        recomendaciones.append('💪 Incluir trabajo de fuerza y prevención de lesiones')
    
    if etapa == 'Competitiva':
        recomendaciones.append('🏆 Enfóquese en la recuperación entre entrenamientos')
        recomendaciones.append('⚕️ Monitoree fatiga y prevención de lesiones')
    
    if etapa == 'Transición':
        recomendaciones.append('😊 Priorice el aspecto recreativo y la diversión')
        recomendaciones.append('🧠 Oportunidad para trabajar aspectos mentales del equipo')
    
    if etapa == 'Preparación General':
        recomendaciones.append('📚 Enfoque en fundamentos y bases técnicas')
        recomendaciones.append('🔄 Variedad de ejercicios para desarrollo integral')
    
    return recomendaciones

def iniciar_servidor():
    """Inicia el servidor Flask en un hilo separado"""
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)

def main():
    """Función principal para iniciar la aplicación"""
    # Iniciar servidor Flask en un hilo separado
    server_thread = threading.Thread(target=iniciar_servidor, daemon=True)
    server_thread.start()
    
    # Esperar un momento para que el servidor inicie
    import time
    time.sleep(1)
    
    # Configurar y crear la ventana de la aplicación
    window = webview.create_window(
        title='🏐 Entrenamiento de Voleibol',
        url='http://127.0.0.1:5000',
        width=1400,
        height=900,
        resizable=True,
        fullscreen=False,
        min_size=(800, 600)
    )
    
    # Iniciar la aplicación de escritorio
    webview.start()

if __name__ == '__main__':
    main()
