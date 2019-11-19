<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading...</span>
    </div>

    <div v-else class="login-form">
      <div v-if="errors.length" class="error-list alert alert-danger">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <div v-for="(error, idx) in errors" :key="idx">{{ error }}</div>
      </div>
      <div class="form-group">
        <label for="id">ID</label>
        <input
        type="text"
        class="form-control"
        id="id"
        placeholder="ID를 입력해주세요."
        v-model="credentials.username"
        @keyup.enter="login"
        >
      </div>
      <div class="form-group">
        <label for="password">PASSWORD</label>
        <input
        type="password"
        class="form-control"
        id="password"
        placeholder="PASSWORD를 입력해주세요."
        v-model="credentials.password"
        @keyup.enter="login"
        >
      </div>
      <button class="btn btn-primary" @click="login">Login</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginForm',
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      },
      loading: false,
      errors: [],
    }
  },
  methods: {
    login() {
      // 1. 로그인 유효성 검사가 끝나면
      if (this.checkForm()) {
        // 2. loading의 상태를 true로 변경하고(spinner-border가 돈다.)
        this.loading = true
        // 3. credentails(username, password) 정보를 담아 djago 서버로 로그인 요청을 보낸다.
        axios.get('http://127.0.0.1:8000/', this.credentials)
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
      } else {
        console.length('로긴 실패ㅠㅠ')
      }
    },
    checkForm() {
      this.errors = []
      // 1. 사용자가 아이디를 입력하지 않은 경우
      if (!this.credentials.username) {
        this.errors.push("ID를 입력해주세요.")
      }
      // 2. 패스워드가 8자 미만인 경우
      if (this.credentials.password.length < 8) {
        this.errors.push("비밀번호는 8자이상 입력해주세요.")
      }
      // 3. 아이디와 패스워드를 모두 잘 입력한 경우
      if (this.errors.length === 0) {
        return true
      }
    },
  }
}
</script>

<style>

</style>