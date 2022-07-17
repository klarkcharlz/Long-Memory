import Cookies from 'universal-cookie';


function get_token_from_storage() {
    const cookies = new Cookies();
    return cookies.get('token');
}

function set_token_to_storage(token) {
    const cookies = new Cookies()
    cookies.set('token', token)
}

export {get_token_from_storage, set_token_to_storage};
