import axios from 'axios'

export function getSampleTable() {
    const url = 'http://127.0.0.1:8000/test/get_sample_table?login_token=' + window.sessionStorage.getItem('ACCESS_TOKEN');
    window.open(url);
    // return axios.get(
    //     'http://127.0.0.1:8000/test/get_sample_table', { params: { login_token: window.sessionStorage.getItem('ACCESS_TOKEN') } }
    // )

}
export function getOldSampleTable() {
    const url = 'http://127.0.0.1:8000/test/get_old_sample_table?login_token=' + window.sessionStorage.getItem('ACCESS_TOKEN');
    window.open(url);
}

export function getCompanyInfo(obj) {
    return axios.post(
        'http://127.0.0.1:8000/test/get_company_info', obj
    )
}