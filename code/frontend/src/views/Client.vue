// 客户方，公司上传和下载
<template>
<div class="client">
    <h1>欢迎登录，请选择要执行的操作</h1>

    <el-button type="primary" @click="getSampleTable">下载样例</el-button>

    <el-button type="info" @click="getOldSampleTable">下载历史</el-button>
    <br/>
    <br/>
    <el-upload class="inline-block" :multiple='false' :auto-upload='true' list-type='text' :show-file-list='true' :before-upload="beforeUpload" :drag='true' action='' :limit="1" :on-exceed="handleExceed" :http-request="uploadFile">
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        <div class="el-upload__tip" slot="tip">一次只能上传一个文件，仅限text格式，单文件不超过1MB</div>
    </el-upload>

</div>
</template>

<script>
import {
    getSampleTable,
    getOldSampleTable,
    uploadSampleTable
} from "@/api/client"; //获取数据的接口
import axios from 'axios'

export default {
    methods: {
        // **************上传excel文件开始***************************
        // 上传文件之前的钩子
        beforeUpload(file) {
            //判断文件格式
            let hz = file.name.split(".")[1]
            if (hz != 'xlsx' && hz != 'xls') {
                return false;
            }
        },
        // 上传文件个数超过定义的数量
        handleExceed(files, fileList) {
            this.$message.warning(`当前限制选择 1 个文件，请删除后继续上传`)
        },
        // 上传文件
        uploadFile(item) {
            let fileObj = item.file
            const form = new FormData() // FormData 对象
           // form.append('login_token', window.sessionStorage.getItem('ACCESS_TOKEN'))
            form.append('file', fileObj) // 文件对象  'file'是后台接收的参数名
            let a =[{login: window.sessionStorage.getItem('ACCESS_TOKEN'), file: fileObj}];
            uploadSampleTable(form).then(response => {
                console.log(response.data.msg);
            });
           
        },

        // **************上传excel文件结束***************************
        getSampleTable() {
            // getSampleTable(window.sessionStorage.getItem('ACCESS_TOKEN'))
            getSampleTable();
        },
        getOldSampleTable() {
           getOldSampleTable()
        },
        uploadSampleTable() {
            uploadSampleTable();
        }
    },

}
</script>

<style>
.client {
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    padding: 4%;
    max-width: 600px;
    margin: 0 auto;
}

/* .inline-block {
    display: inline-block;
} */
</style>
