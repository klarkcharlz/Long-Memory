const formatDate = (date_) => {

    let date = new Date(date_);

    let dd = date.getDate();
    if (dd < 10) dd = '0' + dd;

    let mm = date.getMonth() + 1;
    if (mm < 10) mm = '0' + mm;

    let yy = date.getFullYear() % 100;
    if (yy < 10) yy = '0' + yy;

    return dd + '.' + mm + '.' + yy;
}

const parseResponse = (data) => {
    let status = [];
    for(const key in data){
        // status.push(`${key}: ${data[key]}`)
        status.push(`${data[key]}`)
    }
    return status.join("\n");
}

export {formatDate, parseResponse};
