// 客户方，公司上传和下载
<template>
<div class="client">

    <el-drawer title="上传与下载" :visible.sync="drawer" :with-header="false">
        <el-button type="primary" @click="getSampleTable">下载样例</el-button>

        <el-button type="info" @click="getOldSample">下载历史</el-button>
        <br />
        <br />
        <el-upload class="inline-block" :multiple='false' :auto-upload='true' list-type='text' :show-file-list='true' :before-upload="beforeUpload" :drag='true' action='' :limit="1" :on-exceed="handleExceed" :http-request="uploadFile">
            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
            <div class="el-upload__tip" slot="tip">仅限csv格式，单文件不超过1MB</div>
        </el-upload>
    </el-drawer>

    <el-card>
        <h1>企业信息概况</h1>
        <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
            上传与下载
        </el-button>
        <div class="el-upload__tip">（具体信息请下载查看）</div>
        <el-form label-position="right" :model="'companyInfoForm'" label-width="100px" ref="companyInfoForm">
            <el-row>
                <el-col :span="20">
                    <el-form-item label="法人单位名称" prop="法人单位名称">
                        <el-input :disabled="true" v-model="companyInfoForm.法人单位名称"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="4">
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="12">
                    <el-form-item label="统一社会信用代码" prop="统一社会信用代码">
                        <el-input :disabled="true" v-model="companyInfoForm.统一社会信用代码"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="12">
                    <el-form-item label="计划类型" prop="组织机构代码">
                        <el-input :disabled="true" v-model="companyInfoForm.组织机构代码"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>

            <el-row>
                <el-col :span="12">
                    <el-form-item label="联系方式" prop="联系方式">
                        <el-input :disabled="true" v-model="companyInfoForm.联系方式.手机"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="12">
                    <el-form-item label="企业所在地行政区划代码" prop="企业所在地行政区划代码">
                        <el-input :disabled="true" v-model="companyInfoForm.企业所在地行政区划代码"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="12">
                    <el-form-item label="单位隶属关系" prop="单位隶属关系">
                        <el-input :disabled="true" v-model="companyInfoForm.单位隶属关系"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="12">
                    <el-form-item label="行业类别代码" prop="行业类别代码">
                        <el-input :disabled="true" v-model="companyInfoForm.行业类别代码"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="12">
                    <el-form-item label="企业规模" prop="企业规模">
                        <el-input :disabled="true" v-model="companyInfoForm.企业规模"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="12">
                    <el-form-item label="登记注册类型" prop="登记注册类型">
                        <el-input :disabled="true" v-model="companyInfoForm.登记注册类型"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="20">
                    <el-form-item label="企业从业人员平均人数" prop="企业从业人员平均人数">
                        <el-input :disabled="true" v-model="companyInfoForm.企业从业人员平均人数"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="4"></el-col>
            </el-row>
        </el-form>
    </el-card>
</div>
</template>

<script>
import {
    getSampleTable,
    getOldSampleTable,
    uploadSampleTable,
    getCompanyInfo
} from "@/api/client"; //获取数据的接口

import axios from "axios";

export default {
    data() {
        return {
            drawer: false,
            companyInfoForm: {
                统一社会信用代码: '',
                组织机构代码: '',
                法人单位名称: '',
                联系方式: '',
                企业所在地行政区划代码: '',
                单位隶属关系: '',
                行业类别代码: '',
                企业规模: '',
                登记注册类型: '',
                企业从业人员平均人数: ''
            }
        }
    },
    created() {
        // zhege
        this.getCompanyDetailInfo();
    },
    methods: {
        getCompanyDetailInfo() {
            let a = new Object();
            a.login_token = window.sessionStorage.getItem('ACCESS_TOKEN');
            getCompanyInfo(a).then(response => {
                if (response.data.msg === "null") {
                    this.$message('暂无数据，请下载样例后上传')
                } else {
                    this.companyInfoForm = JSON.parse(response.data.msg);
                }

                // this.companyInfoForm = JSON.stringify(JSON.parse(response.data.msg));
            })
        },
        // **************上传excel文件开始***************************
        // 上传文件之前的钩子
        beforeUpload(file) {
            //判断文件格式
            let hz = file.name.split(".")[1];
            if (hz != "xlsx" && hz != "xls") {
                return false;
            }
        },
        // 上传文件个数超过定义的数量
        handleExceed(files, fileList) {
            this.$message.warning(`当前限制选择 1 个文件，请删除后继续上传`);
        },
        // 上传文件
        uploadFile(item) {
            let fileObj = item.file;
            const formData = new FormData(); // FormData 对象
            formData.append(
                "login_token",
                window.sessionStorage.getItem("ACCESS_TOKEN")
            );
            formData.append("file", fileObj); // 文件对象  'file'是后台接收的参数名

            axios({
                    method: "post",
                    url: `http://121.43.189.184:8000/test/upload_sample_table`,
                    data: formData,
                    headers: {
                        "Content-Type": "multipart/form-data;charset=utf-8", //'application/json;charset=UTF-8'
                        login_token: window.sessionStorage.getItem("ACCESS_TOKEN")
                    }
                })
                .then(function (response) {
                    return response;
                })
                .catch(function (error) {
                    return error;
                });
        },
        download(filename, text) {
            var element = document.createElement('a')
            element.setAttribute(
                'href',
                'data:text/plain;charset=utf-8,' + encodeURIComponent(text)
            )
            element.setAttribute('download', filename)
            element.style.display = 'none'
            document.body.appendChild(element)
            element.click()
            document.body.removeChild(element)
        },
        // **************上传excel文件结束***************************
        getSampleTable() {
            // getSampleTable(window.sessionStorage.getItem('ACCESS_TOKEN'))
            getSampleTable();
        },
        getOldSample() {
            getOldSampleTable().then(response => {
               download("公司信息详情", response.data.msg.file)

            })
            // getOldSampleTable().then(res => {
            //     alert(res.data.msg.file);
            //     res.data.msg.file;
            //     // download("公司信息详情", res.data.msg.file)
            // })
        },
        uploadSampleTable() {
           
            uploadSampleTable().then(response => {
                alert(response.data.msg)
                this.$message(response.data.msg);

            })
        }
    }
};
</script>

<style>
.client {
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    padding: 4%;
    max-width: 100%;
    margin: 0 auto;
}

em {
    font-style: normal;

}

/* .inline-block {
    display: inline-block;
} */
</style>
