import axios from 'axios'

export function getSampleTable() {
    const url = 'http://121.43.189.184:8000/test/get_sample_table?login_token=' + window.sessionStorage.getItem('ACCESS_TOKEN');
    window.open(url);
    // return axios.get(
    //     'http://121.43.189.184:8000/test/get_sample_table', { params: { login_token: window.sessionStorage.getItem('ACCESS_TOKEN') } }
    // )

}
export function getOldSampleTable() {
    const url = 'http://121.43.189.184:8000/test/get_old_sample_table?login_token=' + window.sessionStorage.getItem('ACCESS_TOKEN');
    window.open(url);
}
export function uploadSampleTable(form) {
    return axios.post(
        'http://121.43.189.184:8000/test/upload_sample_table', { formData: form }
    )
}