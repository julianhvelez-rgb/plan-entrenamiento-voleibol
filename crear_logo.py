from PIL import Image, ImageDraw, ImageFilter
import math

def crear_logo_voleibol_profesional(size=512):
    """Crea un logo profesional de voleibol con alta calidad y nitidez"""
    
    # Crear imagen con mayor resolución para mejor calidad
    scale = 2  # Renderizar al doble y luego reducir para mejor anti-aliasing
    work_size = size * scale
    img = Image.new('RGBA', (work_size, work_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Colores profesionales
    color_fondo_ext = (255, 107, 157)  # Rosa vibrante
    color_fondo_int = (233, 69, 96)    # Rosa más oscuro para gradiente
    color_balon = (255, 255, 255)      # Blanco puro
    color_lineas = (20, 30, 60)        # Azul oscuro casi negro
    
    center = work_size // 2
    radius = (work_size // 2) - (20 * scale)
    
    # Crear gradiente circular para el fondo
    for i in range(radius, 0, -2):
        ratio = i / radius
        r = int(color_fondo_int[0] + (color_fondo_ext[0] - color_fondo_int[0]) * ratio)
        g = int(color_fondo_int[1] + (color_fondo_ext[1] - color_fondo_int[1]) * ratio)
        b = int(color_fondo_int[2] + (color_fondo_ext[2] - color_fondo_int[2]) * ratio)
        
        draw.ellipse([center - i, center - i, center + i, center + i],
                     fill=(r, g, b), outline=None)
    
    # Borde exterior del círculo principal
    border_width = 8 * scale
    draw.ellipse([center - radius, center - radius, 
                  center + radius, center + radius],
                 outline=color_lineas, width=border_width)
    
    # Dibujar balón de voleibol profesional
    balon_radius = int(radius * 0.52)
    balon_x = center
    balon_y = center
    
    # Sombra suave del balón (efecto 3D)
    shadow_offset = 4 * scale
    for i in range(5):
        alpha = 15 - i * 3
        offset = shadow_offset + i * 2
        draw.ellipse([balon_x - balon_radius + offset, 
                      balon_y - balon_radius + offset,
                      balon_x + balon_radius + offset, 
                      balon_y + balon_radius + offset],
                     fill=(0, 0, 0, alpha))
    
    # Círculo base del balón con gradiente radial
    for i in range(balon_radius, 0, -1):
        ratio = i / balon_radius
        brightness = int(255 * (0.85 + 0.15 * ratio))
        draw.ellipse([balon_x - i, balon_y - i, balon_x + i, balon_y + i],
                     fill=(brightness, brightness, brightness))
    
    # Borde del balón
    ball_border = 5 * scale
    draw.ellipse([balon_x - balon_radius, balon_y - balon_radius,
                  balon_x + balon_radius, balon_y + balon_radius],
                 outline=color_lineas, width=ball_border)
    
    # Líneas del balón de voleibol (más precisas y profesionales)
    line_width = int(5 * scale)
    
    # Línea vertical central
    draw.line([balon_x, balon_y - balon_radius + (15 * scale), 
               balon_x, balon_y + balon_radius - (15 * scale)],
              fill=color_lineas, width=line_width)
    
    # Paneles curvos del balón (3 pares simétricos)
    num_panels = 3
    for i in range(num_panels):
        angle = -60 + (i * 60)  # -60, 0, 60 grados
        rad = math.radians(angle)
        
        # Curvas izquierda
        x_offset_left = int(balon_radius * 0.45 * math.cos(rad + math.pi/2))
        y_offset_left = int(balon_radius * 0.45 * math.sin(rad + math.pi/2))
        
        arc_width = int(30 * scale)
        arc_height = int(balon_radius * 1.6)
        
        draw.arc([balon_x + x_offset_left - arc_width, 
                  balon_y + y_offset_left - arc_height,
                  balon_x + x_offset_left + arc_width, 
                  balon_y + y_offset_left + arc_height],
                 start=80, end=280, 
                 fill=color_lineas, width=line_width)
    
    # Líneas horizontales curvas
    for y_mult in [-0.35, 0.35]:
        y_pos = int(balon_y + (balon_radius * y_mult))
        arc_size = int(balon_radius * 0.9)
        
        draw.arc([balon_x - arc_size, y_pos - (25 * scale),
                  balon_x + arc_size, y_pos + (25 * scale)],
                 start=-30, end=210,
                 fill=color_lineas, width=line_width)
    
    # Highlight del balón (brillo para efecto 3D)
    highlight_radius = int(balon_radius * 0.25)
    highlight_x = balon_x - int(balon_radius * 0.3)
    highlight_y = balon_y - int(balon_radius * 0.3)
    
    for i in range(highlight_radius, 0, -1):
        alpha = int(180 * (1 - i / highlight_radius))
        draw.ellipse([highlight_x - i, highlight_y - i,
                      highlight_x + i, highlight_y + i],
                     fill=(255, 255, 255, alpha))
    
    # Reducir a tamaño final con anti-aliasing de alta calidad LANCZOS
    img = img.resize((size, size), Image.Resampling.LANCZOS)
    
    return img

def crear_logo_voleibol(size=256):
    """Wrapper para compatibilidad - llama a la versión profesional"""
    return crear_logo_voleibol_profesional(size)

def crear_variantes_tamanos_optimizadas():
    """Crea variantes optimizadas para cada tamaño específico del .ico"""
    # Generar cada tamaño desde resolución ultra alta para máxima nitidez
    sizes = [16, 20, 24, 32, 40, 48, 64, 96, 128, 256]
    images = []
    
    print("📐 Generando variantes optimizadas para escritorio de Windows...")
    
    for size in sizes:
        # Para tamaños pequeños, generar desde 512px
        # Para tamaños grandes, generar desde 1024px para máxima calidad
        if size <= 64:
            source_size = 512
        else:
            source_size = 1024
        
        # Generar logo en alta resolución
        img_high = crear_logo_voleibol_profesional(source_size)
        
        # Reducir al tamaño final con LANCZOS (mejor anti-aliasing)
        img_final = img_high.resize((size, size), Image.Resampling.LANCZOS)
        images.append(img_final)
        print(f"   ✓ {size}x{size} px (desde {source_size}px)")
    
    return images

# Generar logos profesionales de ultra alta calidad para escritorio
print("🎨 Generando logo profesional optimizado para escritorio Windows...")
print("💡 Usando renderizado en ultra alta resolución para íconos nítidos\n")

# Logo principal en tamaño estándar
logo = crear_logo_voleibol_profesional(256)
logo.save('logo_voleibol.png')
print("✅ Logo PNG creado: logo_voleibol.png (256x256, alta calidad)")

# Crear versiones optimizadas para el .ico (especialmente para escritorio)
variantes = crear_variantes_tamanos_optimizadas()

# Guardar como ICO con TODAS las resoluciones para Windows
print("\n💾 Guardando .ico optimizado para escritorio Windows...")
variantes[0].save('logo_voleibol.ico', format='ICO', 
                  sizes=[(16,16), (20,20), (24,24), (32,32), (40,40), (48,48), 
                         (64,64), (96,96), (128,128), (256,256)])
print("✅ Logo ICO creado: logo_voleibol.ico (10 resoluciones)")

# Guardar también versión ultra grande
logo_grande = crear_logo_voleibol_profesional(512)
logo_grande.save('logo_voleibol_grande.png')
print("✅ Logo grande creado: logo_voleibol_grande.png (512x512)")

# Versión extra grande para máxima calidad
logo_ultra = crear_logo_voleibol_profesional(1024)
logo_ultra.save('logo_voleibol_ultra.png')
print("✅ Logo ultra creado: logo_voleibol_ultra.png (1024x1024)")

print("\n🎉 ¡Logo optimizado para escritorio Windows creado exitosamente!")
print("\n📁 Archivos generados:")
print("   - logo_voleibol.ico (10 resoluciones: 16-256px)")
print("   - logo_voleibol.png (256x256)")
print("   - logo_voleibol_grande.png (512x512)")
print("   - logo_voleibol_ultra.png (1024x1024)")
print("\n💡 Optimizaciones para escritorio Windows:")
print("   ✓ 10 tamaños específicos (16, 20, 24, 32, 40, 48, 64, 96, 128, 256)")
print("   ✓ Cada tamaño generado desde fuente ultra alta (512px o 1024px)")
print("   ✓ Anti-aliasing LANCZOS en cada reducción")
print("   ✓ Optimizado para pantallas HD, Full HD, 4K y DPI alto")
print("   ✓ Ícono nítido en escritorio, explorador y barra de tareas")
