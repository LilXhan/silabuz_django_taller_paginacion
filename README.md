# Taller

Para esta parte haremos la pequeña implementación de nuestra paginación con la vista basada en clases. Haremos uso de nuestro proyecto con los libros, por lo que no necesitaremos ni del cache ni de Celery (pueden eliminarlo o tener otro repositorio sin esas partes añadidas).

## Paginación en Class Based Views

Si recordamos nuestra vista que muestra nuestro libros, es la siguiente:

```py
class BookList(ListView):
    model = Book
    template_name = "booklist.html"
```

Para añadir la paginación a la vista, solo necesitaremos la siguiente línea:

```py
class BookList(ListView):
    model = Book
    template_name = "booklist.html"
    paginate_by = 10
```

Donde el número es la cantidad de resultados mostrados por página.

Si ejecutamos nuestro proyecto, podremos ver que se muestran únicamente 10 resultados, pero ¿cómo podemos cambiar de página?.

Dentro de la URL podemos ver lo siguiente.

```sample
http://127.0.0.1:8000/?page=1
```

`?page=1` es lo que marca nuestro número de página, si lo modificamos podremos acceder a los siguientes resultados. Pero, ¿cómo podemos hacerlo desde la vista del usuario sin necesidad de modificar la URL?.

La modificación correspondería hacerla dentro de nuestro template, para añadir la paginación de forma correcta, modificamos `booklist.html` de la siguiente forma:

```html
<div class="pagination">
    <span class="step-links">
        {% if page_obj.has_previous %}
            <a href="?page=1">&laquo; Primera</a>
            <a href="?page={{ page_obj.previous_page_number }}">Anterior</a>
        {% endif %}

        <span class="current">
            Página {{ page_obj.number }} de {{ page_obj.paginator.num_pages }}.
        </span>

        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">Siguiente</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">Último &raquo;</a>
        {% endif %}
    </span>
</div>
```

Con este `div` agregado al final de la página, si ejecutamos nuestra aplicación obtendremos el siguiente resultado:

![Paginación](https://photos.silabuz.com/uploads/big/1d660ffec47890e78424e547d2d676aa.PNG)

Si vemos al final, ya nos sale el número de página, y los controles para cambiar la vista.

## Tarea

Implementar la misma vista con paginación, pero con una view basada en función.

Investigar como podemos acceder al page_obj sin necesidad de enviarlo como contexto dentro de nuestra vista basada en clases.

Investigar si existen otros tipos de vistas genéricas que implementan de forma similar la paginación.

(Opcional) Implementar los otros tipos de vistas genéricas que encuentren con paginación incluida.

[Diapositiva](https://docs.google.com/presentation/d/e/2PACX-1vSG8yRoH4qxMp2vSzJxSmbOi3rDKONq-GJ2DMht5QQszjR7xjwmQI-aR0cMtWUgkPlECT9K2XaDzmsJ/embed?start=false&loop=false&delayms=3000#slide=id.g15e42d7d16b_0_31)
[Teoria](https://www.youtube.com/watch?v=3nmoz1SjPVQ&list=PLxI5H7lUXWhjV-yCSEuJXxsDmNESrvbw3&index=19&ab_channel=Silabuz)