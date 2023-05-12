
const grados_nivelacademico = async () => {
    try {
        let id_nivelacademico = localStorage.getItem('nivel_academico');
        console.log('estamos aqui')
        if (id_nivelacademico != 0) {
            const response = await fetch("/grados/" + id_nivelacademico + "/0")
            const data = await response.json();
            data.grados.forEach(element => {
                if (element.nivel_academico_id == id_nivelacademico) {
                    document.getElementById("grados_filtrados").style.display = "block"
                    document.getElementById("grados").style.display = "none"
                    clase_filtrada = document.getElementById("grados_filtrados")
                    label = document.createElement('label')
                    label.setAttribute('id', 'grado_' + element.id)
                    label.classList = 'custom-control custom-radio'
                    input = document.createElement('input')
                    input.setAttribute('id',  element.id)
                    input.setAttribute('type', 'radio')
                    input.classList = 'custom-control-input'
                    div = document.createElement('div')
                    div.classList = 'custom-control-label'
                    div.setAttribute('onClick', 'clases_grados(' + element.id + ')')
                    div.innerHTML = element.nombre
                    clase_filtrada.appendChild(label)
                    label.appendChild(input)
                    label.appendChild(div)
                }
            });

            console.log(data)

        }else{
            const response = await fetch("/grados/" + "0/0")
            const data = await response.json();
            data.grados.forEach(element => {
                if (element.nivel_academico_id == id_nivelacademico) {
                    console.log(element)
                    document.getElementById("grados_filtrados").style.display = "block"
                    document.getElementById("grados").style.display = "none"
                    clase_filtrada = document.getElementById("grados_filtrados")
                    label = document.createElement('label')
                    label.setAttribute('id', 'grado_' + element.id)
                    label.classList = 'custom-control custom-radio'
                    input = document.createElement('input')
                    input.setAttribute('id',  element.id)
                    input.setAttribute('type', 'radio')
                    input.classList = 'custom-control-input'
                    div = document.createElement('div')
                    div.classList = 'custom-control-label'
                    div.setAttribute('onClick', 'clases_grados(' + element.id + ')')
                    div.innerHTML = element.nombre
                    clase_filtrada.appendChild(label)
                    label.appendChild(input)
                    label.appendChild(div)
                }
            });  
        }
    } catch (error) {
        console.log(error)
    }
}


const clases_grados = async (grado) => {
    localStorage.removeItem('grados_filtrados')

    localStorage.setItem('filtro_grados', 0);
    localStorage.setItem('grado_academico',grado);
   
    document.getElementById('grado_sin_filtro'+grado).checked = true;
    try {
        id_nivelacademico = 0
        clase_filtrada = document.getElementById("clases_por_grado").innerHTML = '';
        if (grado && id_nivelacademico != 0) {
            const response = await fetch("/grados/" + id_nivelacademico + "/" + grado + "/")
            const data = await response.json();
            data.clases.forEach(element => {
                                
                if (element.grado == grado) {
                    document.getElementById("clases_por_grado").style.display = "block"
                    document.getElementById("clases").style.display = "none"

                    clase_filtrada = document.getElementById("clases_por_grado")
                    label = document.createElement('label')
                    label.setAttribute('id', 'clase_' + element.id)
                    label.classList = 'custom-control custom-radio'
                    input = document.createElement('input')
                    input.setAttribute('id',  element.id)
                    input.setAttribute('type', 'radio')
                    input.classList = 'custom-control-input'
                    div = document.createElement('div')
                    div.classList = 'custom-control-label'
                    div.innerHTML = element.nombre

                    clase_filtrada.appendChild(label)
                    label.appendChild(input)
                    label.appendChild(div)
                }
               
            });

            console.log(data.clases)
           
        }
        else{
            localStorage.removeItem('grados_filtrados')

        fetch("/repositorio/" + id_dirigido + "/0/0/"+ grado +'/' )
        .then(response => response.json())
        .then(data => {
        clase_filtrada = document.getElementById("repositorio").innerHTML = '';
            if(undefined ==data.repositorio){
                clase_filtrada = document.getElementById("repositorios").innerHTML = '';
                document.getElementById("advertencia").style.display ="block"
                return
            }
            console.log(data)
            data.repositorio.forEach(element => {
                document.getElementById("repositorios").style.display = "none"
                if (element.grados_id = grado) {
                    document.getElementById("advertencia").style.display ="none"
                    document.getElementById("advertencia_clase").style.display ="none"
                    console.log('data',element)
                    repositorios = document.getElementById("repositorio")
                    a = document.createElement('a')
                    a.href = "/repositorio_detalle/" + element.page_ptr_id
                    div_clumnnas = document.createElement('div')
                    div_clumnnas.classList = 'col-md-6 col-lg-3'
                    div_cards = document.createElement('div')
                    div_cards.classList ='example-1 cards mb-5'
                    div_wrapper = document.createElement('div')
                    div_wrapper.classList = 'wrapper'
                    figure = document.createElement('figure')
                    img =  document.createElement('img')
                    img.classList = 'card-img'
                    img.src = '/media/'+ element.imagen_portada_id__file
                    div_data = document.createElement('div')
                    div_data.classList = 'date'
                    span_day = document.createElement('span')
                    span_day.classList = 'day'
                    span_day.innerHTML = element.grados_id +'°'
                    span_month = document.createElement('span')
                    span_month.classList = 'month'
                    span_month.innerHTML = 'Grado'
                    div_content = document.createElement('div')
                    div_content.classList = 'content'
                    div_date = document.createElement('div')
                    div_date.classList = 'data'
                    span = document.createElement('span')
                    span.classList = 'author'
                    span.innerHTML = element.grados_id__nivel_academico__nivel_academico
                    h1 = document.createElement('h3')
                    h1.classList = 'p text-justify font-weight-800'
                    h1.innerHTML = element.titulo
                    p = document.createElement('span')
                    p.classList = 'text module line-clamp '
                    p.innerHTML = element.descripcion   
                    span1 = document.createElement('span')
                    span1.classList = 'author'
                    span1.innerHTML = 'No. de visitas:' + element.visitas
                    repositorios.appendChild(div_clumnnas)
                    div_clumnnas.appendChild(div_cards)
                    div_cards.appendChild(div_wrapper)
                    div_wrapper.appendChild(figure)
                    div_wrapper.appendChild(div_data)
                    div_wrapper.appendChild(div_date)
                    figure.appendChild(img)
                    div_data.appendChild(span_day)
                    div_data.appendChild(span_month)
                    div_date.appendChild(a)
                    a.appendChild(div_content)
                    div_content.appendChild(span)
                    div_content.appendChild(h1)
                    div_content.appendChild(p)
                    div_content.appendChild(span1)
                   
                     

                }
                 
            });
        });
        }
    } catch (error) {
        console.log(error)
    }
}


function cargar_repositorio_nivel(){
        id_nivelacademico = localStorage.getItem('nivel_academico')
        id_dirigido = localStorage.getItem('id_dirigido');
    if(id_dirigido != 0  && id_nivelacademico != 0){
        console.log(id_nivelacademico,'si hay nivel academico',id_dirigido)
        fetch("/repositorio/" + id_dirigido + "/"+id_nivelacademico+ "/0/0/" )
        .then(response => response.json())
        .then(data => {
            console.log(data)
            data.repositorio.forEach(element => {
                if (element.grados_id__nivel_academico == id_nivelacademico) {
                    document.getElementById("repositorios").style.display = "none"
                    repositorios = document.getElementById("repositorio")
                    div_clumnnas = document.createElement('div')
                    div_clumnnas.classList = 'col-md-6 col-lg-3'
                    div_cards = document.createElement('div')
                    div_cards.classList ='example-1 cards mb-5'
                    div_wrapper = document.createElement('div')
                    a = document.createElement('a')
                    a.href =  "/repositorio_detalle/" + element.page_ptr_id
                    div_wrapper.classList = 'wrapper'
                    figure = document.createElement('figure')
                    img =  document.createElement('img')
                    img.classList = 'card-img'
                    img.src = '/media/'+ element.imagen_portada_id__file
                    div_data = document.createElement('div')
                    div_data.classList = 'date'
                    span_day = document.createElement('span')
                    span_day.classList = 'day'
                    span_day.innerHTML = element.grados_id+'°'
                    span_month = document.createElement('span')
                    span_month.classList = 'month'
                    span_month.innerHTML = 'Grado'
                    div_content = document.createElement('div')
                    div_content.classList = 'content'
                    div_date = document.createElement('div')
                    div_date.classList = 'data'
                    span = document.createElement('span')
                    span.classList = 'author'
                    span.innerHTML = element.grados_id__nivel_academico__nivel_academico
                    h1 = document.createElement('h3')
                    h1.classList = 'p text-justify font-weight-800'
                    h1.innerHTML = element.titulo
                    p = document.createElement('span')
                    p.classList = 'text module line-clamp '
                    p.innerHTML = element.descripcion
                    span1 = document.createElement('span')
                    span1.classList = 'author'
                    span1.innerHTML = 'No. de visitas:' + element.visitas
                    repositorios.appendChild(div_clumnnas)
                    div_clumnnas.appendChild(div_cards)
                    div_cards.appendChild(div_wrapper)
                    div_wrapper.appendChild(figure)
                    div_wrapper.appendChild(div_data)
                    div_wrapper.appendChild(div_date)
                    figure.appendChild(img)
                    div_data.appendChild(span_day)
                    div_data.appendChild(span_month)
                    div_date.appendChild(div_content)
                    div_date.appendChild(a)
                    a.appendChild(div_content)
                    div_content.appendChild(span)
                    div_content.appendChild(h1)
                    div_content.appendChild(p)
                    div_content.appendChild(span1)

                }
            });
        });
    }
    else{
        console.log('no hay nivel academico')
        fetch("/repositorio/" + id_dirigido + "/0" + "/0/0/" )
        .then(response => response.json())
        .then(data => {
            console.log(data)
            data.repositorio.forEach(element => {
                    document.getElementById("grados").style.display = "block"
                    document.getElementById("grados_filtrados").style.display = "none"
                    document.getElementById("repositorios").style.display = "none"
                    repositorios = document.getElementById("repositorio")
                    div_clumnnas = document.createElement('div')
                    a= document.createElement('a')
                    div_clumnnas.classList = 'col-md-6 col-lg-3'
                    div_cards = document.createElement('div')
                    div_cards.classList ='example-1 cards mb-5'
                    div_wrapper = document.createElement('div')
                    div_wrapper.classList = 'wrapper'
                    figure = document.createElement('figure')
                    img =  document.createElement('img')
                    img.classList = 'card-img'
                    img.src = '/media/'+ element.imagen_portada_id__file
                    a.href =  "/repositorio_detalle/" + element.page_ptr_id
                    div_data = document.createElement('div')
                    div_data.classList = 'date'
                    span_day = document.createElement('span')
                    span_day.classList = 'day'
                    span_day.innerHTML = element.grados_id + '°'
                    span_month = document.createElement('span')
                    span_month.classList = 'month'
                    span_month.innerHTML = 'Grado'
                    div_content = document.createElement('div')
                    div_content.classList = 'content'
                    div_date = document.createElement('div')
                    div_date.classList = 'data'
                    span = document.createElement('span')
                    span.classList = 'author'
                    span.innerHTML = element.grados__nivel_academico__nivel_academico
                    h1 = document.createElement('h3')
                    h1.classList = 'p text-justify font-weight-800'
                    h1.innerHTML = element.titulo
                    p = document.createElement('span')
                    p.classList = 'text  module line-clamp'
                    p.innerHTML = element.descripcion   
                    span1 = document.createElement('span')
                    span1.classList = 'author'
                    span1.innerHTML = 'No. de visitas:' + element.visitas
                    repositorios.appendChild(div_clumnnas)
                    div_clumnnas.appendChild(div_cards)
                    div_cards.appendChild(div_wrapper)
                    div_wrapper.appendChild(figure)
                    div_wrapper.appendChild(div_data)
                    div_wrapper.appendChild(div_date)
                    figure.appendChild(img)
                    div_data.appendChild(span_day)
                    div_data.appendChild(span_month)
                    div_date.appendChild(a)
                    a.appendChild(div_content)
                    div_content.appendChild(span)
                    div_content.appendChild(h1)
                    div_content.appendChild(p)
                    div_content.appendChild(span1)
                 
 
            });
        });
        localStorage.removeItem('filtro_grados')
        localStorage.removeItem('nivel_academico')
        localStorage.removeItem('grado_academico')

    }

   
}

function cargar_repositorio_grado(grado){
    id_nivelacademico = localStorage.getItem('nivel_academico')
    id_dirigido = localStorage.getItem('id_dirigido');
    clase_filtrada = document.getElementById("repositorio").innerHTML = '';
   
if(id_nivelacademico){
    console.log('si hay grado academico')
    localStorage.removeItem("grados_filtrados")
    fetch("/repositorio/" + id_dirigido + "/"+id_nivelacademico+ "/" + grado +"/0/" )
    .then(response => response.json())
    .then(data => {
        
        data.repositorio.forEach(element => {
        console.log( grado == element.page_id__grados)
            
            if (element.page_id__grados == grado) {
               console.log(element)
               Swal.fire({
                position: 'top-end',
                icon: 'success',
                title: 'Your work has been saved',
                showConfirmButton: false,
                timer: 1500
              })

                document.getElementById("repositorios").style.display = "none"
                repositorios = document.getElementById("repositorio")
                div_clumnnas = document.createElement('div')
                div_clumnnas.classList = 'col-md-6 col-lg-3'
                div_cards = document.createElement('div')
                div_cards.classList ='example-1 cards mb-5'
                div_wrapper = document.createElement('div')
                div_wrapper.classList = 'wrapper'
                figure = document.createElement('figure')
                img =  document.createElement('img')
                a= document.createElement('a')
                a.href =  "/repositorio_detalle/" + element.page_ptr_id
                img.classList = 'card-img'
                img.src = '/media/'+ element.imagen_id__file
                div_data = document.createElement('div')
                div_data.classList = 'date'
                span_day = document.createElement('span')
                span_day.classList = 'day'
                span_day.innerHTML = element.page_id__grados
                span_month = document.createElement('span')
                span_month.classList = 'month'
                span_month.innerHTML = 'Grado'
                div_content = document.createElement('div')
                div_content.classList = 'content'
                div_date = document.createElement('div')
                div_date.classList = 'data'
                span = document.createElement('span')
                span.classList = 'author'
                span.innerHTML = element.page_id__grados__nivel_academico__nivel_academico
                h1 = document.createElement('h3')
                h1.classList = 'p text-justify font-weight-800'
                h1.innerHTML = element.page_id__titulo
                p = document.createElement('span')
                p.classList = 'text  module line-clamp'
                p.innerHTML = element.page_id__descripcion   
                span1 = document.createElement('span')
                span1.classList = 'author'
                span1.innerHTML = 'No. de visitas:' + element.page_id__visitas
                repositorios.appendChild(div_clumnnas)
                div_clumnnas.appendChild(div_cards)
                div_cards.appendChild(div_wrapper)
                div_wrapper.appendChild(figure)
                div_wrapper.appendChild(div_data)
                div_wrapper.appendChild(div_date)
                figure.appendChild(img)
                div_data.appendChild(span_day)
                div_data.appendChild(span_month)
                div_date.appendChild(a)
                a.appendChild(div_content)
                div_content.appendChild(span)
                div_content.appendChild(h1)
                div_content.appendChild(p)
                div_content.appendChild(span1)

            }
            return
        });
    });
}
else{
    console.log(id_dirigido, 'no viene el nivel academico ')
  
    fetch("/repositorio/"  + id_dirigido + "/0" +"/0/0/" )
    .then(response => response.json())
    .then(data => {
        data.repositorio.forEach(element => {
                document.getElementById("repositorios").style.display = "none"
                repositorios = document.getElementById("repositorio")
                div_clumnnas = document.createElement('div')
                div_clumnnas.classList = 'col-md-6 col-lg-3'
                div_cards = document.createElement('div')
                div_cards.classList ='example-1 cards mb-5'
                div_wrapper = document.createElement('div')
                div_wrapper.classList = 'wrapper'
                figure = document.createElement('figure')
                img =  document.createElement('img')
                img.classList = 'card-img'
                img.src = '/media/'+ element.imagen_id__file
                div_data = document.createElement('div')
                div_data.classList = 'date'
                span_day = document.createElement('span')
                span_day.classList = 'day'
                span_day.innerHTML = element.page_id__grados
                span_month = document.createElement('span')
                span_month.classList = 'month'
                span_month.innerHTML = 'Grado'
                div_content = document.createElement('div')
                div_content.classList = 'content'
                div_date = document.createElement('div')
                div_date.classList = 'data'
                span = document.createElement('span')
                span.classList = 'author'
                span.innerHTML = element.page_id__grados__nivel_academico__nivel_academico
                h1 = document.createElement('h3')
                h1.classList = 'p text-justify font-weight-800'
                h1.innerHTML = element.page_id__titulo
                p = document.createElement('span')
                p.classList = 'text  module line-clamp'
                p.innerHTML = element.page_id__descripcion   
                span1 = document.createElement('span')
                span1.classList = 'author'
                span1.innerHTML = 'No. de visitas:' + element.page_id__visitas
                repositorios.appendChild(div_clumnnas)
                div_clumnnas.appendChild(div_cards)
                div_cards.appendChild(div_wrapper)
                div_wrapper.appendChild(figure)
                div_wrapper.appendChild(div_data)
                div_wrapper.appendChild(div_date)
                figure.appendChild(img)
                div_data.appendChild(span_day)
                div_data.appendChild(span_month)
                div_date.appendChild(a)
                a.appendChild(div_content)
                div_content.appendChild(span)
                div_content.appendChild(h1)
                div_content.appendChild(p)
                div_content.appendChild(span1)

        });
    });
}


}

function cargar_repositorio_clase(id_clase){
    id_nivelacademico = localStorage.getItem('nivel_academico')
    id_dirigido = localStorage.getItem('id_dirigido');
    clase_filtrada = document.getElementById("repositorio").innerHTML = '';
    id_grado = localStorage.getItem('grado_academico')
if(id_nivelacademico){
    console.log('si hay grado academico')
    localStorage.removeItem("grados_filtrados")
    fetch("/repositorio/" + id_dirigido + "/"+id_nivelacademico+ "/" + id_clase +"/" +id_grado +"/" )
    .then(response => response.json())
    .then(data => {
        clase_filtrada = document.getElementById("repositorios").innerHTML = '';

        if(data.message =='Not Found5'){
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'La Clase seleccionada, no cuenta con recursos disponibles.! !',
                footer: '<a href="">Mostrar todo los recursos disponibles</a>'
              })
              return 
        }
        else{
        data.repositorio.forEach(element => {
            if (element.clase_id == id_clase) {
               console.log(element)
               ;

                document.getElementById("repositorios").style.display = "none"
                repositorios = document.getElementById("repositorio")
                div_clumnnas = document.createElement('div')
                div_clumnnas.classList = 'col-md-6 col-lg-3'
                div_cards = document.createElement('div')
                div_cards.classList ='example-1 cards mb-5'
                div_wrapper = document.createElement('div')
                div_wrapper.classList = 'wrapper'
                figure = document.createElement('figure')
                img =  document.createElement('img')
                img.classList = 'card-img'
                img.src = '/media/'+ element.imagen_id__file
                div_data = document.createElement('div')
                div_data.classList = 'date'
                span_day = document.createElement('span')
                span_day.classList = 'day'
                span_day.innerHTML = element.page_id__grados
                span_month = document.createElement('span')
                span_month.classList = 'month'
                span_month.innerHTML = 'Grado'
                div_content = document.createElement('div')
                div_content.classList = 'content'
                div_date = document.createElement('div')
                div_date.classList = 'data'
                span = document.createElement('span')
                span.classList = 'author'
                span.innerHTML = element.page_id__grados__nivel_academico__nivel_academico
                h1 = document.createElement('h3')
                h1.classList = 'p text-justify font-weight-800'
                h1.innerHTML = element.page_id__titulo
                p = document.createElement('span')
                p.classList = 'text'
                p.innerHTML = element.page_id__descripcion   
                span1 = document.createElement('span')
                span1.classList = 'author'
                span1.innerHTML = 'No. de visitas:' + element.page_id__visitas
                repositorios.appendChild(div_clumnnas)
                div_clumnnas.appendChild(div_cards)
                div_cards.appendChild(div_wrapper)
                div_wrapper.appendChild(figure)
                div_wrapper.appendChild(div_data)
                div_wrapper.appendChild(div_date)
                figure.appendChild(img)
                div_data.appendChild(span_day)
                div_data.appendChild(span_month)
                div_date.appendChild(a)
                a.appendChild(div_content)
                div_content.appendChild(span)
                div_content.appendChild(h1)
                div_content.appendChild(p)
                div_content.appendChild(span1)

            }
            return
        });
    }
    });
}
else{
    console.log(id_dirigido, 'no viene el nivel academico ')
    
    fetch("/repositorio/"  + id_dirigido + "/0/" + id_clase +"/0/" )
    .then(response => response.json())
    .then(data => {
        console.log(data)
        if(data.message == 'Not Found3'){
            clase_filtrada = document.getElementById("repositorios").innerHTML = '';
            Swal.fire({
                position: 'top-end',
                icon: 'success',
                title: 'Your work has been saved',
                showConfirmButton: false,
                timer: 1500
              })
           
            return  
        }else
        {
        data.repositorio.forEach(element => {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'La Clase seleccionada, no cuenta con recursos disponibles.! !',
                footer: '<a href="">Why do I have this issue?</a>'
              })
                document.getElementById("repositorios").style.display = "none"
                repositorios = document.getElementById("repositorio")
                div_clumnnas = document.createElement('div')
                div_clumnnas.classList = 'col-md-6 col-lg-3'
                div_cards = document.createElement('div')
                div_cards.classList ='example-1 cards mb-5'
                div_wrapper = document.createElement('div')
                div_wrapper.classList = 'wrapper'
                figure = document.createElement('figure')
                img =  document.createElement('img')
                img.classList = 'card-img'
                img.src = '/media/'+ element.imagen_id__file
                div_data = document.createElement('div')
                div_data.classList = 'date'
                span_day = document.createElement('span')
                span_day.classList = 'day'
                span_day.innerHTML = element.page_id__grados
                span_month = document.createElement('span')
                span_month.classList = 'month'
                span_month.innerHTML = 'Grado'
                div_content = document.createElement('div')
                div_content.classList = 'content'
                div_date = document.createElement('div')
                div_date.classList = 'data'
                span = document.createElement('span')
                span.classList = 'author'
                span.innerHTML = element.page_id__grados__nivel_academico__nivel_academico
                h1 = document.createElement('h3')
                h1.classList = 'p text-justify font-weight-800'
                h1.innerHTML = element.page_id__titulo
                p = document.createElement('span')
                p.classList = 'text  module line-clamp'
                p.innerHTML = element.page_id__descripcion   
                span1 = document.createElement('span')
                span1.classList = 'author'
                span1.innerHTML = 'No. de visitas:' + element.page_id__visitas
                repositorios.appendChild(div_clumnnas)
                div_clumnnas.appendChild(div_cards)
                div_cards.appendChild(div_wrapper)
                div_wrapper.appendChild(figure)
                div_wrapper.appendChild(div_data)
                div_wrapper.appendChild(div_date)
                figure.appendChild(img)
                div_data.appendChild(span_day)
                div_data.appendChild(span_month)
                div_date.appendChild(div_content)
                div_content.appendChild(span)
                div_content.appendChild(h1)
                div_content.appendChild(p)
                div_content.appendChild(span1)

        });
    }
    });
}


}

 
 
 