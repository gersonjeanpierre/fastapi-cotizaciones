def calcular_precio_celtex(ancho_plancha_celtex_metros, largo_plancha_celtex_metros, precio_base_plancha, ancho_trabajo_metros, largo_trabajo_metros, margen_seguridad_porcentaje=5):
    """
    Calcula el precio del Celtex para un trabajo de vinil específico.

    Args:
        ancho_plancha_celtex_metros (float): Ancho de la plancha de Celtex en metros.
        largo_plancha_celtex_metros (float): Largo de la plancha de Celtex en metros.
        precio_base_plancha (float): Precio base de la plancha de Celtex completa.
        ancho_trabajo_metros (float): Ancho del trabajo de vinil a imprimir en metros.
        largo_trabajo_metros (float): Largo del trabajo de vinil a imprimir en metros.
        margen_seguridad_porcentaje (float): Porcentaje adicional para cubrir desperdicios (por defecto 5%).

    Returns:
        float: El precio estimado del Celtex para el trabajo, incluyendo el margen de seguridad.
    """

    # 1. Calcular el área total de la plancha de Celtex
    area_total_plancha = ancho_plancha_celtex_metros * largo_plancha_celtex_metros
    print(f"Área total de la plancha de Celtex: {area_total_plancha:.2f} m²")

    # 2. Determinar el costo por metro cuadrado de Celtex
    costo_por_metro_cuadrado = precio_base_plancha / area_total_plancha
    print(f"Costo por metro cuadrado de Celtex: {costo_por_metro_cuadrado:.2f} unidades/m²")

    # 3. Calcular el área de tu trabajo de vinil
    area_trabajo = ancho_trabajo_metros * largo_trabajo_metros
    print(f"Área del trabajo a imprimir: {area_trabajo:.2f} m²")

    # Calcular el costo base del Celtex para este trabajo
    costo_base_trabajo = area_trabajo * costo_por_metro_cuadrado

    # Aplicar el margen de seguridad
    costo_con_margen = costo_base_trabajo * (1 + margen_seguridad_porcentaje / 100)
    print(f"Costo base del Celtex para el trabajo (sin margen): {costo_base_trabajo:.2f} unidades")
    print(f"Margen de seguridad aplicado: {margen_seguridad_porcentaje}%")

    return costo_con_margen

# --- Instrucciones de uso ---

# Define las dimensiones de tu plancha de Celtex y su precio base
ANCHO_PLANCHA = 1.2  # metros
LARGO_PLANCHA = 2.4  # metros
PRECIO_PLANCHA_BASE = 37  # unidades monetarias

# Ejemplo de uso:
# Supongamos que tienes un trabajo de vinil de 1 metro de ancho por 0.5 metros de largo
ancho_trabajo_ejemplo = 1.0  # metros
largo_trabajo_ejemplo = 0.5  # metros

precio_final_celtex = calcular_precio_celtex(
    ANCHO_PLANCHA,
    LARGO_PLANCHA,
    PRECIO_PLANCHA_BASE,
    ancho_trabajo_ejemplo,
    largo_trabajo_ejemplo
)

print(f"\nEl precio estimado del Celtex para tu trabajo es: {precio_final_celtex:.2f} unidades")

# Otro ejemplo con un margen de seguridad diferente
print("\n--- Otro ejemplo con 10% de margen de seguridad ---")
precio_final_celtex_alto_margen = calcular_precio_celtex(
    ANCHO_PLANCHA,
    LARGO_PLANCHA,
    PRECIO_PLANCHA_BASE,
    0.8,  # otro ancho de trabajo
    1.2,  # otro largo de trabajo
    margen_seguridad_porcentaje=10
)
print(f"El precio estimado del Celtex para tu trabajo (con 10% de margen) es: {precio_final_celtex_alto_margen:.2f} unidades")