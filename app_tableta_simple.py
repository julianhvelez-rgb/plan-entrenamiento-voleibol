"""
Aplicación Web Simplificada de Entrenamiento de Voleibol
Optimizada para tabletas (Android, iOS, Windows)
"""

from flask import Flask, jsonify, request
from datetime import datetime
import json
import os

app = Flask(__name__)

# Logging simplificado
def log_request(path, method, status_code):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {method} {path} -> {status_code}")
    sys.stdout.flush()

import sys

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
            'Saltos de activación'
        ],
        'tecnica_avanzada': [
            'Remate desde zona 4',
            'Bloqueo individual y en parejas',
            'Saques de arriba',
            'Recepción en formación W',
            'Colocación desde zona 3'
        ],
        'trabajo_grupal': [
            'Rotaciones y posiciones',
            'Cadena: recepción-colocación-remate',
            'Bloqueo-defensa-contraataque',
            'Juego dirigido 6 vs 6'
        ],
        'acondicionamiento': [
            'Saltos al cajón (3x8)',
            'Burpees (3x10)',
            'Desplazamientos (30s x3)',
            'Core: planchas laterales'
        ]
    },
    'Precompetitiva': {
        'calentamiento': [
            'Activación cardiovascular intensa',
            'Desplazamientos específicos',
            'Pases en triángulo',
            'Saltos y bloqueos'
        ],
        'tactica_equipo': [
            'Sistemas de recepción 3-1-2 / 3-2-1',
            'Sistemas ofensivos 4-2 / 5-1',
            'Jugadas ensayadas',
            'Cobertura de bloqueo',
            'Transiciones defensa-ataque'
        ],
        'simulacion': [
            'Set completo 6 vs 6',
            'Situaciones de presión',
            'Práctica de rotaciones',
            'Estrategias vs formaciones'
        ],
        'acondicionamiento': [
            'Intervalos alta intensidad',
            'Circuito de potencia',
            'Saltos explosivos',
            'Recuperación activa'
        ]
    },
    'Competitiva': {
        'calentamiento': [
            'Rutina de precompetencia',
            'Activación neuromuscular',
            'Práctica de remate y saque',
            'Mentalización'
        ],
        'mantenimiento': [
            'Repaso de jugadas clave',
            'Ajustes tácticos',
            'Situaciones críticas',
            'Trabajo por posición'
        ],
        'estrategia': [
            'Análisis del rival',
            'Comunicación en cancha',
            'Rotaciones optimizadas',
            'Gestión de sustituciones'
        ],
        'recuperacion': [
            'Estiramientos prolongados',
            'Trabajo de movilidad',
            'Ejercicios de descarga',
            'Hidratación'
        ]
    },
    'Transición': {
        'calentamiento': [
            'Actividad recreativa',
            'Juegos lúdicos',
            'Movilidad relajada'
        ],
        'recreativo': [
            'Vóley playa',
            'Juegos modificados',
            'Actividades multideportivas',
            'Competencias divertidas'
        ],
        'recuperacion_activa': [
            'Yoga para atletas',
            'Natación',
            'Trote suave',
            'Estiramientos'
        ],
        'evaluacion': [
            'Reflexión sobre temporada',
            'Evaluación de progreso',
            'Metas personales',
            'Feedback grupal'
        ]
    }
}

EJERCICIOS_FUNDAMENTOS = {
    'saque': [
        'Saques de abajo (principiantes)',
        'Saques de arriba tipo tenis',
        'Saques flotadores',
        'Saques en salto (avanzado)',
        'Práctica de precisión en zonas'
    ],
    'recepcion': [
        'Recepción básica en parejas',
        'Recepción en formación W',
        'Recepción de saque fuerte',
        'Recepción con desplazamiento',
        'Recepción en movimiento'
    ],
    'armado': [
        'Colocación desde zona 3',
        'Levantada en movimiento',
        'Dosificación de balones',
        'Colocación a diferentes zonas',
        'Levantada de emergencia'
    ],
    'ataque': [
        'Remate desde zona 4',
        'Remate desde zona 2',
        'Remate en salto',
        'Remate con carrera',
        'Ataque en primera línea'
    ],
    'bloqueo': [
        'Bloqueo individual',
        'Bloqueo en parejas',
        'Bloqueo en tríos',
        'Bloqueo defensivo',
        'Cobertura de bloqueo'
    ],
    'defensa': [
        'Defensa baja',
        'Defensa en movimiento',
        'Cobertura defensiva',
        'Defensa en profundidad',
        'Defensa de transición'
    ]
}

# HTML simplificado embebido
HTML_CONTENT = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🏐 Entrena Voleibol WH</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 10px;
            color: #333;
        }
        
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px 20px;
            text-align: center;
        }
        
        .header h1 {
            font-size: 32px;
            margin-bottom: 5px;
        }
        
        .header p {
            font-size: 14px;
            opacity: 0.9;
        }
        
        .tabs {
            display: flex;
            border-bottom: 2px solid #eee;
            background: #f8f8f8;
        }
        
        .tab-btn {
            flex: 1;
            padding: 15px;
            border: none;
            background: none;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            color: #666;
            transition: all 0.3s;
            border-bottom: 3px solid transparent;
        }
        
        .tab-btn.active {
            color: #667eea;
            border-bottom-color: #667eea;
            background: white;
        }
        
        .content {
            padding: 20px;
        }
        
        .tab-pane {
            display: none;
        }
        
        .tab-pane.active {
            display: block;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            font-weight: 600;
            margin-bottom: 8px;
            color: #333;
        }
        
        select, input {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 14px;
            transition: border-color 0.3s;
        }
        
        select:focus, input:focus {
            outline: none;
            border-color: #667eea;
        }
        
        button {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s;
        }
        
        button:active {
            transform: scale(0.98);
        }
        
        .result {
            background: #f0f4ff;
            padding: 20px;
            border-radius: 8px;
            margin-top: 20px;
            max-height: 400px;
            overflow-y: auto;
        }
        
        .result h3 {
            color: #667eea;
            margin-bottom: 10px;
        }
        
        .result ul {
            list-style: none;
            padding-left: 15px;
        }
        
        .result li {
            padding: 8px 0;
            border-bottom: 1px solid #ddd;
            color: #555;
        }
        
        .result li:before {
            content: "✓ ";
            color: #667eea;
            font-weight: bold;
            margin-right: 8px;
        }
        
        .spinner {
            display: none;
            text-align: center;
            padding: 20px;
        }
        
        .spinner.show {
            display: block;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏐 Entrena Voleibol</h1>
            <p>Sistema de planificación para tablets</p>
        </div>
        
        <div class="tabs">
            <button class="tab-btn active" onclick="switchTab('plan')">📋 Plan</button>
            <button class="tab-btn" onclick="switchTab('ejercicios')">📚 Ejercicios</button>
            <button class="tab-btn" onclick="switchTab('info')">ℹ️ Info</button>
        </div>
        
        <div class="content">
            <!-- TAB: Plan -->
            <div id="plan" class="tab-pane active">
                <form id="form-plan">
                    <div class="form-group">
                        <label>👥 Rango de Edad</label>
                        <select id="edad" required>
                            <option value="">Seleccionar...</option>
                            <option value="8-10">8-10 años (Iniciación)</option>
                            <option value="11-13">11-13 años (Desarrollo)</option>
                            <option value="14-16">14-16 años (Perfeccionamiento)</option>
                            <option value="17+">17+ años (Alto Rendimiento)</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label>🔢 Cantidad de Jugadoras</label>
                        <input type="number" id="cantidad" min="4" max="30" value="12" required>
                    </div>
                    
                    <div class="form-group">
                        <label>📊 Etapa de Entrenamiento</label>
                        <select id="etapa" required>
                            <option value="">Seleccionar...</option>
                            <option value="Preparación General">Preparación General</option>
                            <option value="Preparación Específica">Preparación Específica</option>
                            <option value="Precompetitiva">Precompetitiva</option>
                            <option value="Competitiva">Competitiva</option>
                            <option value="Transición">Transición</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label>⏱️ Duración (minutos)</label>
                        <input type="number" id="tiempo" min="60" max="150" value="90" required>
                    </div>
                    
                    <div class="form-group">
                        <label>⚡ Fundamento (opcional)</label>
                        <select id="fundamento">
                            <option value="">Todos</option>
                            <option value="saque">🏐 Saque</option>
                            <option value="recepcion">🤲 Recepción</option>
                            <option value="armado">🙌 Armado</option>
                            <option value="ataque">⚡ Ataque</option>
                            <option value="bloqueo">🛡️ Bloqueo</option>
                            <option value="defensa">🏃 Defensa</option>
                        </select>
                    </div>
                    
                    <button type="submit">Generar Plan</button>
                </form>
                
                <div class="spinner" id="spinner">⏳ Generando plan...</div>
                <div class="result" id="result" style="display:none;"></div>
            </div>
            
            <!-- TAB: Ejercicios -->
            <div id="ejercicios" class="tab-pane">
                <div class="form-group">
                    <label>📊 Selecciona una Etapa</label>
                    <select id="etapa-ej" onchange="loadEjercicios()">
                        <option value="">Seleccionar...</option>
                        <option value="Preparación General">Preparación General</option>
                        <option value="Preparación Específica">Preparación Específica</option>
                        <option value="Precompetitiva">Precompetitiva</option>
                        <option value="Competitiva">Competitiva</option>
                        <option value="Transición">Transición</option>
                    </select>
                </div>
                <div class="result" id="result-ej"></div>
            </div>
            
            <!-- TAB: Info -->
            <div id="info" class="tab-pane">
                <div class="result">
                    <h3>🏐 Sobre esta App</h3>
                    <p style="color: #666; font-size: 14px; line-height: 1.6;">
                        <strong>Versión:</strong> 4.0 Mejorada<br>
                        <strong>Última actualización:</strong> 2 de Marzo, 2026<br>
                        <strong>Duración máxima:</strong> 150 minutos (2.5 horas)<br>
                        <strong>Ejercicios:</strong> +80 opciones<br><br>
                        <strong>Características:</strong><br>
                        ✓ Entrenamientos personalizados<br>
                        ✓ Enfoque en niños 8-10 años<br>
                        ✓ Base de ejercicios ampliada<br>
                        ✓ Funciona offline<br><br>
                        <strong>Para usar en PC:</strong> Ejecuta EntrenamientoVoleibol_Pro_Final.exe
                    </p>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        function switchTab(tab) {
            document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
            document.getElementById(tab).classList.add('active');
            event.target.classList.add('active');
        }
        
        document.getElementById('form-plan').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const edad = document.getElementById('edad').value;
            const cantidad = document.getElementById('cantidad').value;
            const etapa = document.getElementById('etapa').value;
            const tiempo = document.getElementById('tiempo').value;
            const fundamento = document.getElementById('fundamento').value;
            
            document.getElementById('spinner').classList.add('show');
            document.getElementById('result').style.display = 'none';
            
            try {
                const response = await fetch('/api/generar-plan', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ edad, cantidad, etapa, tiempo, fundamento })
                });
                
                const data = await response.json();
                
                let html = `<h3>✅ Plan Generado</h3>`;
                html += `<p><strong>Fecha:</strong> ${data.fecha}</p>`;
                html += `<p><strong>Duración:</strong> ${tiempo} minutos</p>`;
                if (fundamento) {
                    const nombr = {'saque': '🏐 Saque', 'recepcion': '🤲 Recepción', 'armado': '🙌 Armado', 'ataque': '⚡ Ataque', 'bloqueo': '🛡️ Bloqueo', 'defensa': '🏃 Defensa'};
                    html += `<p><strong>Enfoque:</strong> ${nombr[fundamento]}</p>`;
                }
                html += `<h3 style="margin-top: 15px;">Ejercicios:</h3>`;
                
                if (data.secciones) {
                    data.secciones.forEach(sec => {
                        html += `<h3 style="margin-top: 15px; color: #667eea; font-size: 16px;">${sec.nombre}</h3>`;
                        html += `<ul style="margin-bottom: 15px;">`;
                        sec.ejercicios.forEach(ej => {
                            html += `<li>${ej}</li>`;
                        });
                        html += `</ul>`;
                    });
                }
                
                document.getElementById('result').innerHTML = html;
                document.getElementById('result').style.display = 'block';
            } catch (err) {
                document.getElementById('result').innerHTML = `<p style="color: red;">Error: ${err.message}</p>`;
                document.getElementById('result').style.display = 'block';
            } finally {
                document.getElementById('spinner').classList.remove('show');
            }
        });
        
        async function loadEjercicios() {
            const etapa = document.getElementById('etapa-ej').value;
            if (!etapa) return;
            
            try {
                const response = await fetch(`/api/ejercicios/${encodeURIComponent(etapa)}`);
                const data = await response.json();
                
                let html = `<h3>📚 Ejercicios - ${etapa}</h3>`;
                
                Object.entries(data).forEach(([cat, ejercicios]) => {
                    html += `<h3 style="margin-top: 15px; color: #667eea; font-size: 14px;">${cat.replace(/_/g, ' ').toUpperCase()}</h3>`;
                    html += `<ul style="margin-bottom: 15px;">`;
                    ejercicios.forEach(ej => {
                        html += `<li>${ej}</li>`;
                    });
                    html += `</ul>`;
                });
                
                document.getElementById('result-ej').innerHTML = html;
            } catch (err) {
                document.getElementById('result-ej').innerHTML = `<p style="color: red;">Error: ${err.message}</p>`;
            }
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    """Página principal - servir HTML inline"""
    return HTML_CONTENT, 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/api/generar-plan', methods=['POST'])
def generar_plan():
    """Generar plan de entrenamiento personalizado"""
    data = request.get_json()
    
    edad = data.get('edad')
    cantidad = int(data.get('cantidad', 12))
    etapa = data.get('etapa')
    tiempo = int(data.get('tiempo', 90))
    fundamento = data.get('fundamento', '')
    
    plan = {
        'fecha': datetime.now().strftime('%d/%m/%Y %H:%M'),
        'edad': edad,
        'cantidad': cantidad,
        'etapa': etapa,
        'tiempo': tiempo,
        'fundamento': fundamento if fundamento else None,
        'secciones': []
    }
    
    # Obtener ejercicios de la etapa
    ejercicios_etapa = EJERCICIOS_DB.get(etapa, {})
    
    # Filtrar ejercicios por fundamento si está seleccionado
    if fundamento and fundamento in EJERCICIOS_FUNDAMENTOS:
        palabras_clave = EJERCICIOS_FUNDAMENTOS[fundamento]
        ejercicios_etapa_filtrado = {}
        
        for categoria, ejercicios in ejercicios_etapa.items():
            ejercicios_relacionados = []
            for ejercicio in ejercicios:
                # Buscar coincidencias con palabras clave del fundamento
                if any(palabra.lower() in ejercicio.lower() for palabra in palabras_clave):
                    ejercicios_relacionados.append(ejercicio)
            
            # Si la categoría tiene ejercicios relacionados, mantenerlos
            if ejercicios_relacionados:
                ejercicios_etapa_filtrado[categoria] = ejercicios_relacionados
            else:
                # Si no hay coincidencias exactas, mantener algunos ejercicios genéricos
                ejercicios_etapa_filtrado[categoria] = ejercicios[:2]
        
        ejercicios_etapa = ejercicios_etapa_filtrado if ejercicios_etapa_filtrado else ejercicios_etapa
    
    # Distribuir ejercicios por secciones
    tiempo_por_seccion = tiempo // len(ejercicios_etapa) if ejercicios_etapa else 0
    
    for categoria, ejercicios in ejercicios_etapa.items():
        # Seleccionar un número de ejercicios basado en el tiempo disponible
        num_ejercicios = max(2, min(len(ejercicios), tiempo_por_seccion // 10))
        ejercicios_seleccionados = ejercicios[:num_ejercicios]
        
        plan['secciones'].append({
            'nombre': categoria.replace('_', ' ').title(),
            'duracion': f'{tiempo_por_seccion} min aprox',
            'ejercicios': ejercicios_seleccionados
        })
    
    return jsonify(plan)

@app.route('/api/ejercicios/<etapa>')
def obtener_ejercicios(etapa):
    """Obtener todos los ejercicios de una etapa"""
    ejercicios = EJERCICIOS_DB.get(etapa, {})
    return jsonify(ejercicios)

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'version': '4.0'})

# Manejador de errores 404
@app.errorhandler(404)
def not_found(error):
    """Manejar rutas no encontradas"""
    return jsonify({
        'error': 'Ruta no encontrada',
        'path': request.path,
        'method': request.method,
        'status': 404,
        'rutas_disponibles': [
            '/',
            '/api/generar-plan',
            '/api/ejercicios/<etapa>',
            '/health'
        ]
    }), 404

# Manejador de errores 500
@app.errorhandler(500)
def server_error(error):
    """Manejar errores del servidor"""
    return jsonify({
        'error': 'Error interno del servidor',
        'status': 500
    }), 500

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🏐 ENTRENA VOLEIBOL WH - SERVIDOR TABLETA ACTIVO")
    print("="*70)
    print("\n✅ SERVIDOR FUNCIONANDO CORRECTAMENTE\n")
    print("📍 ACCESO DESDE LOCALHOST:")
    print("   http://localhost:5000/")
    print("\n📱 ACCESO DESDE TABLETA (MISMA RED):")
    print("   http://10.143.157.177:5000/")
    print("   http://192.168.x.x:5000/  (reemplaza x con tu IP)")
    print("\n💡 RUTAS DISPONIBLES:")
    print("   GET  /                     → Página principal")
    print("   POST /api/generar-plan     → Generar plan (JSON)")
    print("   GET  /api/ejercicios/<etapa> → Listar ejercicios")
    print("   GET  /health               → Verificar estado")
    print("\n⚠️ ERROR 404?")
    print("   1. Verifica la IP correcta (ipconfig)")
    print("   2. Usa http:// NO https://")
    print("   3. Incluye el puerto :5000")
    print("\n" + "="*70 + "\n")
    
    app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)
