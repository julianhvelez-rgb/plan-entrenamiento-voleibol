import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
from datetime import datetime
import os
import random
import math
from PIL import Image, ImageTk

class EntrenamientoVoleibolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🏐 Sistema de Entrenamiento de Voleibol")
        self.root.geometry("1400x900")
        self.root.configure(bg='#1a1a2e')
        
        # Límite de tiempo del entrenamiento (minutos)
        self.TIEMPO_MAXIMO = 150
        
        # Cargar logo si existe
        try:
            if os.path.exists('logo_voleibol.ico'):
                self.root.iconbitmap('logo_voleibol.ico')
        except:
            pass
        
        # Paleta de colores moderna y atractiva
        self.colors = {
            'bg_dark': '#0a0e27',
            'bg_medium': '#1a1f3a',
            'bg_light': '#252b48',
            'accent': '#ff6b9d',
            'accent_hover': '#ff4d7d',
            'secondary': '#4d7cfe',
            'text': '#ffffff',
            'text_secondary': '#b8c5d6',
            'cyan': '#00d9ff',
            'court_green': '#2d5016',
            'ball_color': '#ffd700',
            'success': '#4caf50',
            'warning': '#ff9800',
            'card_bg': '#1e2439',
            'gradient_start': '#ff6b9d',
            'gradient_end': '#4d7cfe'
        }
        
        # Variables
        self.edad_var = tk.StringVar()
        self.cantidad_var = tk.StringVar()
        self.etapa_var = tk.StringVar()
        self.fundamento_var = tk.StringVar()
        self.ejercicio_actual = None
        self.lista_ejercicios_plan = []
        
        # Datos
        self.etapas = {
            'Preparación General': 'general',
            'Preparación Específica': 'especifica',
            'Precompetitiva': 'precompetitiva',
            'Competitiva': 'competitiva',
            'Transición': 'transicion'
        }
        
        self.fundamentos = {
            'Todos los fundamentos': 'todos',
            '🏐 Saque': 'saque',
            '🤲 Recepción': 'recepcion',
            '🙌 Armado/Levantada': 'armado',
            '⚡ Ataque/Remate': 'ataque',
            '🛡️ Bloqueo': 'bloqueo',
            '🏃 Defensa': 'defensa'
        }
        
        self.ejercicios_db = self._cargar_ejercicios()
        
        # Configurar estilo
        self._configurar_estilos()
        
        # Crear interfaz
        self._crear_interfaz()
        
    def _configurar_estilos(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Estilo para botones
        style.configure('Accent.TButton',
                       background=self.colors['accent'],
                       foreground=self.colors['text'],
                       borderwidth=0,
                       focuscolor='none',
                       padding=15,
                       font=('Segoe UI', 11, 'bold'))
        
        style.map('Accent.TButton',
                 background=[('active', self.colors['accent_hover'])])
        
        # Estilo para frames
        style.configure('Dark.TFrame', background=self.colors['bg_dark'])
        style.configure('Medium.TFrame', background=self.colors['bg_medium'])
        
        # Estilo para labels
        style.configure('Title.TLabel',
                       background=self.colors['bg_dark'],
                       foreground=self.colors['accent'],
                       font=('Segoe UI', 24, 'bold'))
        
        style.configure('Subtitle.TLabel',
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text'],
                       font=('Segoe UI', 14, 'bold'))
        
        style.configure('Normal.TLabel',
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text'],
                       font=('Segoe UI', 10))
        
        # Estilo para combobox
        style.configure('TCombobox',
                       fieldbackground=self.colors['bg_light'],
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text'],
                       arrowcolor=self.colors['accent'])
        
    def _crear_interfaz(self):
        # Frame principal
        main_container = tk.Frame(self.root, bg=self.colors['bg_dark'])
        main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header
        self._crear_header(main_container)
        
        # Notebook para pestañas
        notebook = ttk.Notebook(main_container)
        notebook.pack(fill='both', expand=True, pady=20)
        
        # Pestañas
        self.tab_plan = self._crear_tab_plan(notebook)
        self.tab_visualizacion = self._crear_tab_visualizacion(notebook)
        self.tab_ejercicios = self._crear_tab_ejercicios(notebook)
        
        notebook.add(self.tab_plan, text='  📋 Crear Plan  ')
        notebook.add(self.tab_visualizacion, text='  🏐 Visualización Cancha  ')
        notebook.add(self.tab_ejercicios, text='  📚 Base de Ejercicios  ')
        
    def _crear_header(self, parent):
        header = tk.Frame(parent, bg=self.colors['bg_dark'])
        header.pack(fill='x', pady=(0, 20))
        
        # Intentar cargar y mostrar logo pequeño
        logo_frame = tk.Frame(header, bg=self.colors['bg_dark'])
        logo_frame.pack(pady=5)
        
        try:
            if os.path.exists('logo_voleibol.png'):
                logo_img = Image.open('logo_voleibol.png')
                logo_img = logo_img.resize((60, 60), Image.Resampling.LANCZOS)
                self.logo_photo = ImageTk.PhotoImage(logo_img)
                logo_label = tk.Label(logo_frame, image=self.logo_photo, bg=self.colors['bg_dark'])
                logo_label.pack()
        except:
            pass
        
        # Título
        title = tk.Label(header,
                        text="🏐 SISTEMA DE ENTRENAMIENTO DE VOLEIBOL",
                        bg=self.colors['bg_dark'],
                        fg=self.colors['accent'],
                        font=('Segoe UI', 28, 'bold'))
        title.pack(pady=10)
        
        subtitle = tk.Label(header,
                           text="Planificación profesional para entrenadoras",
                           bg=self.colors['bg_dark'],
                           fg=self.colors['text_secondary'],
                           font=('Segoe UI', 12))
        subtitle.pack()
        
    def _crear_tab_plan(self, parent):
        tab = tk.Frame(parent, bg=self.colors['bg_dark'])
        
        # Scroll
        canvas = tk.Canvas(tab, bg=self.colors['bg_dark'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['bg_dark'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Contenedor izquierdo y derecho (2 columnas)
        left_frame = tk.Frame(scrollable_frame, bg=self.colors['bg_dark'])
        left_frame.pack(side='left', fill='both', expand=True, padx=10)
        
        right_frame = tk.Frame(scrollable_frame, bg=self.colors['bg_dark'])
        right_frame.pack(side='right', fill='both', expand=True, padx=10)
        
        # FORMULARIO (Izquierda)
        form_frame = self._crear_seccion(left_frame, "Datos del Entrenamiento", "⚙️")
        
        # Edad
        self._crear_campo_con_label(form_frame, "Rango de Edad:",
                                    ['8-10 años (Iniciación)',
                                     '11-13 años (Desarrollo)',
                                     '14-16 años (Perfeccionamiento)',
                                     '17+ años (Alto Rendimiento)'],
                                    self.edad_var)
        
        # Cantidad
        cantidad_frame = tk.Frame(form_frame, bg=self.colors['card_bg'])
        cantidad_frame.pack(fill='x', pady=12)
        
        tk.Label(cantidad_frame,
                text="Cantidad de Asistentes:",
                bg=self.colors['card_bg'],
                fg=self.colors['cyan'],
                font=('Segoe UI', 12, 'bold')).pack(anchor='w', pady=(0, 8))
        
        cantidad_entry = tk.Entry(cantidad_frame,
                                 textvariable=self.cantidad_var,
                                 bg=self.colors['bg_light'],
                                 fg=self.colors['text'],
                                 font=('Segoe UI', 13),
                                 insertbackground=self.colors['accent'],
                                 relief='flat',
                                 bd=0,
                                 highlightthickness=2,
                                 highlightcolor=self.colors['accent'],
                                 highlightbackground=self.colors['bg_light'])
        cantidad_entry.pack(fill='x', ipady=10)
        
        # Etapa
        self._crear_campo_con_label(form_frame, "Etapa de Entrenamiento:",
                                    list(self.etapas.keys()),
                                    self.etapa_var)
        
        # Fundamento
        self._crear_campo_con_label(form_frame, "Fundamento a Trabajar:",
                                    list(self.fundamentos.keys()),
                                    self.fundamento_var)
        
        # Botóngener con diseño llamativo
        btn_generar = tk.Button(form_frame,
                               text="⚡ GENERAR PLAN DE ENTRENAMIENTO",
                               bg=self.colors['secondary'],
                               fg=self.colors['text'],
                               font=('Segoe UI', 13, 'bold'),
                               relief='flat',
                               cursor='hand2',
                               command=self._generar_plan,
                               padx=25,
                               pady=18,
                               activebackground='#3d6cfe',
                               activeforeground='white',
                               borderwidth=0)
        btn_generar.pack(fill='x', pady=20)
        
        # Efectos hover
        btn_generar.bind('<Enter>', lambda e: btn_generar.config(bg='#3d6cfe'))
        btn_generar.bind('<Leave>', lambda e: btn_generar.config(bg=self.colors['secondary']))
        
        # Botón guardar con diseño secundario
        btn_guardar = tk.Button(form_frame,
                               text="💾 GUARDAR PLAN",
                               bg=self.colors['success'],
                               fg=self.colors['text'],
                               font=('Segoe UI', 11, 'bold'),
                               relief='flat',
                               cursor='hand2',
                               command=self._guardar_plan,
                               padx=20,
                               pady=12,
                               activebackground='#45a049',
                               borderwidth=0)
        btn_guardar.pack(fill='x', pady=(10, 0))
        
        # Efectos hover
        btn_guardar.bind('<Enter>', lambda e: btn_guardar.config(bg='#45a049'))
        btn_guardar.bind('<Leave>', lambda e: btn_guardar.config(bg=self.colors['success']))
        
        # Panel de estadísticas visuales
        stats_frame = tk.Frame(right_frame, bg=self.colors['bg_dark'])
        stats_frame.pack(fill='x', pady=(0, 10))
        
        self.stats_canvas = tk.Canvas(stats_frame, bg=self.colors['card_bg'], 
                                      height=120, highlightthickness=1,
                                      highlightbackground=self.colors['bg_light'])
        self.stats_canvas.pack(fill='x', padx=5)
        
        # RESULTADOS (Derecha)
        result_frame = self._crear_seccion(right_frame, "Plan Generado", "📋")
        
        self.resultado_text = scrolledtext.ScrolledText(result_frame,
                                                        bg=self.colors['bg_light'],
                                                        fg=self.colors['text'],
                                                        font=('Segoe UI', 10),
                                                        relief='flat',
                                                        wrap='word',
                                                        padx=15,
                                                        pady=15,
                                                        selectbackground=self.colors['accent'],
                                                        selectforeground='white')
        self.resultado_text.pack(fill='both', expand=True)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        return tab
        
    def _crear_tab_visualizacion(self, parent):
        tab = tk.Frame(parent, bg=self.colors['bg_dark'])
        
        # Panel de control superior con mejor diseño
        control_frame = tk.Frame(tab, bg=self.colors['card_bg'], highlightthickness=1,
                                highlightbackground=self.colors['bg_light'])
        control_frame.pack(fill='x', padx=10, pady=10)
        
        # Título
        tk.Label(control_frame,
                text="📊 Diagramas de Cancha",
                bg=self.colors['card_bg'],
                fg=self.colors['accent'],
                font=('Segoe UI', 14, 'bold')).pack(pady=(10, 5))
        
        tk.Label(control_frame,
                text="Selecciona el tipo de diagrama:",
                bg=self.colors['card_bg'],
                fg=self.colors['text_secondary'],
                font=('Segoe UI', 11)).pack(pady=(0, 10))
        
        diagramas = ['Cancha Completa', 'Formación W', 'Formación 3-2-1',
                    'Remate', 'Bloqueo', 'Ejercicio Parejas', 'Estaciones']
        
        diagrama_var = tk.StringVar()
        combo = ttk.Combobox(control_frame,
                            textvariable=diagrama_var,
                            values=diagramas,
                            state='readonly',
                            font=('Segoe UI', 11),
                            width=30)
        combo.pack(pady=10)
        combo.current(0)
        
        btn_mostrar = tk.Button(control_frame,
                               text="🔄 Mostrar Diagrama",
                               bg=self.colors['secondary'],
                               fg=self.colors['text'],
                               font=('Segoe UI', 11, 'bold'),
                               relief='flat',
                               cursor='hand2',
                               command=lambda: self._mostrar_diagrama(diagrama_var.get()),
                               padx=20,
                               pady=10,
                               activebackground='#3d6cfe',
                               borderwidth=0)
        btn_mostrar.pack(pady=(0, 15))
        
        # Efectos hover
        btn_mostrar.bind('<Enter>', lambda e: btn_mostrar.config(bg='#3d6cfe'))
        btn_mostrar.bind('<Leave>', lambda e: btn_mostrar.config(bg=self.colors['secondary']))
        
        # Canvas para dibujar
        canvas_frame = tk.Frame(tab, bg=self.colors['bg_dark'])
        canvas_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        self.canvas_cancha = tk.Canvas(canvas_frame,
                                       bg='#2d5016',
                                       highlightthickness=0)
        self.canvas_cancha.pack(fill='both', expand=True)
        
        # Mostrar diagrama inicial
        self.root.after(100, lambda: self._mostrar_diagrama('Cancha Completa'))
        
        return tab
        
    def _crear_tab_ejercicios(self, parent):
        tab = tk.Frame(parent, bg=self.colors['bg_dark'])
        
        # Frame superior con mejor diseño
        top_frame = tk.Frame(tab, bg=self.colors['card_bg'], highlightthickness=1,
                            highlightbackground=self.colors['bg_light'])
        top_frame.pack(fill='x', padx=10, pady=10)
        
         # Título
        tk.Label(top_frame,
                text="📚 Base de Datos de Ejercicios",
                bg=self.colors['card_bg'],
                fg=self.colors['accent'],
                font=('Segoe UI', 14, 'bold')).pack(pady=(10, 5))
        
        tk.Label(top_frame,
                text="Etapa de Entrenamiento:",
                bg=self.colors['card_bg'],
                fg=self.colors['cyan'],
                font=('Segoe UI', 11, 'bold')).pack(pady=(5, 10))
        
        etapa_ejercicios = tk.StringVar()
        combo = ttk.Combobox(top_frame,
                            textvariable=etapa_ejercicios,
                            values=list(self.etapas.keys()),
                            state='readonly',
                            font=('Segoe UI', 11),
                            width=30)
        combo.pack(side='left', padx=10)
        combo.current(0)
        
        btn_cargar = tk.Button(top_frame,
                              text="📖 Cargar Ejercicios",
                              bg=self.colors['secondary'],
                              fg=self.colors['text'],
                              font=('Segoe UI', 11, 'bold'),
                              relief='flat',
                              cursor='hand2',
                              command=lambda: self._cargar_ejercicios_etapa(etapa_ejercicios.get()),
                              padx=20,
                              pady=10,
                              activebackground='#3d6cfe',
                              borderwidth=0)
        btn_cargar.pack(pady=(0, 15))
        
        # Efectos hover
        btn_cargar.bind('<Enter>', lambda e: btn_cargar.config(bg='#3d6cfe'))
        btn_cargar.bind('<Leave>', lambda e: btn_cargar.config(bg=self.colors['secondary']))
        
        # Text area para ejercicios con marco
        text_container = tk.Frame(tab, bg=self.colors['card_bg'], highlightthickness=1,
                                 highlightbackground=self.colors['bg_light'])
        text_container.pack(fill='both', expand=True, padx=10, pady=(0, 10))
        
        self.ejercicios_text = scrolledtext.ScrolledText(text_container,
                                                         bg=self.colors['bg_light'],
                                                         fg=self.colors['text'],
                                                         font=('Segoe UI', 10),
                                                         relief='flat',
                                                         wrap='word',
                                                         padx=20,
                                                         pady=20,
                                                         selectbackground=self.colors['accent'])
        self.ejercicios_text.pack(fill='both', expand=True)
        
        # Cargar ejercicios iniciales
        self.root.after(100, lambda: self._cargar_ejercicios_etapa('Preparación General'))
        
        return tab
    
    def _crear_seccion(self, parent, titulo, icono=""):
        # Frame con efecto card
        frame = tk.Frame(parent, bg=self.colors['card_bg'], relief='flat', highlightthickness=1,
                        highlightbackground=self.colors['bg_light'])
        frame.pack(fill='both', expand=True, pady=10, padx=5)
        
        # Header con gradiente simulado
        header = tk.Frame(frame, bg=self.colors['accent'], height=50)
        header.pack(fill='x')
        
        # Contenedor para título e icono
        header_content = tk.Frame(header, bg=self.colors['accent'])
        header_content.pack(expand=True)
        
        titulo_completo = f"{icono} {titulo}" if icono else titulo
        
        tk.Label(header_content,
                text=titulo_completo,
                bg=self.colors['accent'],
                fg=self.colors['text'],
                font=('Segoe UI', 16, 'bold'),
                pady=15).pack()
        
        content = tk.Frame(frame, bg=self.colors['card_bg'])
        content.pack(fill='both', expand=True, padx=20, pady=20)
        
        return content
    
    def _crear_campo_con_label(self, parent, label_text, valores, variable):
        frame = tk.Frame(parent, bg=self.colors['card_bg'])
        frame.pack(fill='x', pady=12)
        
        tk.Label(frame,
                text=label_text,
                bg=self.colors['card_bg'],
                fg=self.colors['cyan'],
                font=('Segoe UI', 12, 'bold')).pack(anchor='w', pady=(0, 8))
        
        combo = ttk.Combobox(frame,
                            textvariable=variable,
                            values=valores,
                            state='readonly',
                            font=('Segoe UI', 11),
                            width=35)
        combo.pack(fill='x', ipady=5)
        
        if valores:
            combo.current(0)
    
    def _filtrar_ejercicios_por_fundamento(self, ejercicios, fundamento):
        """Filtra ejercicios según el fundamento seleccionado"""
        palabras_clave = {
            'saque': ['saque', 'servicio', 'servidor'],
            'recepcion': ['recepción', 'recepcion', 'pase de antebrazo', 'antebrazos', 'recibir'],
            'armado': ['armado', 'armada', 'levantada', 'dedos', 'colocación', 'colocacion', 'setter', 'pase de dedos'],
            'ataque': ['ataque', 'remate', 'rematar', 'atacante', 'spike'],
            'bloqueo': ['bloqueo', 'bloquear', 'bloqueador', 'block'],
            'defensa': ['defensa', 'defensivo', 'defender', 'planchar', 'salvada']
        }
        
        ejercicios_filtrados = {}
        keywords = palabras_clave.get(fundamento, [])
        
        if not keywords:
            return ejercicios
        
        for categoria, lista_ejercicios in ejercicios.items():
            ejercicios_categoria = []
            for ejercicio in lista_ejercicios:
                ejercicio_lower = ejercicio.lower()
                # Verificar si alguna palabra clave está en el ejercicio
                if any(keyword in ejercicio_lower for keyword in keywords):
                    ejercicios_categoria.append(ejercicio)
            
            # Si hay ejercicios filtrados para esta categoría, agregarlos
            if ejercicios_categoria:
                ejercicios_filtrados[categoria] = ejercicios_categoria
        
        # Si no hay ejercicios filtrados, añadir ejercicios genéricos relacionados
        if not ejercicios_filtrados:
            ejercicios_filtrados = self._crear_ejercicios_genericos_fundamento(fundamento)
        
        return ejercicios_filtrados
    
    def _crear_ejercicios_genericos_fundamento(self, fundamento):
        """Crea ejercicios genéricos para un fundamento específico"""
        ejercicios_genericos = {
            'saque': {
                'Calentamiento': [
                    'Calentamiento con movimientos de saque',
                    'Estiramiento de hombros y brazos'
                ],
                'Técnica_Saque': [
                    'Práctica de saque bajo individual',
                    'Saque por encima de la cabeza',
                    'Saque a zonas específicas de la cancha',
                    'Competencia de precisión de saque',
                    'Saque con diferentes tipos de efecto'
                ]
            },
            'recepcion': {
                'Calentamiento': [
                    'Calentamiento con pases de antebrazo',
                    'Movimientos laterales y posición baja'
                ],
                'Técnica_Recepción': [
                    'Recepción en parejas',
                    'Recepción de saque',
                    'Recepción con desplazamiento',
                    'Ejercicio W de recepción',
                    'Recepción a zona específica'
                ]
            },
            'armado': {
                'Calentamiento': [
                    'Calentamiento con pases de dedos',
                    'Ejercicios de muñecas y coordinación'
                ],
                'Técnica_Armado': [
                    'Pase de dedos en parejas',
                    'Armado desde diferentes posiciones',
                    'Armado a zona de ataque',
                    'Secuencia recepción-armado-ataque',
                    'Armado con desplazamiento'
                ]
            },
            'ataque': {
                'Calentamiento': [
                    'Calentamiento con saltos y aproximación',
                    'Ejercicios de coordinación de brazos'
                ],
                'Técnica_Ataque': [
                    'Aproximación y remate sin balón',
                    'Remate desde zona 4',
                    'Remate desde zona 2',
                    'Combinación armado-remate',
                    'Remate con oposición de bloqueo'
                ]
            },
            'bloqueo': {
                'Calentamiento': [
                    'Saltos y desplazamientos en red',
                    'Ejercicios de timing'
                ],
                'Técnica_Bloqueo': [
                    'Bloqueo individual en zonas',
                    'Desplazamiento lateral y bloqueo',
                    'Bloqueo doble coordinado',
                    'Lectura del atacante y bloqueo',
                    'Transición bloqueo-defensa'
                ]
            },
            'defensa': {
                'Calentamiento': [
                    'Calentamiento con posición baja',
                    'Ejercicios de reacción rápida'
                ],
                'Técnica_Defensa': [
                    'Defensa de ataques en posición 6',
                    'Defensa lateral con plancha',
                    'Ejercicio de salvadas',
                    'Defensa en 3 líneas',
                    'Transición defensa-contraataque'
                ]
            }
        }
        
        return ejercicios_genericos.get(fundamento, {
            'Ejercicios': ['Ejercicios básicos de ' + fundamento]
        })
    
    def _generar_plan(self):
        if not self.cantidad_var.get():
            messagebox.showwarning("Datos Incompletos", "Por favor ingresa la cantidad de asistentes")
            return
            
        try:
            cantidad = int(self.cantidad_var.get())
            if cantidad <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número mayor a 0")
            return
        
        edad = self.edad_var.get()
        etapa = self.etapa_var.get()
        fundamento = self.fundamento_var.get()
        fundamento_codigo = self.fundamentos.get(fundamento, 'todos')
        
        # Limpiar resultado
        self.resultado_text.delete('1.0', tk.END)
        
        # Generar plan
        plan = f"""
╔══════════════════════════════════════════════════════════════╗
║          📅 PLAN DE ENTRENAMIENTO GENERADO                   ║
╚══════════════════════════════════════════════════════════════╝

📆 Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}
👥 Asistentes: {cantidad} niñas
🎯 Edad: {edad}
📊 Etapa: {etapa}
🏐 Fundamento: {fundamento}

{'═' * 65}
📋 RECOMENDACIONES DE ORGANIZACIÓN
{'═' * 65}

"""
        
        # Recomendaciones según cantidad
        if cantidad <= 6:
            plan += f"""
✓ Grupo pequeño ({cantidad} niñas)
  • Trabajo técnico individualizado
  • Ejercicios en parejas o tríos
  • Atención personalizada alta
  • Juego: 3 vs 3 o minivoleibol
"""
        elif cantidad <= 12:
            plan += f"""
✓ Grupo mediano ({cantidad} niñas)
  • Dividir en 2 equipos de 6
  • Rotación por estaciones
  • Trabajo de equipo y técnica
  • Juego: 6 vs 6 con rotaciones
"""
        else:
            plan += f"""
✓ Grupo grande ({cantidad} niñas)
  • Dividir en {cantidad // 6} equipos de 6
  • Sistema de estaciones múltiples
  • Rotación cada 10-15 minutos
  • Juego: torneo entre equipos
"""
        
        plan += f"\n{'═' * 65}\n"
        plan += "💪 EJERCICIOS PROGRAMADOS\n"
        plan += f"{'═' * 65}\n\n"
        
        # Cargar ejercicios
        ejercicios = self.ejercicios_db.get(etapa, {})
        
        # Filtrar ejercicios por fundamento si no es "todos"
        if fundamento_codigo != 'todos':
            ejercicios = self._filtrar_ejercicios_por_fundamento(ejercicios, fundamento_codigo)
        
        tiempo_total = 0
        ejercicios_seleccionados = {}
        
        # Calcular y ajustar tiempos para no exceder 120 minutos
        categorias_lista = list(ejercicios.items())
        tiempo_por_categoria = self.TIEMPO_MAXIMO // len(categorias_lista) if categorias_lista else 0
        
        for i, (categoria, lista_ejercicios) in enumerate(categorias_lista, 1):
            # Tiempo base según categoría
            if 'calentamiento' in categoria.lower():
                tiempo = min(10, tiempo_por_categoria)
            elif 'acondicionamiento' in categoria.lower() or 'recuperacion' in categoria.lower():
                tiempo = min(15, tiempo_por_categoria)
            elif 'recreativo' in categoria.lower():
                tiempo = min(20, tiempo_por_categoria)
            else:
                tiempo = min(25, tiempo_por_categoria)
            
            # Verificar límite de tiempo
            if tiempo_total + tiempo > self.TIEMPO_MAXIMO:
                tiempo = self.TIEMPO_MAXIMO - tiempo_total
                if tiempo <= 0:
                    break
            
            tiempo_total += tiempo
            
            # Seleccionar ejercicios proporcionales al tiempo
            num_ejercicios = max(2, min(len(lista_ejercicios), tiempo // 5))
            ejercicios_cat = lista_ejercicios[:num_ejercicios]
            ejercicios_seleccionados[categoria] = ejercicios_cat
            
            plan += f"\n{i}. {categoria.replace('_', ' ').upper()}\n"
            plan += "-" * 65 + "\n"
            plan += f"⏱️  Duración: {tiempo} minutos\n\n"
            
            for j, ejercicio in enumerate(ejercicios_cat, 1):
                plan += f"   {j}. {ejercicio}\n"
            
            if tiempo_total >= self.TIEMPO_MAXIMO:
                break
        
        plan += f"\n{'═' * 65}\n"
        if tiempo_total > self.TIEMPO_MAXIMO:
            plan += f"⚠️  DURACIÓN AJUSTADA: {tiempo_total} minutos (límite: {self.TIEMPO_MAXIMO} min)\n"
        else:
            plan += f"⏱️  DURACIÓN TOTAL: {tiempo_total} minutos ({tiempo_total/60:.1f} horas)\n"
        plan += f"{'═' * 65}\n"
        
        # Insertar en el text widget
        self.resultado_text.insert('1.0', plan)
        
        # Guardar plan actual para poder guardarlo
        self.plan_actual = plan
        
        # Mostrar estadísticas visuales
        self._mostrar_estadisticas(tiempo_total, len(categorias_lista), cantidad)
        
        mensaje = f"Plan generado correctamente\nDuración: {tiempo_total} minutos"
        if tiempo_total > self.TIEMPO_MAXIMO:
            mensaje += f"\n⚠️ Ajustado al límite de {self.TIEMPO_MAXIMO} minutos"
        messagebox.showinfo("✅ Éxito", mensaje)
    
    def _guardar_plan(self):
        if not hasattr(self, 'plan_actual'):
            messagebox.showwarning("Advertencia", "Primero debes generar un plan")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
            initialfile=f"plan_entrenamiento_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(self.plan_actual)
                messagebox.showinfo("✅ Guardado", f"Plan guardado exitosamente en:\n{filename}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")
    
    def _mostrar_estadisticas(self, tiempo_total, num_categorias, cantidad):
        """Dibuja estadísticas visuales atractivas en el canvas"""
        self.stats_canvas.delete('all')
        width = self.stats_canvas.winfo_width()
        if width < 10:
            width = 800
        height = 120
        
        # Título
        self.stats_canvas.create_text(width // 2, 15,
                                      text="📊 Resumen del Plan",
                                      fill=self.colors['accent'],
                                      font=('Segoe UI', 14, 'bold'))
        
        # Tres tarjetas de estadísticas
        card_width = (width - 60) // 3
        y_start = 45
        
        stats = [
            ("⏱️", "DURACIÓN", f"{tiempo_total} min", self.colors['accent']),
            ("📚", "CATEGORÍAS", str(num_categorias), self.colors['secondary']),
            ("👥", "ASISTENTES", str(cantidad), self.colors['cyan'])
        ]
        
        for i, (icon, label, value, color) in enumerate(stats):
            x = 20 + (i * (card_width + 10))
            
            # Tarjeta
            self.stats_canvas.create_rectangle(x, y_start, x + card_width, y_start + 60,
                                              fill=self.colors['bg_light'],
                                              outline=color,
                                              width=2)
            
            # Icono y valor
            self.stats_canvas.create_text(x + card_width // 2, y_start + 18,
                                         text=f"{icon} {value}",
                                         fill=color,
                                         font=('Segoe UI', 16, 'bold'))
            
            # Label
            self.stats_canvas.create_text(x + card_width // 2, y_start + 43,
                                         text=label,
                                         fill=self.colors['text_secondary'],
                                         font=('Segoe UI', 9))
    
    def _mostrar_diagrama(self, tipo):
        self.canvas_cancha.delete('all')
        width = self.canvas_cancha.winfo_width()
        height = self.canvas_cancha.winfo_height()
        
        if width < 10:  # Canvas no inicializado
            width = 700
            height = 500
        
        if tipo == 'Cancha Completa':
            self._dibujar_cancha_completa(width, height)
        elif tipo == 'Formación W':
            self._dibujar_formacion_w(width, height)
        elif tipo == 'Formación 3-2-1':
            self._dibujar_formacion_321(width, height)
        elif tipo == 'Remate':
            self._dibujar_ejercicio_remate(width, height)
        elif tipo == 'Bloqueo':
            self._dibujar_ejercicio_bloqueo(width, height)
        elif tipo == 'Ejercicio Parejas':
            self._dibujar_ejercicio_parejas(width, height)
        elif tipo == 'Estaciones':
            self._dibujar_estaciones(width, height)
    
    def _dibujar_cancha_completa(self, width, height):
        # Centro
        cx, cy = width // 2, height // 2
        
        # Cancha
        cancha_w, cancha_h = min(width - 80, 500), min(height - 60, 300)
        x1, y1 = cx - cancha_w // 2, cy - cancha_h // 2
        x2, y2 = cx + cancha_w // 2, cy + cancha_h // 2
        
        # Fondo de cancha
        self.canvas_cancha.create_rectangle(x1, y1, x2, y2,
                                           fill='#2d5016',
                                           outline='white',
                                           width=3)
        
        # Red (línea central)
        self.canvas_cancha.create_line(x1, cy, x2, cy,
                                       fill='white',
                                       width=4)
        
        self.canvas_cancha.create_text(cx, cy - 20,
                                       text="RED",
                                       fill='yellow',
                                       font=('Segoe UI', 14, 'bold'))
        
        # Zonas de ataque (3 metros)
        zona_ataque = cancha_h // 4
        self.canvas_cancha.create_line(x1, y1 + zona_ataque, x2, y1 + zona_ataque,
                                       fill='white',
                                       width=2,
                                       dash=(5, 3))
        self.canvas_cancha.create_line(x1, y2 - zona_ataque, x2, y2 - zona_ataque,
                                       fill='white',
                                       width=2,
                                       dash=(5, 3))
        
        # Posiciones equipo superior
        self._dibujar_posicion(cx - cancha_w // 4, y1 + zona_ataque + 40, "5", "Zag Izq")
        self._dibujar_posicion(cx, y1 + zona_ataque + 40, "6", "Zag Centro")
        self._dibujar_posicion(cx + cancha_w // 4, y1 + zona_ataque + 40, "1", "Zag Der")
        
        self._dibujar_posicion(cx - cancha_w // 4, cy - 40, "4", "Del Izq")
        self._dibujar_posicion(cx, cy - 40, "3", "Colocador")
        self._dibujar_posicion(cx + cancha_w // 4, cy - 40, "2", "Del Der")
        
        # Posiciones equipo inferior
        self._dibujar_posicion(cx - cancha_w // 4, cy + 40, "2", "Del Der")
        self._dibujar_posicion(cx, cy + 40, "3", "Colocador")
        self._dibujar_posicion(cx + cancha_w // 4, cy + 40, "4", "Del Izq")
        
        self._dibujar_posicion(cx - cancha_w // 4, y2 - zona_ataque - 40, "1", "Zag Der")
        self._dibujar_posicion(cx, y2 - zona_ataque - 40, "6", "Zag Centro")
        self._dibujar_posicion(cx + cancha_w // 4, y2 - zona_ataque - 40, "5", "Zag Izq")
        
        # Etiquetas
        self.canvas_cancha.create_text(cx, y1 - 30,
                                       text="EQUIPO A",
                                       fill='white',
                                       font=('Segoe UI', 16, 'bold'))
        self.canvas_cancha.create_text(cx, y2 + 30,
                                       text="EQUIPO B",
                                       fill='white',
                                       font=('Segoe UI', 16, 'bold'))
        
        # Dimensiones
        self.canvas_cancha.create_text(cx, y2 + 60,
                                       text="📏 18m x 9m  |  Zona ataque: 3m",
                                       fill='#00d9ff',
                                       font=('Segoe UI', 11))
    
    def _dibujar_posicion(self, x, y, numero, nombre):
        # Círculo para jugadora
        r = 25
        self.canvas_cancha.create_oval(x - r, y - r, x + r, y + r,
                                       fill='#e94560',
                                       outline='white',
                                       width=2)
        
        self.canvas_cancha.create_text(x, y,
                                       text=numero,
                                       fill='white',
                                       font=('Segoe UI', 14, 'bold'))
        
        self.canvas_cancha.create_text(x, y + r + 15,
                                       text=nombre,
                                       fill='white',
                                       font=('Segoe UI', 8))
    
    def _dibujar_formacion_w(self, width, height):
        cx, cy = width // 2, height // 2
        cancha_w, cancha_h = min(width - 100, 600), min(height - 100, 450)
        
        x1, y1 = cx - cancha_w // 2, cy - cancha_h // 2
        x2, y2 = cx + cancha_w // 2, cy + cancha_h // 2
        
        # Cancha
        self.canvas_cancha.create_rectangle(x1, y1, x2, y2,
                                           fill='#2d5016',
                                           outline='white',
                                           width=3)
        
        # Red
        self.canvas_cancha.create_line(x1, cy, x2, cy, fill='white', width=4)
        self.canvas_cancha.create_text(cx, cy - 25, text="RED", fill='yellow',
                                       font=('Segoe UI', 14, 'bold'))
        
        # Título
        self.canvas_cancha.create_text(cx, y1 - 30,
                                       text="FORMACIÓN EN W (RECEPCIÓN)",
                                       fill='white',
                                       font=('Segoe UI', 18, 'bold'))
        
        # Posiciones en W
        # Zagueros
        self._dibujar_jugadora(cx - cancha_w // 3, y1 + 100, "Zag Izq")
        self._dibujar_jugadora(cx + cancha_w // 3, y1 + 100, "Zag Der")
        self._dibujar_jugadora(cx, y1 + 180, "Zag Centro")
        
        # Delanteros
        self._dibujar_jugadora(cx - cancha_w // 3, cy - 60, "Del Izq")
        self._dibujar_jugadora(cx + cancha_w // 3, cy - 60, "Del Der")
        
        # Saque
        self.canvas_cancha.create_text(cx, y2 - 40,
                                       text="🏐 DIRECCIÓN DEL SAQUE ↑",
                                       fill='#00d9ff',
                                       font=('Segoe UI', 12, 'bold'))
    
    def _dibujar_formacion_321(self, width, height):
        cx, cy = width // 2, height // 2
        cancha_w, cancha_h = min(width - 100, 600), min(height - 100, 450)
        
        x1, y1 = cx - cancha_w // 2, cy - cancha_h // 2
        x2, y2 = cx + cancha_w // 2, cy + cancha_h // 2
        
        # Cancha
        self.canvas_cancha.create_rectangle(x1, y1, x2, y2,
                                           fill='#2d5016',
                                           outline='white',
                                           width=3)
        
        # Red
        self.canvas_cancha.create_line(x1, cy, x2, cy, fill='white', width=4)
        
        # Título
        self.canvas_cancha.create_text(cx, y1 - 30,
                                       text="FORMACIÓN 3-2-1 (RECEPCIÓN)",
                                       fill='white',
                                       font=('Segoe UI', 18, 'bold'))
        
        # 1 Zaguero
        self._dibujar_jugadora(cx, y1 + 100, "Zag Centro")
        
        # 2 Laterales
        self._dibujar_jugadora(cx - cancha_w // 3, y1 + 170, "Lateral Izq")
        self._dibujar_jugadora(cx + cancha_w // 3, y1 + 170, "Lateral Der")
        
        # 3 Delanteros
        self._dibujar_jugadora(cx - cancha_w // 3, cy - 60, "Del Izq")
        self._dibujar_jugadora(cx, cy - 60, "Colocador")
        self._dibujar_jugadora(cx + cancha_w // 3, cy - 60, "Del Der")
    
    def _dibujar_ejercicio_remate(self, width, height, skip_title=False):
        cx, cy = width // 2, height // 2
        
        # Título
        if not skip_title:
            self.canvas_cancha.create_text(cx, 40,
                                           text="EJERCICIO: RECEPCIÓN → COLOCACIÓN → REMATE",
                                           fill='white',
                                           font=('Segoe UI', 18, 'bold'))
        
        # Cancha simplificada
        cancha_w, cancha_h = 500, 300
        x1, y1 = cx - cancha_w // 2, cy - cancha_h // 2
        x2, y2 = cx + cancha_w // 2, cy + cancha_h // 2
        
        self.canvas_cancha.create_rectangle(x1, y1, x2, y2,
                                           fill='#2d5016',
                                           outline='white',
                                           width=3)
        
        # Red
        self.canvas_cancha.create_line(x1, cy, x2, cy, fill='white', width=4)
        
        # Sacadora
        sac_x, sac_y = cx, y2 - 50
        self._dibujar_jugadora(sac_x, sac_y, "Sacadora")
        
        # Receptora
        rec_x, rec_y = cx - 100, cy + 80
        self._dibujar_jugadora(rec_x, rec_y, "Receptora")
        
        # Colocadora
        col_x, col_y = cx, cy - 80
        self._dibujar_jugadora(col_x, col_y, "Colocadora")
        
        # Rematadora
        rem_x, rem_y = cx + 150, cy - 100
        self._dibujar_jugadora(rem_x, rem_y, "Rematadora")
        
        # Flechas
        self._dibujar_flecha(sac_x, sac_y - 30, rec_x, rec_y - 30, "#00d9ff", "1. Saque")
        self._dibujar_flecha(rec_x, rec_y - 30, col_x, col_y + 30, "#ffa500", "2. Recepción")
        self._dibujar_flecha(col_x + 30, col_y, rem_x - 30, rem_y, "#e94560", "3. Colocación")
    
    def _dibujar_ejercicio_bloqueo(self, width, height, skip_title=False):
        cx, cy = width // 2, height // 2
        
        if not skip_title:
            self.canvas_cancha.create_text(cx, 40,
                                           text="EJERCICIO: BLOQUEO Y DEFENSA",
                                           fill='white',
                                           font=('Segoe UI', 18, 'bold'))
        
        # Cancha
        cancha_w, cancha_h = 500, 300
        x1, y1 = cx - cancha_w // 2, cy - cancha_h // 2
        x2, y2 = cx + cancha_w // 2, cy + cancha_h // 2
        
        self.canvas_cancha.create_rectangle(x1, y1, x2, y2,
                                           fill='#2d5016',
                                           outline='white',
                                           width=3)
        
        # Red
        self.canvas_cancha.create_line(x1, cy, x2, cy, fill='white', width=4)
        
        # Bloqueadoras (arriba)
        self._dibujar_jugadora(cx - 150, cy - 40, "Bloq 1")
        self._dibujar_jugadora(cx, cy - 40, "Bloq 2")
        self._dibujar_jugadora(cx + 150, cy - 40, "Bloq 3")
        
        # Defensoras (abajo)
        self._dibujar_jugadora(cx - 150, cy + 100, "Def Izq")
        self._dibujar_jugadora(cx, cy + 100, "Def Centro")
        self._dibujar_jugadora(cx + 150, cy + 100, "Def Der")
    
    def _dibujar_ejercicio_parejas(self, width, height):
        cx, cy = width // 2, height // 2
        
        self.canvas_cancha.create_text(cx, 40,
                                       text="EJERCICIO EN PAREJAS - PASES",
                                       fill='white',
                                       font=('Segoe UI', 18, 'bold'))
        
        # Parejas
        espaciado = 150
        inicio_y = 120
        
        for i in range(4):
            y = inicio_y + i * 120
            x1 = cx - 200
            x2 = cx + 200
            
            self._dibujar_jugadora(x1, y, f"J{i*2+1}")
            self._dibujar_jugadora(x2, y, f"J{i*2+2}")
            
            # Flecha bidireccional
            self.canvas_cancha.create_line(x1 + 30, y, x2 - 30, y,
                                          fill='#00d9ff',
                                          width=3,
                                          arrow='both')
    
    def _dibujar_estaciones(self, width, height):
        cx, cy = width // 2, height // 2
        
        self.canvas_cancha.create_text(cx, 40,
                                       text="ORGANIZACIÓN POR ESTACIONES",
                                       fill='white',
                                       font=('Segoe UI', 18, 'bold'))
        
        estaciones = [
            ("Estación 1\nPase de Dedos", cx - 300, cy - 150),
            ("Estación 2\nPase de Antebrazos", cx + 100, cy - 150),
            ("Estación 3\nSaques", cx - 300, cy + 100),
            ("Estación 4\nDefensa", cx + 100, cy + 100)
        ]
        
        for nombre, x, y in estaciones:
            # Rectángulo de estación
            self.canvas_cancha.create_rectangle(x - 100, y - 60, x + 100, y + 60,
                                               fill=self.colors['bg_light'],
                                               outline=self.colors['accent'],
                                               width=3)
            
            self.canvas_cancha.create_text(x, y,
                                          text=nombre,
                                          fill='white',
                                          font=('Segoe UI', 12, 'bold'),
                                          justify='center')
    
    def _dibujar_jugadora(self, x, y, nombre):
        r = 20
        self.canvas_cancha.create_oval(x - r, y - r, x + r, y + r,
                                       fill='#e94560',
                                       outline='white',
                                       width=2)
        
        self.canvas_cancha.create_text(x, y + r + 15,
                                       text=nombre,
                                       fill='white',
                                       font=('Segoe UI', 9, 'bold'))
    
    def _dibujar_flecha(self, x1, y1, x2, y2, color, texto=""):
        self.canvas_cancha.create_line(x1, y1, x2, y2,
                                       fill=color,
                                       width=3,
                                       arrow='last',
                                       arrowshape=(16, 20, 6))
        
        if texto:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            self.canvas_cancha.create_text(mx, my - 15,
                                          text=texto,
                                          fill=color,
                                          font=('Segoe UI', 10, 'bold'))
    
    def _visualizar_ejercicio_individual(self, nombre_ejercicio):
        """Detecta el tipo de ejercicio y muestra su visualización"""
        self.ejercicio_actual = nombre_ejercicio
        
        # Cambiar a la pestaña de visualización
        # (asumiendo que el notebook es accesible)
        
        nombre_lower = nombre_ejercicio.lower()
        
        # Detectar tipo de ejercicio
        if any(word in nombre_lower for word in ['parejas', 'duplas', 'dos']):
            self._dibujar_ejercicio_especifico_parejas(nombre_ejercicio)
        elif any(word in nombre_lower for word in ['círculo', 'circulo', 'rueda', 'ronda']):
            self._dibujar_ejercicio_especifico_circulo(nombre_ejercicio)
        elif any(word in nombre_lower for word in ['remate', 'atacar', 'ataque']):
            self._dibujar_ejercicio_especifico_remate(nombre_ejercicio)
        elif any(word in nombre_lower for word in ['bloqueo', 'bloque', 'bloq']):
            self._dibujar_ejercicio_especifico_bloqueo(nombre_ejercicio)
        elif any(word in nombre_lower for word in ['saque', 'servicio', 'sacar']):
            self._dibujar_ejercicio_especifico_saque(nombre_ejercicio)
        elif any(word in nombre_lower for word in ['recepción', 'recepcion', 'defensa']):
            self._dibujar_ejercicio_especifico_recepcion(nombre_ejercicio)
        elif any(word in nombre_lower for word in ['colocación', 'colocacion']):
            self._dibujar_ejercicio_especifico_colocacion(nombre_ejercicio)
        elif any(word in nombre_lower for word in ['pase', 'voleo', 'dedos', 'antebrazos']):
            self._dibujar_ejercicio_especifico_pases(nombre_ejercicio)
        elif any(word in nombre_lower for word in ['desplazamiento', 'movilidad', 'correr', 'trote']):
            self._dibujar_ejercicio_especifico_desplazamientos(nombre_ejercicio)
        elif any(word in nombre_lower for word in ['físico', 'fisico', 'fuerza', 'saltos', 'abdominales']):
            self._dibujar_ejercicio_especifico_fisico(nombre_ejercicio)
        else:
            # Ejercicio genérico
            self._dibujar_ejercicio_generico(nombre_ejercicio)
    
    def _dibujar_ejercicio_especifico_parejas(self, nombre):
        self.canvas_cancha.delete('all')
        width = self.canvas_cancha.winfo_width()
        height = self.canvas_cancha.winfo_height()
        if width < 10: width, height = 800, 600
        
        self.canvas_cancha.create_text(width//2, 40,
                                       text=f"EJERCICIO: {nombre.upper()}",
                                       fill='white',
                                       font=('Segoe UI', 16, 'bold'))
        
        # Dibujar ejercicio en parejas específico
        cx, cy = width // 2, height // 2
        sep = 180
        
        for i in range(3):
            y = cy - 150 + i * 150
            x1, x2 = cx - 250, cx + 50
            
            self._dibujar_jugadora(x1, y, f"J{i*2+1}")
            self._dibujar_jugadora(x2, y, f"J{i*2+2}")
            
            # Balón entre ellas
            self.canvas_cancha.create_oval(cx - 100 - 8, y - 8, cx - 100 + 8, y + 8,
                                          fill='#ffd700', outline='white', width=2)
            
            # Flecha bidireccional
            self.canvas_cancha.create_line(x1 + 25, y, x2 - 25, y,
                                          fill='#00d9ff', width=3, arrow='both')
        
        # Instrucciones
        self.canvas_cancha.create_text(width//2, height - 40,
                                       text="↔ Pases alternados entre parejas  •  🏐 Balón  •  👥 Jugadoras",
                                       fill='#00d9ff',
                                       font=('Segoe UI', 11))
    
    def _dibujar_ejercicio_especifico_circulo(self, nombre):
        self.canvas_cancha.delete('all')
        width = self.canvas_cancha.winfo_width()
        height = self.canvas_cancha.winfo_height()
        if width < 10: width, height = 800, 600
        
        cx, cy = width // 2, height // 2
        
        self.canvas_cancha.create_text(cx, 40,
                                       text=f"EJERCICIO: {nombre.upper()}",
                                       fill='white',
                                       font=('Segoe UI', 16, 'bold'))
        
        # Círculo de jugadoras
        num_jugadoras = 8
        radio = 150
        
        for i in range(num_jugadoras):
            angulo = (2 * math.pi / num_jugadoras) * i - math.pi/2
            x = cx + radio * math.cos(angulo)
            y = cy + radio * math.sin(angulo)
            
            self._dibujar_jugadora(x, y, f"J{i+1}")
            
            # Línea al centro
            self.canvas_cancha.create_line(x, y, cx, cy,
                                          fill='#00d9ff', width=1, dash=(3, 2))
        
        # Balón en el centro
        self.canvas_cancha.create_oval(cx - 12, cy - 12, cx + 12, cy + 12,
                                      fill='#ffd700', outline='white', width=3)
        
        self.canvas_cancha.create_text(cx, height - 40,
                                       text="Pases en secuencia  •  Mantener el balón en el aire",
                                       fill='#00d9ff',
                                       font=('Segoe UI', 11))
    
    def _dibujar_ejercicio_especifico_saque(self, nombre):
        self.canvas_cancha.delete('all')
        width = self.canvas_cancha.winfo_width()
        height = self.canvas_cancha.winfo_height()
        if width < 10: width, height = 800, 600
        
        cx, cy = width // 2, height // 2
        cancha_w, cancha_h = 500, 350
        
        x1, y1 = cx - cancha_w // 2, cy - cancha_h // 2
        x2, y2 = cx + cancha_w // 2, cy + cancha_h // 2
        
        self.canvas_cancha.create_text(cx, 40,
                                       text=f"EJERCICIO: {nombre.upper()}",
                                       fill='white',
                                       font=('Segoe UI', 16, 'bold'))
        
        # Cancha
        self.canvas_cancha.create_rectangle(x1, y1, x2, y2,
                                           fill='#2d5016', outline='white', width=3)
        self.canvas_cancha.create_line(x1, cy, x2, cy, fill='white', width=4)
        
        # Sacadoras (fila)
        for i in range(4):
            sx = x1 + 50 + i * 120
            sy = y2 - 50
            self._dibujar_jugadora(sx, sy, f"S{i+1}")
            
            # Trayectoria del saque
            tx = sx + (random.randint(-50, 50) if i % 2 else 0)
            ty = y1 + 80 + random.randint(0, 50)
            
            self.canvas_cancha.create_line(sx, sy - 25, tx, ty,
                                          fill='#ffd700', width=3,
                                          arrow='last', dash=(5, 3))
        
        self.canvas_cancha.create_text(cx, height - 40,
                                       text="🎯 Practicar técnica de saque  •  Apuntar a zonas específicas",
                                       fill='#00d9ff',
                                       font=('Segoe UI', 11))
    
    def _dibujar_ejercicio_especifico_recepcion(self, nombre):
        self.canvas_cancha.delete('all')
        width = self.canvas_cancha.winfo_width()
        height = self.canvas_cancha.winfo_height()
        if width < 10: width, height = 800, 600
        
        cx, cy = width // 2, height // 2
        
        self.canvas_cancha.create_text(cx, 40,
                                       text=f"EJERCICIO: {nombre.upper()}",
                                       fill='white',
                                       font=('Segoe UI', 16, 'bold'))
        
        # Cancha simplificada
        cancha_w, cancha_h = 500, 350
        x1, y1 = cx - cancha_w // 2, cy - cancha_h // 2
        x2, y2 = cx + cancha_w // 2, cy + cancha_h // 2
        
        self.canvas_cancha.create_rectangle(x1, y1, x2, y2,
                                           fill='#2d5016', outline='white', width=3)
        self.canvas_cancha.create_line(x1, cy, x2, cy, fill='white', width=4)
        
        # Formación W de recepción
        self._dibujar_jugadora(cx - 150, y1 + 100, "R1")
        self._dibujar_jugadora(cx + 150, y1 + 100, "R2")
        self._dibujar_jugadora(cx, y1 + 170, "R3")
        
        # Colocadora
        self._dibujar_jugadora(cx, cy - 60, "COL")
        
        # Balones llegando
        for i, x in enumerate([cx - 100, cx, cx + 100]):
            self.canvas_cancha.create_oval(x - 8, y2 - 100 - 8, x + 8, y2 - 100 + 8,
                                          fill='#ffd700', outline='white', width=2)
            # Flecha hacia receptoras
            self.canvas_cancha.create_line(x, y2 - 100, x, y1 + 120,
                                          fill='#00d9ff', width=2, arrow='last', dash=(3, 3))
        
        self.canvas_cancha.create_text(cx, height - 40,
                                       text="Formación W  •  Recepción a la colocadora",
                                       fill='#00d9ff',
                                       font=('Segoe UI', 11))
    
    def _dibujar_ejercicio_especifico_remate(self, nombre):
        """Ya existe, usar la función existente pero con título personalizado"""
        self.canvas_cancha.delete('all')
        width = self.canvas_cancha.winfo_width()
        height = self.canvas_cancha.winfo_height()
        if width < 10: width, height = 800, 600
        
        cx, cy = width // 2, height // 2
        
        self.canvas_cancha.create_text(cx, 40,
                                       text=f"EJERCICIO: {nombre.upper()}",
                                       fill='white',
                                       font=('Segoe UI', 16, 'bold'))
        
        # Reutilizar el código de remate existente
        self._dibujar_ejercicio_remate(width, height, skip_title=True)
    
    def _dibujar_ejercicio_especifico_bloqueo(self, nombre):
        """Usar función existente con título personalizado"""
        self.canvas_cancha.delete('all')
        width = self.canvas_cancha.winfo_width()
        height = self.canvas_cancha.winfo_height()
        if width < 10: width, height = 800, 600
        
        cx, cy = width // 2, height // 2
        
        self.canvas_cancha.create_text(cx, 40,
                                       text=f"EJERCICIO: {nombre.upper()}",
                                       fill='white',
                                       font=('Segoe UI', 16, 'bold'))
        
        self._dibujar_ejercicio_bloqueo(width, height, skip_title=True)
    
    def _dibujar_ejercicio_especifico_colocacion(self, nombre):
        self.canvas_cancha.delete('all')
        width = self.canvas_cancha.winfo_width()
        height = self.canvas_cancha.winfo_height()
        if width < 10: width, height = 800, 600
        
        cx, cy = width // 2, height // 2
        
        self.canvas_cancha.create_text(cx, 40,
                                       text=f"EJERCICIO: {nombre.upper()}",
                                       fill='white',
                                       font=('Segoe UI', 16, 'bold'))
        
        # Cancha
        cancha_w, cancha_h = 500, 350
        x1, y1 = cx - cancha_w // 2, cy - cancha_h // 2
        x2, y2 = cx + cancha_w // 2, cy + cancha_h // 2
        
        self.canvas_cancha.create_rectangle(x1, y1, x2, y2,
                                           fill='#2d5016', outline='white', width=3)
        self.canvas_cancha.create_line(x1, cy, x2, cy, fill='white', width=4)
        
        # Colocadora en zona 3
        col_x, col_y = cx, cy - 40
        self._dibujar_jugadora(col_x, col_y, "COL")
        
        # Rematadoras en zonas  2 y 4
        self._dibujar_jugadora(cx - 180, cy - 80, "Z4")
        self._dibujar_jugadora(cx + 180, cy - 80, "Z2")
        
        # Pasadora
        self._dibujar_jugadora(cx, cy + 100, "PAS")
        
        # Flechas de colocación
        self._dibujar_flecha(cx, cy + 100, col_x, col_y + 25, '#00d9ff', "1. Pase")
        self._dibujar_flecha(col_x - 20, col_y - 20, cx - 180, cy - 60, '#ffa500', "2. Coloc Z4")
        self._dibujar_flecha(col_x + 20, col_y - 20, cx + 180, cy - 60, '#e94560', "3. Coloc Z2")
        
        self.canvas_cancha.create_text(cx, height - 40,
                                       text="Colocación a diferentes zonas  •  Precisión y altura",
                                       fill='#00d9ff',
                                       font=('Segoe UI', 11))
    
    def _dibujar_ejercicio_especifico_pases(self, nombre):
        self.canvas_cancha.delete('all')
        width = self.canvas_cancha.winfo_width()
        height = self.canvas_cancha.winfo_height()
        if width < 10: width, height = 800, 600
        
        cx, cy = width // 2, height // 2
        
        self.canvas_cancha.create_text(cx, 40,
                                       text=f"EJERCICIO: {nombre.upper()}",
                                       fill='white',
                                       font=('Segoe UI', 16, 'bold'))
        
        # Triángulo de pases
        radio = 120
        for i in range(3):
            angulo = (2 * math.pi / 3) * i - math.pi/2
            x = cx + radio * math.cos(angulo)
            y = cy + radio * math.sin(angulo)
            
            self._dibujar_jugadora(x, y, f"J{i+1}")
            
            # Flecha al siguiente
            next_i = (i + 1) % 3
            next_angle = (2 * math.pi / 3) * next_i - math.pi/2
            next_x = cx + radio * math.cos(next_angle)
            next_y = cy + radio * math.sin(next_angle)
            
            # Punto medio para la flecha
            mid_x = (x + next_x) / 2
            mid_y = (y + next_y) / 2
            
            self.canvas_cancha.create_line(x, y, next_x, next_y,
                                          fill='#00d9ff', width=3, arrow='last')
        
        # Balón en el centro
        self.canvas_cancha.create_oval(cx - 10, cy - 10, cx + 10, cy + 10,
                                      fill='#ffd700', outline='white', width=2)
        
        self.canvas_cancha.create_text(cx, height - 40,
                                       text="🔄 Pases en triángulo  •  Mantener ritmo constante",
                                       fill='#00d9ff',
                                       font=('Segoe UI', 11))
    
    def _dibujar_ejercicio_especifico_desplazamientos(self, nombre):
        self.canvas_cancha.delete('all')
        width = self.canvas_cancha.winfo_width()
        height = self.canvas_cancha.winfo_height()
        if width < 10: width, height = 800, 600
        
        cx, cy = width // 2, height // 2
        
        self.canvas_cancha.create_text(cx, 40,
                                       text=f"EJERCICIO: {nombre.upper()}",
                                       fill='white',
                                       font=('Segoe UI', 16, 'bold'))
        
        # Patrón de desplazamiento en zigzag
        puntos = [
            (cx - 200, cy - 150),
            (cx + 200, cy - 100),
            (cx - 200, cy - 50),
            (cx + 200, cy),
            (cx - 200, cy + 50),
            (cx + 200, cy + 100),
            (cx - 200, cy + 150)
        ]
        
        # Dibujar línea de desplazamiento
        for i in range(len(puntos) - 1):
            x1, y1 = puntos[i]
            x2, y2 = puntos[i + 1]
            self.canvas_cancha.create_line(x1, y1, x2, y2,
                                          fill='#ffa500', width=4, arrow='last')
            
            # Conos en cada punto
            self.canvas_cancha.create_polygon(
                x1 - 10, y1 + 15,
                x1 + 10, y1 + 15,
                x1, y1 - 15,
                fill='#e94560', outline='white', width=2
            )
        
        # Jugadora en inicio
        self._dibujar_jugadora(puntos[0][0], puntos[0][1], "START")
        
        self.canvas_cancha.create_text(cx, height - 40,
                                       text="⚡ Desplazamientos laterales  •  Cambios de dirección rápidos",
                                       fill='#00d9ff',
                                       font=('Segoe UI', 11))
    
    def _dibujar_ejercicio_especifico_fisico(self, nombre):
        self.canvas_cancha.delete('all')
        width = self.canvas_cancha.winfo_width()
        height = self.canvas_cancha.winfo_height()
        if width < 10: width, height = 800, 600
        
        cx, cy = width // 2, height // 2
        
        self.canvas_cancha.create_text(cx, 40,
                                       text=f"EJERCICIO: {nombre.upper()}",
                                       fill='white',
                                       font=('Segoe UI', 16, 'bold'))
        
        # Estaciones de ejercicio físico
        ejercicios = [
            ("Sentadillas", cx - 250, cy - 120),
            ("Planchas", cx + 100, cy - 120),
            ("Saltos", cx - 250, cy + 80),
            ("Abdominales", cx + 100, cy + 80)
        ]
        
        for nombre_ej, x, y in ejercicios:
            # Área de ejercicio
            self.canvas_cancha.create_rectangle(x - 80, y - 50, x + 80, y + 50,
                                               fill=self.colors['bg_light'],
                                               outline=self.colors['accent'],
                                               width=3)
            
            self.canvas_cancha.create_text(x, y - 25,
                                          text=nombre_ej,
                                          fill='white',
                                          font=('Segoe UI', 12, 'bold'))
            
            # Iconos de jugadoras pequeñas
            for i in range(3):
                jx = x - 40 + i * 40
                jy = y + 15
                self.canvas_cancha.create_oval(jx - 8, jy - 8, jx + 8, jy + 8,
                                              fill=self.colors['accent'])
        
        self.canvas_cancha.create_text(cx, height - 40,
                                       text="💪 Acondicionamiento físico  •  Circuit training  •  Rotación cada estación",
                                       fill='#00d9ff',
                                       font=('Segoe UI', 11))
    
    def _dibujar_ejercicio_generico(self, nombre):
        self.canvas_cancha.delete('all')
        width = self.canvas_cancha.winfo_width()
        height = self.canvas_cancha.winfo_height()
        if width < 10: width, height = 800, 600
        
        cx, cy = width // 2, height // 2
        
        self.canvas_cancha.create_text(cx, 40,
                                       text=f"EJERCICIO: {nombre.upper()}",
                                       fill='white',
                                       font=('Segoe UI', 16, 'bold'))
        
        # Cancha genérica
        cancha_w, cancha_h = 500, 350
        x1, y1 = cx - cancha_w // 2, cy - cancha_h // 2
        x2, y2 = cx + cancha_w // 2, cy + cancha_h // 2
        
        self.canvas_cancha.create_rectangle(x1, y1, x2, y2,
                                           fill='#2d5016', outline='white', width=3)
        self.canvas_cancha.create_line(x1, cy, x2, cy, fill='white', width=4)
        
        # Jugadoras distribuidas
        posiciones = [
            (cx - 150, cy - 100), (cx, cy - 100), (cx + 150, cy - 100),
            (cx - 150, cy + 100), (cx, cy + 100), (cx + 150, cy + 100)
        ]
        
        for i, (x, y) in enumerate(posiciones):
            self._dibujar_jugadora(x, y, f"J{i+1}")
        
        self.canvas_cancha.create_text(cx, height - 40,
                                       text="🏐 Disposición general en cancha",
                                       fill='#00d9ff',
                                       font=('Segoe UI', 11))
    
    def _cargar_ejercicios_etapa(self, etapa):
        self.ejercicios_text.delete('1.0', tk.END)
        
        ejercicios = self.ejercicios_db.get(etapa, {})
        self.lista_ejercicios_plan = []
        
        texto = f"\n{'═' * 70}\n"
        texto += f"   EJERCICIOS - {etapa.upper()}\n"
        texto += f"{'═' * 70}\n\n"
        
        for categoria, lista in ejercicios.items():
            texto += f"\n📋 {categoria.replace('_', ' ').title()}:\n"
            texto += "-" * 70 + "\n"
            for i, ejercicio in enumerate(lista, 1):
                texto += f"   {i}. {ejercicio}\n"
                self.lista_ejercicios_plan.append(ejercicio)
            texto += "\n"
        
        self.ejercicios_text.insert('1.0', texto)
        
        # Agregar información de cómo visualizar
        info = "\n" + "="*70 + "\n"
        info += "💡 TIP: Haz doble clic en un ejercicio del plan para verlo en la cancha\n"
        info += "="*70 + "\n"
        self.ejercicios_text.insert('end', info)
        for categoria, lista in ejercicios.items():
            texto += f"\n📋 {categoria.replace('_', ' ').title()}:\n"
            texto += "-" * 70 + "\n"
            for i, ejercicio in enumerate(lista, 1):
                texto += f"   {i}. {ejercicio}\n"
            texto += "\n"
        
        self.ejercicios_text.insert('1.0', texto)
    
    def _cargar_ejercicios(self):
        return {
            'Preparación General': {
                'Calentamiento': [
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
                'Técnica Básica': [
                    'Posición básica y desplazamientos',
                    'Golpe de antebrazos contra la pared',
                    'Golpe de dedos en parejas',
                    'Saques de abajo',
                    'Recepción básica',
                    'Posición de defensa (en \"V\" o lista)',
                    'Movimientos de brazos con balón',
                    'Práctica de contacto suave con pelota',
                    'Pase de dedos individual contra pared',
                    'Coordinación de brazos y piernas',
                    'Toque de antebrazos contra pared',
                    'Control del balón en el aire'
                ],
                'Juegos Grupales': [
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
                'Coordinación y Habilidades': [
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
                'Acondicionamiento Suave': [
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
                'Calentamiento': [
                    'Trote con cambios de dirección',
                    'Desplazamientos defensivos',
                    'Pases en movimiento',
                    'Saltos de activación',
                    'Agilidad con cambios rápidos',
                    'Calentamiento específico por posición',
                    'Simulación de movimientos de juego'
                ],
                'Técnica Avanzada': [
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
                'Trabajo Grupal': [
                    'Rotaciones y posiciones',
                    'Cadena: recepción-colocación-remate',
                    'Bloqueo-defensa-contraataque',
                    'Juego dirigido 6 vs 6',
                    'Práctica de sistemas de juego',
                    'Coordinación entre posiciones',
                    'Situaciones de juego real'
                ],
                'Acondicionamiento': [
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
                'Calentamiento': [
                    'Activación cardiovascular intensa',
                    'Desplazamientos específicos',
                    'Pases en triángulo',
                    'Saltos y bloqueos',
                    'Simulación de situaciones competitivas',
                    'Calentamiento enfocado en técnica'
                ],
                'Táctica de Equipo': [
                    'Sistemas de recepción 3-1-2 / 3-2-1',
                    'Sistemas ofensivos 4-2 / 5-1',
                    'Jugadas ensayadas',
                    'Cobertura de bloqueo',
                    'Transiciones defensa-ataque',
                    'Temas defensivos específicos',
                    'Estrategias de ataque'
                ],
                'Simulación': [
                    'Set completo 6 vs 6',
                    'Situaciones de presión',
                    'Práctica de rotaciones',
                    'Estrategias vs formaciones',
                    'Simulaciones de partidos',
                    'Análisis de errores'
                ],
                'Acondicionamiento': [
                    'Intervalos alta intensidad',
                    'Circuito de potencia',
                    'Saltos explosivos',
                    'Recuperación activa',
                    'Trabajo específico de resistencia'
                ]
            },
            'Competitiva': {
                'Calentamiento': [
                    'Rutina de precompetencia',
                    'Activación neuromuscular',
                    'Práctica de remate y saque',
                    'Mentalización',
                    'Movimientos dinámicos'
                ],
                'Mantenimiento': [
                    'Repaso de jugadas clave',
                    'Ajustes tácticos',
                    'Situaciones críticas',
                    'Trabajo por posición',
                    'Set de práctica corto',
                    'Correcciones técnicas'
                ],
                'Estrategia': [
                    'Análisis del rival',
                    'Comunicación en cancha',
                    'Rotaciones optimizadas',
                    'Gestión de sustituciones',
                    'Tácticas especiales'
                ],
                'Recuperación': [
                    'Estiramientos prolongados',
                    'Trabajo de movilidad',
                    'Ejercicios de descarga',
                    'Hidratación',
                    'Enfoque mental'
                ]
            },
            'Transición': {
                'Calentamiento': [
                    'Actividad recreativa',
                    'Juegos lúdicos',
                    'Movilidad relajada',
                    'Ejercicios de bajo impacto'
                ],
                'Recreativo': [
                    'Vóley playa',
                    'Juegos modificados',
                    'Actividades multideportivas',
                    'Competencias divertidas',
                    'Juegos de coordinación',
                    'Actividades en grupo'
                ],
                'Recuperación Activa': [
                    'Yoga para atletas',
                    'Natación',
                    'Trote suave',
                    'Estiramientos',
                    'Juegos de coordinación',
                    'Actividad lúdica',
                    'Movilidad con ejercicios'
                ],
                'Evaluación': [
                    'Reflexión sobre temporada',
                    'Evaluación de progreso',
                    'Metas personales',
                    'Feedback grupal',
                    'Planificación futura'
                ]
            }
        }


if __name__ == "__main__":
    root = tk.Tk()
    app = EntrenamientoVoleibolGUI(root)
    root.mainloop()
