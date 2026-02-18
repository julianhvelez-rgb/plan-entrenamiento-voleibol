"""
Script para crear iconos para la PWA - Versión completa con todos los tamaños
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_pwa_icon(size, output_path, is_maskable=False):
    """Crea un icono circular con el logo de voleibol"""
    # Para iconos maskable, agregar 20% de margen de seguridad
    if is_maskable:
        actual_size = int(size * 0.8)
        margin_offset = int((size - actual_size) / 2)
    else:
        actual_size = size
        margin_offset = 0
    
    # Crear imagen con fondo
    img = Image.new('RGB', (size, size), color='#ff6b9d' if is_maskable else '#0a0e27')
    draw = ImageDraw.Draw(img)
    
    # Si es maskable, dibujar fondo completo
    if is_maskable:
        draw.rectangle([0, 0, size, size], fill='#ff6b9d')
    
    # Dibujar círculo de fondo principal
    margin = int(actual_size * 0.1) + margin_offset
    circle_size = actual_size - int(actual_size * 0.2)
    circle_pos = margin_offset + int(actual_size * 0.1)
    
    draw.ellipse(
        [circle_pos, circle_pos, circle_pos + circle_size, circle_pos + circle_size], 
        fill='#0a0e27' if is_maskable else '#ff6b9d', 
        outline='#ffffff', 
        width=max(2, int(actual_size*0.02))
    )
    
    # Dibujar "red" de voleibol (líneas)
    center = size // 2
    line_width = max(2, int(actual_size * 0.03))
    
    # Línea vertical (red)
    line_height = circle_size - int(actual_size * 0.1)
    line_top = circle_pos + int(actual_size * 0.05)
    draw.rectangle(
        [center-line_width//2, line_top, center+line_width//2, line_top + line_height], 
        fill='#ffffff'
    )
    
    # Líneas horizontales (red)
    for i in range(3):
        y = line_top + line_height * i // 3
        line_left = circle_pos + int(actual_size * 0.05)
        line_right = circle_pos + circle_size - int(actual_size * 0.05)
        draw.rectangle(
            [line_left, y-line_width//2, line_right, y+line_width//2], 
            fill='#ffffff'
        )
    
    # Dibujar círculo (balón)
    ball_size = int(actual_size * 0.2)
    ball_x = center + int(actual_size * 0.12)
    ball_y = center - int(actual_size * 0.12)
    draw.ellipse(
        [ball_x-ball_size//2, ball_y-ball_size//2, ball_x+ball_size//2, ball_y+ball_size//2], 
        fill='#ffd700', 
        outline='#ffffff', 
        width=max(1, int(actual_size*0.01))
    )
    
    # Agregar detalles en el balón
    segment_width = max(1, int(actual_size*0.008))
    draw.arc(
        [ball_x-ball_size//2, ball_y-ball_size//2, ball_x+ball_size//2, ball_y+ball_size//2],
        0, 180, fill='#ffffff', width=segment_width
    )
    draw.arc(
        [ball_x-ball_size//2, ball_y-ball_size//2, ball_x+ball_size//2, ball_y+ball_size//2],
        90, 270, fill='#ffffff', width=segment_width
    )
    
    # Guardar
    img.save(output_path, 'PNG', optimize=True)
    print(f"✅ Icono creado: {output_path} ({size}x{size})")

def create_screenshot(output_path):
    """Crea una captura de pantalla simulada para la PWA"""
    width, height = 540, 720
    img = Image.new('RGB', (width, height), color='#0a0e27')
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([0, 0, width, 100], fill='#ff6b9d')
    
    # Título (simulado)
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    draw.text((width//2, 50), "🏐 Entrenamientos", fill='#ffffff', anchor="mm", font=font)
    
    # Cards simuladas
    card_colors = ['#1e2439', '#1a1f3a', '#252b48']
    for i in range(3):
        y_pos = 120 + i * 180
        draw.rectangle([20, y_pos, width-20, y_pos+150], fill=card_colors[i % len(card_colors)], outline='#ff6b9d', width=2)
        draw.text((40, y_pos+20), f"Ejercicio {i+1}", fill='#ffffff', font=font)
    
    img.save(output_path, 'PNG', optimize=True)
    print(f"✅ Screenshot creado: {output_path}")

# Crear directorio si no existe
os.makedirs('static/img', exist_ok=True)

# Tamaños estándar de iconos para PWA
sizes = [72, 96, 128, 144, 152, 192, 384, 512]

print("🎨 Creando iconos estándar...")
for size in sizes:
    create_pwa_icon(size, f'static/img/icon-{size}.png', is_maskable=False)

print("\n🎭 Creando iconos maskable (adaptables)...")
create_pwa_icon(192, 'static/img/icon-maskable-192.png', is_maskable=True)
create_pwa_icon(512, 'static/img/icon-maskable-512.png', is_maskable=True)

print("\n📸 Creando screenshot...")
create_screenshot('static/img/screenshot1.png')

print("\n🎉 ¡Todos los iconos PWA creados exitosamente!")
print("📱 La app ahora se instalará como aplicación independiente en Android")
