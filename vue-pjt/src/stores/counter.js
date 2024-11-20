import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
export const useMovieStore = defineStore('movie', () => {
  const token = 'Token b63f63cb8d56de105c3e5b5c526686222ab0917a'
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/community`,
      headers: {
        Authorization: token,
        Accept: 'application/json'
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
    data: {
      username, password1, password2, nickname, email
    }
  })
    .then((res) => {
      console.log(res)
      console.log('회원가입 성공')
      const password = password1
      logIn({ username, password })
    })
    .catch((error) => {
      console.error(error.response)
  })
}

  return { articles, API_URL, getArticles, signUp }
})
