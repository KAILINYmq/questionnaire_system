<template>
    <el-main>
    <el-input placeholder="请输入要搜索的联系人" prefix-icon="el-icon-search" v-model="searchFile"></el-input>
      <el-table :data="tableData"  v-loading="loading" border  height="680px" style="width: 100%">
      <el-table-column label="编号" width="100" prop="id">
      </el-table-column>
      <el-table-column  label="姓名"  prop="name"  width="100">
      </el-table-column>
      <el-table-column  label="电话"  prop="phone"  width="180">
      </el-table-column>
      <el-table-column  label="生日"  prop="brithday"  width="80">
      </el-table-column>
      <el-table-column  label="性别"  prop="gender"  width="80">
      </el-table-column>
      <el-table-column  label="年龄"  prop="age"  width="80">
      </el-table-column>
      <el-table-column  label="住址"  prop="address"  width="280">
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            @click="handleDelete(scope.$index, scope.row)"
            size="mini"
            type="danger">联系ta
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <!-- 分页底部 -->
    <el-pagination
      background      
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="currentPage"
      :page-sizes="[5,10,15]"
      :page-size="pagesize"
      layout="total,jumper,prev, pager, next,sizes"
      :total="files_count"
    ></el-pagination>
    </el-main>
</template>
<script>
import {
  getCompanyList
} from "@/api/backstage";//获取数据的接口
    export default {
        name: "phoneList",
        data(){
            let tableDataAll = [];
            return{
                tableData:[],
                // 是否加载数据
                loading:true,
                currentPage:1,
                pagesize:10,
                files_count:5,
                fileList:[],
                searchFile:"",
                
            };
        },
         created: function() {
    this.hadleGetFilesListApi();
  },
    methods:{
    //分页 初始页currentPage、初始每页数据数pagesize和数据testpage--->控制每页几条
    handleSizeChange:function(size){
        this.pagesize = size;
        this.hadleGetFilesListApi();
        console.log(this.pagesize)
        console.log(this.hadleGetFilesListApi())
    },
    // 控制页面的切换
    handleCurrentChange: function(currentPage) {
        this.currentPage = currentPage;
        // console.log(currentPage)
        this.hadleGetFilesListApi();
    },
    //对所有数据进行分页处理 发送请求
    hadleGetFilesListApi() {
      selectphoneAll(this.currentPage, this.pagesize)
        .then(res => {
          console.log("111"+res);
          this.tableData = res.data.filesInfo;
          console.log("3333"+this.tableData);
          this.files_count = res.data.files_count;
          this.tableDateAll = res.data.filesInfo;
          this.loading = false;
        })
        .catch({});
    }
    }
}
</script>

