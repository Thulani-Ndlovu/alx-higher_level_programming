$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (input_)=>{
    $('UL#list_movies').append(...input_.results.map(movie => `<li>${movie.title}</li>`));
});