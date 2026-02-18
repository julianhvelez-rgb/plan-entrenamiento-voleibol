import os
from datetime import datetime

class EntrenamientoVoleibol:
    def __init__(self):
        self.etapas = {
            '1': 'Preparación General',
            '2': 'Preparación Específica',
            '3': 'Precompetitiva',
            '4': 'Competitiva',
            '5': 'Transición'
        }
        
        self.ejercicios_db = {
                    # NUEVA BASE DE EJERCICIOS DINÁMICOS POR MODALIDAD
                    self.ejercicios_dinamicos = {
                        'Individual': [
                            'Toques rápidos en pared: Control de antebrazos y coordinación.',
                            'Saque objetivo: Precisión y potencia del saque.',
                            'Recepción zigzag: Desplazamiento y control en recepción.',
                            'Control con toque de dedos: Sensibilidad y control de dedos.',
                            'Saltos con toque de balón: Potencia de salto y coordinación.',
                            'Dribbling de balón: Destreza manual y control.',
                            'Lanzamiento y recepción contra pared: Adaptabilidad y reacción.',
                            'Carrera con balón: Coordinación y resistencia.',
                            'Toques sentados: Control y fuerza en posiciones no convencionales.',
                            'Desplazamiento reactivo: Reacción y agilidad.'
                        ],
                        'Parejas': [
                            'Toques continuos: Coordinación y comunicación.',
                            'Pase y desplazamiento: Anticipación y desplazamiento.',
                            'Mini-competencia de saques: Precisión bajo presión.',
                            'Recepción y ataque: Fluidez defensa-ataque.',
                            'Juego de reflejos: Reflejos y reacción.',
                            'Pase bajo presión: Decisión rápida.',
                            'Toques con obstáculos: Control de altura.',
                            'Reto de control: Consistencia y concentración.',
                            'Pase con giro: Coordinación y equilibrio.',
                            'Pase y sentadilla: Trabajo físico y técnico.'
                        ],
                        'Tríos': [
                            'Ronda de pases: Versatilidad técnica y ritmo.',
                            'Ataque y defensa: Roles y rotación.',
                            'Carrera de relevos con balón: Trabajo en equipo y resistencia.',
                            'Pase en triángulo: Precisión y anticipación.',
                            'Juego de eliminación: Concentración y motivación lúdica.',
                            'Pase con salto: Potencia y coordinación.',
                            'Defensa en zona: Cobertura y desplazamiento.',
                            'Pase sorpresa: Atención y reacción.',
                            'Pase con cambio de dirección: Adaptabilidad y comunicación.',
                            'Reto de precisión: Estrategia y control.'
                        ],
                        'Grupos': [
                            'Rondo voleibolero: Rapidez de pase y visión periférica.',
                            'Mini-partido rotativo: Adaptación y táctica.',
                            'Carrera de relevos con obstáculos: Agilidad y trabajo en equipo.',
                            'Competencia de saques: Precisión y competitividad.',
                            'Defensa en cadena: Coordinación defensiva.',
                            'Juego de “eliminados”: Concentración y presión lúdica.',
                            'Pase múltiple: Atención y trabajo colectivo.',
                            'Circuito técnico: Desarrollo integral de habilidades.',
                            'Juego de roles: Versatilidad y comprensión de roles.',
                            'Competencia de resistencia: Resistencia y disciplina.'
                        ]
                    }
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
    
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def dibujar_cancha_completa(self):
        """Dibuja la cancha de voleibol con zonas numeradas"""
        print("\n" + "="*70)
        print("                    CANCHA DE VOLEIBOL")
        print("="*70)
        print("")
        print("        ┌────────────────────────────────────────────┐")
        print("        │                  EQUIPO A                  │")
        print("        │                                            │")
        print("        │      [5]           [6]           [1]       │")
        print("        │    Zaguero      Zaguero       Zaguero      │")
        print("        │   Izquierdo     Central       Derecho      │")
        print("        │                                            │")
        print("        │      [4]           [3]           [2]       │")
        print("        │   Delantero    Colocador     Delantero     │")
        print("        │   Izquierdo                   Derecho      │")
        print("        │                                            │")
        print("        ├════════════════════════════════════════════┤  RED")
        print("        │                                            │")
        print("        │      [2]           [3]           [4]       │")
        print("        │   Delantero    Colocador     Delantero     │")
        print("        │   Derecho                    Izquierdo     │")
        print("        │                                            │")
        print("        │      [1]           [6]           [5]       │")
        print("        │    Zaguero      Zaguero       Zaguero      │")
        print("        │   Derecho       Central       Izquierdo    │")
        print("        │                                            │")
        print("        │                  EQUIPO B                  │")
        print("        └────────────────────────────────────────────┘")
        print("")
        print("  📏 Dimensiones: 18m x 9m  |  🎯 Zona de ataque: 3m")
        print("="*70)
    
    def dibujar_formacion_recepcion(self, sistema="W"):
        """Dibuja formaciones de recepción"""
        print("\n" + "="*70)
        if sistema == "W":
            print("            FORMACIÓN EN W (RECEPCIÓN)")
            print("="*70)
            print("")
            print("        ┌────────────────────────────────────────────┐")
            print("        │                                            │")
            print("        │         ●                  ●               │  Zagueros")
            print("        │      Zag Izq           Zag Der             │")
            print("        │                                            │")
            print("        │                  ●                         │  Zaguero")
            print("        │              Zag Central                   │  Central")
            print("        │                                            │")
            print("        │    ●                              ●        │  Delanteros")
            print("        │  Del Izq                      Del Der      │  laterales")
            print("        │                                            │")
            print("        ├════════════════════════════════════════════┤  RED")
            print("        │           🏐 Dirección del saque           │")
            print("        └────────────────────────────────────────────┘")
        else:  # 3-2-1
            print("          FORMACIÓN 3-2-1 (RECEPCIÓN)")
            print("="*70)
            print("")
            print("        ┌────────────────────────────────────────────┐")
            print("        │                                            │")
            print("        │                  ●                         │  1 Zaguero")
            print("        │              Zag Central                   │")
            print("        │                                            │")
            print("        │         ●                  ●               │  2 Laterales")
            print("        │       Lateral           Lateral            │")
            print("        │                                            │")
            print("        │    ●          ●                ●           │  3 Delanteros")
            print("        │  Del Izq   Colocador       Del Der         │")
            print("        │                                            │")
            print("        ├════════════════════════════════════════════┤  RED")
            print("        │           🏐 Dirección del saque           │")
            print("        └────────────────────────────────────────────┘")
        print("")
    
    def dibujar_ejercicio_parejas(self):
        """Dibuja ejercicio en parejas"""
        print("\n" + "="*70)
        print("              EJERCICIO EN PAREJAS")
        print("="*70)
        print("")
        print("        ┌────────────────────────────────────────────┐")
        print("        │                                            │")
        print("        │         ●  ←→  ●         ●  ←→  ●          │")
        print("        │        P1      P2       P3      P4         │")
        print("        │                                            │")
        print("        │              🏐   🏐   🏐                   │")
        print("        │                                            │")
        print("        │         ●  ←→  ●         ●  ←→  ●          │")
        print("        │        P5      P6       P7      P8         │")
        print("        │                                            │")
        print("        │              🏐   🏐   🏐                   │")
        print("        │                                            │")
        print("        │         ●  ←→  ●         ●  ←→  ●          │")
        print("        │        P9     P10      P11     P12         │")
        print("        │                                            │")
        print("        └────────────────────────────────────────────┘")
        print("")
        print("  ● Jugadora  |  🏐 Balón  |  ←→ Pases entre parejas")
        print("="*70)
    
    def dibujar_ejercicio_circulo(self, cantidad):
        """Dibuja ejercicio en círculo"""
        print("\n" + "="*70)
        print(f"          EJERCICIO EN CÍRCULO ({cantidad} jugadoras)")
        print("="*70)
        print("")
        if cantidad <= 6:
            print("                    ●  P1")
            print("                   ╱ ╲")
            print("                  ╱   ╲")
            print("             ●  P6     P2  ●")
            print("              ╲           ╱")
            print("               ╲    🏐   ╱")
            print("                ╲       ╱")
            print("             ●  P5     P3  ●")
            print("                  ╲   ╱")
            print("                   ╲ ╱")
            print("                    ●  P4")
        else:
            print("                 ●  P1    ●  P2")
            print("                ╱              ╲")
            print("           ●  P8                P3  ●")
            print("            ╲                      ╱")
            print("             ╲        🏐          ╱")
            print("              ╲                  ╱")
            print("           ●  P7                P4  ●")
            print("                ╲              ╱")
            print("                 ●  P6    ●  P5")
        print("")
        print("  ● Jugadora  |  🏐 Balón  |  Pases en secuencia")
        print("="*70)
    
    def dibujar_ejercicio_remate(self):
        """Dibuja ejercicio de remate"""
        print("\n" + "="*70)
        print("           EJERCICIO: RECEPCIÓN - COLOCACIÓN - REMATE")
        print("="*70)
        print("")
        print("        ┌────────────────────────────────────────────┐")
        print("        │                                            │")
        print("        │              ↗ ●  [Rematadora]             │")
        print("        │            ↗   Zona 4                      │")
        print("        │          ↗                                 │")
        print("        │        🏐  [3. REMATE]                     │")
        print("        │      ↗                                     │")
        print("        │    ●  [Colocadora]                         │")
        print("        │    ↑   Zona 3                              │")
        print("        │    │  [2. COLOCACIÓN]                      │")
        print("        │    🏐                                       │")
        print("        ├════╪══════════════════════════════════════┤  RED")
        print("        │    │                                       │")
        print("        │    ●  [Receptora]                          │")
        print("        │       Zona 5                               │")
        print("        │       [1. RECEPCIÓN]                       │")
        print("        │                                            │")
        print("        │              ↓ 🏐                          │")
        print("        │                                            │")
        print("        │              ●  [Sacadora]                 │")
        print("        │                                            │")
        print("        └────────────────────────────────────────────┘")
        print("")
        print("  Secuencia: Saque → Recepción → Colocación → Remate")
        print("="*70)
    
    def dibujar_ejercicio_bloqueo(self):
        """Dibuja ejercicio de bloqueo"""
        print("\n" + "="*70)
        print("              EJERCICIO: BLOQUEO Y DEFENSA")
        print("="*70)
        print("")
        print("        ┌────────────────────────────────────────────┐")
        print("        │                                            │")
        print("        │         ●          ●          ●            │")
        print("        │      Bloq 1     Bloq 2     Bloq 3          │")
        print("        │        ║          ║          ║             │")
        print("        ├════════╬══════════╬══════════╬═════════════┤  RED")
        print("        │        ║          ║          ║             │")
        print("        │        ↓ 🏐       ↓ 🏐       ↓ 🏐          │")
        print("        │      Remate     Remate     Remate          │")
        print("        │                                            │")
        print("        │    ●                    ●           ●      │")
        print("        │  Def Izq             Def Cen     Def Der   │")
        print("        │                                            │")
        print("        │              ●  [Colocadora]               │")
        print("        │                                            │")
        print("        └────────────────────────────────────────────┘")
        print("")
        print("  Bloqueadoras saltan | Defensoras reciben | Colocadora arma")
        print("="*70)
    
    def dibujar_estaciones(self, cantidad):
        """Dibuja organización por estaciones"""
        num_estaciones = min(4, (cantidad + 2) // 3)
        print("\n" + "="*70)
        print(f"        ORGANIZACIÓN POR ESTACIONES ({num_estaciones} estaciones)")
        print("="*70)
        print("")
        
        if num_estaciones == 2:
            print("        ┌──────────────────────┬──────────────────────┐")
            print("        │   ESTACIÓN 1         │   ESTACIÓN 2         │")
            print("        │   Técnica Individual │   Juego en Parejas   │")
            print("        │                      │                      │")
            print("        │   ● ● ●              │   ●―●    ●―●         │")
            print("        │   🏐🏐🏐              │   🏐      🏐          │")
            print("        │                      │                      │")
            print("        │   Tiempo: 10-15 min  │   Tiempo: 10-15 min  │")
            print("        └──────────────────────┴──────────────────────┘")
        elif num_estaciones == 3:
            print("        ┌──────────────┬──────────────┬──────────────┐")
            print("        │  ESTACIÓN 1  │  ESTACIÓN 2  │  ESTACIÓN 3  │")
            print("        │  Saques      │  Defensa     │  Remate      │")
            print("        │              │              │              │")
            print("        │   ● ● ●      │  ● ● ●       │  ● ● ●       │")
            print("        │   🏐🏐🏐      │  🏐🏐🏐       │  🏐🏐🏐       │")
            print("        │              │              │              │")
            print("        │ 10-12 min    │ 10-12 min    │ 10-12 min    │")
            print("        └──────────────┴──────────────┴──────────────┘")
        else:  # 4 estaciones
            print("        ┌─────────────┬─────────────┐")
            print("        │ ESTACIÓN 1  │ ESTACIÓN 2  │")
            print("        │ Pase Dedos  │ Pase Antebr │")
            print("        │  ● ● ●      │  ● ● ●      │")
            print("        │  🏐🏐        │  🏐🏐        │")
            print("        ├─────────────┼─────────────┤")
            print("        │ ESTACIÓN 3  │ ESTACIÓN 4  │")
            print("        │ Saques      │ Defensa     │")
            print("        │  ● ● ●      │  ● ● ●      │")
            print("        │  🏐🏐        │  🏐🏐        │")
            print("        └─────────────┴─────────────┘")
            print("")
            print("        Rotación cada 8-10 minutos")
        
        print("")
        print(f"  👥 {cantidad} jugadoras ÷ {num_estaciones} estaciones = ~{cantidad//num_estaciones} por grupo")
        print("="*70)
    
    def mostrar_diagrama_ejercicio(self, tipo_ejercicio, cantidad):
        """Muestra el diagrama apropiado según el tipo de ejercicio"""
        tipo_lower = tipo_ejercicio.lower()
        
        if 'parejas' in tipo_lower:
            self.dibujar_ejercicio_parejas()
        elif 'circulo' in tipo_lower or 'pase' in tipo_lower and cantidad <= 8:
            self.dibujar_ejercicio_circulo(cantidad)
        elif 'remate' in tipo_lower or 'colocación' in tipo_lower:
            self.dibujar_ejercicio_remate()
        elif 'bloqueo' in tipo_lower or 'defensa' in tipo_lower:
            self.dibujar_ejercicio_bloqueo()
        elif 'recepción' in tipo_lower and 'formación' in tipo_lower:
            self.dibujar_formacion_recepcion()
        elif cantidad > 12:
            self.dibujar_estaciones(cantidad)
        else:
            self.dibujar_cancha_completa()
    
    def mostrar_menu_principal(self):
        print("\n" + "="*60)
        print(" 🏐  SISTEMA DE ENTRENAMIENTO DE VOLEIBOL  🏐")
        print("="*60)
        print("\n1. Crear Plan de Entrenamiento del Día")
        print("2. Ver Base de Ejercicios por Etapa")
        print("3. Generar Plan Personalizado")
        print("4. Ver Diagramas de Cancha y Ejercicios")
        print("5. Salir")
        print("6. Ver Ejercicios Dinámicos por Modalidad")
        print("\n" + "="*60)
        return input("\nSeleccione una opción: ")
    
    def obtener_rango_edad(self):
        print("\n" + "-"*60)
        print("RANGO DE EDAD DE LAS NIÑAS")
        print("-"*60)
        print("\n1. 8-10 años (Iniciación)")
        print("2. 11-13 años (Desarrollo)")
        print("3. 14-16 años (Perfeccionamiento)")
        print("4. 17+ años (Alto Rendimiento)")
        
        opcion = input("\nSeleccione el rango de edad: ")
        rangos = {
            '1': '8-10 años (Iniciación)',
            '2': '11-13 años (Desarrollo)',
            '3': '14-16 años (Perfeccionamiento)',
            '4': '17+ años (Alto Rendimiento)'
        }
        return rangos.get(opcion, '11-13 años (Desarrollo)')
    
    def obtener_asistentes(self):
        while True:
            try:
                cantidad = int(input("\n¿Cuántas niñas asistieron hoy al entrenamiento? "))
                if cantidad > 0:
                    return cantidad
                else:
                    print("Por favor ingrese un número mayor a 0")
            except ValueError:
                print("Por favor ingrese un número válido")
    
    def seleccionar_etapa(self):
        print("\n" + "-"*60)
        print("ETAPA DE ENTRENAMIENTO")
        print("-"*60)
        for key, value in self.etapas.items():
            print(f"{key}. {value}")
        
        opcion = input("\nSeleccione la etapa actual: ")
        return self.etapas.get(opcion, 'Preparación General')
    
    def recomendar_organizacion(self, cantidad):
        print("\n" + "-"*60)
        print("RECOMENDACIONES DE ORGANIZACIÓN")
        print("-"*60)
        
        if cantidad <= 6:
            print(f"\n✓ Grupo pequeño ({cantidad} niñas)")
            print("  - Trabajo técnico individualizado")
            print("  - Ejercicios en parejas o tríos")
            print("  - Atención personalizada alta")
            print("  - Juego: 3 vs 3 o minivoleibol")
        elif cantidad <= 12:
            print(f"\n✓ Grupo mediano ({cantidad} niñas)")
            print("  - Dividir en 2 equipos de 6")
            print("  - Rotación por estaciones")
            print("  - Trabajo de equipo y técnica")
            print("  - Juego: 6 vs 6 con rotaciones")
        elif cantidad <= 18:
            print(f"\n✓ Grupo grande ({cantidad} niñas)")
            print("  - Dividir en 3 equipos de 6")
            print("  - Sistema de estaciones (3-4)")
            print("  - Rotación cada 10-15 minutos")
            print("  - Juego: torneo entre equipos")
        else:
            print(f"\n✓ Grupo muy grande ({cantidad} niñas)")
            print("  - Dividir en 4 o más equipos")
            print("  - Múltiples estaciones de trabajo")
            print("  - Asistentes o capitanas por grupo")
            print("  - Rotación organizada y rápida")
        
        # Mostrar diagrama visual
        if cantidad > 12:
            self.dibujar_estaciones(cantidad)
        elif cantidad >= 6:
            self.dibujar_cancha_completa()
    
    def mostrar_ejercicios_etapa(self, etapa):
        print("\n" + "="*60)
        print(f"EJERCICIOS DISPONIBLES - {etapa.upper()}")
        print("="*60)
        
        ejercicios = self.ejercicios_db.get(etapa, {})
        for categoria, lista_ejercicios in ejercicios.items():
            print(f"\n📋 {categoria.replace('_', ' ').title()}:")
            for i, ejercicio in enumerate(lista_ejercicios, 1):
                print(f"   {i}. {ejercicio}")
    
    def seleccionar_ejercicios_personalizados(self, etapa):
        ejercicios_seleccionados = {}
        ejercicios = self.ejercicios_db.get(etapa, {})
        
        print("\n" + "-"*60)
        print("SELECCIÓN PERSONALIZADA DE EJERCICIOS")
        print("-"*60)
        print("\nPara cada categoría, ingrese los números de ejercicios separados por comas")
        print("(Ejemplo: 1,3,4) o presione Enter para seleccionar todos\n")
        
        for categoria, lista_ejercicios in ejercicios.items():
            print(f"\n📋 {categoria.replace('_', ' ').title()}:")
            for i, ejercicio in enumerate(lista_ejercicios, 1):
                print(f"   {i}. {ejercicio}")
            
            seleccion = input(f"\n¿Qué ejercicios de {categoria} desea incluir? (Enter para todos): ").strip()
            
            if seleccion == "":
                ejercicios_seleccionados[categoria] = lista_ejercicios
            else:
                try:
                    indices = [int(x.strip()) - 1 for x in seleccion.split(',')]
                    ejercicios_seleccionados[categoria] = [lista_ejercicios[i] for i in indices if 0 <= i < len(lista_ejercicios)]
                except:
                    print("⚠️  Selección inválida, se incluirán todos los ejercicios de esta categoría")
                    ejercicios_seleccionados[categoria] = lista_ejercicios
        
        return ejercicios_seleccionados
    
    def generar_plan_entrenamiento(self, edad, cantidad, etapa, ejercicios_personalizados=None):
        self.limpiar_pantalla()
        print("\n" + "="*60)
        print("📅  PLAN DE ENTRENAMIENTO GENERADO")
        print("="*60)
        print(f"\n📆 Fecha: {datetime.now().strftime('%d/%m/%Y')}")
        print(f"👥 Asistentes: {cantidad} niñas")
        print(f"🎯 Edad: {edad}")
        print(f"📊 Etapa: {etapa}")
        print("\n" + "="*60)
        
        self.recomendar_organizacion(cantidad)
        
        print("\n" + "="*60)
        print("ESTRUCTURA DEL ENTRENAMIENTO")
        print("="*60)
        
        if ejercicios_personalizados:
            ejercicios = ejercicios_personalizados
        else:
            ejercicios = self.ejercicios_db.get(etapa, {})
        
        tiempo_total = 0
        
        for i, (categoria, lista_ejercicios) in enumerate(ejercicios.items(), 1):
            print(f"\n{i}. {categoria.replace('_', ' ').title().upper()}")
            print("-" * 60)
            
            # Asignar tiempos aproximados según categoría
            if 'calentamiento' in categoria:
                tiempo = 10
            elif 'acondicionamiento' in categoria or 'recuperacion' in categoria:
                tiempo = 15
            elif 'recreativo' in categoria:
                tiempo = 25
            else:
                tiempo = 20
            
            tiempo_total += tiempo
            print(f"⏱️  Duración estimada: {tiempo} minutos")
            print()
            
            for j, ejercicio in enumerate(lista_ejercicios, 1):
                print(f"   {j}. {ejercicio}")
        
        print("\n" + "="*60)
        print(f"⏱️  DURACIÓN TOTAL ESTIMADA: {tiempo_total} minutos ({tiempo_total/60:.1f} horas)")
        print("="*60)
        
        # Mostrar algunos diagramas clave
        print("\n" + "="*60)
        print("VISUALIZACIÓN DE EJERCICIOS EN CANCHA")
        print("="*60)
        
        ver_diagramas = input("\n¿Desea ver los diagramas de ejercicios en cancha? (s/n): ").lower()
        if ver_diagramas == 's':
            # Mostrar diagrama según la etapa
            if etapa in ['Preparación Específica', 'Precompetitiva', 'Competitiva']:
                self.dibujar_ejercicio_remate()
                input("\nPresione Enter para ver más diagramas...")
                self.dibujar_ejercicio_bloqueo()
                input("\nPresione Enter para ver formaciones...")
                self.dibujar_formacion_recepcion("W")
            elif etapa == 'Preparación General':
                self.dibujar_ejercicio_parejas()
                input("\nPresione Enter para ver más diagramas...")
                self.dibujar_ejercicio_circulo(min(cantidad, 8))
            else:  # Transición
                self.dibujar_ejercicio_circulo(min(cantidad, 6))
                input("\nPresione Enter para ver la cancha completa...")
                self.dibujar_cancha_completa()
        
        # Sugerencias adicionales
        print("\n💡 SUGERENCIAS ADICIONALES:")
        if cantidad > 12:
            print("   • Considere tener un asistente para manejar grupos grandes")
        if '8-10' in edad:
            print("   • Mantenga ejercicios divertidos y variados para esta edad")
            print("   • Sesiones más cortas, alta rotación de actividades")
        if etapa == 'Competitiva':
            print("   • Enfóquese en la recuperación entre entrenamientos")
            print("   • Monitoree fatiga y prevención de lesiones")
        if etapa == 'Transición':
            print("   • Priorice el aspecto recreativo y la diversión")
            print("   • Oportunidad para trabajar aspectos mentales del equipo")
        
        print("\n" + "="*60)
    
    def guardar_plan(self, edad, cantidad, etapa):
        filename = f"plan_entrenamiento_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*60 + "\n")
            f.write("PLAN DE ENTRENAMIENTO DE VOLEIBOL\n")
            f.write("="*60 + "\n\n")
            f.write(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
            f.write(f"Asistentes: {cantidad} niñas\n")
            f.write(f"Edad: {edad}\n")
            f.write(f"Etapa: {etapa}\n")
            f.write("\n" + "="*60 + "\n")
            f.write("EJERCICIOS PROGRAMADOS\n")
            f.write("="*60 + "\n\n")
            
            ejercicios = self.ejercicios_db.get(etapa, {})
            for categoria, lista_ejercicios in ejercicios.items():
                f.write(f"\n{categoria.replace('_', ' ').title()}:\n")
                f.write("-" * 40 + "\n")
                for ejercicio in lista_ejercicios:
                    f.write(f"  - {ejercicio}\n")
        
        print(f"\n✅ Plan guardado en: {filename}")
    
    def ejecutar(self):
        while True:
            self.limpiar_pantalla()
            opcion = self.mostrar_menu_principal()
            
            if opcion == '1':
                self.limpiar_pantalla()
                edad = self.obtener_rango_edad()
                cantidad = self.obtener_asistentes()
                etapa = self.seleccionar_etapa()
                self.generar_plan_entrenamiento(edad, cantidad, etapa)
                
                guardar = input("\n¿Desea guardar este plan? (s/n): ").lower()
                if guardar == 's':
                    self.guardar_plan(edad, cantidad, etapa)
                
                input("\nPresione Enter para continuar...")
            
            elif opcion == '2':
                self.limpiar_pantalla()
                etapa = self.seleccionar_etapa()
                self.mostrar_ejercicios_etapa(etapa)
                input("\nPresione Enter para continuar...")
            
            elif opcion == '3':
                self.limpiar_pantalla()
                edad = self.obtener_rango_edad()
                cantidad = self.obtener_asistentes()
                etapa = self.seleccionar_etapa()
                ejercicios_personalizados = self.seleccionar_ejercicios_personalizados(etapa)
                self.generar_plan_entrenamiento(edad, cantidad, etapa, ejercicios_personalizados)
                
                guardar = input("\n¿Desea guardar este plan personalizado? (s/n): ").lower()
                if guardar == 's':
                    self.guardar_plan(edad, cantidad, etapa)
                
                input("\nPresione Enter para continuar...")
            
            elif opcion == '4':
                self.limpiar_pantalla()
                print("\n" + "="*60)
                print("DIAGRAMAS DE CANCHA Y EJERCICIOS")
                print("="*60)
                print("\n1. Cancha completa con zonas")
                print("2. Formación en W (Recepción)")
                print("3. Formación 3-2-1 (Recepción)")
                print("4. Ejercicio en parejas")
                print("5. Ejercicio en círculo")
                print("6. Recepción-Colocación-Remate")
                print("7. Bloqueo y Defensa")
                print("8. Organización por estaciones")
                print("9. Volver al menú principal")
                
                diagrama = input("\nSeleccione el diagrama a visualizar: ")
                
                if diagrama == '1':
                    self.dibujar_cancha_completa()
                elif diagrama == '2':
                    self.dibujar_formacion_recepcion("W")
                elif diagrama == '3':
                    self.dibujar_formacion_recepcion("3-2-1")
                elif diagrama == '4':
                    self.dibujar_ejercicio_parejas()
                elif diagrama == '5':
                    cantidad = int(input("¿Cuántas jugadoras? (6-12): ") or "6")
                    self.dibujar_ejercicio_circulo(cantidad)
                elif diagrama == '6':
                    self.dibujar_ejercicio_remate()
                elif diagrama == '7':
                    self.dibujar_ejercicio_bloqueo()
                elif diagrama == '8':
                    cantidad = int(input("¿Cuántas jugadoras en total? ") or "12")
                    self.dibujar_estaciones(cantidad)
                
                if diagrama != '9':
                    input("\nPresione Enter para continuar...")
            
            elif opcion == '5':
                print("\n¡Gracias por usar el Sistema de Entrenamiento de Voleibol! 🏐")
                print("¡Buen entrenamiento!\n")
                break
            elif opcion == '6':
                self.limpiar_pantalla()
                print("\n" + "="*60)
                print("EJERCICIOS DINÁMICOS POR MODALIDAD")
                print("="*60)
                for modalidad, lista in self.ejercicios_dinamicos.items():
                    print(f"\n📋 {modalidad}:")
                    for i, ejercicio in enumerate(lista, 1):
                        print(f"   {i}. {ejercicio}")
                input("\nPresione Enter para continuar...")
            else:
                print("\n⚠️  Opción inválida. Por favor intente de nuevo.")
                input("Presione Enter para continuar...")

# Punto de entrada del programa
if __name__ == "__main__":
    app = EntrenamientoVoleibol()
    app.ejecutar()
