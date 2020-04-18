// 客户方，公司上传和下载
<template>
<div class="client">
    <!-- <a href="http://121.43.189.184:8000/upload_table/15814777631/15815015401style_sheet.xlsx" target="_blank">aaa</a> -->
    <!-- <a href="http://121.43.189.184:8000/upload_table/15815015311style_sheet.xlsx">测试下载</a> -->

    <el-drawer title="上传与下载" :visible.sync="drawer" :with-header="false">
        <el-button type="primary" @click="getSampleTable">下载样例</el-button>
        <el-button type="info" @click="getOldSample">下载历史</el-button>
        <br />
        <br />
        <el-upload class="inline-block" :multiple='false' :auto-upload='true' list-type='text' :show-file-list='true' :before-upload="beforeUpload" :drag='true' action='' :http-request="uploadFile">
            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
            <div class="el-upload__tip" slot="tip">仅限 xls/xlsx 格式，单文件不超过 1MB</div>
        </el-upload>
    </el-drawer>

    <el-card>
        <h1>企业信息概况</h1>
        <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
            上传与下载
        </el-button>
        <div class="el-upload__tip">（具体信息请下载查看）</div>
        <el-form label-position="right" :model="companyInfoForm" label-width="170px" ref="companyInfoForm">
            <el-row>
                <el-col :span="16">
                    <el-form-item label="法人单位名称" prop="法人单位名称">
                        <el-input :disabled="true" v-model="companyInfoForm.法人单位名称"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="12">
                    <el-form-item label="统一社会信用代码" prop="统一社会信用代码">
                        <el-input :disabled="true" v-model="companyInfoForm.统一社会信用代码"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="12">
                    <el-form-item label="组织机构代码" prop="组织机构代码">
                        <el-input :disabled="true" v-model="companyInfoForm.组织机构代码"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="12">
                    <el-form-item label="联系方式（手机号）" prop="联系方式">
                        <el-input :disabled="true" v-model="companyInfoForm.联系方式.手机"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="12">
                    <el-form-item label="联系方式（固话）" prop="联系方式">
                        <el-input :disabled="true" v-model="companyInfoForm.联系方式.固话"></el-input>
                    </el-form-item>
                </el-col>

            </el-row>

            <el-row>

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
                <el-col :span="16">
                    <el-form-item label="企业从业人员平均人数" prop="企业从业人员平均人数">
                        <el-input :disabled="true" v-model="companyInfoForm.企业从业人员平均人数"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8"></el-col>
            </el-row>
        </el-form>

        <h3>从业人员工资报酬</h3>
        <el-table  :data="moneyTable" :header-cell-style="{background:'#eef1f6',color:'#606266'}" style="width: 100%" max-height="500px" border fit highlight-current-row align="center" stripe>
            <el-table-column prop="职工代码" label="职工代码" width="40">
            </el-table-column>
            <el-table-column prop="出生年份" label="出生年份" width="60">
            </el-table-column>
            <el-table-column prop="性别" label="性别" width="40">
            </el-table-column>
            <el-table-column prop="学历" label="学历" width="70">
            </el-table-column>
            <el-table-column prop="是否工会会员" label="是否工会会员" width="60">
            </el-table-column>
            <el-table-column prop="基本工资（类）" label="基本工资（类）">
            </el-table-column>
            <el-table-column prop="绩效工资（类)" label="绩效工资（类)">
            </el-table-column>
            <el-table-column prop="用工形式" label="用工形式">
            </el-table-column>
            <el-table-column prop="津补贴（类）" label="津补贴（类）" width="100">
            </el-table-column>
            <el-table-column prop="管理岗位/专业技术职称/职业技能等级" label="管理岗位/专业技术职称/职业技能等级" width="200">
            </el-table-column>
            <el-table-column prop="全年工资报酬合计" label="全年工资报酬合计" width="100">
            </el-table-column>
            <el-table-column prop="加班加点工资" label="加班加点工资" width="100">
            </el-table-column>
            <el-table-column prop="参加工作年份" label="参加工作年份" width="100">
            </el-table-column>
            <el-table-column prop="全年周平均工作小时数" label="全年周平均工作小时数">
            </el-table-column>
            <el-table-column prop="劳动合同类型" label="劳动合同类型" width="100">
            </el-table-column>

        </el-table>
    </el-card>
</div>
</template>

<script>
import {
    getSampleTable,
    getOldSampleTable,
    getCompanyInfo
} from "@/api/client"; //获取数据的接口
import {
    root_path
} from "@/api/backstage";

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
            },
            moneyTable: [],
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
                    let moneyList = JSON.parse(response.data.msg).从业人员工资报酬
                    this.companyInfoForm = JSON.parse(response.data.msg);
                    for (let i in moneyList) {
                        this.moneyTable.push(moneyList[i])
                    }
                    // console.log(JSON.stringify(JSON.parse(response.data.msg)))
                    // console.log(window.sessionStorage.getItem('ACCESS_TOKEN'))
                }

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
                    url: `${root_path}/test/upload_sample_table`,
                    data: formData,
                    headers: {
                        "Content-Type": "multipart/form-data;charset=utf-8", //'application/json;charset=UTF-8'
                        login_token: window.sessionStorage.getItem("ACCESS_TOKEN")
                    }
                })
                .then(function (response) {
                    alert(response.data.msg)
                    if (response.data.status == 1) {
                        
                        location.reload()
                    } 
                    return response;
                })
                .catch(function (error) {
                    return error;
                });
        },
        

        // **************上传excel文件结束***************************
        getSampleTable() {
            getSampleTable();
        },
        getOldSample() {
            getOldSampleTable().then(response => {
                let resData = response.data.msg;
                console.log(JSON.parse(JSON.stringify(response.data.msg)))
                let dataArray = JSON.parse(JSON.stringify(response.data.msg))
                // let msgIndex = JSON.stringify(response.data.msg)
                alert(resData.length)
                let obj = new Object();
                obj = JSON.parse(JSON.stringify(resData[resData.length - 1]))
                console.log(obj)
                // alert(obj)
                window.location.href = root_path + JSON.parse(dataArray[dataArray.length - 1]).file // alert(JSON.stringify(response.data.msg[0].file))
                console.log(response)
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
