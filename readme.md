Hola, soy Fabio, este es mi proyecto de Catálogo de Películas, Series, Libros y Cómics

Antes que nada me gustaria decir que la calidad del profesorado fue excelente, se entendio todo y muy bien, gracias Diego y Norman.
Lamentablemente a mediados del cursado tuve un fallecimiento de un familiar que me afecto mucho y me saco tiempo, no pude darle la atencion que me hubiera gustado, me da bronca ver lo que era mi entrega dos y lo que estoy entregando ahora, pero bueno, la proxima
sera.

La idea este proyecto es proporcionar a los usuarios una plataforma para mantener un catálogo personalizado de sus películas, series, libros y cómics favoritos. Los usuarios podrán registrar y gestionar sus elementos multimedia, ver detalles, buscar y actualizar información según sus necesidades.

## Descripción de Modelos
El modelo `CustomUser` representa a los usuarios del sistema y extiende el modelo de usuario predeterminado de Django. Los campos incluidos son:

- `username`: Nombre de usuario único.
- `email`: Correo electrónico del usuario.
- `password`: Contraseña del usuario.

### Movie
El modelo `Movie` representa una película en el catálogo. Los campos incluidos son:

- `title`: Título de la película.
- `description`: Descripción de la película.
- `release_year`: Año de lanzamiento de la película.

### Series
El modelo `Series` representa una serie en el catálogo. Los campos incluidos son:

- `title`: Título de la serie.
- `description`: Descripción de la serie.
- `release_year`: Año de lanzamiento de la serie.

### Book
El modelo `Book` representa un libro en el catálogo. Los campos incluidos son:

- `title`: Título del libro.
- `description`: Descripción del libro.
- `release_year`: Año de lanzamiento del libro.

### Comic
El modelo `Comic` representa un cómic en el catálogo. Los campos incluidos son:

- `title`: Título del cómic.
- `description`: Descripción del cómic.
- `release_year`: Año de lanzamiento del cómic.

## Acceso al Panel de Administración
user = admin1234
pass = admin1234