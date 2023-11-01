$('document').raedy(()=>{
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (input_)=>{
        $('DIV#hello').text(input_.hello);
    });
});