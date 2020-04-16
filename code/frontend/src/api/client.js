import axios from 'axios'
import {root_path} from "@/api/backstage"

export function getSampleTable() {
    const url = `${root_path}/test/get_sample_table?login_token=` + window.sessionStorage.getItem('ACCESS_TOKEN');
    window.open(url);
}

export function getOldSampleTable() {
    const url = `${root_path}/test/get_old_sample_table?login_token=` + window.sessionStorage.getItem('ACCESS_TOKEN');
    window.open(url);
}

export function getCompanyInfo(obj) {
    return axios.post(
        `${root_path}/test/get_company_info`, obj
    )
}