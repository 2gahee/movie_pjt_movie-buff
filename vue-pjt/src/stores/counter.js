import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'



export const useMovieStore = defineStore('movie', () => {
  const articles = ref([])
  const nowOns = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  const router = useRouter()



  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/community`,
      headers: {
        Authorization: `Token ${token.value}`
        // Accept: 'application/json'
      },
      withCredentials: true
    })
    .then(res => {
      articles.value = res.data
      console.log(res.data)
      
    })
    .catch(err => console.log(err))
  }

const signUp = function (payload) {
  const { username, password1, password2, nickname, email } = payload

  axios({
    method:'post',
    url: `${API_URL}/accounts/signup/`,
    withCredentials: true,
    data: {
      username, password1, password2, nickname, email
    }
  })
    .then((res) => {
      if (res.data) {
        console.log('회원가입 성공:', res.data);
        const password = password1
        logIn({ username, password })
      } else {
        console.error('응답 데이터 없음');
      }

    })
    .catch((error) => {
      // console.error(error.response)
      console.error('Error response:', error.response);
      if (error.response && error.response.data) {
        console.error('Error details:', error.response.data);
        // non_field_errors가 있을 경우 그 내용을 확인
        if (error.response.data.non_field_errors) {
          console.error('Non-field errors:', error.response.data.non_field_errors);
        }
      }

  })
}


const logIn = function (payload) {
  const { username, password } = payload

  axios({
    method: 'post',
    url: `${API_URL}/accounts/login/`,
    data: {
      username, password
    }
  })
    .then((res) => {
      token.value = res.data.key
      router.push({ name: 'Articles' })
      console.log(res.data)
      console.log('로그인 성공')
    })
    .catch((err) => {
      console.log(err)
    })
}


const getNowOns = function () {
  axios({
    method: 'get',
    url: `${API_URL}/movies/now-on/`,
    headers: {
      Authorization: `Token ${token.value}`
      // Accept: 'application/json'
    },
    withCredentials: true
  })
  .then(res => {
    nowOns.value = res.data
    console.log(res.data)
  })
  .catch(err => console.log(err))
}


  return { articles, API_URL, getArticles, signUp, logIn, token, getNowOns, isLogin, nowOns }
})
