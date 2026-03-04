// ==========================================
// JAVASCRIPT - ENTRENAMIENTO VOLEIBOL TABLETA
// ==========================================

// Variables globales
let planActual = null;
let deferredPrompt = null;

// Inicialización
document.addEventListener('DOMContentLoaded', function() {
    initTabs();
    initFormPlan();
    initConsultaEjercicios();
    initEntrenamientos6Minutos();
    initRangeSlider();
    initInstallPrompt();
    
    // Registrar Service Worker para PWA
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/sw.js', { scope: '/' })
            .then(registration => {
                console.log('✅ Service Worker registrado:', registration.scope);
                
                // Verificar estado
                if (registration.active) {
                    console.log('✅ Service Worker activo');
                }
            })
            .catch(error => {
                console.error('❌ Error al registrar Service Worker:', error);
            });
    }
    
    // Detectar si se está ejecutando como PWA
    if (window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone === true) {
        console.log('✅ Ejecutándose como PWA instalada');
        document.body.classList.add('pwa-mode');
    } else {
        console.log('📱 Ejecutándose en navegador');
    }
});

// ========== INSTALL PROMPT ==========
function initInstallPrompt() {
    const installPrompt = document.getElementById('install-prompt');
    const installButton = document.getElementById('install-button');
    const dismissButton = document.getElementById('dismiss-button');
    
    // Capturar el evento beforeinstallprompt
    window.addEventListener('beforeinstallprompt', (e) => {
        console.log('🎉 beforeinstallprompt activado - La app ES instalable');
        
        // Prevenir el prompt automático de Chrome
        e.preventDefault();
        
        // Guardar el evento para usarlo después
        deferredPrompt = e;
        
        // Mostrar nuestro botón de instalación personalizado
        installPrompt.style.display = 'block';
    });
    
    // Manejar clic en botón "Instalar Ahora"
    installButton.addEventListener('click', async () => {
        if (!deferredPrompt) {
            console.log('❌ No hay prompt disponible');
            alert('La instalación no está disponible. Intenta:\n\n1. Cerrar Chrome completamente\n2. Borrar caché de Chrome\n3. Volver a abrir esta página');
            return;
        }
        
        // Ocultar nuestro prompt
        installPrompt.style.display = 'none';
        
        // Mostrar el prompt de instalación
        deferredPrompt.prompt();
        
        // Esperar la respuesta del usuario
        const { outcome } = await deferredPrompt.userChoice;
        console.log(`🎯 Usuario eligió: ${outcome}`);
        
        if (outcome === 'accepted') {
            console.log('✅ Usuario aceptó la instalación');
        } else {
            console.log('❌ Usuario rechazó la instalación');
        }
        
        // Limpiar el prompt
        deferredPrompt = null;
    });
    
    // Manejar clic en "Más tarde"
    dismissButton.addEventListener('click', () => {
        installPrompt.style.display = 'none';
        console.log('⏰ Usuario pospuso la instalación');
    });
    
    // Detectar cuando la app fue instalada
    window.addEventListener('appinstalled', (evt) => {
        console.log('✅ ¡App instalada exitosamente!');
        installPrompt.style.display = 'none';
    });
    
    // Verificar si beforeinstallprompt no se activa (debugging)
    setTimeout(() => {
        if (!deferredPrompt && !window.matchMedia('(display-mode: standalone)').matches) {
            console.log('⚠️ beforeinstallprompt NO se activó después de 3 segundos');
            console.log('Posibles causas:');
            console.log('- Service Worker no registrado correctamente');
            console.log('- Manifest.json con errores');
            console.log('- Ya está instalada');
            console.log('- Chrome no reconoce criterios de instalabilidad');
        }
    }, 3000);
}

// ========== TABS ==========
function initTabs() {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const tabId = this.dataset.tab;
            
            // Remover active de todos
            tabBtns.forEach(b => b.classList.remove('active'));
            tabContents.forEach(c => c.classList.remove('active'));
            
            // Agregar active al seleccionado
            this.classList.add('active');
            document.getElementById(`tab-${tabId}`).classList.add('active');
        });
    });
}

// ========== FORM PLAN ==========
function initFormPlan() {
    const form = document.getElementById('form-plan');
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = {
            edad: document.getElementById('edad').value,
            cantidad: document.getElementById('cantidad').value,
            etapa: document.getElementById('etapa').value,
            fundamento: document.getElementById('fundamento').value,
            tiempo: document.getElementById('tiempo').value
        };
        
        // Validación
        if (!formData.edad || !formData.cantidad || !formData.etapa) {
            showToast('⚠️ Por favor completa todos los campos obligatorios', 'warning');
            return;
        }
        
        showLoading();
        
        try {
            const response = await fetch('/api/generar-plan', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });
            
            if (!response.ok) {
                throw new Error('Error al generar el plan');
            }
            
            planActual = await response.json();
            mostrarPlan(planActual);
            hideLoading();
            showToast('✅ Plan generado exitosamente', 'success');
            
            // Scroll al resultado
            document.getElementById('resultado-plan').scrollIntoView({ 
                behavior: 'smooth', 
                block: 'start' 
            });
            
        } catch (error) {
            hideLoading();
            showToast('❌ Error al generar el plan: ' + error.message, 'error');
            console.error('Error:', error);
        }
    });
}

function mostrarPlan(plan) {
    const resultadoDiv = document.getElementById('resultado-plan');
    const detallesDiv = document.getElementById('plan-detalles');
    
    let html = `
        <div class="plan-info">
            <div class="plan-info-grid">
                <div class="plan-info-item">
                    <div class="plan-info-label">👥 Edad</div>
                    <div class="plan-info-value">${plan.parametros.edad}</div>
                </div>
                <div class="plan-info-item">
                    <div class="plan-info-label">🔢 Jugadoras</div>
                    <div class="plan-info-value">${plan.parametros.cantidad}</div>
                </div>
                <div class="plan-info-item">
                    <div class="plan-info-label">📅 Etapa</div>
                    <div class="plan-info-value">${plan.parametros.etapa}</div>
                </div>
                <div class="plan-info-item">
                    <div class="plan-info-label">⏱️ Duración</div>
                    <div class="plan-info-value">${plan.parametros.tiempo} min</div>
                </div>
            </div>
        </div>
        
        <div class="plan-secciones">
    `;
    
    // Agregar secciones de ejercicios
    plan.secciones.forEach(seccion => {
        html += `
            <div class="plan-section">
                <div class="plan-section-header">
                    <h3 class="plan-section-title">${seccion.nombre}</h3>
                    <span class="plan-section-duration">${seccion.duracion}</span>
                </div>
                <div class="ejercicios-list">
        `;
        
        seccion.ejercicios.forEach(ejercicio => {
            html += `<div class="ejercicio-item">▪️ ${ejercicio}</div>`;
        });
        
        html += `
                </div>
            </div>
        `;
    });
    
    html += `</div>`;
    
    // Agregar recomendaciones
    if (plan.recomendaciones && plan.recomendaciones.length > 0) {
        html += `
            <div class="recomendaciones">
                <h3 class="plan-section-title">💡 Recomendaciones</h3>
        `;
        
        plan.recomendaciones.forEach(rec => {
            html += `<div class="recomendacion-item">${rec}</div>`;
        });
        
        html += `</div>`;
    }
    
    detallesDiv.innerHTML = html;
    resultadoDiv.style.display = 'block';
}

// ========== CONSULTA EJERCICIOS ==========
function initConsultaEjercicios() {
    const selectEtapa = document.getElementById('etapa-consulta');
    
    selectEtapa.addEventListener('change', async function() {
        const etapa = this.value;
        
        if (!etapa) {
            document.getElementById('ejercicios-lista').innerHTML = '';
            return;
        }
        
        try {
            const response = await fetch(`/api/ejercicios/${encodeURIComponent(etapa)}`);
            
            if (!response.ok) {
                throw new Error('Error al obtener ejercicios');
            }
            
            const ejercicios = await response.json();
            mostrarEjercicios(ejercicios);
            
        } catch (error) {
            showToast('❌ Error al cargar ejercicios: ' + error.message, 'error');
            console.error('Error:', error);
        }
    });
}

function mostrarEjercicios(ejercicios) {
    const listaDiv = document.getElementById('ejercicios-lista');
    
    let html = '';
    
    for (const [categoria, lista] of Object.entries(ejercicios)) {
        html += `
            <div class="ejercicio-categoria">
                <h3 class="ejercicio-categoria-title">${categoria.replace('_', ' ').toUpperCase()}</h3>
        `;
        
        lista.forEach(ejercicio => {
            html += `<div class="ejercicio-item">▪️ ${ejercicio}</div>`;
        });
        
        html += `</div>`;
    }
    
    listaDiv.innerHTML = html;
}

// ========== ENTRENAMIENTOS 6 MINUTOS ==========
function initEntrenamientos6Minutos() {
    const etapaSelect = document.getElementById('etapa-6min');
    const sesionSelect = document.getElementById('sesion-6min');
    const detalleDiv = document.getElementById('entrenamiento-6min-detalle');

    if (!etapaSelect || !sesionSelect || !detalleDiv) {
        return;
    }

    etapaSelect.addEventListener('change', async function() {
        const etapa = this.value;
        detalleDiv.innerHTML = '';

        if (!etapa) {
            sesionSelect.innerHTML = '<option value="">Primero selecciona una etapa...</option>';
            sesionSelect.disabled = true;
            return;
        }

        try {
            const response = await fetch(`/api/entrenamientos-6min?etapa=${encodeURIComponent(etapa)}`);
            if (!response.ok) {
                throw new Error('No se pudieron cargar las sesiones');
            }

            const data = await response.json();
            sesionSelect.innerHTML = '<option value="">Seleccionar sesión...</option>';

            data.sesiones.forEach(sesion => {
                const option = document.createElement('option');
                option.value = sesion.id;
                option.textContent = sesion.nombre;
                sesionSelect.appendChild(option);
            });

            sesionSelect.disabled = false;
            showToast('✅ Sesiones cargadas', 'success');
        } catch (error) {
            sesionSelect.innerHTML = '<option value="">Error al cargar sesiones</option>';
            sesionSelect.disabled = true;
            showToast('❌ ' + error.message, 'error');
        }
    });

    sesionSelect.addEventListener('change', async function() {
        const etapa = etapaSelect.value;
        const sesion = this.value;

        if (!etapa || !sesion) {
            detalleDiv.innerHTML = '';
            return;
        }

        try {
            const response = await fetch(
                `/api/entrenamientos-6min?etapa=${encodeURIComponent(etapa)}&sesion=${encodeURIComponent(sesion)}`
            );
            if (!response.ok) {
                throw new Error('No se pudo cargar el detalle de la sesión');
            }

            const data = await response.json();
            mostrarDetalle6Min(data, detalleDiv);
        } catch (error) {
            detalleDiv.innerHTML = '';
            showToast('❌ ' + error.message, 'error');
        }
    });
}

function mostrarDetalle6Min(data, contenedor) {
    const sesion = data.sesion;

    const fases = [
        { key: 'inicio', titulo: '🟢 Inicio (Individual)' },
        { key: 'desarrollo', titulo: '🟡 Desarrollo (Parejas/Tríos)' },
        { key: 'final', titulo: '🔴 Final (Grupos)' }
    ];

    let html = `
        <div class="plan-info">
            <div class="plan-info-grid">
                <div class="plan-info-item">
                    <div class="plan-info-label">📅 Etapa</div>
                    <div class="plan-info-value">${data.etapa}</div>
                </div>
                <div class="plan-info-item">
                    <div class="plan-info-label">⏱️ Bloque Base</div>
                    <div class="plan-info-value">${data.duracion_base}</div>
                </div>
                <div class="plan-info-item">
                    <div class="plan-info-label">🔄 Cambio</div>
                    <div class="plan-info-value">cada ${data.cambio_cada}</div>
                </div>
            </div>
        </div>

        <div class="plan-section">
            <div class="plan-section-header">
                <h3 class="plan-section-title">${sesion.nombre}</h3>
                <span class="plan-section-duration">${data.refuerzo_equipo}</span>
            </div>
        </div>
    `;

    fases.forEach(fase => {
        const bloque = sesion[fase.key];
        html += `
            <div class="plan-section">
                <div class="plan-section-header">
                    <h3 class="plan-section-title">${fase.titulo}</h3>
                    <span class="plan-section-duration">${bloque.duracion}</span>
                </div>
                <div class="ejercicio-item">Modalidad: ${bloque.tipo}</div>
        `;

        bloque.ejercicios.forEach(ejercicio => {
            html += `<div class="ejercicio-item">▪️ ${ejercicio}</div>`;
        });

        html += `</div>`;
    });

    html += `
        <div class="recomendaciones">
            <h3 class="plan-section-title">💡 Lógica de Progresión</h3>
            <div class="recomendacion-item">Inicia en trabajo individual técnico.</div>
            <div class="recomendacion-item">Cambia cada 3 minutos a interacción en parejas/tríos.</div>
            <div class="recomendacion-item">Extiende con bloque grupal para reforzar trabajo en equipo.</div>
        </div>
    `;

    contenedor.innerHTML = html;
    contenedor.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ========== DIAGRAMAS ==========
function mostrarDiagrama(tipo) {
    const display = document.getElementById('diagrama-display');
    let html = '';
    
    switch(tipo) {
        case 'cancha':
            html = `
                <h3 style="color: var(--color-accent); margin-bottom: 2rem;">CANCHA DE VOLEIBOL - ZONAS</h3>
                <pre style="font-size: 0.9rem; line-height: 1.4; text-align: center;">
        ┌────────────────────────────────────────────┐
        │                  EQUIPO A                  │
        │                                            │
        │      [5]           [6]           [1]       │
        │    Zaguero      Zaguero       Zaguero      │
        │   Izquierdo     Central       Derecho      │
        │                                            │
        │      [4]           [3]           [2]       │
        │   Delantero    Colocador     Delantero     │
        │   Izquierdo                   Derecho      │
        │                                            │
        ├════════════════════════════════════════════┤  RED
        │                                            │
        │      [2]           [3]           [4]       │
        │   Delantero    Colocador     Delantero     │
        │   Derecho                    Izquierdo     │
        │                                            │
        │      [1]           [6]           [5]       │
        │    Zaguero      Zaguero       Zaguero      │
        │   Derecho       Central       Izquierdo    │
        │                                            │
        │                  EQUIPO B                  │
        └────────────────────────────────────────────┘

  📏 Dimensiones: 18m x 9m  |  🎯 Zona de ataque: 3m
                </pre>
            `;
            break;
            
        case 'formacion-w':
            html = `
                <h3 style="color: var(--color-accent); margin-bottom: 2rem;">FORMACIÓN EN W (RECEPCIÓN)</h3>
                <pre style="font-size: 0.9rem; line-height: 1.4; text-align: center;">
        ┌────────────────────────────────────────────┐
        │                                            │
        │         ●                  ●               │  Zagueros
        │      Zag Izq           Zag Der             │
        │                                            │
        │                  ●                         │  Zaguero
        │              Zag Central                   │  Central
        │                                            │
        │    ●                              ●        │  Delanteros
        │  Del Izq                      Del Der      │  laterales
        │                                            │
        ├════════════════════════════════════════════┤  RED
        │           🏐 Dirección del saque           │
        └────────────────────────────────────────────┘

  ● Jugadora receptora  |  Forma de W para cobertura
                </pre>
            `;
            break;
            
        case 'formacion-321':
            html = `
                <h3 style="color: var(--color-accent); margin-bottom: 2rem;">FORMACIÓN 3-2-1 (RECEPCIÓN)</h3>
                <pre style="font-size: 0.9rem; line-height: 1.4; text-align: center;">
        ┌────────────────────────────────────────────┐
        │                                            │
        │                  ●                         │  1 Zaguero
        │              Zag Central                   │
        │                                            │
        │         ●                  ●               │  2 Laterales
        │       Lateral           Lateral            │
        │                                            │
        │    ●          ●                ●           │  3 Delanteros
        │  Del Izq   Colocador       Del Der         │
        │                                            │
        ├════════════════════════════════════════════┤  RED
        │           🏐 Dirección del saque           │
        └────────────────────────────────────────────┘

  ● Jugadora  |  Tres líneas de recepción
                </pre>
            `;
            break;
            
        case 'rotaciones':
            html = `
                <h3 style="color: var(--color-accent); margin-bottom: 2rem;">SISTEMA DE ROTACIONES</h3>
                <pre style="font-size: 0.9rem; line-height: 1.4; text-align: center;">
        Rotación en sentido horario después de recuperar saque:

                2 → 3 → 4
                ↑       ↓
                1 ← 6 ← 5

        Posiciones:
        1️⃣ Zaguero Derecho (Saque)
        2️⃣ Delantero Derecho
        3️⃣ Delantero Central (Colocador)
        4️⃣ Delantero Izquierdo (Atacante principal)
        5️⃣ Zaguero Izquierdo
        6️⃣ Zaguero Central

        Al recuperar el saque, todas rotan una posición en sentido horario.
                </pre>
            `;
            break;
    }
    
    display.innerHTML = html;
    display.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ========== RANGE SLIDER ==========
function initRangeSlider() {
    const rangeInput = document.getElementById('tiempo');
    const rangeValue = document.getElementById('tiempo-value');
    
    rangeInput.addEventListener('input', function() {
        rangeValue.textContent = `${this.value} min`;
    });
}

// ========== UTILIDADES ==========
function showLoading() {
    document.getElementById('loading').style.display = 'flex';
}

function hideLoading() {
    document.getElementById('loading').style.display = 'none';
}

function showToast(message, type = 'success') {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.className = 'toast show';
    
    if (type === 'warning') {
        toast.style.background = 'var(--color-warning)';
    } else if (type === 'error') {
        toast.style.background = '#f44336';
    } else {
        toast.style.background = 'var(--color-success)';
    }
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

function nuevoPlan() {
    document.getElementById('resultado-plan').style.display = 'none';
    document.getElementById('form-plan').reset();
    document.getElementById('tiempo-value').textContent = '90 min';
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function imprimirPlan() {
    window.print();
}

function compartirPlan() {
    if (navigator.share && planActual) {
        const texto = generarTextoPlano(planActual);
        
        navigator.share({
            title: '🏐 Plan de Entrenamiento',
            text: texto
        }).then(() => {
            showToast('✅ Plan compartido exitosamente', 'success');
        }).catch((error) => {
            // Si falla share, copiar al portapapeles
            copiarAlPortapapeles(texto);
        });
    } else if (planActual) {
        // Fallback: copiar al portapapeles
        const texto = generarTextoPlano(planActual);
        copiarAlPortapapeles(texto);
    }
}

function generarTextoPlano(plan) {
    let texto = `🏐 PLAN DE ENTRENAMIENTO DE VOLEIBOL\n`;
    texto += `Fecha: ${plan.fecha}\n\n`;
    texto += `📋 PARÁMETROS:\n`;
    texto += `▪️ Edad: ${plan.parametros.edad}\n`;
    texto += `▪️ Jugadoras: ${plan.parametros.cantidad}\n`;
    texto += `▪️ Etapa: ${plan.parametros.etapa}\n`;
    texto += `▪️ Duración: ${plan.parametros.tiempo} min\n\n`;
    
    texto += `📝 EJERCICIOS:\n\n`;
    
    plan.secciones.forEach(seccion => {
        texto += `${seccion.nombre} (${seccion.duracion}):\n`;
        seccion.ejercicios.forEach(ejercicio => {
            texto += `  ▪️ ${ejercicio}\n`;
        });
        texto += `\n`;
    });
    
    if (plan.recomendaciones && plan.recomendaciones.length > 0) {
        texto += `💡 RECOMENDACIONES:\n`;
        plan.recomendaciones.forEach(rec => {
            texto += `${rec}\n`;
        });
    }
    
    return texto;
}

function copiarAlPortapapeles(texto) {
    if (navigator.clipboard) {
        navigator.clipboard.writeText(texto).then(() => {
            showToast('📋 Plan copiado al portapapeles', 'success');
        }).catch(() => {
            showToast('⚠️ No se pudo copiar el plan', 'warning');
        });
    } else {
        // Fallback para navegadores antiguos
        const textarea = document.createElement('textarea');
        textarea.value = texto;
        textarea.style.position = 'fixed';
        textarea.style.opacity = '0';
        document.body.appendChild(textarea);
        textarea.select();
        
        try {
            document.execCommand('copy');
            showToast('📋 Plan copiado al portapapeles', 'success');
        } catch (err) {
            showToast('⚠️ No se pudo copiar el plan', 'warning');
        }
        
        document.body.removeChild(textarea);
    }
}

// ========== PREVENIR ZOOM EN DOBLE TAP ==========
let lastTouchEnd = 0;
document.addEventListener('touchend', function(event) {
    const now = (new Date()).getTime();
    if (now - lastTouchEnd <= 300) {
        event.preventDefault();
    }
    lastTouchEnd = now;
}, false);
