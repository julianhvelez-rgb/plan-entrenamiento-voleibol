
// ===============================
// APP DE ENTRENAMIENTO VOLEIBOL JS PURO
// ===============================

// Base de datos de ejercicios (simplificada y ampliable)
const ejerciciosDB = {
	"Preparación General": {
		"Calentamiento": [
			"Trote suave alrededor de la cancha (5 min)",
			"Movilidad articular completa",
			"Estiramientos dinámicos",
			"Juego de atrapar en parejas"
		],
		"Técnica Básica": [
			"Posición básica y desplazamientos",
			"Golpe de antebrazos contra la pared",
			"Golpe de dedos en parejas",
			"Saques de abajo",
			"Recepción básica"
		],
		"Juegos Grupales": [
			"Pase 10: mantener el balón sin que caiga",
			"Carrera de relevos con balón",
			"Círculo de pases (grupos de 5-6)",
			"Mini voleibol"
		],
		"Acondicionamiento": [
			"Sentadillas (3x10)",
			"Planchas (3x15-20 seg)",
			"Saltos (3x10)",
			"Abdominales (3x12)"
		]
	},
	"Preparación Específica": {
		"Calentamiento": [
			"Trote con cambios de dirección",
			"Desplazamientos defensivos",
			"Pases en movimiento",
			"Saltos de activación"
		],
		"Técnica Avanzada": [
			"Remate desde zona 4",
			"Bloqueo individual y en parejas",
			"Saques de arriba",
			"Recepción en formación W",
			"Colocación desde zona 3"
		],
		"Trabajo Grupal": [
			"Rotaciones y posiciones",
			"Cadena: recepción-colocación-remate",
			"Bloqueo-defensa-contraataque",
			"Juego dirigido 6 vs 6"
		],
		"Acondicionamiento": [
			"Saltos al cajón (3x8)",
			"Burpees (3x10)",
			"Desplazamientos (30s x3)",
			"Core: planchas laterales"
		]
	},
	"Precompetitiva": {
		"Calentamiento": [
			"Activación cardiovascular intensa",
			"Desplazamientos específicos",
			"Pases en triángulo",
			"Saltos y bloqueos"
		],
		"Táctica de Equipo": [
			"Sistemas de recepción 3-1-2 / 3-2-1",
			"Sistemas ofensivos 4-2 / 5-1",
			"Jugadas ensayadas",
			"Cobertura de bloqueo",
			"Transiciones defensa-ataque"
		],
		"Simulación": [
			"Set completo 6 vs 6",
			"Situaciones de presión",
			"Práctica de rotaciones",
			"Estrategias vs formaciones"
		],
		"Acondicionamiento": [
			"Intervalos alta intensidad",
			"Circuito de potencia",
			"Saltos explosivos",
			"Recuperación activa"
		]
	},
	"Competitiva": {
		"Calentamiento": [
			"Rutina de precompetencia",
			"Activación neuromuscular",
			"Práctica de remate y saque",
			"Mentalización"
		],
		"Mantenimiento": [
			"Repaso de jugadas clave",
			"Ajustes tácticos",
			"Situaciones críticas",
			"Trabajo por posición",
			"Set de práctica corto"
		],
		"Estrategia": [
			"Análisis del rival",
			"Comunicación en cancha",
			"Rotaciones optimizadas",
			"Gestión de sustituciones"
		],
		"Recuperación": [
			"Estiramientos prolongados",
			"Trabajo de movilidad",
			"Ejercicios de descarga",
			"Hidratación"
		]
	},
	"Transición": {
		"Calentamiento": [
			"Actividad recreativa",
			"Juegos lúdicos",
			"Movilidad relajada"
		],
		"Recreativo": [
			"Vóley playa",
			"Juegos modificados",
			"Actividades multideportivas",
			"Competencias divertidas"
		],
		"Recuperación Activa": [
			"Yoga para atletas",
			"Natación",
			"Trote suave",
			"Estiramientos",
			"Juegos de coordinación"
		],
		"Evaluación": [
			"Reflexión sobre temporada",
			"Evaluación de progreso",
			"Metas personales",
			"Feedback grupal"
		]
	}
};

// Utilidades
function shuffleArray(array) {
	const arr = array.slice();
	for (let i = arr.length - 1; i > 0; i--) {
		const j = Math.floor(Math.random() * (i + 1));
		[arr[i], arr[j]] = [arr[j], arr[i]];
	}
	return arr;
}

// Generar plan de entrenamiento
function generarPlan(params) {
	const etapa = params.etapa;
	const tiempo = parseInt(params.tiempo, 10);
	const fundamento = params.fundamento;
	const ejerciciosEtapa = ejerciciosDB[etapa];
	const categorias = Object.keys(ejerciciosEtapa);
	const tiempoPorCat = Math.floor(tiempo / categorias.length);
	const secciones = [];

	categorias.forEach(cat => {
		let lista = ejerciciosEtapa[cat];
		if (fundamento && fundamento !== 'todos') {
			// Filtrar por fundamento si aplica
			lista = lista.filter(ej => ej.toLowerCase().includes(fundamento));
			if (lista.length === 0) lista = ejerciciosEtapa[cat];
		}
		const ejerciciosCat = shuffleArray(lista).slice(0, Math.max(2, Math.floor(tiempoPorCat / 5)));
		secciones.push({
			nombre: cat,
			duracion: `${tiempoPorCat} min`,
			ejercicios: ejerciciosCat
		});
	});

	return {
		fecha: new Date().toLocaleDateString(),
		parametros: params,
		secciones,
		recomendaciones: [
			'Mantén la motivación alta y adapta el plan según el grupo.',
			'Recuerda hidratar y calentar bien antes de iniciar.'
		]
	};
}

// Mostrar plan generado
function mostrarPlan(plan) {
	const resultadoDiv = document.getElementById('resultado-plan');
	const detallesDiv = document.getElementById('plan-detalles');
	let html = `
		<div class="plan-info">
			<div class="plan-info-grid">
				<div class="plan-info-item"><div class="plan-info-label">👥 Edad</div><div class="plan-info-value">${plan.parametros.edad}</div></div>
				<div class="plan-info-item"><div class="plan-info-label">🔢 Jugadoras</div><div class="plan-info-value">${plan.parametros.cantidad}</div></div>
				<div class="plan-info-item"><div class="plan-info-label">📅 Etapa</div><div class="plan-info-value">${plan.parametros.etapa}</div></div>
				<div class="plan-info-item"><div class="plan-info-label">⏱️ Duración</div><div class="plan-info-value">${plan.parametros.tiempo} min</div></div>
			</div>
		</div>
		<div class="plan-secciones">
	`;
	plan.secciones.forEach(seccion => {
		html += `<div class="plan-section"><div class="plan-section-header"><h3 class="plan-section-title">${seccion.nombre}</h3><span class="plan-section-duration">${seccion.duracion}</span></div><div class="ejercicios-list">`;
		seccion.ejercicios.forEach(ejercicio => {
			html += `<div class="ejercicio-item">▪️ ${ejercicio}</div>`;
		});
		html += `</div></div>`;
	});
	html += `</div>`;
	if (plan.recomendaciones && plan.recomendaciones.length > 0) {
		html += `<div class="recomendaciones"><h3 class="plan-section-title">💡 Recomendaciones</h3>`;
		plan.recomendaciones.forEach(rec => {
			html += `<div class="recomendacion-item">${rec}</div>`;
		});
		html += `</div>`;
	}
	detallesDiv.innerHTML = html;
	resultadoDiv.style.display = 'block';
}

// Manejar formulario de plan
document.addEventListener('DOMContentLoaded', function() {
	// Tabs
	document.querySelectorAll('.tab-btn').forEach(btn => {
		btn.addEventListener('click', function() {
			document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
			document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
			this.classList.add('active');
			document.getElementById('tab-' + this.dataset.tab).classList.add('active');
		});
	});

	// Plan
	const form = document.getElementById('form-plan');
	form.addEventListener('submit', function(e) {
		e.preventDefault();
		const params = {
			edad: document.getElementById('edad').value,
			cantidad: document.getElementById('cantidad').value,
			etapa: document.getElementById('etapa').value,
			fundamento: document.getElementById('fundamento').value,
			tiempo: document.getElementById('tiempo').value
		};
		if (!params.edad || !params.cantidad || !params.etapa) {
			alert('Por favor completa todos los campos obligatorios');
			return;
		}
		const plan = generarPlan(params);
		mostrarPlan(plan);
		document.getElementById('resultado-plan').scrollIntoView({ behavior: 'smooth', block: 'start' });
	});

	// Range slider
	const rangeInput = document.getElementById('tiempo');
	const rangeValue = document.getElementById('tiempo-value');
	rangeInput.addEventListener('input', function() {
		rangeValue.textContent = `${this.value} min`;
	});

	// Consultar ejercicios
	document.getElementById('etapa-consulta').addEventListener('change', function() {
		const etapa = this.value;
		const listaDiv = document.getElementById('ejercicios-lista');
		if (!etapa) {
			listaDiv.innerHTML = '';
			return;
		}
		const ejercicios = ejerciciosDB[etapa];
		let html = '';
		for (const [categoria, lista] of Object.entries(ejercicios)) {
			html += `<div class="ejercicio-categoria"><h3 class="ejercicio-categoria-title">${categoria.toUpperCase()}</h3>`;
			lista.forEach(ejercicio => {
				html += `<div class="ejercicio-item">▪️ ${ejercicio}</div>`;
			});
			html += `</div>`;
		}
		listaDiv.innerHTML = html;
	});
});

// Funciones de impresión y compartir (simples)
function imprimirPlan() {
	window.print();
}
function compartirPlan() {
	alert('Para compartir, copia el texto o usa las opciones del navegador.');
}
function nuevoPlan() {
	document.getElementById('resultado-plan').style.display = 'none';
	document.getElementById('form-plan').reset();
	document.getElementById('tiempo-value').textContent = '90 min';
	window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Diagramas (igual que antes)
function mostrarDiagrama(tipo) {
	const display = document.getElementById('diagrama-display');
	let html = '';
	switch(tipo) {
		case 'cancha':
			html = `<h3 style="color: var(--color-accent); margin-bottom: 2rem;">CANCHA DE VOLEIBOL - ZONAS</h3><pre style="font-size: 0.9rem; line-height: 1.4; text-align: center;">        ┌────────────────────────────────────────────┐\n        │                  EQUIPO A                  │\n        │                                            │\n        │      [5]           [6]           [1]       │\n        │    Zaguero      Zaguero       Zaguero      │\n        │   Izquierdo     Central       Derecho      │\n        │                                            │\n        │      [4]           [3]           [2]       │\n        │   Delantero    Colocador     Delantero     │\n        │   Izquierdo                   Derecho      │\n        │                                            │\n        ├════════════════════════════════════════════┤  RED\n        │                                            │\n        │      [2]           [3]           [4]       │\n        │   Delantero    Colocador     Delantero     │\n        │   Derecho                    Izquierdo     │\n        │                                            │\n        │      [1]           [6]           [5]       │\n        │    Zaguero      Zaguero       Zaguero      │\n        │   Derecho       Central       Izquierdo    │\n        │                                            │\n        │                  EQUIPO B                  │\n        └────────────────────────────────────────────┘\n\n  📏 Dimensiones: 18m x 9m  |  🎯 Zona de ataque: 3m</pre>`;
			break;
		case 'formacion-w':
			html = `<h3 style="color: var(--color-accent); margin-bottom: 2rem;">FORMACIÓN EN W (RECEPCIÓN)</h3><pre style="font-size: 0.9rem; line-height: 1.4; text-align: center;">        ┌────────────────────────────────────────────┐\n        │                                            │\n        │         ●                  ●               │  Zagueros\n        │      Zag Izq           Zag Der             │\n        │                                            │\n        │                  ●                         │  Zaguero\n        │              Zag Central                   │  Central\n        │                                            │\n        │    ●                              ●        │  Delanteros\n        │  Del Izq                      Del Der      │  laterales\n        │                                            │\n        ├════════════════════════════════════════════┤  RED\n        │           🏐 Dirección del saque           │\n        └────────────────────────────────────────────┘\n\n  ● Jugadora receptora  |  Forma de W para cobertura</pre>`;
			break;
		case 'formacion-321':
			html = `<h3 style="color: var(--color-accent); margin-bottom: 2rem;">FORMACIÓN 3-2-1 (RECEPCIÓN)</h3><pre style="font-size: 0.9rem; line-height: 1.4; text-align: center;">        ┌────────────────────────────────────────────┐\n        │                                            │\n        │                  ●                         │  1 Zaguero\n        │              Zag Central                   │\n        │                                            │\n        │         ●                  ●               │  2 Laterales\n        │       Lateral           Lateral            │\n        │                                            │\n        │    ●          ●                ●           │  3 Delanteros\n        │  Del Izq   Colocador       Del Der         │\n        │                                            │\n        ├════════════════════════════════════════════┤  RED\n        │           🏐 Dirección del saque           │\n        └────────────────────────────────────────────┘\n\n  ● Jugadora  |  Tres líneas de recepción</pre>`;
			break;
		case 'rotaciones':
			html = `<h3 style="color: var(--color-accent); margin-bottom: 2rem;">SISTEMA DE ROTACIONES</h3><pre style="font-size: 0.9rem; line-height: 1.4; text-align: center;">        Rotación en sentido horario después de recuperar saque:\n\n                2 → 3 → 4\n                ↑       ↓\n                1 ← 6 ← 5\n\n        Posiciones:\n        1️⃣ Zaguero Derecho (Saque)\n        2️⃣ Delantero Derecho\n        3️⃣ Delantero Central (Colocador)\n        4️⃣ Delantero Izquierdo (Atacante principal)\n        5️⃣ Zaguero Izquierdo\n        6️⃣ Zaguero Central\n\n        Al recuperar el saque, todas rotan una posición en sentido horario.</pre>`;
			break;
	}
	display.innerHTML = html;
	display.scrollIntoView({ behavior: 'smooth', block: 'start' });
}
