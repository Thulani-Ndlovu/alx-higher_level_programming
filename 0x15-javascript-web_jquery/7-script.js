$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (information)=>{
    $('DIV#character').text(information.name);
});