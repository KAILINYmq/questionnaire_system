// 后台管理界面
<template>
<div>
    <el-container>
        <el-header>
            <h3>后台管理</h3>
        </el-header>

        <!-- 主面板----公司详细信息以及该公司的删除和增加 -->
        <el-main>
            <div class="main-div">
                <el-button @click="drawer = true" type="primary" style="margin-right: 100%;">
                    公司新增
                </el-button>
                <el-drawer title="公司新增" :visible.sync="drawer" :with-header="false">
                    <div class="add-company">
                        <el-divider content-position="left">
                            <h3>公司新增</h3>
                        </el-divider>
                        <div>
                            <el-form label-width="140px" :model="addCompanyForm" :rules="rules" ref="addCompanyForm">
                                <el-form-item label="统一社会信用码" prop="username">
                                    <el-input  placeholder="请输入统一信代码" v-model="addCompanyForm.username"  clearable>
                                    </el-input>
                                </el-form-item>
                                <el-form-item label="联系方式(手机号)" prop="mobile">
                                    <el-input  placeholder="请输入联系方式" v-model="addCompanyForm.mobile" onkeyup="this.value=this.value.replace(/[^\d.]/g,'');" clearable>
                                    </el-input>
                                </el-form-item>
                                <el-form-item label="密码" prop="password">
                                    <el-input placeholder="请输入密码" v-model="addCompanyForm.password" show-password></el-input>
                                </el-form-item>
                                <el-form-item>
                                    <el-button type="primary" @click="addCompanyUser('addCompanyForm')">增加</el-button>
                                </el-form-item>
                            </el-form>

                        </div>
                    </div>
                </el-drawer>
                <!-- 公司详细信息 -->
                <el-row>
                    <el-col :span="24">
                        <div class="company-info">
                            <el-dialog :visible.sync="companyInfoVisible" @closed="resetForm('companyInfoForm')">
                                <el-divider content-position="center">
                                    <h3>公司详细信息</h3>
                                </el-divider>
                                <el-form label-position="right" :model="companyInfoForm" label-width="160px" ref="companyInfoForm">
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
                                            <el-form-item label="联系方式(手机)" prop="联系方式">
                                                <el-input :disabled="true" v-model="companyInfoForm.联系方式.手机"></el-input>
                                            </el-form-item>
                                        </el-col>
                                        <el-col :span="12">
                                            <el-form-item label="联系方式(固话)" prop="联系方式">
                                                <el-input :disabled="true" v-model="companyInfoForm.联系方式.固话"></el-input>
                                            </el-form-item>
                                        </el-col>
                                    </el-row>
                                    <el-row>
                                        <el-col :span="24">
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
                                        <el-col :span="12">
                                            <el-form-item label="企业从业人员平均人数" prop="企业从业人员平均人数">
                                                <el-input :disabled="true" v-model="companyInfoForm.企业从业人员平均人数"></el-input>
                                            </el-form-item>
                                        </el-col>
                                        <el-col :span="12"></el-col>
                                    </el-row>
                                </el-form>
                                <div slot="footer" class="dialog-footer">
                                    <el-button size="small" @click="companyInfoVisible = false">取 消</el-button>
                                </div>
                            </el-dialog>
                            <el-divider content-position="left">
                                <h3>公司详细信息</h3>
                            </el-divider>
                            <div class="company-info-table">
                                <el-table v-loading="loading" :data="CompanyBriefTable.filter(data => !search || data.法人单位名称.toLowerCase().includes(search.toLowerCase()))" :header-cell-style="{background:'#eef1f6',color:'#606266'}" style="width: 100%" max-height="500px" border fit highlight-current-row align="center" stripe>
                                    <el-table-column type="index" label="#"></el-table-column>
                                    <el-table-column prop="统一社会信用代码" label="统一社会信用代码" width="200">
                                    </el-table-column>
                                    <el-table-column prop="组织机构代码" label="组织机构代码" width="100">
                                    </el-table-column>
                                    <el-table-column prop="法人单位名称" label="法人单位名称" width="200">
                                    </el-table-column>
                                    <el-table-column prop="联系方式.固话" label="联系方式" width="200">
                                    </el-table-column>
                                    <el-table-column prop="企业所在地行政区划代码" label="企业所在地行政区划代码" width="100">
                                    </el-table-column>
                                    <el-table-column prop="单位隶属关系" label="单位隶属关系" width="200">
                                    </el-table-column>
                                    <el-table-column prop="行业类别代码" label="行业类别代码" width="100">
                                    </el-table-column>
                                    <el-table-column prop="企业规模" label="企业规模" width="200">
                                    </el-table-column>
                                    <el-table-column prop="登记注册类型" label="登记注册类型" width="100">
                                    </el-table-column>
                                    <el-table-column prop="企业从业人员平均人数" label="企业从业人员平均人数" width="200">
                                    </el-table-column>
                                    <el-table-column fixed="right" width="150px">
                                        <template slot="header">
                                            <el-input v-model="search" size="mini" placeholder="输入 法人单位名称 关键字以搜索" />
                                        </template>
                                        <template slot-scope="scope">
                                            <el-button size="mini" @click="handleView(scope.$index, scope.row)">查看</el-button>
                                            <el-button size="mini" type="danger" @click="delCompany(scope.$index, scope.row)">删除</el-button>
                                        </template>
                                    </el-table-column>
                                </el-table>
                                <div class="block">
                                    <el-pagination v-if="pageshow" background @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page.sync="currentPage" :page-size.sync="pagesize" :page-sizes="[5, 10, 20, 50, 100]" layout="total,jumper,prev, pager, next,sizes" :total="files_count">
                                    </el-pagination>
                                </div>

                            </div>
                            <el-dialog :visible.sync="testVisible">
                                {{companyInfo}}
                            </el-dialog>
                        </div>
                    </el-col>

                </el-row>
            </div>
        </el-main>

    </el-container>

</div>
</template>

<script>
import axios from 'axios'
import {
    getCompanyList,
    getCompanyInfo,
    delCompany,
    getNewUser,
    addCompany
} from "@/api/backstage"; //获取数据的接口
export default {
    data() {
        return {
            rules: {
                username: [{
                        required: true,
                        message: '请输入统一社会信用代码',
                        trigger: 'blur'
                    },
                    // {
                    //     min: 6,
                    //     max: 6,
                    //     message: '长度为 18 个字符',
                    //     trigger: 'blur'
                    // }
                ],
                mobile: [{
                        required: true,
                        message: '请输入联系方式',
                        trigger: 'blur'
                    },
                    {
                        min: 11,
                        max: 11,
                        message: '长度为 11 个数字',
                        trigger: 'blur'
                    }
                ],
                password: [{
                        required: true,
                        message: '请输入密码',
                        trigger: 'blur'
                    },
                    {
                        min: 6,
                        max: 16,
                        message: '长度为 6~16 个字符',
                        trigger: 'blur'
                    }
                ]
            },
            // 分页
            loading: true,
            // 当前页
            currentPage: 1,
            // 每页大小
            pagesize: 5,
            files_count: 0,
            pageshow: true,
            // page_count: 0,
            testVisible: false,
            companyInfo: '',
            search: '',

            totalPage: 0,
            lastPageSize: 0,
            totalFiles: 0,

            addCompanyForm: {
                login_token: '',
                username: '',
                mobile: '',
                password: ''
            },
            drawer: false,
            CompanyBriefTable: [],
            companyInfoVisible: false,
            addCompanyTable: [],
            showEdit: [], //显示编辑框
            companyInfoForm: {
                统一社会信用代码: '',
                组织机构代码: '',
                法人单位名称: '',
                // 法定代表人: '',
                联系方式: '',
                企业所在地行政区划代码: '',
                单位隶属关系: '',
                行业类别代码: '',
                企业规模: '',
                登记注册类型: '',
                企业从业人员平均人数: ''
            },
        }
    },
    created() {
        this.hadleGetFilesListApi();

    },
    methods: {
        // 新增公司
        addCompanyUser(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    this.addCompanyForm.login_token = window.sessionStorage.getItem('ACCESS_TOKEN');
                    addCompany(this.addCompanyForm).then(res => {
                        if (res.data.status === 0) {
                            this.message(res.data.msg)
                        } else {
                            this.addCompanyForm = '';
                            this.$message({
                                message: '添加成功',
                                type: 'success'
                            });
                        }
                    })
                } else {
                    console.log('error submit!!');
                    return false;
                }
            });

        },
        handleSizeChange(val) {
            this.pagesize = val; //cur_page 当前页
            this.CompanyBriefTable.length = 0;
            this.hadleGetFilesListApi(); //获取数据
            this.pageshow = false; //让分页隐藏
            this.$nextTick(() => { //重新渲染分页
                this.pageshow = true;
            });
            console.log(`每页 ${val} 条`);
        },
        handleCurrentChange(val) {
            this.currentPage = val; //cur_page 当前页
            this.CompanyBriefTable.length = 0;
            this.hadleGetFilesListApi(); //获取数据
            this.pageshow = false; //让分页隐藏
            this.$nextTick(() => { //重新渲染分页
                this.pageshow = true;
            });
            console.log(`当前页: ${val}`);
        },
        //对所有数据进行分页处理 发送请求
        hadleGetFilesListApi() {
            var a = new Object();
            a.login_token = window.sessionStorage.getItem('ACCESS_TOKEN');
            // 返回多少条数据
            a.page_size = this.pagesize;
            // 第几页
            a.page_no = this.currentPage;
            getCompanyList(a).then(response => {
                    // 共几页
                    this.page_count = response.data.page_num;
                    response.data.msg.forEach(a => {
                        this.files_count = response.data.sum;
                        this.CompanyBriefTable.push(JSON.parse(a))
                    })
                    this.files_count = response.data.msg.length;
                    this.loading = false;
                })
                .catch({});
        },

        resetForm(formName) {
            this.$refs[formName].resetFields();
        },

        // ***********************分页结束*******************

        handleEdit: function (index, row) {
            //遍历数组改变editeFlag
            console.log(row)
            console.log(index);
            this.addCompanyTable[index].editeFlag = true;
        },
        handleView(index, row) {
            // 方式一，查看列表信息
            console.log(row._id.$oid)
            console.log(JSON.stringify(row))
            this.companyInfoForm.企业所在地行政区划代码 = row.企业所在地行政区划代码;
            this.companyInfoForm.统一社会信用代码 = row.统一社会信用代码;
            this.companyInfoForm.企业从业人员平均人数 = row.企业从业人员平均人数;
            this.companyInfoForm.组织机构代码 = row.组织机构代码;
            this.companyInfoForm.法人单位名称 = row.法人单位名称;
            this.companyInfoForm.单位隶属关系 = row.单位隶属关系;
            this.companyInfoForm.行业类别代码 = row.行业类别代码;
            this.companyInfoForm.登记注册类型 = row.登记注册类型;
            this.companyInfoForm.法定代表人 = row['法定代表人 （单位负责人）'];
            this.companyInfoForm.联系方式 = row.联系方式;
            this.companyInfoForm.企业规模 = row.企业规模;
            this.companyInfoVisible = true;

            // 方式二，调用后端接口
            // let a = new Object();
            // a.login_token = window.sessionStorage.getItem('ACCESS_TOKEN');
            // a.id = row._id.$oid;
            // console.log(JSON.stringify(a))
            // getCompanyInfo(a).then(response => {
            //     this.companyInfo = JSON.stringify(JSON.parse(response.data.msg));
            // })
            // this.testVisible = true;

        },
        deleteRow(index, rows) {
            rows.splice(index, 1);
        },
        delCompany(index, row) {
            let a = new Object();
            a.login_token = window.sessionStorage.getItem('ACCESS_TOKEN');
            a.id = row._id.$oid;
            this.deleteRow(index, this.CompanyBriefTable);
            console.log(JSON.stringify(a))
            delCompany(a).then(response => {
                this.companyInfo = JSON.stringify(JSON.parse(response.data.msg));
            })
            this.CompanyBriefTable.length = 0;
            this.hadleGetFilesListApi()
            console.log("shanchu")
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
        }

    }
}
</script>

<style>
.main-div {

    /* margin-top: 5px; */
    padding-top: 10px;
    padding-left: 10px;
    padding-right: 10px;
    padding-bottom: 20px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}

.add-company {

    padding-top: 9px;

}

.company-info {

    padding-top: 8px;
    border: 1px solid rgba(0, 0, 0, 0.1);

    /* margin-top: 15px; */
    /* margin-left: 40px; */
}

.company-info-table {
    border: 1px solid rgba(0, 0, 0, 0.1);

}

.add-btn {
    padding-top: 8px;
    margin-right: 200px;
}

.el-header {
    background-color: #000;
    color: #fff;
}

.el-aside {
    background-color: #D3DCE6;
    color: #333;
}

.el-main {
    background-color: #fafafa;
    color: #333;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

body>.el-container {
    margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
    line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
    line-height: 320px;
}
</style>
