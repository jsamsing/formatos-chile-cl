"""Todo el texto de formatos-chile.cl. Cada formato tiene campos, una plantilla con {campo} y texto legal verificado
(Código del Trabajo y Dirección del Trabajo). Revisar si cambia la ley y actualizar REVISADO."""

DOMINIO = "https://formatos-chile.cl"
MARCA = "Formatos Chile"
REVISADO = "2026-11-23"
GA4 = "G-9BR5XRGH80"
INDEXNOW_KEY = "8b2d4f6a1c3e5a7b9d0f2e4c6a8b1d3f"

RED = [
    {"url": "https://horadechile.cl/", "nombre": "Hora de Chile", "texto": "Hora exacta y cambio de hora", "vivo": True},
    {"url": "https://feriados-de-chile.cl/", "nombre": "Feriados de Chile", "texto": "Feriados y fines de semana largos", "vivo": True},
    {"url": "https://formatos-chile.cl/", "nombre": "Formatos Chile", "texto": "Cartas y documentos listos para usar", "vivo": True},
    {"url": "https://calculadora-chile.cl/", "nombre": "Calculadora Chile", "texto": "Sueldo líquido, IVA, UF y más", "vivo": False},
]

AVISOS = [
    {"id": "searchlab", "icono": "pin", "url": "https://www.searchlab.cl/?utm_source=formatoschile&utm_medium=aviso&utm_campaign=casa",
     "titulo": "¿Tu negocio aparece en Google Maps?", "texto": "Página web, ficha de Google Maps y preparación para buscadores con IA desde $9.990 al mes.", "cta": "Ver planes"},
    {"id": "bifrok", "icono": "wifi", "url": "https://bifrok.com/es-cl/?utm_source=formatoschile&utm_medium=aviso&utm_campaign=casa",
     "titulo": "¿Te cambias de casa o de trabajo?", "texto": "Compara planes de fibra, TV y Starlink en tu nueva comuna y habla con un vendedor.", "cta": "Comparar planes"},
]

FIRMA = "\n\n\n____________________________\n{nombre}\nRUT {rut}"

FORMATOS = [
    {"slug": "carta-de-renuncia-voluntaria", "nombre": "Carta de renuncia voluntaria",
     "title": "Carta de renuncia voluntaria: formato para completar Chile",
     "desc": "Formato de carta de renuncia voluntaria para Chile: complétalo, cópialo o descárgalo en Word o PDF. Incluye el aviso de 30 días y cómo ratificarla.",
     "corta": "La carta de renuncia voluntaria se entrega por escrito y con al menos 30 días de anticipación (artículo 159 N.º 2 del Código del Trabajo). Para que el empleador pueda invocarla, debe ratificarse ante un ministro de fe: inspector del trabajo, notario u oficial del Registro Civil, o en línea en el portal Mi DT con ClaveÚnica.",
     "campos": [("ciudad", "Ciudad", "Santiago"), ("fecha", "Fecha de la carta", "23 de noviembre de 2026"), ("empresa", "Empresa", "Comercial Los Andes SpA"),
                ("cargo", "Tu cargo", "asistente administrativo"), ("ultimo_dia", "Último día de trabajo", "23 de diciembre de 2026"),
                ("nombre", "Tu nombre completo", "María José Pérez Soto"), ("rut", "Tu RUT", "12.345.678-9")],
     "plantilla": "{ciudad}, {fecha}\n\nSeñores\n{empresa}\nPresente\n\nDe mi consideración:\n\nMediante esta carta presento mi renuncia voluntaria a mi cargo de {cargo} en {empresa}, según el artículo 159 número 2 del Código del Trabajo.\n\nDoy el aviso con la anticipación que indica la ley: mi último día de trabajo será el {ultimo_dia}.\n\nAgradezco la confianza y lo aprendido durante este tiempo, y quedo disponible para dejar mis tareas en orden antes de mi salida.\n\nSaluda atentamente," + FIRMA,
     "pasos": ["Entrega la carta firmada al empleador y pide una copia con fecha y firma de recibido.",
               "Ratifícala ante un ministro de fe: Inspección del Trabajo, notaría u oficial del Registro Civil, o en línea en Mi DT (dt.gob.cl) con tu ClaveÚnica.",
               "Si avisas con menos de 30 días, la renuncia igual vale: según la Dirección del Trabajo, el empleador no puede descontar de tu finiquito los días de aviso que faltaron.",
               "Después del término, revisa que el finiquito incluya vacaciones pendientes y remuneraciones adeudadas."],
     "faqs": [("¿Con cuántos días de anticipación hay que renunciar?", "Con al menos 30 días, según el artículo 159 N.º 2 del Código del Trabajo. Si avisas con menos, la renuncia no queda inválida y el empleador no puede descontar esos días del finiquito."),
              ("¿Dónde se ratifica la renuncia?", "Ante un ministro de fe: inspector del trabajo, notario u oficial del Registro Civil, o de forma electrónica en el portal Mi DT de la Dirección del Trabajo, con ClaveÚnica."),
              ("¿Tengo que explicar por qué renuncio?", "No. Basta con indicar que renuncias, tu cargo y tu último día de trabajo.")]},
    {"slug": "carta-de-amonestacion", "nombre": "Carta de amonestación",
     "title": "Carta de amonestación: formato y ejemplo para empresas",
     "desc": "Formato de carta de amonestación escrita para trabajadores en Chile: complétalo con el hecho, la fecha y la norma del reglamento interno, y descárgalo.",
     "corta": "La carta de amonestación es una sanción escrita que el empleador entrega al trabajador por una falta concreta. Solo puede aplicarse si la falta y la sanción están en el reglamento interno de la empresa (artículo 154 del Código del Trabajo), y debe describir el hecho con fecha.",
     "campos": [("ciudad", "Ciudad", "Temuco"), ("fecha", "Fecha", "23 de noviembre de 2026"), ("trabajador", "Nombre del trabajador", "Juan Carlos Muñoz Díaz"),
                ("cargo", "Cargo del trabajador", "bodeguero"), ("hecho", "Hecho que se sanciona", "llegó 45 minutos tarde sin aviso ni justificación"),
                ("fecha_hecho", "Fecha del hecho", "20 de noviembre de 2026"), ("norma", "Norma del reglamento interno", "artículo 12 del Reglamento Interno de Orden, Higiene y Seguridad"),
                ("empresa", "Empresa", "Distribuidora del Sur Ltda."), ("nombre", "Nombre de quien firma", "Paula Rojas Fuentes"), ("rut", "RUT de quien firma", "15.678.901-2")],
     "plantilla": "{ciudad}, {fecha}\n\nSeñor(a)\n{trabajador}\n{cargo}\nPresente\n\nRef.: Amonestación escrita\n\nPor medio de esta carta, {empresa} le comunica una amonestación escrita por el siguiente hecho: el {fecha_hecho}, usted {hecho}.\n\nEsta conducta infringe el {norma}, que establece la amonestación escrita como sanción.\n\nLe pedimos ajustar su conducta a las normas de la empresa. Usted puede presentar sus descargos por escrito si no está de acuerdo con esta medida.\n\nSe entrega copia de esta carta al trabajador.\n\nAtentamente," + FIRMA + "\nEn representación de {empresa}\n\n\nRecibí copia: ____________________   Fecha: ____________",
     "pasos": ["Describe un solo hecho, con fecha y de forma objetiva, sin adjetivos.",
               "Cita la norma del reglamento interno que se infringió: si no está en el reglamento, la sanción no corresponde.",
               "Entrega una copia al trabajador y pídele que firme el recibo; si se niega, deja constancia con un testigo.",
               "Guarda la carta en la carpeta del trabajador."],
     "faqs": [("¿Una carta de amonestación es despido?", "No. Es una sanción escrita por una falta concreta y no termina el contrato."),
              ("¿Qué pasa si el trabajador no firma?", "La firma solo acredita que la recibió. Si se niega, deja constancia con un testigo de que se le entregó.")]},
    {"slug": "carta-de-presentacion", "nombre": "Carta de presentación",
     "title": "Carta de presentación para trabajo: formato y ejemplo simple",
     "desc": "Formato de carta de presentación para postular a un trabajo en Chile: complétalo con el cargo, tu experiencia y tus datos, y descárgalo en Word o PDF.",
     "corta": "La carta de presentación acompaña tu currículum: en tres o cuatro párrafos cuenta a qué cargo postulas, qué experiencia o habilidades aportas y cómo contactarte. Conviene adaptarla a cada empresa y no repetir el CV completo.",
     "campos": [("ciudad", "Ciudad", "Valparaíso"), ("fecha", "Fecha", "23 de noviembre de 2026"), ("empresa", "Empresa a la que postulas", "Hotel Puerto Alegre"),
                ("cargo", "Cargo al que postulas", "recepcionista"), ("experiencia", "Tu experiencia principal", "dos años de atención a público en un hostal de Valparaíso"),
                ("habilidad", "Algo que te distingue", "manejo inglés intermedio y sistemas de reservas"), ("nombre", "Tu nombre", "Camila Andrea Torres Vera"),
                ("telefono", "Teléfono", "+56 9 1234 5678"), ("correo", "Correo", "camila.torres@correo.cl")],
     "plantilla": "{ciudad}, {fecha}\n\nSeñores\n{empresa}\nPresente\n\nEstimados:\n\nLes escribo para postular al cargo de {cargo} en {empresa}.\n\nCuento con {experiencia}, y además {habilidad}. Me interesa aportar esa experiencia a su equipo y seguir creciendo en el área.\n\nAdjunto mi currículum con el detalle de mi experiencia. Quedo disponible para una entrevista cuando les acomode.\n\nMuchas gracias por su tiempo.\n\nSaludos cordiales,\n\n{nombre}\n{telefono} · {correo}",
     "pasos": ["Adapta la carta a cada postulación: nombra la empresa y el cargo exacto.",
               "Destaca uno o dos logros concretos, no todo tu currículum.",
               "Revisa la ortografía y que tus datos de contacto estén correctos.",
               "Envíala junto al CV, en PDF si es por correo."],
     "faqs": [("¿Qué largo debe tener una carta de presentación?", "Una página como máximo: tres o cuatro párrafos breves bastan."),
              ("¿Se firma la carta de presentación?", "Si la envías por correo no es necesario firmarla; basta con tu nombre y tus datos de contacto.")]},
    {"slug": "carta-de-recomendacion-laboral", "nombre": "Carta de recomendación laboral",
     "title": "Carta de recomendación laboral: formato para completar",
     "desc": "Formato de carta de recomendación laboral para Chile: completa los datos del trabajador, su cargo, tiempo y fortalezas, y descárgala en Word o PDF.",
     "corta": "La carta de recomendación laboral la firma un jefe o empleador para respaldar a un trabajador ante otra empresa. Debe indicar el cargo, el período trabajado, las fortalezas observadas y un contacto para verificar la información.",
     "campos": [("ciudad", "Ciudad", "Concepción"), ("fecha", "Fecha", "23 de noviembre de 2026"), ("trabajador", "Nombre del trabajador", "Diego Ignacio Soto Lagos"),
                ("rut_trabajador", "RUT del trabajador", "18.234.567-8"), ("cargo", "Cargo que tuvo", "vendedor"), ("empresa", "Empresa", "Ferretería El Roble"),
                ("periodo", "Período trabajado", "marzo de 2023 a octubre de 2026"), ("fortalezas", "Fortalezas", "responsable, puntual y con muy buen trato con los clientes"),
                ("nombre", "Nombre de quien recomienda", "Rodrigo Pizarro Leiva"), ("cargo_firma", "Cargo de quien recomienda", "jefe de ventas"), ("rut", "RUT de quien recomienda", "11.222.333-4"), ("telefono", "Teléfono de contacto", "+56 9 8765 4321")],
     "plantilla": "{ciudad}, {fecha}\n\nA quien corresponda:\n\nRecomiendo a {trabajador}, RUT {rut_trabajador}, quien se desempeñó como {cargo} en {empresa} entre {periodo}.\n\nDurante ese tiempo demostró ser una persona {fortalezas}. Cumplió sus funciones de buena forma y dejó una buena impresión en el equipo.\n\nPor lo anterior, lo recomiendo sin reservas para cualquier cargo similar. Quedo disponible para entregar más referencias al teléfono {telefono}.\n\nAtentamente," + FIRMA + "\n{cargo_firma}, {empresa}",
     "pasos": ["La firma un jefe directo o el empleador, con su cargo y un teléfono de contacto.",
               "Indica fechas reales de inicio y término: es lo primero que verifican.",
               "Menciona fortalezas concretas que hayas observado.",
               "Entrégala en PDF o impresa y firmada."],
     "faqs": [("¿Quién puede firmar una carta de recomendación laboral?", "Un jefe directo, el dueño de la empresa o alguien de recursos humanos que conozca el trabajo de la persona."),
              ("¿Es obligatorio dar una carta de recomendación?", "No; la empresa no está obligada. Distinto es el certificado de antigüedad laboral, que solo acredita el período trabajado.")]},
    {"slug": "poder-simple", "nombre": "Poder simple",
     "title": "Poder simple: formato para autorizar un trámite en Chile",
     "desc": "Formato de poder simple para Chile: autoriza a otra persona a hacer un trámite en tu nombre. Complétalo, imprímelo y fírmalo. Te decimos cuándo no sirve.",
     "corta": "El poder simple es un documento firmado por ti, sin notario, que autoriza a otra persona a hacer un trámite específico en tu nombre, como retirar un documento. Muchas instituciones exigen además la copia de la cédula de ambos, y algunos trámites piden poder notarial: confírmalo antes de ir.",
     "campos": [("ciudad", "Ciudad", "Rancagua"), ("fecha", "Fecha", "23 de noviembre de 2026"), ("nombre", "Tu nombre (quien da el poder)", "Luis Alberto Reyes Campos"),
                ("rut", "Tu RUT", "9.876.543-2"), ("apoderado", "Nombre de quien hará el trámite", "Fernanda Reyes González"), ("rut_apoderado", "RUT de quien hará el trámite", "20.111.222-3"),
                ("tramite", "Trámite que autorizas", "retirar mi licencia de conducir"), ("institucion", "Ante qué institución", "la Dirección de Tránsito de la Municipalidad de Rancagua")],
     "plantilla": "PODER SIMPLE\n\n{ciudad}, {fecha}\n\nYo, {nombre}, RUT {rut}, autorizo a {apoderado}, RUT {rut_apoderado}, para que en mi nombre y representación pueda {tramite} ante {institucion}.\n\nEste poder se otorga solo para el trámite indicado." + FIRMA + "\n\nSe adjunta copia de la cédula de identidad de ambas personas.",
     "pasos": ["Escribe un solo trámite y la institución, lo más preciso posible.",
               "Firma con la misma firma de tu cédula de identidad.",
               "Adjunta una copia de tu cédula y de la de quien hará el trámite.",
               "Antes de ir, confirma en la institución si aceptan poder simple o exigen poder ante notario."],
     "faqs": [("¿El poder simple necesita notario?", "No: se firma sin notario. Pero algunos trámites, como vender un vehículo o una propiedad, exigen poder notarial o escritura pública."),
              ("¿Cuánto dura un poder simple?", "Sirve para el trámite indicado; si la institución pide uno reciente, haz uno nuevo con la fecha del día.")]},
    {"slug": "cv-formato-harvard", "nombre": "CV formato Harvard",
     "title": "CV formato Harvard: plantilla gratis para completar Chile",
     "desc": "Plantilla de CV formato Harvard para Chile: completa tus datos y descárgalo en Word o PDF. Orden cronológico inverso, una página y sin foto.",
     "corta": "El CV formato Harvard es un currículum de una página, sin foto ni diseño, ordenado en secciones fijas: datos de contacto, perfil, experiencia laboral y educación de lo más reciente a lo más antiguo, y al final habilidades e idiomas. Se usa porque es fácil de leer para un reclutador y para los sistemas que filtran postulaciones.",
     "campos": [("nombre", "Nombre completo", "María José Pérez Soto"),
                ("contacto", "Ciudad, teléfono y correo", "Santiago · +56 9 1234 5678 · mariajose.perez@correo.cl"),
                ("linkedin", "LinkedIn o portafolio (opcional)", "linkedin.com/in/mariajoseperez"),
                ("perfil", "Perfil profesional (2 o 3 líneas)", "Administradora con 5 años de experiencia en gestión de compras y control de inventario en empresas de retail. Busco aportar orden y ahorro en un área de abastecimiento.", "multi"),
                ("experiencia", "Experiencia laboral (de la más reciente a la más antigua)", "Comercial Los Andes SpA, Santiago — Jefa de compras (marzo 2023 – actualidad)\n• Negocié con 40 proveedores y bajé el costo de compra en un 8 %.\n• Implementé un control de stock semanal que redujo los quiebres de inventario.\n\nDistribuidora Sur Ltda., Rancagua — Asistente de compras (enero 2020 – febrero 2023)\n• Gestioné órdenes de compra y facturas de 25 proveedores.", "multi"),
                ("educacion", "Educación (de la más reciente a la más antigua)", "Universidad de Santiago de Chile — Ingeniería en Administración (2015 – 2019)\nLiceo Bicentenario de Rancagua — Enseñanza media (2011 – 2014)", "multi"),
                ("habilidades", "Habilidades y herramientas", "Excel avanzado, SAP, negociación con proveedores, licencia de conducir clase B", "multi"),
                ("idiomas", "Idiomas", "Español nativo, inglés intermedio")],
     "plantilla": """{nombre}
{contacto}
{linkedin}

PERFIL
{perfil}

EXPERIENCIA LABORAL
{experiencia}

EDUCACIÓN
{educacion}

HABILIDADES
{habilidades}

IDIOMAS
{idiomas}""",
     "pasos": ["Escribe tu experiencia y tu educación desde lo más reciente hacia lo más antiguo.",
               "En cada trabajo pon empresa, ciudad, cargo y fechas, y luego 2 o 3 logros con cifras cuando las tengas.",
               "Ajusta el perfil y las habilidades a cada aviso: usa las mismas palabras que pide la oferta.",
               "Descárgalo en Word para darle formato o guárdalo en PDF con «Imprimir»: el PDF es lo que se envía."],
     "faqs": [("¿El CV formato Harvard lleva foto?", "No. El formato Harvard no lleva foto ni datos como edad o estado civil; en Chile muchas empresas igual aceptan CV con foto, así que agrégala solo si el aviso la pide."),
              ("¿Cuántas páginas debe tener?", "Una página si tienes menos de 10 años de experiencia; dos como máximo si tienes más. Deja solo lo que sirve para el cargo al que postulas."),
              ("¿Qué pongo si no tengo experiencia?", "Pon primero la educación y suma prácticas, trabajos de verano, voluntariados o proyectos de estudio, con lo que hiciste y lo que lograste.")]},
]

PAGINAS = [
    {"path": "/", "tpl": "home.html",
     "title": "Formatos Chile: cartas y documentos gratis para completar",
     "desc": "Formatos gratis para Chile: carta de renuncia voluntaria, amonestación, presentación, recomendación laboral y poder simple. Complétalos y descárgalos.",
     "h1": "Formatos y cartas para completar",
     "corta": "Elige un formato, completa tus datos y el documento se arma solo. Puedes copiarlo, descargarlo en Word o guardarlo en PDF. No pedimos registro y tus datos no salen de tu navegador.",
     "faqs": [("¿Los formatos son gratis?", "Sí, todos son gratis y sin registro."),
              ("¿Se guardan mis datos?", "No. El documento se arma en tu navegador; lo que escribes no se envía a ningún servidor."),
              ("¿Sirven como asesoría legal?", "No. Son formatos de referencia con la normativa chilena vigente; para casos particulares consulta a la Inspección del Trabajo o a un abogado.")]},
] + [{"path": f"/{f['slug']}/", "tpl": "formato.html", "f": f, "title": f["title"], "desc": f["desc"], "h1": f["nombre"], "corta": f["corta"], "faqs": f["faqs"]} for f in FORMATOS] + [
    {"path": "/tamano-carta/", "tpl": "tamano.html",
     "title": "Tamaño carta: medidas de la hoja carta en cm, mm y pulgadas",
     "desc": "Medidas de la hoja tamaño carta: 21,59 × 27,94 cm (8,5 × 11 pulgadas). Compara con oficio y A4, y revisa los píxeles para imprimir a 300 ppp.",
     "h1": "Tamaño carta: medidas de la hoja",
     "corta": "La hoja tamaño carta mide 21,59 × 27,94 cm, es decir 215,9 × 279,4 mm u 8,5 × 11 pulgadas. Es el formato más usado en Chile para imprimir documentos; el tamaño oficio es igual de ancho pero más largo (21,59 × 33,02 cm), y el A4 es un poco más angosto y más largo (21 × 29,7 cm).",
     "faqs": [("¿Cuánto mide una hoja tamaño carta?", "21,59 × 27,94 cm, que equivalen a 8,5 × 11 pulgadas."),
              ("¿Es lo mismo tamaño carta que A4?", "No. El A4 mide 21 × 29,7 cm: es 6 mm más angosto y casi 2 cm más largo que la hoja carta."),
              ("¿Cuántos píxeles tiene una hoja carta?", "A 300 puntos por pulgada (calidad de impresión) son 2.550 × 3.300 píxeles; a 150 ppp, 1.275 × 1.650.")]},
    {"path": "/carta-gantt/", "tpl": "gantt.html",
     "title": "Carta Gantt: plantilla gratis en Excel con ejemplo para usar",
     "desc": "Plantilla de carta Gantt gratis: escribe tus tareas, inicio y duración, y descárgala en Excel o PDF. Incluye un ejemplo y cómo hacerla paso a paso.",
     "h1": "Carta Gantt: plantilla y ejemplo",
     "corta": "Una carta Gantt es un cronograma en forma de tabla: cada fila es una tarea del proyecto y cada columna una semana o un día; la barra pintada muestra cuándo empieza y cuánto dura cada tarea. Sirve para ver de un vistazo qué se hace en paralelo, qué depende de qué y si el proyecto va atrasado.",
     "faqs": [("¿Qué es una carta Gantt?", "Es un cronograma de barras: las tareas van en filas, el tiempo en columnas y cada barra marca el inicio y la duración de una tarea. Lleva el nombre de Henry Gantt, que la popularizó a comienzos del siglo XX."),
              ("¿Cómo se hace una carta Gantt en Excel?", "Pon las tareas en la primera columna y las semanas en la primera fila, y pinta las celdas de cada tarea entre su semana de inicio y su semana de término. Con esta plantilla el archivo de Excel sale listo para seguir editándolo."),
              ("¿Conviene usar días o semanas?", "Semanas para proyectos de más de un mes; días para proyectos cortos o eventos.")]},
    {"path": "/privacidad/", "tpl": "legal.html", "noindex": True,
     "title": "Privacidad y cookies de Formatos Chile",
     "desc": "Cómo trata Formatos Chile los datos de quienes visitan el sitio: los documentos se arman en tu navegador y la medición de visitas es con consentimiento.",
     "h1": "Privacidad y cookies"},
]
