<template>
<div class="main">
    <h1>登录</h1>

    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px">
        <el-form-item label="统一代码" prop="username">
            <el-input v-model="ruleForm.username" placeholder="请输入社会信用统一代码" clearable ></el-input>
        </el-form-item>
    </el-form>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px">
        <el-form-item label="密码" prop="password">
            <el-input v-model="ruleForm.password" type="password" placeholder="请输入密码" show-password clearable></el-input>
        </el-form-item>
        <el-button class="btn" type="primary" @click="submitForm('ruleForm')" clearable>登录</el-button>
        <el-dialog :visible.sync="visible" title="提示">
            <p>{{message}}</p>
        </el-dialog>
    </el-form>
</div>
</template>

<script>
import axios from 'axios'
import {root_path} from "@/api/backstage"

export default {
    data() {
        return {
            visible: false,
            message: '',

            ruleForm: {
                username: '',
                password: ''
            },
            rules: {
                username: [{
                        required: true,
                        message: '请输入统一社会信用代码',
                        trigger: 'blur'
                    },
                    {
                        min: 1,
                        max: 18,
                        message: '长度为 18 个字符',
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
                        max: 6,
                        message: '长度为 8~16 个字符',
                        trigger: 'blur'
                    }
                ]
            }
        }
    },
    methods: {
        submitForm(formName) {
            this.$refs[formName].validate(valid => {
                if (valid) {
                    const loading = this.$loading({
                        lock: true,
                        text: '加载中',
                        spinner: 'el-icon-loading',
                        background: 'rgba(0, 0, 0, 0.7)'
                    })

                    axios.post(`${root_path}/api/login`, this.ruleForm)
                        .then(response => {
                            loading.close()
                            const data = response.data
                            // alert(data.msg)
                            if (data.msg === "登录成功") {
                                // 保存登录凭证
                                window.sessionStorage.setItem('ACCESS_TOKEN', response.data.login_token)
                                // 跳转到指定页面
                                this.$router.push({
                                    path: '/client'
                                })
                            } else if (data.msg === "admin登录成功") {
                                
                                window.sessionStorage.setItem('ACCESS_TOKEN', response.data.login_token)
                                this.$router.push({
                                    path: '/back'
                                    // path: '/client'
                                })
                            } else {
                                this.visible = true
                                this.message = response.data.msg
                            }
                        })
                        .catch(function (error) {
                            console.log(error)
                        })
                } else {
                    console.log('error submit!!')
                    return false
                }
            })
        },
        resetForm(formName) {
            this.$refs[formName].resetFields()
        }
    }
}
</script>

<style>
.main {
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    padding: 4%;
    max-width: 450px;
    margin: 0 auto;
}
</style>
