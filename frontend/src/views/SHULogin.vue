<template>
  <v-container fill-height>
    <v-row justify="center">
      <v-card class="elevation-12" width="450px">
        <v-toolbar color="primary" dark flat>
          <v-toolbar-title>登录</v-toolbar-title>
        </v-toolbar>
        <v-expand-transition>
          <v-alert tile class="radius-0" type="error" v-if="showLoginFailed">
            登录失败：请检查学生证号和密码
          </v-alert>
        </v-expand-transition>

        <v-form class="pa-5">
          <v-card-text>
            <v-text-field
              v-model="stuId"
              prepend-icon="mdi-account"
              :counter="8"
              label="学号"
              :rules="stuIdRules"
              required
            >
            </v-text-field>
            <v-text-field
              v-model="password"
              label="密码"
              prepend-icon="mdi-lock"
              :rules="passwordRules"
              required
              @click:append="showPsswrd = !showPsswrd"
              :append-icon="showPsswrd ? 'mdi-eye' : 'mdi-eye-off'"
              :type="showPsswrd ? 'text' : 'password'"
              @keyup.enter="login"
            >
            </v-text-field>
            <v-select
              v-model="selectedTerm"
              :items="termSelections"
              :rules="termRules"
              label="选择学期"
              required
              @keyup.enter="login"
            >
            </v-select>
          </v-card-text>
          <v-card-actions>
            <v-spacer />
            <v-btn
              :disabled="this.loginBtnDisabled"
              @click="login"
              color="primary"
              >登录</v-btn
            >
          </v-card-actions>
        </v-form>
      </v-card>
    </v-row>
  </v-container>
</template>
<script>
import { loginAPI } from "@/api/course";
export default {
  name: "SHULogin",
  data() {
    return {
      // form data
      stuId: "",
      password: "",
      selectedTerm: "秋季选课",
      // text rules
      stuIdRules: [
        (v) => !!v || "必须输入学号!",
        (v) => (v && v.length <= 8) || "学号长度不合法!",
      ],
      passwordRules: [(v) => !!v || "必须输入密码!"],
      termRules: [(v) => !!v || "必须选择选课学期!"],
      termSelections: ["春季选课", "夏季选课", "秋季选课", "冬季选课"],
      showPsswrd: false,
      showLoginFailed: false,
      loginBtnDisabled: false,
    };
  },
  methods: {
    login() {
      this.loginBtnDisabled = true;
      let loginParam = {
        stu_id: this.stuId,
        password: this.password,
        term_id: this.selectedTerm.substr(0, 1),
      };
      console.log("待发送的表单: ", loginParam);
      // 不能使用异步方法!必须等待响应返回
      loginAPI(loginParam).then((res) => {
        // 修改sessionStorage中的登陆状态
        sessionStorage.setItem("loginState", res.login_state);
        let loginState = sessionStorage.getItem("loginState");
        // console.log(typeof loginState); // 你妈竟然是一个string
        if (loginState && loginState == "true") {
          console.log("登陆成功!");
          this.$router.push("/course_old");
        } else {
          console.log("登录失败!");
          this.showLoginFailed = true;
          this.loginBtnDisabled = false;
        }
      });
    },
  },
};
</script>

