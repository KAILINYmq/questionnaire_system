<template>
  <div class="main">
    <h1>登录页面</h1>

    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px">
      <el-form-item label="统一代码" prop="login_id">
        <el-input v-model="ruleForm.login_id" placeholder="请输入社会信用统一代码"></el-input>
      </el-form-item>
    </el-form>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px">
      <el-form-item label="密码" prop="password">
        <el-input v-model="ruleForm.password" type="password" placeholder="请输入密码" show-password></el-input>
      </el-form-item>
      <el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
      <el-dialog :visible.sync="visible" title="提示">
        <p>{{message}}</p>
      </el-dialog>
    </el-form>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  data () {
    return {
      visible: false,
      message: '',

      ruleForm: {
        login_id: '123123123123123123',
        password: '123456789'
      },
      rules: {
        login_id: [
          {
            required: true,
            message: '请输入统一社会信用代码',
            trigger: 'blur'
          },
          { min: 18, max: 18, message: '长度为 18 个字符', trigger: 'blur' }
        ],
        password: [
          {
            required: true,
            message: '请输入密码',
            trigger: 'blur'
          },
          { min: 8, max: 16, message: '长度为 8~16 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          const loading = this.$loading({
            lock: true,
            text: '加载中',
            spinner: 'el-icon-loading',
            background: 'rgba(0, 0, 0, 0.7)'
          })

          axios
            .post('http://127.0.0.1/api/login', this.ruleForm)
            .then(response => {
              console.log(response)
              loading.close()
              const data = response.data
              if (data.status === 0) {
                // 保存登录凭证
                // 跳转到指定页面
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
    resetForm (formName) {
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
