import axios from 'axios'


export function getCompanyList(obj) {
    return axios.post(
        'http://121.43.189.184:8000/test/get_company_list', obj
    )
}
export function getCompanyInfo(obj) {
    return axios.post(
        'http://121.43.189.184:8000/test/get_company_info', obj
    )
}
export function delCompany(obj) {
    return axios.post(
        'http://121.43.189.184:8000/test/del_company', obj
    )
}