import axios from 'axios'


export function getCompanyList(obj) {
    return axios.post(
        'http://127.0.0.1:8000/test/get_company_list', obj
    )
}
export function getCompanyInfo(obj) {
    return axios.post(
        'http://127.0.0.1:8000/test/get_company_info', obj
    )
}
export function delCompany(obj) {
    return axios.post(
        'http://127.0.0.1:8000/test/del_company', obj
    )
}

export function getNewUser(obj) {
    return axios.post(
        'http://127.0.0.1:8000/test/get_new_users', obj
    )
}
export function addCompany(obj) {
    return axios.post(
        'http://127.0.0.1:8000/test/add_company', obj
    )
}