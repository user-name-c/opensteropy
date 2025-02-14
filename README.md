


# OpenStereoPy  

**OpenStereoPy** es una librería en Python para realizar rotaciones de planos en 3D respecto a un eje definido. Es útil en geología estructural y análisis de orientación de planos en el espacio.  

> ⚠️ **Estado:** La librería aún está en desarrollo y puede estar sujeta a cambios en futuras versiones.  

## Instalación  

Por ahora, puedes clonar el repositorio y usarlo directamente en tu proyecto:  

```bash
git clone https://github.com/user-name-c/openstereopy.git
```

## Uso  

Aquí tienes un ejemplo de cómo crear un plano, definir un eje y rotarlo con *OpenStereoPy*:  

```python
import openstereopy as st

# Crear un plano y un eje
plane = st.Plane.from_strike(5, 39)
axis = st.Axis(5, 0)
angulo_rotacion = -39

# Rotar el plano
rotated_plane = st.rotate_plane(plane, axis, angulo_rotacion)
rot_plane_strike_strike, rot_plane_strike_dip = rotated_plane.to_strike()

print(f"Plano rotado: {rotated_plane.dip_dir:.2f}°, {rotated_plane.dip:.2f}°")
print(f"Plano rotado PMD: {rot_plane_strike_strike:.2f}°, {rot_plane_strike_dip:.2f}°")
```

## Contribuciones  

Si quieres contribuir al desarrollo de *OpenStereoPy*, siéntete libre de hacer un *fork*, reportar problemas o enviar *pull requests*.  

