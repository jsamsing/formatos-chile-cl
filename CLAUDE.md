# Formatos Chile — formatos-chile.cl

Sitio útil de SearchLab (repo público: sin datos privados ni credenciales aquí): formatos de cartas y documentos para Chile que se completan en el navegador (nada se envía a servidores) y se copian, descargan en Word (.doc) o imprimen/guardan en PDF. Avisos de la casa SOLO a searchlab.cl y Bifrok (resuelvealtiro.cl cuando esté publicado); nunca Pieza al Tiro ni ELCOM. Etiqueta «Sponsored» + rel="sponsored".

## Stack
- `content.py` (`FORMATOS`: campos, plantilla con {campo}, pasos y FAQ con texto legal verificado en el Código del Trabajo y la Dirección del Trabajo) + `templates/` (Jinja2, CSS y JS inline) → `python3 build.py` → `dist/`. El build FALLA si title fuera de 50-60, description fuera de 100-160, JSON-LD inválido o enlace interno roto.
- Publicación: la acción «Sitios útiles (publicar)» del repo privado de SearchLab revisa este repo cada 15 min, construye y sube por SSH.
- Keywords (Semrush 2026-11, base Chile): carta de renuncia (voluntaria) ~20k, carta Gantt 33k, tamaño carta 12k, formato CV/Harvard ~10k, carta de amonestación 2,4k, carta de presentación 2,4k, recomendación laboral 1,6k, poder simple 1k. Próximas páginas: tamaño carta y medidas de hojas, plantilla carta Gantt, CV formato Harvard, declaración jurada simple, contrato de arriendo, cotización.
- Eventos GA4: formato_start, formato_copiar, formato_word, formato_pdf, aviso_click.
- Nunca presentar los formatos como asesoría legal.
- Menú móvil: hamburguesa a la DERECHA, panel desde la derecha, enlaces de 48 px.
