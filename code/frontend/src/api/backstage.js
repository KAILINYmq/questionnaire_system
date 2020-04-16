import axios from 'axios'

const root_path = "" // http://127.0.0.1:8000

export function getCompanyList(obj) {
    return axios.post(
        `${root_path}/test/get_company_list`, obj
    )
}
export function getCompanyInfo(obj) {
    return axios.post(
        `${root_path}/test/get_company_info`, obj
    )
}
export function delCompany(obj) {
    return axios.post(
        `${root_path}/test/del_company`, obj
    )
}

export function getNewUser(obj) {
    return axios.post(
        `${root_path}/test/get_new_users`, obj
    )
}
export function addCompany(obj) {
    return axios.post(
        `${root_path}/test/add_company`, obj
    )
}
export {root_path}
