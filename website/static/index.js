// this javascript is already linked in base.html
// when needed use this file for your js codes

function delete_rocket(rocket_id) {
    document.location = '/delete_rocket?rocket_id=' + rocket_id
}
function delete_rocket_d1(rocket_id) {
    document.location = '/delete_rocket_detail_1?rocket_id=' + rocket_id
}
function delete_rocket_d2(rocket_id) {
    document.location = '/delete_rocket_detail_2?rocket_id=' + rocket_id
}
