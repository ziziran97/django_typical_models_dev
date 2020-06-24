<!--
 * @Author: your name
 * @Date: 2020-06-22 18:09:09
 * @LastEditTime: 2020-06-23 15:20:16
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /demo1/src/App.vue
-->
<template>
<div id="app">
  <div class="all">
    <div class="one">
      <div class="oneType" v-for="(item,index) in one" :key="index">
        <b>{{ one[index].name }}</b>
      </div>
    </div>
    <div class="twothreefour">
      <div class="two">
        <div class="twoType"
        v-for="(item, index) in two" :key="index"
        @mouseenter="open(index)">
          <b>{{ two[index].name }}</b>
        </div>
      </div>
        <div class="threefour" v-if="flag"
        @mouseleave="close()">
        <div class="threefourType" v-for="(item, index) in three1" :key=
        "index">
          <span class="three">{{ three1[index] }}</span>
          <span class="four" v-for="(item4, index4) in four1" :key="index4">
            {{ four1[index4] }}&nbsp;
          </span>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
  import Axios from 'axios'
  export default{
    name: 'app',
    data(){
      return{
        one:[],
        two:[],
        three:[],
        four:[],
        flag:false,
        three1:[],
        four1:[]
      }
    },
    methods: {
      getData() {
        const api = 'http://127.0.0.1:8000';
        var api1 = api + 'api/Type1';
        var api2 = api + 'api/Type2';
        var api3 = api + 'api/Type3';
        var api4 = api + 'api/Type4';
        Axios.get(api1)
        .then(function(response){
          // console.log(response);
          for (var i=0; i<response.data.length; i++){
            // console.log(response.data[i])
            Type1.push(response.data[i])
          }
          // console.log(Type1)
        })
        .catch(function (error){
          console.log(error);
        });
        this.one = Type1;
        Axios.get(api2)
        .then(function (response){
          // console.log(response)
          for (var i=0;i<response.data.length;i++){
            // console.log(response.data[i])

          }
        })
      }
    }
  }
</script>

<style>
*{
  /* 样式初始化 */
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
.all{
  /* 将整个导航栏组件做整体设置 */
  /* 宽度占浏览器80%，高度400px；背景为灰色；上边距50px；左右居中 */
  /* 设置为flex弹性盒子，并且定义为高度不够自动折叠模式，用于横向排列子元素 */
  width: 80%;
  height: 400px;
  background: #eee;
  margin: 50px auto;
  display: -webkit-flex; /* Safari */
  display: flex;
  flex-wrap: wrap;
}
.one{
  /* 设置一级类目所占地区的样式，宽度沾满all盒子的100% */
  width: 100%;
  height: 50px;
  background: #FF8888;
  display: flex;
  display: -webkit-flex; /* Safari */
  flex-wrap: wrap;
  /* 弹性盒子内部的子元素都均匀排列成一横排，并且左右两边都留有一定空隙 */
  justify-content: space-around;
}
.oneType:hover{
  background-color: rgba(210, 102, 30, 0.89);
  color: #eee;
}
.twothreefour{
  /* 盛放二、三、四级目录的盒子 */
  width: 100%;
  height: 350px;
  background: #66FF66;
  display: -webkit-flex; /* Safari */
  display: flex;
  flex-wrap: wrap;
  /* 弹性盒子内部的子元素都均匀排列成一横排，并且左右两边都不留空隙 */
  justify-content: space-between;
}
.two{
  /* 设置盛放二级类目的弹性盒子 */
  width: 15%;
  height: 100%;
  background: #77FFCC;
  display: -webkit-flex;
  display: flex;
  /* 弹性盒子内部的子元素从上到下排成一列 */
  flex-direction: column;
}
.twoType{
  width: 100%;
  height: 40px;
  line-height: 40px;
  text-align: center;
  background: #EEFFBB;
}
.twoType:hover{
  background-color: black;
  color: #eee;
}
.threefour{
  width: 40%;
  margin-right: 45%;
  height: 100%;
  background: #33FFDD;
  display: -webkit-flex;
  display: flex;
  flex-direction: column;
}
.threefourType{
  margin: 10px auto;
}
.three{
  font-family: 微软雅黑,黑体;
  font-size: 16px;
  font-weight: 800;
}
.four{
  font-family: 宋体;
  font-size: 12px;
  font-weight: 400;
}
</style>
