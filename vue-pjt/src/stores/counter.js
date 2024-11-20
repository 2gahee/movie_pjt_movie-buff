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
  return { articles, API_URL, getArticles }
})
