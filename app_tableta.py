"""
Aplicación Web de Entrenamiento de Voleibol
Optimizada para tabletas (Android, iOS, Windows)
"""

from flask import Flask, render_template, jsonify, request, make_response
from datetime import datetime
import random

app = Flask(__name__)

# Base de datos de ejercicios
EJERCICIOS_DB = {
    'Preparación General': {
        'calentamiento': [
            'Trote suave alrededor de la cancha (5 min)',
            'Movilidad articular completa',
            'Estiramientos dinámicos',
            'Juego de atrapar en parejas',
            'Caminata lateral con brazos',
            'Saltos ligeros en el lugar',
            'Giros de cintura con brazos extendidos',
            'Círculos de brazos hacia adelante y atrás',
            'Desplazamientos laterales suaves'
        ],
        'tecnica_basica': [
            'Posición básica y desplazamientos',
            'Golpe de antebrazos contra la pared',
            'Golpe de dedos en parejas',
            'Saques de abajo',
            'Recepción básica',
            'Posición de defensa (en "V" o lista)',
            'Movimientos de brazos con balón',
            'Práctica de contacto suave con pelota',
            'Pase de dedos individual contra pared',
            'Coordinación de brazos y piernas',
            'Toque de antebrazos contra pared',
            'Control del balón en el aire'
        ],
        'juegos_grupos': [
            'Pase 10: mantener el balón sin que caiga',
            'Carrera de relevos con balón',
            'Círculo de pases (grupos de 5-6)',
            'Mini voleibol (3 vs 3)',
            'Pases en parejas en movimiento',
            'Juego del espejo: copiar movimientos',
            'Carreras con cambios de dirección',
            'Relevos de velocidad',
            'Juego de los números',
            'Pases en triángulo',
            'Competencia de precisión de pases',
            'Juego modificado con 4 vs 4',
            'Voleibol de cancha reducida'
        ],
        'coordinacion_habilidades': [
            'Saltos alternados con brazos',
            'Equilibrio en una pierna',
            'Desplazamientos en línea recta',
            'Carreras de espalda',
            'Saltos laterales (lado a lado)',
            'Coordinación ojo-mano con balón',
            'Pases mientras se camina',
            'Lanzamientos y recepciones',
            'Ejercicios de agilidad con conos',
            'Trabajo de footwork básico',
            'Cambios rápidos de dirección'
        ],
        'acondicionamiento': [
            'Sentadillas (3x10)',
            'Planchas (3x15-20 seg)',
            'Saltos (3x10)',
            'Abdominales (3x12)',
            'Flexiones modificadas (de rodillas)',
            'Levantamiento de piernas acostadas',
            'Puentes glúteos',
            'Patadas hacia atrás',
            'Ejercicios de equilibrio',
            'Trabajo de core ligero',
            'Estiramientos finales personalizados'
        ]
    },
    'Preparación Específica': {
        'calentamiento': [
            'Trote con cambios de dirección',
            'Desplazamientos defensivos',
            'Pases en movimiento',
            'Saltos de activación',
            'Agilidad con cambios rápidos',
            'Calentamiento específico por posición',
            'Simulación de movimientos de juego'
        ],
        'tecnica_avanzada': [
            'Remate desde zona 4',
            'Bloqueo individual y en parejas',
            'Saques de arriba',
            'Recepción en formación W',
            'Colocación desde zona 3',
            'Recepción con desplazamiento',
            'Remate en salto progresivo',
            'Defensa baja en movimiento',
            'Coordinación recepción-ataque'
        ],
        'trabajo_grupal': [
            'Rotaciones y posiciones',
            'Cadena: recepción-colocación-remate',
            'Bloqueo-defensa-contraataque',
            'Juego dirigido 6 vs 6',
            'Práctica de sistemas de juego',
            'Coordinación entre posiciones',
            'Situaciones de juego real'
        ],
        'acondicionamiento': [
            'Saltos al cajón (3x8)',
            'Burpees (3x10)',
            'Desplazamientos (30s x3)',
            'Core: planchas laterales',
            'Saltos explosivos',
            'Trabajo de velocidad',
            'Resistencia muscular específica'
        ]
    },
    'Precompetitiva': {
        'calentamiento': [
            'Activación cardiovascular intensa',
            'Desplazamientos específicos',
            'Pases en triángulo',
            'Saltos y bloqueos',
            'Simulación de situaciones competitivas',
            'Calentamiento enfocado en técnica'
        ],
        'tactica_equipo': [
            'Sistemas de recepción 3-1-2 / 3-2-1',
            'Sistemas ofensivos 4-2 / 5-1',
            'Jugadas ensayadas',
            'Cobertura de bloqueo',
            'Transiciones defensa-ataque',
            'Temas defensivos específicos',
            'Estrategias de ataque'
        ],
        'simulacion': [
            'Set completo 6 vs 6',
            'Situaciones de presión',
            'Práctica de rotaciones',
            'Estrategias vs formaciones',
            'Simulaciones de partidos',
            'Análisis de errores'
        ],
        'acondicionamiento': [
            'Intervalos alta intensidad',
            'Circuito de potencia',
            'Saltos explosivos',
            'Recuperación activa',
            'Trabajo específico de resistencia'
        ]
    },
    'Competitiva': {
        'calentamiento': [
            'Rutina de precompetencia',
            'Activación neuromuscular',
            'Práctica de remate y saque',
            'Mentalización',
            'Movimientos dinámicos'
        ],
        'mantenimiento': [
            'Repaso de jugadas clave',
            'Ajustes tácticos',
            'Situaciones críticas',
            'Trabajo por posición',
            'Set de práctica corto',
            'Correcciones técnicas'
        ],
        'estrategia': [
            'Análisis del rival',
            'Comunicación en cancha',
            'Rotaciones optimizadas',
            'Gestión de sustituciones',
            'Tácticas especiales'
        ],
        'recuperacion': [
            'Estiramientos prolongados',
            'Trabajo de movilidad',
            'Ejercicios de descarga',
            'Hidratación',
            'Enfoque mental'
        ]
    },
    'Transición': {
        'calentamiento': [
            'Actividad recreativa',
            'Juegos lúdicos',
            'Movilidad relajada',
            'Ejercicios de bajo impacto'
        ],
        'recreativo': [
            'Vóley playa',
            'Juegos modificados',
            'Actividades multideportivas',
            'Competencias divertidas',
            'Juegos de coordinación',
            'Actividades en grupo'
        ],
        'recuperacion_activa': [
            'Yoga para atletas',
            'Natación',
            'Trote suave',
            'Estiramientos',
            'Juegos de coordinación',
            'Actividad lúdica',
            'Movilidad con ejercicios'
        ],
        'evaluacion': [
            'Reflexión sobre temporada',
            'Evaluación de progreso',
            'Metas personales',
            'Feedback grupal',
            'Planificación futura'
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

# Entrenamientos de 6 minutos (cambio cada 3 minutos)
# Estructura progresiva: Inicio (individual) -> Desarrollo (parejas/trios) -> Final (grupos)
ENTRENAMIENTOS_6_MINUTOS = {
    'Preparación General': {
        'sesion_1': {
            'nombre': 'Toque y Control Progresivo',
            'inicio': {
                'duracion': '3 min',
                'tipo': 'Individual',
                'ejercicios': [
                    'Toque de dedos contra pared',
                    'Toques rápidos de antebrazos en pared'
                ]
            },
            'desarrollo': {
                'duracion': '3 min',
                'tipo': 'Parejas/Tríos',
                'ejercicios': [
                    'Toques continuos en parejas',
                    'Pase en triángulo (tríos)'
                ]
            },
            'final': {
                'duracion': '3 min (extra recomendado)',
                'tipo': 'Grupos (trabajo en equipo)',
                'ejercicios': [
                    'Círculo de pases en grupo',
                    'Mini juego de control colectivo'
                ]
            }
        },
        'sesion_2': {
            'nombre': 'Recepción Progresiva',
            'inicio': {
                'duracion': '3 min',
                'tipo': 'Individual',
                'ejercicios': [
                    'Recepción individual contra pared',
                    'Desplazamiento reactivo con balón'
                ]
            },
            'desarrollo': {
                'duracion': '3 min',
                'tipo': 'Parejas/Tríos',
                'ejercicios': [
                    'Recepción y pase en parejas',
                    'Recepción en triángulo'
                ]
            },
            'final': {
                'duracion': '3 min (extra recomendado)',
                'tipo': 'Grupos (trabajo en equipo)',
                'ejercicios': [
                    'Cadena recepción-colocación-remate',
                    'Mini voleibol 3 vs 3'
                ]
            }
        },
        'sesion_3': {
            'nombre': 'Saque y Precisión',
            'inicio': {
                'duracion': '3 min',
                'tipo': 'Individual',
                'ejercicios': [
                    'Saque objetivo individual por zonas',
                    'Control de gesto de saque'
                ]
            },
            'desarrollo': {
                'duracion': '3 min',
                'tipo': 'Parejas/Tríos',
                'ejercicios': [
                    'Saque y recepción en parejas',
                    'Reto de precisión en tríos'
                ]
            },
            'final': {
                'duracion': '3 min (extra recomendado)',
                'tipo': 'Grupos (trabajo en equipo)',
                'ejercicios': [
                    'Competencia de saques por equipos',
                    'Juego dirigido con inicio por saque'
                ]
            }
        }
    },
    'Preparación Específica': {
        'sesion_1': {
            'nombre': 'Defensa Progresiva',
            'inicio': {
                'duracion': '3 min',
                'tipo': 'Individual',
                'ejercicios': [
                    'Postura defensiva y desplazamiento',
                    'Defensa de balón lanzado individual'
                ]
            },
            'desarrollo': {
                'duracion': '3 min',
                'tipo': 'Parejas/Tríos',
                'ejercicios': [
                    'Defensa y pase en parejas',
                    'Cobertura defensiva en tríos'
                ]
            },
            'final': {
                'duracion': '3 min (extra recomendado)',
                'tipo': 'Grupos (trabajo en equipo)',
                'ejercicios': [
                    'Defensa en cadena por equipo',
                    'Juego 6 vs 6 con foco defensivo'
                ]
            }
        },
        'sesion_2': {
            'nombre': 'Bloqueo y Cobertura',
            'inicio': {
                'duracion': '3 min',
                'tipo': 'Individual',
                'ejercicios': [
                    'Saltos de bloqueo individual',
                    'Timing de manos en red'
                ]
            },
            'desarrollo': {
                'duracion': '3 min',
                'tipo': 'Parejas/Tríos',
                'ejercicios': [
                    'Bloqueo en parejas',
                    'Bloqueo + cobertura en tríos'
                ]
            },
            'final': {
                'duracion': '3 min (extra recomendado)',
                'tipo': 'Grupos (trabajo en equipo)',
                'ejercicios': [
                    'Bloqueo-defensa-contraataque por equipo',
                    'Juego competitivo con puntos por bloqueo'
                ]
            }
        },
        'sesion_3': {
            'nombre': 'Remate Progresivo',
            'inicio': {
                'duracion': '3 min',
                'tipo': 'Individual',
                'ejercicios': [
                    'Aproximación y salto sin balón',
                    'Remate controlado con lanzamiento'
                ]
            },
            'desarrollo': {
                'duracion': '3 min',
                'tipo': 'Parejas/Tríos',
                'ejercicios': [
                    'Colocación-remate en parejas',
                    'Ataque en triángulo'
                ]
            },
            'final': {
                'duracion': '3 min (extra recomendado)',
                'tipo': 'Grupos (trabajo en equipo)',
                'ejercicios': [
                    'Secuencia completa por equipo',
                    'Juego 6 vs 6 con foco en ataque'
                ]
            }
        }
    },
    'Precompetitiva': {
        'sesion_1': {
            'nombre': 'Transiciones Rápidas',
            'inicio': {
                'duracion': '3 min',
                'tipo': 'Individual',
                'ejercicios': [
                    'Transición ataque-defensa individual',
                    'Lectura de balón y reacción'
                ]
            },
            'desarrollo': {
                'duracion': '3 min',
                'tipo': 'Parejas/Tríos',
                'ejercicios': [
                    'Transición en parejas',
                    'Rotación táctica en tríos'
                ]
            },
            'final': {
                'duracion': '3 min (extra recomendado)',
                'tipo': 'Grupos (trabajo en equipo)',
                'ejercicios': [
                    'Transiciones 6 vs 6',
                    'Situaciones de presión por equipos'
                ]
            }
        },
        'sesion_2': {
            'nombre': 'Sistemas de Juego',
            'inicio': {
                'duracion': '3 min',
                'tipo': 'Individual',
                'ejercicios': [
                    'Posicionamiento por rol',
                    'Desplazamiento táctico individual'
                ]
            },
            'desarrollo': {
                'duracion': '3 min',
                'tipo': 'Parejas/Tríos',
                'ejercicios': [
                    'Combinaciones tácticas en parejas',
                    'Cobertura táctica en tríos'
                ]
            },
            'final': {
                'duracion': '3 min (extra recomendado)',
                'tipo': 'Grupos (trabajo en equipo)',
                'ejercicios': [
                    'Sistema 4-2 / 5-1 en equipo',
                    'Set corto con consignas tácticas'
                ]
            }
        }
    },
    'Competitiva': {
        'sesion_1': {
            'nombre': 'Activación Competitiva',
            'inicio': {
                'duracion': '3 min',
                'tipo': 'Individual',
                'ejercicios': [
                    'Activación neuromuscular individual',
                    'Saque de precisión con objetivo'
                ]
            },
            'desarrollo': {
                'duracion': '3 min',
                'tipo': 'Parejas/Tríos',
                'ejercicios': [
                    'Recepción-ataque en parejas',
                    'Cobertura de ataque en tríos'
                ]
            },
            'final': {
                'duracion': '3 min (extra recomendado)',
                'tipo': 'Grupos (trabajo en equipo)',
                'ejercicios': [
                    'Juego competitivo por puntos',
                    'Cierre táctico de equipo'
                ]
            }
        }
    },
    'Transición': {
        'sesion_1': {
            'nombre': 'Reactivación Coordinativa',
            'inicio': {
                'duracion': '3 min',
                'tipo': 'Individual',
                'ejercicios': [
                    'Coordinación individual con balón',
                    'Movilidad activa con control'
                ]
            },
            'desarrollo': {
                'duracion': '3 min',
                'tipo': 'Parejas/Tríos',
                'ejercicios': [
                    'Pases recreativos en parejas',
                    'Reto técnico en tríos'
                ]
            },
            'final': {
                'duracion': '3 min (extra recomendado)',
                'tipo': 'Grupos (trabajo en equipo)',
                'ejercicios': [
                    'Juego cooperativo por equipos',
                    'Actividad lúdica grupal con balón'
                ]
            }
        }
    }
}

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/manifest.json')
def manifest():
    """Servir el manifest de la PWA con headers correctos"""
    response = make_response(app.send_static_file('manifest.json'))
    response.headers['Content-Type'] = 'application/manifest+json'
    response.headers['Cache-Control'] = 'no-cache'
    return response

@app.route('/sw.js')
def service_worker():
    """Servir el service worker con headers correctos"""
    response = make_response(app.send_static_file('js/sw.js'))
    response.headers['Content-Type'] = 'application/javascript'
    response.headers['Service-Worker-Allowed'] = '/'
    response.headers['Cache-Control'] = 'no-cache'
    return response

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
            # Adaptar ejercicios grupales para grupos pequeños
            ejercicios_adaptados = [f"{ej} (adaptar a grupo pequeño)" for ej in ejercicios[:3]]
        elif cantidad > 15 and 'parejas' in categoria.lower():
            # Adaptar ejercicios de parejas para grupos grandes
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

@app.route('/api/entrenamientos-6min')
def obtener_entrenamientos_6min():
    """Obtiene entrenamientos de 6 minutos con 3 momentos"""
    etapa = request.args.get('etapa')
    sesion = request.args.get('sesion')

    if not etapa:
        return jsonify({
            'resumen': {
                'duracion_base': '6 min',
                'cambio_cada': '3 min',
                'estructura': 'Inicio (individual) -> Desarrollo (parejas/trios) -> Final (grupos)',
                'nota': 'La fase final grupal se recomienda como bloque extra para reforzar el trabajo en equipo.'
            },
            'etapas': list(ENTRENAMIENTOS_6_MINUTOS.keys())
        })

    if etapa not in ENTRENAMIENTOS_6_MINUTOS:
        return jsonify({'error': 'Etapa no encontrada'}), 404

    sesiones_etapa = ENTRENAMIENTOS_6_MINUTOS[etapa]

    if not sesion:
        sesiones = [
            {'id': key, 'nombre': value['nombre']}
            for key, value in sesiones_etapa.items()
        ]
        return jsonify({
            'etapa': etapa,
            'duracion_base': '6 min',
            'cambio_cada': '3 min',
            'sesiones': sesiones
        })

    if sesion not in sesiones_etapa:
        return jsonify({'error': 'Sesión no encontrada para la etapa seleccionada'}), 404

    return jsonify({
        'etapa': etapa,
        'sesion_id': sesion,
        'duracion_base': '6 min',
        'cambio_cada': '3 min',
        'refuerzo_equipo': '3 min extra recomendados en fase final',
        'sesion': sesiones_etapa[sesion]
    })

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

if __name__ == '__main__':
    import socket
    
    # Obtener IP local
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except:
        local_ip = "localhost"
    
    print("=" * 70)
    print("🏐 ENTRENA VOLEIBOL WH")
    print("=" * 70)
    print()
    print("✅ Servidor HTTP iniciado correctamente")
    print()
    print("📱 USO CON NGROK (RECOMENDADO):")
    print("=" * 70)
    print()
    print("   1. Abre otra terminal y ejecuta:")
    print("      cd C:\\ngrok")
    print("      .\\ngrok.exe http 5000")
    print()
    print("   2. Ngrok te dará una URL como:")
    print("      https://abc123.ngrok-free.app")
    print()
    print("   3. Abre esa URL en tu tableta")
    print("      ✅ Chrome reconocerá la app como instalable")
    print("      ✅ Aparecerá 'Instalar app'")
    print()
    print("💡 ACCESO LOCAL (sin ngrok):")
    print(f"   http://{local_ip}:5000")
    print("   (Solo para probar, no permite instalación)")
    print()
    print("=" * 70)
    print()
    
    # Iniciar servidor HTTP (ngrok maneja el HTTPS)
    app.run(
        host='0.0.0.0', 
        port=5000, 
        debug=True
    )
